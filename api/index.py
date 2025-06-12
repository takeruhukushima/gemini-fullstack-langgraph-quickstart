from fastapi import FastAPI
import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/backend")

# Import the FastAPI app from the backend
from src.agent.app import app as backend_app

# Create a new FastAPI app that will be used by Vercel
app = FastAPI()

# Mount the backend app at the root
app.mount("/", backend_app)
