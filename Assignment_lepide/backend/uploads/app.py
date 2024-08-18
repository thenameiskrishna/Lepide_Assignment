from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from summarizer import summarize_text

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    with open(filepath, 'r') as f:
        file_content = f.read()
    
    return jsonify({'content': file_content})

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    content = data.get('content', '')
    
    # Call the summarization function from summarizer.py
    summary = summarize_text(content)
    
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
