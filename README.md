# Meta CAPI + HubSpot tracking starter

Small, working pieces for getting the right conversions back to Meta when you run Meta Ads and sell through HubSpot.

| Folder | What it is |
|---|---|
| [`browser/track.js`](browser/track.js) | One `track()` call that sends the same event to the Meta Pixel, gtag and the dataLayer with a shared `event_id`, so the Conversions API copy is deduplicated. |
| [`server/send_deal_to_meta.py`](server/send_deal_to_meta.py) | Minimal example that sends a HubSpot deal outcome (qualified, won with amount) to the Conversions API with correct `user_data` and a stable `event_id`. |
| [`checklists/`](checklists/) | Deduplication checklist to run in Events Manager. |

GTM users: the [Event ID variable template](https://github.com/tonibitencourt/gtm-event-id-generator) gives every tag on the same dataLayer event the same id.

## The path this starter covers

1. **Browser:** the event is born on the page with an `event_id`.
2. **Web GTM:** reads the dataLayer and fires the Pixel and the server request.
3. **Server-side GTM + Conversions API:** resends to Meta with the same `event_id`.
4. **CRM:** HubSpot deal stages go back to Meta, so campaigns learn from customers, not form fills.

## Guides

Free, practical guides: https://lp.bitencourtco.com/kit-tracking/en/guides/?utm_source=github&utm_medium=referral&utm_campaign=starter

- Free field guide: [13 Silent Tracking Failures](https://tonibitencourt.gumroad.com/l/13-silent-tracking-failures?utm_source=github&utm_medium=referral&utm_campaign=starter)
- The complete setup (47-page manual + AI-ready Markdown, server-side GTM on your own VPS, the HubSpot bot with deal stages): [4-Layer Tracking Kit](https://tonibitencourt.gumroad.com/l/4-layer-tracking?utm_source=github&utm_medium=referral&utm_campaign=starter)

MIT License · Bitencourt & Co. · Meta, Google Tag Manager and HubSpot are trademarks of their owners.
