import time
import openai
import logging
import re
import plotly.graph_objects as go
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Retrieve the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(filename='evaluation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
