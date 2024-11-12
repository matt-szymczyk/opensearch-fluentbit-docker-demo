import logging
import time
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def generate_logs():
    while True:
        actions = ["login", "logout", "purchase", "view_page", "add_to_cart"]
        status_codes = [200, 201, 400, 401, 500]
        
        logger.info({
            "action": random.choice(actions),
            "status_code": random.choice(status_codes),
            "user_id": random.randint(1, 1000)
        })
        time.sleep(2)

if __name__ == "__main__":
    logger.info("Application started")
    generate_logs()
