# Continuous Delivery Tools
Tools for build and delivery

## jiraQuery.py
- Pass Jira credentials and JQL query, and this will return a JSON dump of issues.
- Example:

  ```bash
  python jiraQuery.py "Myemail@domain.com" "MyCredentials" "MyDomain" "Your JQL Query"

## cleanWorkspace.py
- This script is for the cleanup of build environments. It will remove all files and subfolders from the target location.
- Use this either post or pre-build to remove build and other temporary artifacts from the working directory.
- Example:

  ```bash
  python cleanWorkspace.py "your_folder_path_here"

## buildUnity.py
- This script will build a Unity project using the specified parameters.
- Example:

  ```bash
  python unity_build.py "C:\Program Files\Unity\Hub\Editor\2021.3.24f1" "YourJobName" "YourWorkspacePath" "YourBuildNumber"
