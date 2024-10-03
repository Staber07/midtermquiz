import requests
import json


access_token = "MmZkMDRmYTctY2YxNi00OGQzLWEwZTUtMTlhMzQ4OGJiNDY0MWQ2OGRhYTUtMjIw_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b"


meeting_title = "Test Meeting"
start_time = "2023-10-07T14:00:00Z"
end_time = "2023-10-08T15:00:00Z"


room_name = "Test Room"
participant_email = "participant@example.com"


message_text = "Hello, this is a test message!"


url = "https://webexapis.com/v1/"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}


meeting_data = {
    "title": meeting_title,
    "start": start_time,
    "end": end_time
}
response = requests.post(url + "meetings", headers=headers, json=meeting_data)


if response.status_code == 200:
    print("Meeting created successfully!")
    meeting_id = response.json()["id"]
    print(f"Meeting ID: {meeting_id}")
else:
    print("Failed to create meeting.")


room_data = {
    "title": room_name
}
response = requests.post(url + "rooms", headers=headers, json=room_data)


if response.status_code == 200:
    print("Room created successfully!")
    room_id = response.json()["id"]
    print(f"Room ID: {room_id}")
else:
    print("Failed to create room.")


membership_data = {
    "roomId": room_id,
    "personEmail": participant_email,
    "isModerator": False
}
response = requests.post(url + "memberships", headers=headers, json=membership_data)


if response.status_code == 200:
    print("Participant added successfully!")
else:
    print("Failed to add participant.")


message_data = {
    "roomId": room_id,
    "text": message_text
}
response = requests.post(url + "messages", headers=headers, json=message_data)


if response.status_code == 200:
    print("Message sent successfully!")
    message_id = response.json()["id"]
    print(f"Message ID: {message_id}")
else:
    print("Failed to send message.")


response = requests.get(url + f"messages?roomId={room_id}", headers=headers)


if response.status_code == 200:
    print("Messages retrieved successfully!")
    messages = response.json()["items"]
    for message in messages:
        print(f"Message ID: {message['id']}, Text: {message['text']}")
else:
    print("Failed to retrieve messages.")


def delete_message(message_id):
    response = requests.delete(url + f"messages/{message_id}", headers=headers)
    if response.status_code == 204:
        print("Message deleted successfully!")
    else:
        print("Failed to delete message.")


delete_message(message_id)