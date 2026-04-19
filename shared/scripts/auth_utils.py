import os
import sys

def get_api_key():
    """Pobiera LINGUOFLOW_API_KEY ze zmiennych środowiskowych."""
    api_key = os.getenv("LINGUOFLOW_API_KEY")
    if not api_key:
        print("Error: LINGUOFLOW_API_KEY environment variable not set")
        sys.exit(1)
    return api_key

def get_base_url():
    """Zwraca bazowy URL do API."""
    return "http://localhost:3000/api"
