from flask import Flask
from flask_cors import CORS
from api import api_blueprint  # Import API routes from api.py
import os

app = Flask(__name__)
CORS(app)

# Register API routes
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    # Use the dynamic PORT assigned by Render
    port = int(os.environ.get('PORT', 3000))  # Fallback to 3000 if PORT is not set
    app.run(host='0.0.0.0', port=port)  # Dynamic port for Render