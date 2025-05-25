# Continuous Delivery Tools
Tools for build and delivery

## CI/CD Scripts
These scripts are intended to be used in a CI/CD environment such as Jenkins. They are written in Python for high portability.

### jiraQuery.py
- Pass Jira credentials and JQL query, and this will return a JSON dump of issues.
- Example:

  ```bash
  python jiraQuery.py "Myemail@domain.com" "MyCredentials" "MyDomain" "Your JQL Query"
  ```

### cleanWorkspace.py
- This script is for the cleanup of build environments. It will remove all files and subfolders from the target location.
- Use this either post or pre-build to remove build and other temporary artifacts from the working directory.
- Example:

  ```bash
  python cleanWorkspace.py "your_folder_path_here"
  ```

### buildUnity.py
- This script will build a Unity project using the specified parameters.
- Example:

  ```bash
  python unity_build.py "path/to/your/unity/editor.exe" "YourJobName" "YourWorkspacePath" "YourBuildNumber"
  ```

## UnityScripts

### Build.cs
This is a simple C# script that automates the process of building your Android Unity project from the command line. Note that it will disable the Oculus XR plugin before building, if it's enabled. This script can be called using `buildUnity.py` in your CI/CD environment to automate the process of producing builds.

#### How to Use

1. Copy the `Build.cs` file into your Unity project's ``Assets`` folder.
2. Make sure you have the necessary Unity Editor and target platform set up for your project.
3. Open your preferred command line interface.
4. Navigate to the root folder of your Unity project.

#### Command Line Arguments

To use this script, you can pass the following command line arguments:

- ``-buildTarget``: Specifies the platform you want to build for. Possible values are "Android" or "StandaloneWindows64" (for Windows).
- ``-buildLocation``: Specifies the output location for the build. For example, if you are building for Android, you might use something like `./Builds/MyGame.apk`. For Windows, you might use `./Builds/MyGame.exe`.
- Example:

  ```bash
  path/to/your/unity/editor.exe -quit -batchmode -projectPath path/to/your/unity/project -executeMethod BuildProject.PerformBuild -buildTarget Android -buildLocation ./Builds/MyGame.apk
  ```

This command will build your Unity project for Android and place the output APK file in the "Builds" folder of your project.

## Playwright Scripts
Playwright is used in this project for end-to-end testing.

### smoketest.js
- Runs a simple smoke test by navigating to Google and taking a screenshot.
- Usage:

  ```bash
  node Playwright/smoketest.js
  ```

## SupportScripts
These scripts supply support for working with various 3rd party services like AWS, Azure, and Slack.

### AWS/DownloadFromS3.py
- This script will download a file from S3 using an environment IAM role or a recent CLI authentication.

  ```bash
  python DownloadFromS3.py <bucket_name> <object_name> <file_name>
  ```

### AWS/AppendFileInS3.py
- This script will append text data to a file in S3 using an environment IAM role or a recent CLI authentication. The script will create the file or add the data as a new line in the existing file.
- This script can be used for storing logs in S3.
- Note: The data to be appended is currently hardcoded in the script within the `new_data` variable (e.g., `new_data = "New log data here"`). You will need to modify the script directly to change the appended data.

  ```bash
  python AppendFileInS3.py <bucket_name> <object_key> <region>
  ```

### Azure/GetBlobStorageFile.py
- This script will download a file from Azure blob storage.

  ```bash
  python GetBlobStorageFile.py <connection_string> <container_name> <blob_name> <local_file_path>
  ```

### Azure/HostImagesInBlob.py
- This script will upload all images in a target directory to Blob storage and then write public access urls to a local file.

  ```bash
  python HostImagesInBlob.py <connection_string> <container_name> <directory_path> <output_file>
  ```

### GoogleApps/SendEmailOnFormSubmit.gs
- Combine this script with a Google Form and you can send an email with each submit.

### MSTeams/SendTextToTeams.py
- This script sends a message to a Microsoft Teams channel via an incoming webhook with optional subject, message, and multiple images.
- Note that Teams doesn't not support direct image upload via API and instead requires you to supply hosted links. You can use `HostImagesInBlob.py` to generate these links for images you create.

  ```bash
  python SendTextToTeams.py <webhook_url> <subject> <message> <path_to_image_urls_file>
  ```

### Slack/PostImageAndLogToSlack.py
- This script sends a message to a Slack channel. The message will post a message and then in a thread post addtional images and log content. You pass it a message, a directory of images, a log file, and a slack channel id.

  ```bash
  python PostImageAndLogToSlack.py <message> <directory> <log_file> <channel_id>
  ```

### Slack/PostImageAndTextToSlack.py
- This script sends a message to a Slack channel with an optional image in the main message body.

  ```bash
  python PostImageAndTextToSlack.py <token> <channel_id> <filepath> <text_message>
  ```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
