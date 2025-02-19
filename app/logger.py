import logging

# Configure Logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def log_request(user_text, intent, response):
    """Log user interactions"""
    logging.info(f"User: {user_text}, Intent: {intent}, Response: {response}")
