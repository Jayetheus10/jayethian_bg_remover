from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import tempfile
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
CORS(app, origins=["https://jayethian-image-rb.netlify.app/"])


UPLOAD_FOLDER = tempfile.gettempdir()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "Empty filename"}), 400
    

    filename = secure_filename(file.filename)
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)
    
    try:

        with open(upload_path, 'rb') as f:
            input_image = f.read()
        
        output_image = remove(input_image)  
        

        processed_filename = f"no_bg_{filename}"
        processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        
        with open(processed_path, 'wb') as f:
            f.write(output_image)
        

        download_link = f"https://jayethian-image-rb.netlify.app//download/{processed_filename}"
        
        return jsonify({
            "success" : True,
            "message": "Background removed successfully",
            "download_link": download_link,
            "filename": processed_filename
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        # Clean up original file
        if os.path.exists(upload_path):
            os.remove(upload_path)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    print("Download request for:", filename)
    safe_filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
    
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    
    return send_file(
        file_path,
        as_attachment=True,
        download_name=safe_filename
    )
