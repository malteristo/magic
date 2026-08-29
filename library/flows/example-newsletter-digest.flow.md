# Flow: Newsletter Digest (Example)

*This is an example flow demonstrating the newsletter digest pattern. 
Copy and customize for your own newsletters.*

## Goal
Compile a digest of recent newsletter emails, summarizing each one and organizing 
by topic, delivered as a readable artifact on my desk.

## Trigger
Manual invocation, or monthly on the 1st

## Context
- Newsletters are emails that follow patterns: regular senders, similar subjects, 
  longer-form content meant for reading rather than action
- I want bullet-point summaries (3-5 key points per newsletter)
- Group by theme/topic, not by sender
- Include source links where available
- Skip promotional content—focus on substantive newsletters

**Learning:** Use exact sender email addresses (e.g., `newsletter@example.com`) rather than 
display names ("Example Newsletter") for Gmail queries. Email addresses are stable identifiers; 
display names vary and may not match search patterns.

## Inputs
- email_account: [ADAPT: Your email provider] 
- lookback_days: 30 (optional, how many days back to check)
- newsletter_senders: [ADAPT: List your newsletter sender email addresses]
  - Example format: `sender@newsletter.com (Newsletter Name)`
  - Find the actual sender email in your inbox (not the display name)
- max_newsletters: 50 (optional, cap on how many to process)

## Outputs
- digest: desk/newsletter-digest-{date}.md

## Dependencies
- Gmail: read access through whatever mail integration your substrate has — a native plugin, an MCP gateway, an API client. The flow needs *list messages by query* and *read a message body*; it does not care which tool provides them. Check what is connected rather than assuming a provider.

## Steps
1. **Fetch candidate emails** using Gmail query for newsletter-like content
2. **Filter** to actual newsletters (exclude transactional, promotional-only)
3. **Extract content** from each newsletter
4. **Summarize** each newsletter (3-5 bullet points)
5. **Categorize** by topic/theme
6. **Compile** into organized digest artifact
7. **Save** to desk/ with date-stamped filename

## Adaptations
**Required before first use:**
- Connect your email provider, by whatever route your substrate offers
- Add your actual newsletter sender email addresses
- Adjust newsletter_query if your newsletters use different labels/categories

**Optional customizations:**
- Change lookback_days for different timeframes (7 for weekly, 30 for monthly)
- Modify output location
- Adjust summary depth (more/fewer bullet points)
- Organize by sender instead of topic

## Origin
Template by: Magic Alliance
Version: 1.0
Created: 2026-01-14
