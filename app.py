from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Mock database to store user settings
USER_SETTINGS_DB = {
    "user_1": {
        "theme": "dark",
        "language": "en",
        "notifications": True
    }
}

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data representing your projects
PROJECTS = [
    {
        "id": 1,
        "title": "Weather Data API",
        "description": "A RESTful API built with Flask and PostgreSQL that aggregates historical weather data.",
        "tech_stack": ["Python", "Flask", "PostgreSQL", "Docker"],
        "github_url": "https://github.com/asalehtx/weather-api",
        "live_demo": "/api/v1/weather-demo" 
    },
    {
        "id": 2,
        "title": "Auth Microservice",
        "description": "JWT-based authentication server built for microservice architectures.",
        "tech_stack": ["Node.js", "Express", "MongoDB", "Redis"],
        "github_url": "https://github.com/asalehtx/auth-service",
        "live_demo": None
    },
    {
        "id": 3,
        "title": "User Configuration Manager",
        "description": "A complete CRUD REST API that allows applications to store, retrieve, modify, and delete user preferences (theme, language, etc).",
        "tech_stack": ["Python", "Flask", "REST API"],
        "github_url": "https://github.com/asalehtx/flask-portfolio",
        "live_demo": "/api/users/user_1/settings" 
    }
]

@app.route('/')
def home():
    """Renders the portfolio homepage."""
    return render_template('index.html', projects=PROJECTS)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Renders a detailed page for a specific project."""
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if project:
        return render_template('project.html', project=project)
    return "Project not found", 404

# --- LIVE API DEMO ENDPOINT ---
@app.route('/api/v1/weather-demo')
def weather_demo():
    """A live demonstration endpoint to show off your API skills."""
    return jsonify({
        "status": "success",
        "data": {
            "location": "Chicago, IL",
            "temperature_c": 22,
            "condition": "Partly Cloudy"
        },
        "message": "This is a live demo endpoint hosted directly on my portfolio!"
    })

# --- USER CONFIGURATION MANAGER API ---

@app.route('/api/users/<user_id>/settings', methods=['GET'])
def get_settings(user_id):
    """READ: View a user's current settings."""
    settings = USER_SETTINGS_DB.get(user_id)
    if not settings:
        return jsonify({"error": "User settings not found"}), 404
    
    return jsonify({
        "message": "Settings retrieved successfully",
        "data": settings
    }), 200

@app.route('/api/users/<user_id>/settings', methods=['POST'])
def create_settings(user_id):
    """CREATE: Add settings for a new user."""
    if user_id in USER_SETTINGS_DB:
        return jsonify({"error": "Settings already exist for this user"}), 400
    
    data = request.get_json()
    
    # Set defaults if the user didn't provide specific fields
    USER_SETTINGS_DB[user_id] = {
        "theme": data.get("theme", "light"),
        "language": data.get("language", "en"),
        "notifications": data.get("notifications", True)
    }
    
    return jsonify({
        "message": f"Settings created for {user_id}",
        "data": USER_SETTINGS_DB[user_id]
    }), 201

@app.route('/api/users/<user_id>/settings', methods=['PUT'])
def update_settings(user_id):
    """UPDATE: Modify existing settings."""
    if user_id not in USER_SETTINGS_DB:
        return jsonify({"error": "User settings not found"}), 404
    
    data = request.get_json()
    
    # Update only the provided fields
    if "theme" in data:
        USER_SETTINGS_DB[user_id]["theme"] = data["theme"]
    if "language" in data:
        USER_SETTINGS_DB[user_id]["language"] = data["language"]
    if "notifications" in data:
        USER_SETTINGS_DB[user_id]["notifications"] = data["notifications"]
        
    return jsonify({
        "message": f"Settings updated for {user_id}",
        "data": USER_SETTINGS_DB[user_id]
    }), 200

@app.route('/api/users/<user_id>/settings', methods=['DELETE'])
def delete_settings(user_id):
    """DELETE: Remove a user's settings."""
    if user_id in USER_SETTINGS_DB:
        del USER_SETTINGS_DB[user_id]
        return jsonify({"message": f"Settings deleted for {user_id}"}), 200
        
    return jsonify({"error": "User settings not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)