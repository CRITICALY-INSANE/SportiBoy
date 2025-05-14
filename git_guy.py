#test
import os
import base64
import requests

global GITHUB_TOKEN,REPO_OWNER,REPO_NAME,FILE_PATH,LOCAL_FILE,NEW_CONTENT
# === CONFIGURATION ===
GITHUB_TOKEN = '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'  # Replace with your GitHub token
#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
REPO_OWNER = 'CRITICALY-INSANE'
REPO_NAME = 'SportiBoy'
FILE_PATH = 'cloud_data.txt'  # GitHub repo path
LOCAL_FILE = 'spotify_report.txt'        # Local file
NEW_CONTENT = 'This is not new content.\nUpdated by Python.'

def new_con(NEW_CONTENT_1):
    global GITHUB_TOKEN,REPO_OWNER,REPO_NAME,FILE_PATH,LOCAL_FILE,NEW_CONTENT
# === STEP 1: Check/Create Local File ===
    NEW_CONTENT=NEW_CONTENT_1
    if not os.path.exists(LOCAL_FILE):
        with open(LOCAL_FILE, 'w') as f:
            f.write(NEW_CONTENT)
    else:
        with open(LOCAL_FILE, 'w') as f:
            f.write(NEW_CONTENT)

    # === STEP 2: Read File and Encode Content ===
    with open(LOCAL_FILE, 'rb') as f:
        encoded_content = base64.b64encode(f.read()).decode('utf-8')

    # === STEP 3: Get File SHA from GitHub (if it exists) ===
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        sha = response.json()['sha']
    else:
        sha = None  # New file

    # === STEP 4: Commit to GitHub ===
    commit_message = "Update or create file via Python"
    data = {
        "message": commit_message,
        "content": encoded_content,
        "branch": "main"
    }
    if sha:
        data["sha"] = sha

    put_response = requests.put(api_url, headers=headers, json=data)

    if put_response.status_code in [200, 201]:
        print("✅ File uploaded/updated on GitHub successfully.")
    else:
        print("❌ Error uploading file:", put_response.json())




##def online():
##    
##    with open('spotify_report.txt', 'r', encoding='utf-8') as file:
##        
##        content = file.read()
##        print(content)  # Optional: Display the content
##        gg.new_con(content)
