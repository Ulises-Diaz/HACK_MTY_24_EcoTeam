pip install twilio

from twilio.rest import Client
import datetime

# Twilio credentials (replace with your own credentials)
account_sid = 'AC2efdb7e7217bcf31792e413dda3bc2fb'
auth_token = 'b8cf6530677827adafcd5256b68f41eb'
twilio_whatsapp_number = 'whatsapp:+14155238886'  # Your Twilio WhatsApp number

# WhatsApp number of your friend for testing
friend_whatsapp_number = 'whatsapp:+528119046392'

# Initialize Twilio Client
client = Client(account_sid, auth_token)

def send_test_alert(location, severity, injuries, car_plate):
    """
    Sends a WhatsApp message with fake accident details for testing purposes.
    
    Parameters:
        location (str): Fake location of the accident.
        severity (str): Fake severity of the accident.
        injuries (str): Fake injury details.
        car_plate (str): Fake license plate.
    """
    # Get current time
    accident_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the message with fake accident details
    message_body = (
        f"🚨 *Test Accident Alert* 🚨\n\n"
        f"📍 *Location*: {location}\n"
        f"🕒 *Time*: {accident_time}\n"
        f"⚠️ *Severity*: {severity}\n"
        f"🚑 *Injuries*: {injuries}\n"
        f"🚗 *Car Plate*: {car_plate}\n\n"
        f"This is a test message."
    )
    
    try:
        # Send WhatsApp message to your friend's number
        message = client.messages.create(
            body=message_body,
            from_="whatsapp:+14155238886",
            to="whatsapp:+528119046392"
        )
        
        print(f"Test WhatsApp message sent successfully. Message SID: {message.sid}")
    
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")

# Trigger fake accident detection for testing
if __name__ == "__main__":
    # Fake accident details for testing
    location = "Test Street, Test City"
    severity = "Minor"
    injuries = "No injuries"
    car_plate = "TEST 1234"

    # Send the test message
    send_test_alert(location, severity, injuries, car_plate)
