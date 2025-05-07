from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Security configurations
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit

# Allowed file types
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'mkv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_content():
    content_type = request.form.get('content_type')
    platforms = request.form.getlist('platforms')

    if content_type == "youtube":
        youtube_url = request.form.get('youtube_url')
        # Process YouTube URL (integration with AI for content repurposing)
        return jsonify({"status": "success", "message": "Content processed for YouTube URL", "platforms": platforms})
    
    elif content_type == "upload":
        if 'video_file' not in request.files:
            return jsonify({"status": "error", "message": "No file part"})
        
        file = request.files['video_file']
        if file.filename == '':
            return jsonify({"status": "error", "message": "No selected file"})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Process the uploaded file (integration with AI for content repurposing)
            return jsonify({"status": "success", "message": "Content processed for uploaded video", "platforms": platforms})
    
    return jsonify({"status": "error", "message": "Invalid request"})

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)