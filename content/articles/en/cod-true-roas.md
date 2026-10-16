---
title: "Cash on delivery is lying to your ROAS: how to calculate the real return for a Saudi store"
url: cod-true-roas
meta_title: "Cash on delivery and true ROAS: a guide for Saudi stores | Ibrahem Muhamed"
description: "Why ad-platform ROAS is inflated when many of your orders are cash on delivery, how to calculate the real return after refused orders, and 5 steps that cut refusals and train the algorithm on real buyers."
card: "The platform counts the order at checkout. A cash-on-delivery order only becomes a sale at the door."
date: 2026-10-16
read: 7
faq:
  - q: "Should I turn off cash on delivery in my store?"
    a: "Usually not. Many Saudi shoppers prefer it, and removing it can cut your conversion rate more than it saves. Measure your delivery rate, calculate the real return, then nudge customers toward prepaying with a small incentive."
  - q: "What is a normal refusal rate for cash-on-delivery orders?"
    a: "It varies a lot by product, city, shipping speed and how well orders are confirmed. Do not rely on a general benchmark; calculate your own from your courier's data for the last 60 to 90 days."
  - q: "Should I send the purchase event at checkout or at delivery?"
    a: "Send it at checkout so you do not lose the signal, add a separate event when the order is actually delivered through the Conversions API or its equivalent, and build lookalike audiences from customers who received and paid."
---

In most Saudi stores, a large share of orders are cash on delivery (COD). That creates a problem you will not see in the ads dashboard: **the platform counts a purchase the moment someone taps the checkout button**, but the store only gets paid if the order arrives and the customer accepts it.

If some orders are refused at the door, or the customer never answers the courier, your Snapchat or TikTok ROAS stays the same while your real revenue is lower, and the shipping and return costs come out of your margin.

## How to calculate the real ROAS

You need two numbers from your own data: **the share of orders that are COD**, and **the successful delivery rate** for those orders from your courier.

**Realised revenue share** = (prepaid share) + (COD share × delivery rate)

**Real ROAS** = platform ROAS × realised revenue share

### Example

- Platform ROAS: **4.0x**
- 70% of orders are COD, 30% are prepaid
- Successful delivery rate on COD orders: 75%

Realised revenue share = 0.30 + (0.70 × 0.75) = **0.825**

Real ROAS = 4.0 × 0.825 = **3.3x**

That is before the shipping cost on returned orders, which you pay with no revenue against it. If your break-even ROAS is 3.5x, a campaign that looks profitable at 4.0x is actually losing money.

<div class="callout">Work out your break-even ROAS with the <a href="/tools/break-even-roas/">break-even ROAS calculator</a>, then compare it with the real ROAS, not the platform number. To see net profit after every cost, use the <a href="/tools/roi-calculator/">ROI calculator</a>.</div>

## Why the algorithm learns the wrong thing

The numbers are only half the problem. When every order is sent to the platform as a "purchase", you teach it to find **people who tap the buy button**, not **people who receive and pay**. Over time campaigns can bring more orders at a lower cost while the refusal rate quietly climbs.

## 5 steps to cut refusals and fix measurement

<ol class="steps">
<li><b>Confirm every order before you ship it.</b> A WhatsApp message or a short call within hours of the order catches the ones that were never serious, before you pay to ship them.</li>
<li><b>Reward prepaying with a small incentive.</b> A small discount, faster shipping or a small gift for paying online raises the share of guaranteed orders without removing the COD option.</li>
<li><b>Send an event at actual delivery.</b> Add a separate event sent when an order is delivered, through Meta's Conversions API or the Snapchat and TikTok equivalents, and build lookalikes from customers who actually received their order.</li>
<li><b>Review refusals by city and by ad.</b> Some cities, ads or offers bring far more refusals than others. Spend less on them, or make prepaying more prominent there.</li>
<li><b>Judge campaigns on delivered orders.</b> Start the monthly report with realised revenue and MER after delivery, not with the order count in the platform.</li>
</ol>

## The takeaway

If your store relies on cash on delivery, platform ROAS is a first estimate only. Multiply it by your realised revenue share before you decide to scale, and train the algorithm on people who receive and pay, not on people who tap the button.
