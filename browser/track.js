/**
 * track(): send one event to the Meta Pixel, gtag and the dataLayer with the SAME event_id.
 * The same id is what lets Meta deduplicate the browser event against its Conversions API copy.
 */
function track(eventName, props) {
  if (typeof window === "undefined") return
  props = props || {}
  var eventId = "e_" + Date.now() + "_" + Math.random().toString(36).slice(2, 10)
  var payload = Object.assign({}, props, { event_id: eventId })

  // One try/catch PER destination: a failure in one must not silently skip the others.
  try { if (typeof window.fbq === "function") window.fbq("trackCustom", eventName, payload, { eventID: eventId }) } catch (e) {}
  try { if (typeof window.gtag === "function") window.gtag("event", eventName, payload) } catch (e) {}
  // The dataLayer is a plain array and always exists: it is the reliable channel for GTM.
  try { window.dataLayer = window.dataLayer || []; window.dataLayer.push(Object.assign({ event: eventName }, payload)) } catch (e) {}
  return eventId
}
