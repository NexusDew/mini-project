import random
import uuid
import json
from datetime import datetime, timedelta


def generate_user():
    return {
        "user_id": str(uuid.uuid4())
    }


def generate_session(user_id):
    return {
        "session_id": str(uuid.uuid4()),
        "user_id": user_id,
        "session_start": datetime.now()
    }


def generate_event(session, num_events=10):
    events = []

    user_id = session["user_id"]
    session_id = session["session_id"]
    time = session["session_start"]

    event_types = ["view", "view", "view", "cart", "purchase", "exit"]

    for _ in range(num_events):

        event_type = random.choices(
            event_types,
            weights=[50, 20, 10, 15, 3, 2],
            k=1
        )[0]

        payload = {}

        if event_type == "view":
            payload = {
                "product_id": str(uuid.uuid4()),
                "price": round(random.uniform(10, 500), 2)
            }

        elif event_type == "cart":
            payload = {
                "product_id": str(uuid.uuid4()),
                "quantity": random.randint(1, 3)
            }
        
        elif event_type == "purchase":
            payload = {
                "order_id": str(uuid.uuid4()),
                "total_amount": round(random.uniform(20, 1000), 2)
            }
        
        elif event_type == "exit":
            break

        time += timedelta(minutes=random.randint(1, 15))

        events.append({
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "event_timestamp": time.isoformat(),
            "user_id": user_id,
            "session_id": session_id,
            "payload": payload
        })
        
    return events


def send_events(events):
    print(f"Sending {len(events)} events")
    json_data = json.dumps(events, indent=2)
    print(json_data)

user = generate_user()
session = generate_session(user["user_id"])
events = generate_event(session)

send_events(events)