#!/usr/bin/env python3
import os
import sys
import json
import requests

# list-exams.py - Lists and filters exams from the LinguoFlow API
# Usage: ./list-exams.py [search_pattern]

def main():
    api_key = os.getenv("LINGUOFLOW_API_KEY")
    if not api_key:
        print("Error: LINGUOFLOW_API_KEY environment variable not set")
        sys.exit(1)

    query = sys.argv[1] if len(sys.argv) > 1 else None
    url = "http://localhost:3000/api/exams"
    headers = {"x-api-key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        exams = data.get("exams", [])

        if query:
            query_lower = query.lower()
            exams = [e for e in exams if query_lower in e.get("test_metadata", {}).get("test_name", "").lower()]

        if not exams:
            if query:
                print(f"No exams matching '{query}' found.")
            else:
                print("No exams found.")
            return

        # Simple table formatting
        header = f"{'ID':<20} | {'Name':<40} | {'Level':<6} | {'Status':<10}"
        print(header)
        print("-" * len(header))
        
        for exam in exams:
            meta = exam.get("test_metadata", {})
            name = meta.get("test_name", "N/A")
            level = meta.get("target_level", "N/A")
            status = exam.get("status", "N/A")
            exam_id = exam.get("id", "N/A")
            
            # Truncate name if too long for table
            display_name = (name[:37] + '..') if len(name) > 40 else name
            print(f"{exam_id:<20} | {display_name:<40} | {level:<6} | {status:<10}")

    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e.response.status_code} - {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
