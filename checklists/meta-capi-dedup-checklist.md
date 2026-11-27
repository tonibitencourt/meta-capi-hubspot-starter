# Meta Conversions API deduplication checklist

- [ ] The `event_id` is created **once**, on the page, per event.
- [ ] The Pixel receives it as `eventID`; the server receives the same value as `event_id`.
- [ ] `event_name` is identical on both paths (`Lead` and `lead` are different events).
- [ ] GTM variables do not generate a new random id per tag (use one id per dataLayer event).
- [ ] Events Manager → Test events: each conversion shows **Browser** and **Server** with the same id.
- [ ] The Test Event Code is removed before publishing.
- [ ] CRM events use a stable id per record and stage (e.g. `<deal id>_won`) so a re-run is not counted again.
- [ ] `fbc` and `fbp` are sent in plain text; email and phone are normalized and SHA-256 hashed.

Guide: https://lp.bitencourtco.com/kit-tracking/en/guides/meta-capi-deduplication-event-id/?utm_source=github&utm_medium=referral&utm_campaign=starter
