from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join('uploads', filename))
            return f'File {filename} uploaded successfully!'
    files = os.listdir('uploads')
    return render_template('index.html', files=files)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join('uploads', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)
