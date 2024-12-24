To build and deploy the backend for your instance of the **AcademicInsights Extension** efficiently, you can follow this step-by-step guide.

### **Step 1: Set Up a Virtual Environment**

Create a Python virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Verify the backend runs locally:

```bash
python app.py
```

The backend should be accessible at `http://localhost:5000`.

---

### **Step 2: Add Docker Support**

Containerize your backend for deployment using Docker.

#### **Dockerfile**:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

#### **Build and Run the Docker Image**:
1. Build the image:
   ```bash
   docker build -t web-extension-backend .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 web-extension-backend
   ```

---

### **Step 3: Deploy the Backend**

Choose a cloud platform to host the backend. Below are some common options:

#### **Option 1: Deploy on AWS (Elastic Beanstalk or EC2)**

1. **Elastic Beanstalk**:
   - Install the Elastic Beanstalk CLI:
     ```bash
     pip install awsebcli
     ```
   - Initialize the project:
     ```bash
     eb init
     ```
   - Deploy the application:
     ```bash
     eb create web-extension-env
     ```

2. **EC2 Instance**:
   - Launch an EC2 instance with Python pre-installed.
   - Install Docker:
     ```bash
     sudo apt update
     sudo apt install docker.io
     ```
   - Transfer files to the instance and build the Docker image:
     ```bash
     docker build -t web-extension-backend .
     docker run -p 5000:5000 web-extension-backend
     ```

---

#### **Option 2: Deploy on Heroku**

1. Install the Heroku CLI:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create web-extension-backend
   ```
4. Add a `Procfile` to the project:
   ```plaintext
   web: gunicorn app:app
   ```
5. Push the app to Heroku:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a web-extension-backend
   git push heroku main
   ```

---

#### **Option 3: Deploy on Google Cloud Platform (GCP)**

1. **Google App Engine**:
   - Create an `app.yaml` file:
     ```yaml
     runtime: python39
     entrypoint: gunicorn -b :$PORT app:app
     ```
   - Deploy the app:
     ```bash
     gcloud app deploy
     ```

2. **Google Kubernetes Engine**:
   - Set up a Kubernetes cluster.
   - Push the Docker image to Google Container Registry (GCR):
     ```bash
     docker tag web-extension-backend gcr.io/<project-id>/web-extension-backend
     docker push gcr.io/<project-id>/web-extension-backend
     ```
   - Deploy the image using Kubernetes YAML configuration.

---

### **Step 4: Update Frontend API URLs**

After deployment, update the API base URL in your extension's `popup.js`:
```javascript
const BASE_URL = "https://your-deployment-url.com";
```

Replace `http://localhost:5000` with your production backend URL.

---

### **Step 5: Secure Your Backend**

1. **Add Authentication**:
   - Verify Firebase ID tokens for all endpoints.
   - Use HTTPS for secure communication.

2. **Rate Limiting**:
   - Protect your APIs from abuse using libraries like `Flask-Limiter`.

3. **Environment Variables**:
   - Use `.env` files or cloud-specific environment variable managers for sensitive data like Firebase credentials.

---

### **Step 6: Monitor and Maintain**

1. **Logging**:
   - Add logging to track requests and errors using Python's `logging` module.

2. **Monitoring**:
   - Use tools like **Prometheus**, **AWS CloudWatch**, or **Google Monitoring** for real-time tracking.

3. **Scaling**:
   - Configure autoscaling for cloud services to handle varying traffic loads.
