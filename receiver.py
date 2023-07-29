from flask import Flask, request, render_template
import pickle
import datetime # Import datetime library
import uuid # Import uuid library

app = Flask(__name__)

@app.route('/record', methods=['POST'])
def record():
    # Get the files from the request
    output_file = request.files['output']
    events_file = request.files['events']

    # Generate unique file names using timestamp or random string
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S') # Get current timestamp as a string
    random_string = uuid.uuid4().hex # Get a random string using uuid library
    output_file_name = f'output_{timestamp}_{random_string}.png' # Change this line to use unique file name for output.png
    events_file_name = f'events_{timestamp}_{random_string}.pkl' # Change this line to use unique file name for output.pkl

    # Save the files in the current directory with unique file names
    output_file.save(output_file_name)
    events_file.save(events_file_name)

    # Load the keyboard events from the output.pkl file
    with open(events_file_name, 'rb') as f:
        events = pickle.load(f)

    # Render a HTML template that displays the screenshot and the keyboard events
    return render_template('record.html', events=events)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500, )
