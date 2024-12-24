from flask import Blueprint, request, jsonify
from firebase_admin import auth, firestore
from datetime import datetime
from flask import Blueprint, request, jsonify
from .scraping.scraper import scrape_website
from .scraping.nlp_analysis import categorize_content
from .scraping.ml_models import predict_learning_style
from functools import wraps
from flask import Blueprint, request, jsonify
from firebase_admin import auth, firestore

db = firestore.client()
main = Blueprint("main", __name__)

# Root route
@main.route("/")
def home():
    return jsonify({"message": "Welcome to the Web Extension Backend!"}), 200

# Save user web activity
@main.route("/save-activity", methods=["POST"])
def save_activity():
    data = request.json
    user_id = data.get("user_id")
    activity = data.get("activity")
    if not user_id or not activity:
        return jsonify({"error": "Missing user_id or activity data"}), 400

    try:
        db.collection("users").document(user_id).collection("activities").add({
            "activity": activity,
            "timestamp": datetime.utcnow()
        })
        return jsonify({"message": "Activity saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get user web activity
@main.route("/get-activity/<user_id>", methods=["GET"])
def get_activity(user_id):
    try:
        activities_ref = db.collection("users").document(user_id).collection("activities")
        activities = [doc.to_dict() for doc in activities_ref.stream()]
        return jsonify({"activities": activities}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Authenticate user
@main.route("/authenticate", methods=["POST"])
def authenticate():
    id_token = request.json.get("id_token")
    if not id_token:
        return jsonify({"error": "Missing id_token"}), 400

    try:
        decoded_token = auth.verify_id_token(id_token)
        user_id = decoded_token["uid"]
        return jsonify({"user_id": user_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
@main.route("/analyze-website", methods=["POST"])
def analyze_website():
    data = request.json
    url = data.get("url")
    
    # Scrape website
    scraped_data = scrape_website(url)
    if "error" in scraped_data:
        return jsonify({"error": scraped_data["error"]}), 400
    
    # NLP for topic categorization
    text = scraped_data.get("text", "")
    topic_info = categorize_content(text)
    
    # Learning style prediction
    features = [
        len(text.split()) / 1000,  # Approximate text density
        scraped_data["images"],
        scraped_data["videos"],
        scraped_data["audio"]
    ]
    learning_style = predict_learning_style(features)
    
    return jsonify({
        "url": url,
        "topic": topic_info["topic"],
        "relevance_score": topic_info["relevance_score"],
        "learning_style": learning_style
    })

@main.route("/dashboard/<user_id>", methods=["GET"])
def firebase_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        id_token = request.headers.get("Authorization")
        if not id_token:
            return jsonify({"error": "Authorization header missing"}), 401
        
        try:
            decoded_token = auth.verify_id_token(id_token)
            request.user = decoded_token
        except Exception as e:
            return jsonify({"error": "Invalid token"}), 401
        
        return f(*args, **kwargs)
    return decorated_function
def dashboard(user_id):
    activities_ref = db.collection("users").document(user_id).collection("activities")
    activities = [doc.to_dict() for doc in activities_ref.stream()]
    
    # Aggregate insights
    topic_counts = {}
    learning_styles = {}
    
    for activity in activities:
        topic = activity.get("topic")
        learning_style = activity.get("learning_style")
        topic_counts[topic] = topic_counts.get(topic, 0) + 1
        learning_styles[learning_style] = learning_styles.get(learning_style, 0) + 1
    
    return jsonify({
        "topic_counts": topic_counts,
        "learning_styles": learning_styles,
        "total_activities": len(activities),
        "message": f"Welcome, {request.user['email']}"
    })



