import requests
import sys
import os

def send_file_to_slack(token, channel_id, filepath, text_message):
    # Validate if the file exists
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist.")
        return

    # Prepare headers for file upload
    headers = {"Authorization": f"Bearer {token}"}

    # Open the file and prepare for upload
    with open(filepath, "rb") as f:
        files = {'file': f}
        data = {
            'channels': channel_id,
            'initial_comment': text_message
        }
        # Upload the file to Slack
        response = requests.post("https://slack.com/api/files.upload", headers=headers, files=files, data=data)

        if response.status_code == 200 and response.json()['ok']:
            print(f"File {filepath} uploaded successfully to channel ID {channel_id}.")
        else:
            print(f"Failed to upload file. Status code: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python SendFileToSlack.py <bot_token> <channel_id> <file_path> <text_message>")
        sys.exit(1)

    bot_token = sys.argv[1]
    channel_id = sys.argv[2]
    file_path = sys.argv[3]
    text_message = sys.argv[4]

    send_file_to_slack(bot_token, channel_id, file_path, text_message)
