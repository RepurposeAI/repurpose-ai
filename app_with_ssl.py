from flask_talisman import Talisman

# Add this to the Flask app
Talisman(app, content_security_policy=None)