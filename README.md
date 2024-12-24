# Web Extension Backend

## Overview
This backend supports the Web History Analyzer Chrome extension by handling authentication, data storage, and analysis.

## Features
- Google Firebase integration
- User activity tracking
- RESTful API for frontend integration

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run locally: `python app.py`

## API Endpoints
- `/authenticate` - Verifies user token.
- `/save-activity` - Saves user web activity.
- `/get-activity/<user_id>` - Fetches user activity data.
