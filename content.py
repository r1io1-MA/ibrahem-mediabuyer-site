"""Loads articles written in /admin (or by hand) from content/articles/<lang>/<slug>.md.

Each file is Markdown with YAML front matter:
  title, url, meta_title, description, card, date, read, faq: [{q, a}]
An article can exist in one language or both; files with the same name are paired.
"""
import os, re, datetime
import yaml, markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(ROOT, 'content', 'articles')
LANGS = ['ar', 'en']

def _read(path):
    raw = open(path, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', raw, re.S)
    fm, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, raw)
    return fm, body

def _date(v):
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.strftime('%Y-%m-%d')
    return str(v or datetime.date.today().isoformat())[:10]

def _minutes(text):
    words = len(re.sub(r'<[^>]+>', ' ', text).split())
    return max(2, round(words / 200))

def load():
    by_slug = {}
    for lang in LANGS:
        d = os.path.join(DIR, lang)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            slug = f[:-3]
            fm, body = _read(os.path.join(d, f))
            if fm.get('draft'):
                continue
            title = str(fm.get('title') or slug)
            html = markdown.markdown(body, extensions=['extra', 'sane_lists'])
            faq = [(str(x.get('q', '')), str(x.get('a', ''))) for x in (fm.get('faq') or []) if x and x.get('q')]
            entry = by_slug.setdefault(slug, {'slug': slug})
            entry[lang] = {
                'title': title,
                'meta_title': str(fm.get('meta_title') or f'{title} | ' + ('إبراهيم محمد' if lang == 'ar' else 'Ibrahem Muhamed')),
                'desc': str(fm.get('description') or fm.get('card') or title),
                'card': str(fm.get('card') or fm.get('description') or ''),
                'body': html,
                'faq': faq,
            }
            if fm.get('cover'): entry.setdefault('cover', str(fm['cover']))
            if fm.get('image'): entry.setdefault('image', str(fm['image']))
            entry.setdefault('date', _date(fm.get('date')))
            entry.setdefault('read', int(fm.get('read') or _minutes(html)))
    # newest first
    return sorted(by_slug.values(), key=lambda a: a['date'], reverse=True)

ARTICLES = load()
