
# **AcademicInsights: A Template Web Extension for Analyzing Student Academic Behavior Online**

## **Overview**

**AcademicInsights** is a Chrome web extension paired with a backend that enables researchers to analyze students' online academic behavior. This tool uses **web scraping**, **machine learning (ML)**, and **natural language processing (NLP)** to provide insights into learning styles, resource usage, and topic relevance. 

This project serves as a customizable template for **edtech researchers**, facilitating studies on how students utilize online resources for learning and how their behavior correlates with academic success.

---

## **Features**
- **Web Scraping**: Extracts and analyzes visited website content.
- **Learning Style Identification**: Classifies behavior into Visual, Auditory, Reading/Writing, or Kinesthetic styles.
- **Topic Categorization**: Matches content to admin-defined academic topics.
- **Google Sign-In**: Authenticates users securely.
- **Backend Integration**: Provides a robust backend API for data processing and storage.
- **Customizable**: Designed for easy adaptation to specific research needs.

---

## **Project Structure**

### **Backend**
```plaintext
backend/
├── app/
│   ├── scraping/               # Web scraping and analysis
│   │   ├── scraper.py          # Scrapes website data
│   │   ├── nlp_analysis.py     # NLP for topic categorization
│   │   ├── ml_models.py        # ML models for learning styles
│   ├── __init__.py             # Initializes Flask app
│   ├── routes.py               # API routes
│   ├── models.py               # Data models for backend (optional)
├── app.py                      # Entry point for the backend
├── config.py                   # Configuration for Firebase and other settings
├── firebase-admin-key.json     # Firebase Admin SDK credentials
├── Dockerfile                  # Docker container configuration
├── requirements.txt            # Backend dependencies
```

### **Frontend**
```plaintext
frontend/
├── icons/                      # Extension icons
│   ├── icon16.jpg
│   ├── icon48.jpg
│   ├── icon128.jpg
├── background.js               # Background script for the extension
├── firebase-config.js          # Firebase configuration for frontend
├── manifest.json               # Chrome extension configuration
├── popup.html                  # HTML for the extension's popup UI
├── popup.js                    # Frontend logic for the popup
├── styles.css                  # CSS for the popup
```

---

## **Getting Started**

### **1. Prerequisites**
- Python 3.9+
- Node.js (optional for additional tools)
- Chrome Browser
- Docker (for backend deployment)
- Firebase Project for Authentication

---

### **2. Backend Setup**

#### **Local Setup**
1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend:
   ```bash
   python app.py
   ```
   The backend will be available at `http://localhost:5000`.

#### **Docker Setup**
1. Build the Docker image:
   ```bash
   docker build -t academic-insights-backend .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 academic-insights-backend
   ```

#### **Files of Interest**
- **API Endpoints**: `app/routes.py`
- **Web Scraping Logic**: `app/scraping/scraper.py`
- **NLP Analysis**: `app/scraping/nlp_analysis.py`
- **Learning Style ML Models**: `app/scraping/ml_models.py`

---

### **3. Frontend Setup**

#### **Local Setup**
1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer Mode**.
3. Click **Load unpacked** and select the `frontend/` folder.

#### **Files of Interest**
- **Extension Configuration**: `frontend/manifest.json`
- **Popup Logic**: `frontend/popup.js`
- **Firebase Configuration**: `frontend/firebase-config.js`

---

### **4. Firebase Setup**
1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/).
2. Enable **Google Authentication** under `Authentication > Sign-in method`.
3. Download the **Admin SDK JSON key** and place it in `backend/firebase-admin-key.json`.
4. Add Firebase configuration to `frontend/firebase-config.js`:
   ```javascript
   export const firebaseConfig = {
     apiKey: "YOUR_API_KEY",
     authDomain: "YOUR_AUTH_DOMAIN",
     projectId: "YOUR_PROJECT_ID",
     storageBucket: "YOUR_STORAGE_BUCKET",
     messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
     appId: "YOUR_APP_ID",
   };
   ```

---

### **5. Deployment**

#### **Backend Deployment**
- Deploy the backend using **Heroku**, **AWS**, or **Google Cloud Run**.
- Update `frontend/popup.js` with the deployed backend URL:
   ```javascript
   const BASE_URL = "https://your-backend-url.com";
   ```

#### **Frontend Deployment**
1. Package the extension:
   - Zip the `frontend/` folder.
2. Submit to the [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole/).

---

## **Using the Tool**

1. **Google Sign-In**:
   - Authenticate using a Google account.
2. **Track Web Activity**:
   - Visit websites and let the extension scrape content.
3. **Analyze Insights**:
   - View learning styles and topic categorization in the extension popup.

---

## **Customization Guide**

1. **Add New Topics**:
   - Edit `app/scraping/nlp_analysis.py` to include new topics and keywords.

2. **Modify Learning Style Models**:
   - Update or retrain models in `app/scraping/ml_models.py` for different user behavior datasets.

3. **Extension UI Customization**:
   - Edit `frontend/popup.html` and `frontend/styles.css`.

---

## **For Researcher Use**

- **Data Access**:
  - Use the `/dashboard/<user_id>` endpoint in `backend/app/routes.py` to retrieve user data.
- **Documentation**:
  - Refer to `backendinstructions.md` for backend setup and `setupLocal.md` or `setupHosted.md` for deployment.

---

## **Future Enhancements**
- Add more advanced NLP models (e.g., GPT-based summarization).
- Enable real-time monitoring with WebSockets.
- Add more robust privacy features for anonymizing user data.

---

## **Support**

For issues, please contact me or open an issue on the project repository! Thanks!