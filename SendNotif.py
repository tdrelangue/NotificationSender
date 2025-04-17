from pushbullet import Pushbullet
import time
import traceback
import sys
import argparse


def CollectAPIKey():
    parser = argparse.ArgumentParser(description='combines files into a pickle object, processes the data, and divides into training sets')
    parser.add_argument('-apikey', dest='apikey', default=None, type=str,
                    help='Api key for push bullet')
    args,_ = parser.parse_known_args()
    
    if args.apikey:
        # If the user provided a key in the cammand we use it
        # Usage: python Geo_Extraction.py <api_key>
        api_key = sys.argv[1]
    else:
        try:
            import os
            from dotenv import load_dotenv
            #if not we try to Load the API key from the .env file
            load_dotenv()
            # Retrieve values from environment variables
            api_key = os.getenv('API_KEY') 
        except :
            # If we can't load the API key from the .env file we ask for it directly
            print("No API provided.")
            api_key = input("Please type your API key then press enter: ")
            print("Next time you want to use this software, know that you can provide your API key by:")
            print("1. Creating a .env file in the same directory as this script with the variable API_KEY")
            print("2. Launching the script with this command: python Geo_Extraction.py <your_api_key>")
    
    return api_key


def SendNotif(title = "Test Notification", body = "This is a test message from Python.", API_KEY=None, feedback=False):
    # Load environment variables from .env file
    if API_KEY is None:
        API_KEY = CollectAPIKey()

    # Initialize the Pushbullet client
    pb = Pushbullet(API_KEY)

    # Send a notification
    push = pb.push_note(title, body)

    if feedback:
        print("Notification sent!" if push else "Failed to send notification.")


import time
import traceback
from pushbullet import Pushbullet

def SendNotif(title="Test Notification", body="This is a test message from Python.", API_KEY=None, feedback=False):
    """Sends a notification using Pushbullet."""
    if API_KEY is None:
        API_KEY = CollectAPIKey()

    pb = Pushbullet(API_KEY)
    push = pb.push_note(title, body)

    if feedback:
        print("Notification sent!" if push else "Failed to send notification.")

def notify_on_completion(func):
    """Decorator to notify upon function success or failure, including runtime."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            runtime = end_time - start_time
            SendNotif(
                title=f"✅ {func.__name__} Completed",
                body=f"Function '{func.__name__}' ran successfully in {runtime:.2f} seconds."
            )
            return result
        except Exception as e:
            end_time = time.time()
            runtime = end_time - start_time
            error_message = f"Function '{func.__name__}' failed after {runtime:.2f} seconds.\nError: {str(e)}"
            SendNotif(
                title=f"❌ {func.__name__} Failed",
                body=error_message
            )
            raise  # Re-raise the error so it prints to the screen
    return wrapper


if __name__ == "__main__":
    SendNotif()
    import requests

    data = {
        "title": "🔥 Local Update",
        "message": "Your model finished training!",
        # Optional: include your device token
        "expo_push_token": "ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]"
    }

    requests.post("http://192.168.137.1:5000/send", json=data)
