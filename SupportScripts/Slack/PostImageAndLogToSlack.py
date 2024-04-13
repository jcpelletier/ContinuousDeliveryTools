import os
import argparse
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def parse_arguments():
    parser = argparse.ArgumentParser(description='Post a message to Slack with optional images and log file.')
    parser.add_argument('message', help='Message to post on Slack')
    parser.add_argument('directory', help='Directory to search for PNG files')
    parser.add_argument('log_file', help='Path to the log file')
    parser.add_argument('channel_id', help='Slack channel ID')
    return parser.parse_args()

def post_message(client, channel, message, thread_ts=None):
    try:
        response = client.chat_postMessage(channel=channel, text=message, thread_ts=thread_ts)
        return response['ts']  # Timestamp of the message
    except SlackApiError as e:
        print(f"Error posting message: {e}")
        return None

def upload_files(client, channel, thread_ts, files):
    for file in files:
        try:
            client.files_upload_v2(channels=channel, file=file, thread_ts=thread_ts)
        except SlackApiError as e:
            print(f"Error uploading file {file}: {e}")

def find_png_files(directory):
    png_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.png')]
    png_files.sort(key=lambda f: os.path.getmtime(f))  # Sort files by timestamp
    return png_files

def main():
    args = parse_arguments()

    # Initialize Slack client
    slack_token = os.environ['SLACK_API_TOKEN']
    client = WebClient(token=slack_token)
    channel = args.channel_id

    # Post the initial message and get its timestamp
    thread_ts = post_message(client, channel, args.message)

    # Find and upload PNG files in the order of their timestamps as replies in the thread
    png_files = find_png_files(args.directory)
    if thread_ts and png_files:
        upload_files(client, channel, thread_ts, png_files)

    # Ensure all files have been uploaded before posting log content
    if thread_ts and os.path.exists(args.log_file):
        with open(args.log_file, 'r') as file:
            log_content = file.read()
            if log_content:
                # Adding a short delay to ensure file uploads are completed
                # You can adjust the sleep time as needed
                import time
                time.sleep(30)  # Wait for 15 seconds

                post_message(client, channel, log_content, thread_ts=thread_ts)

if __name__ == '__main__':
    main()
