import logging
import os

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/rag_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Create logger
logger = logging.getLogger("RAG_APPLICATION")