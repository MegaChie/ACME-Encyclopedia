from authlib.integrations.flask_client import OAuth

# Initialize the OAuth object
oauth = OAuth()

# Expose the OAuth client globally
__all__ = ['oauth']
