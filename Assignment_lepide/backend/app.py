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
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    try:
        file.save(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            file_content = f.read()
        return jsonify({'content': file_content}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    content = data.get('content', '')
    if not content:
        return jsonify({'error': 'No content provided for summarization'}), 400
    
    summary = summarize_text(content)
    return jsonify({'summary': summary}), 200

if __name__ == '__main__':
    app.run(debug=True)
