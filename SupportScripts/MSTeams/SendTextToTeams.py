import json
import requests
import sys


def send_message_to_teams(webhook_url, subject=None, message=None, image_urls=None):
    """
    Sends a message to a Microsoft Teams channel via an incoming webhook with optional subject, message, and multiple images.

    Args:
    webhook_url (str): The URL of the Microsoft Teams channel webhook.
    subject (str, optional): The subject of the message card. Defaults to None.
    message (str, optional): The text message to send to the Teams channel. Defaults to None.
    image_urls (list, optional): The URLs of the images to include in the message. Defaults to None.
    """

    # Initialize 'data' dictionary with required '@type' and '@context'
    data = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
    }

    # Check if a subject is provided
    if subject:
        data["title"] = subject

    # Check if a message is provided
    if message:
        data["text"] = message

    # Check if image URLs are provided
    if image_urls:
        sections = []
        for url in image_urls:
            # Log each image URL
            print(f"Adding image URL to message: {url}")
            # Create separate sections for the image and the clickable link
            image_section = {
                "images": [{"image": url}]
            }
            link_section = {
                "text": f"[{url}]({url})"
            }
            sections.extend([image_section, link_section])  # Add both sections to the list

        data["sections"] = sections  # Assign the list of sections to 'data'

    # Log the message card JSON payload
    print("Sending message card with payload:")
    print(json.dumps(data, indent=4))

    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message, status code: {response.status_code}")


if __name__ == "__main__":
    # Parse command line arguments
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: python script.py <webhook_url> [subject] [message] [path_to_image_urls_file]")
        sys.exit(1)

    # Assign arguments to variables
    webhook_url = args[0]
    subject = args[1] if len(args) > 1 else None
    message = args[2] if len(args) > 2 else None
    image_urls = None

    # Check if the image URLs file argument is provided
    if len(args) > 3:
        image_urls_file = args[3]
        try:
            with open(image_urls_file, 'r') as file:
                image_urls = [line.strip() for line in file.readlines()]
                print(f"Image URLs to send: {len(image_urls)}")
        except FileNotFoundError:
            print(f"Warning: File '{image_urls_file}' not found. Continuing without images.")

    # Send the message to Teams
    send_message_to_teams(webhook_url, subject, message, image_urls)
