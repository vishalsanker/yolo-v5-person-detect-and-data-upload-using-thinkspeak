import requests
import pandas as pd

API_KEY = "RRNTDZDLGYR0LDQQ"  # Write API Key
CHANNEL_ID = "24400265977623"  # Channel ID

# Function to get data from ThingSpeak
def get_thingspeak_data():
    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}&results=1'
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if 'feeds' in data and len(data['feeds']) > 0:
            return data['feeds'][0]  # Return the latest feed
        else:
            return None
    else:
        print("Failed to get data from ThingSpeak")
        return None

# Function to update data to ThingSpeak
def update_latest_data(temp):
    req_url = f'https://api.thingspeak.com/update?api_key={API_KEY}&field1={temp}'
    
    print("Updating data...")
    
    response = requests.get(req_url)
    
    # ThingSpeak returns just the entry ID or 0 if failed, not JSON
    if response.text == '0':
        print("Failed to update data.")
    else:
        print(f"Data updated successfully. Entry ID: {response.text}")

# Example usage
temp = 23  # Temperature data to update
update_latest_data(temp)

latest_data = get_thingspeak_data()
if latest_data:
    print("Latest data from ThingSpeak:", latest_data)
