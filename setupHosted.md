To build, set up, and deploy the **AcademicInsights Web Extension** using a cloud backend hosting, here’s a comprehensive step-by-step guide:

---

## **Step 1: Project Structure**

### **Backend** (`web-extension-backend/`)
```
web-extension-backend/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── routes.py            # API routes
│   ├── scraping/
│   │   ├── scraper.py       # Web scraping logic
│   │   ├── nlp_analysis.py  # NLP for content analysis
│   │   ├── ml_models.py     # ML models for learning styles
├── requirements.txt         # Backend dependencies
├── app.py                   # Entry point for Flask app
├── config.py                # Configuration (e.g., Firebase credentials)
├── firebase-admin-key.json  # Firebase Admin SDK credentials
├── Dockerfile               # Docker setup for backend
├── README.md                # Documentation
```

---

### **Frontend** (`web-extension/`)
```
web-extension/
├── icons/
│   ├── icon16.png
│   ├── icon48.png
│   ├── icon128.png
├── popup.html               # Extension popup UI
├── popup.js                 # Frontend logic
├── styles.css               # Styling for the popup
├── manifest.json            # Chrome extension configuration
├── firebase-config.js       # Firebase configuration for frontend
```

---

## **Step 2: Backend Setup**

### **1. Create a Virtual Environment**
```bash
cd web-extension-backend
python3 -m venv venv
source venv/bin/activate
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Backend Locally**
```bash
python app.py
```

Verify the backend runs at `http://localhost:5000`.

---

### **4. Dockerize the Backend**

Build and run the Docker container:
```bash
docker build -t web-extension-backend .
docker run -p 5000:5000 web-extension-backend
```

---

### **5. Deploy Backend to the Cloud**

#### **Option A: AWS Elastic Beanstalk**
1. Initialize the Elastic Beanstalk project:
   ```bash
   eb init
   ```
2. Deploy the backend:
   ```bash
   eb create web-extension-env
   ```

#### **Option B: Heroku**
1. Create a `Procfile`:
   ```plaintext
   web: gunicorn app:app
   ```
2. Deploy to Heroku:
   ```bash
   heroku create
   git push heroku main
   ```

#### **Option C: Google Cloud Run**
1. Build the Docker image:
   ```bash
   gcloud builds submit --tag gcr.io/your-project-id/web-extension-backend
   ```
2. Deploy to Cloud Run:
   ```bash
   gcloud run deploy --image gcr.io/your-project-id/web-extension-backend
   ```

---

## **Step 3: Frontend Setup**

### **1. Configure `manifest.json`**
Update `web-extension/manifest.json`:
```json
{
  "manifest_version": 3,
  "name": "Web History Analyzer",
  "version": "1.0",
  "permissions": ["history", "storage", "activeTab"],
  "host_permissions": ["<all_urls>"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": "icons/icon16.png"
  },
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

---

### **2. Update Frontend Logic (`popup.js`)**

- Point the API base URL to the deployed backend:
```javascript
const BASE_URL = "https://your-backend-url.com"; // Replace with your backend's URL

// Example API call
fetch(`${BASE_URL}/analyze-website`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: "FirebaseIDToken" // Replace with actual token
  },
  body: JSON.stringify({ url: "https://example.com" })
})
  .then((response) => response.json())
  .then((data) => console.log("Analysis Results:", data))
  .catch((error) => console.error("Error:", error));
```

---

### **3. Load the Extension**
1. Go to `chrome://extensions/` in your browser.
2. Enable **Developer Mode**.
3. Click **Load unpacked** and select the `web-extension/` folder.

---

## **Step 4: Testing**

### **Backend Testing**
- Use **Postman** or **curl** to test endpoints:
  - `/authenticate`
  - `/analyze-website`
  - `/dashboard/<user_id>`

---

### **Frontend Testing**
1. Sign in using Google.
2. Visit a few websites.
3. Use the "Analyze History" feature in the extension popup.
4. Verify results are displayed (e.g., learning styles, topic categorization).

---

## **Step 5: Deploy the Extension**

1. **Package the Extension**:
   - Zip the `web-extension/` folder (excluding irrelevant files like `.git`).

2. **Submit to the Chrome Web Store**:
   - Go to the [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole/).
   - Upload the ZIP file and provide details (e.g., name, description, screenshots).
   - Submit for review.

3. **Monitor Feedback**:
   - Address any issues flagged during the review process.
   - Update the extension as necessary.

---

## **Step 6: Deployment for Researchers**

1. **Provide Backend Access**:
   - Host the backend on a stable cloud platform.
   - Share the backend API base URL with researchers.

2. **Distribute the Extension**:
   - Researchers can download the extension directly from the Chrome Web Store or as a ZIP file to install manually.

3. **Documentation for Researchers**:
   - Create a `README.md` or user guide detailing:
     - How to set up Firebase Authentication.
     - How to use the extension (e.g., sign in, analyze history).
     - Backend endpoints available for research.

---

## **Summary of Steps**

1. **Set Up Backend**:
   - Install dependencies, run locally, dockerize, and deploy to the cloud.

2. **Set Up Frontend**:
   - Update API URLs, test the extension, and package for deployment.

3. **Deploy**:
   - Publish the extension to the Chrome Web Store.
   - Host the backend on AWS, Heroku, or GCP.

4. **Documentation**:
   - Provide detailed instructions for subjects

