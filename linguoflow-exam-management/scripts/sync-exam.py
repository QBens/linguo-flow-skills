#!/usr/bin/env python3
import os
import sys
import json
import requests

# sync-exam.py - Synchronizes an exam JSON file with the LinguoFlow API
# Usage: ./sync-exam.py [file.json] [METHOD: POST/PUT/PATCH] [ID]

def main():
    api_key = os.getenv("LINGUOFLOW_API_KEY")
    if not api_key:
        print("Error: LINGUOFLOW_API_KEY environment variable not set")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Usage: ./sync-exam.py [file.json] [METHOD: POST/PUT/PATCH] [ID]")
        sys.exit(1)

    file_path = sys.argv[1]
    method = sys.argv[2].upper()
    exam_id = sys.argv[3] if len(sys.argv) > 3 else None

    if method in ["PUT", "PATCH"] and not exam_id:
        print(f"Error: Exam ID is required for {method}")
        sys.exit(1)

    with open(file_path, 'r') as f:
        data = json.load(f)

    url = "http://localhost:3000/api/exams"
    if exam_id:
        url = f"{url}/{exam_id}"

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    print(f"Syncing {file_path} using {method} to {url}...")
    
    # Create backup for state-changing operations
    if method in ["PUT", "PATCH"]:
        import shutil
        from datetime import datetime
        
        backup_dir = "backups"
        os.makedirs(backup_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.basename(file_path)
        backup_path = os.path.join(backup_dir, f"{timestamp}_{base_name}.bak")
        
        print(f"Creating local backup: {backup_path}")
        shutil.copy2(file_path, backup_path)
    
    if method == "POST":
        response = requests.post(url, headers=headers, json=data)
    elif method == "PUT":
        response = requests.put(url, headers=headers, json=data)
    elif method == "PATCH":
        response = requests.patch(url, headers=headers, json=data)
    else:
        print(f"Unsupported method: {method}")
        sys.exit(1)

    if response.status_code in [200, 201]:
        print("Sync successful!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error {response.status_code}: {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    main()
