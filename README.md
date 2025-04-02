# Background Removal Service 🖼️✂️
## *Jayethian Image Background Remover*

A Flask-based backend service that automatically removes backgrounds from uploaded images using AI-powered `rembg` library, with a React frontend for easy interaction.

## Features ✨

- **AI-Powered Background Removal**: Uses `rembg` (U²-Net model) for high-quality background removal
- **Simple API**: RESTful endpoints for easy integration
- **Cross-Origin Support**: CORS enabled for frontend compatibility
- **Secure File Handling**: Automatic sanitization of filenames and temp file cleanup
- **Responsive Frontend**: React-based UI with loading states and error handling

## Tech Stack 🛠️

### Backend (Flask)
- Python 3.8+
- Flask (Web framework)
- rembg (Background removal)
- Werkzeug (File security)
- Flask-CORS (Cross-origin support)

### Frontend (React)
- React 18+
- Fetch API for HTTP requests
- CSS animations for loading spinner
- Responsive design

## Installation 💻

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jayet/background-remover.git
   cd background-remover/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## API Endpoints 🌐

### `POST /upload`
- **Purpose**: Upload an image for background removal
- **Request**: 
  - `Content-Type`: multipart/form-data
  - Body: `image` (file field)
- **Response**:
  ```json
  {
    "success": boolean,
    "message": string,
    "download_link": string,
    "filename": string
  }
  ```

### `GET /download/<filename>`
- **Purpose**: Download processed image
- **Response**: File attachment

## Usage Example 🚀

1. Open the React frontend at `http://localhost:3000`
2. Click "Choose an Image" to select a file
3. Click "Remove Image Background" to process
4. Wait for processing to complete (spinner will show)
5. Download will start automatically when ready

## Project Structure 📂

```
background-remover/
├── backend/
│   ├── app.py               # Flask application
│   ├── requirements.txt     # Python dependencies
│   └── uploads/             # Temporary file storage
└── frontend/
    ├── public/              # Static assets
    ├── src/
    │   ├── components/      # React components
    │   ├── App.js           # Main application
    │   └── index.js         # Entry point
    ├── package.json         # Frontend dependencies
    └── README.md            # Frontend documentation
```

## Configuration ⚙️

### Backend Environment Variables
Create a `.env` file in the backend directory:
```
FLASK_ENV=development
MAX_CONTENT_LENGTH=10485760  # 10MB file size limit
```

### Frontend Configuration
Edit `src/config.js` to modify API base URL:
```javascript
export const API_BASE_URL = 'http://localhost:5000';
```

## Troubleshooting 🛠

**Common Issues:**
- **CORS Errors**: Ensure `flask-cors` is properly installed and configured
- **File Upload Fails**: Check file size (default limit: 10MB)
- **Background Removal Fails**: Verify image format (supports JPG, PNG, etc.)

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments 🙏

- The `rembg` library by Daniel Gatis
- Flask community for the excellent web framework
- React team for the frontend library

---

**Happy background removing!** 🎨➡️🖼️
*Signed Jayetheus*