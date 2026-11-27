"""Minimal example: send one HubSpot deal outcome to the Meta Conversions API.

Environment:
  META_PIXEL_ID, META_CAPI_TOKEN, GRAPH_API_VERSION (e.g. the current version listed
  in Meta's Graph API changelog), CURRENCY (e.g. USD)

This is a single-event example. A production setup also needs: reading deals from the
HubSpot API with a cursor, the stage-to-event mapping, retries, and storing fbc/fbp/lead_id
on the contact when the lead arrives.
"""
import hashlib, os, time
import requests

PIXEL_ID = os.environ["META_PIXEL_ID"]
TOKEN = os.environ["META_CAPI_TOKEN"]
VERSION = os.environ["GRAPH_API_VERSION"]
CURRENCY = os.environ.get("CURRENCY", "USD")


def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()


def user_data_from_contact(c):
    if c.get("meta_lead_id"):                       # lead from a Meta lead form: best match
        return {"lead_id": c["meta_lead_id"]}
    ud = {}
    if c.get("meta_fbc"): ud["fbc"] = c["meta_fbc"]  # never hash fbc / fbp
    if c.get("meta_fbp"): ud["fbp"] = c["meta_fbp"]
    if c.get("email"): ud["em"] = [sha256(c["email"].strip().lower())]
    if c.get("phone"):                               # digits only, with country code
        ud["ph"] = [sha256("".join(ch for ch in c["phone"] if ch.isdigit()))]
    return ud


def send(event_name, contact, deal_id, value=None):
    event = {
        "event_name": event_name,
        "event_time": int(time.time()),
        "action_source": "system_generated",        # it did not happen in a browser
        "event_id": f"{deal_id}_{event_name.lower()}",  # stable: a re-run is discarded by Meta
        "user_data": user_data_from_contact(contact),
        "custom_data": {"lead_event_source": "HubSpot", "event_source": "crm"},
    }
    if value is not None:
        event["custom_data"].update(value=value, currency=CURRENCY)
    r = requests.post(f"https://graph.facebook.com/{VERSION}/{PIXEL_ID}/events",
                      params={"access_token": TOKEN}, json={"data": [event]}, timeout=10)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    demo = {"email": "lead@example.com", "meta_fbc": "fb.1.1700000000000.AbCdEf"}
    print(send("Purchase", demo, deal_id="123456", value=1500))
