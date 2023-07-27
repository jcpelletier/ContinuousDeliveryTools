# Continuous Delivery Tools
Tools for build and delivery

# CI/CD Scripts
These scripts are intended to be used in a CI/CD environment such as Jenkins. They are written in Python for high portability.

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
  python unity_build.py "path/to/your/unity/editor.exe" "YourJobName" "YourWorkspacePath" "YourBuildNumber"

# Unity Scripts
These scripts are intended to assist with the build and instrumentation of Unity projects in a CI/CD environment.

## Build.cs

This is a simple C# script that automates the process of building your Unity project from the command line. Note that it will disable the Oculus XR plugin before building, if it's enabled. This script can be called using buildUnity.py in your CI/CD environment to automate the process of producing builds.

### How to Use

1. Copy the `Build.cs` file into your Unity project's `Assets` folder.
2. Make sure you have the necessary Unity Editor and target platform set up for your project.
3. Open your preferred command line interface.
4. Navigate to the root folder of your Unity project.

### Command Line Arguments

To use this script, you can pass the following command line arguments:

- `-buildTarget`: Specifies the platform you want to build for. Possible values are "Android" or "StandaloneWindows64" (for Windows).
- `-buildLocation`: Specifies the output location for the build. For example, if you are building for Android, you might use something like `./Builds/MyGame.apk`. For Windows, you might use `./Builds/MyGame.exe`.
- Example:

  ```bash
  "path/to/your/unity/editor.exe" -quit -batchmode -projectPath "path/to/your/unity/project" -executeMethod BuildProject.PerformBuild -buildTarget Android -buildLocation "./Builds/MyGame.apk"`

This command will build your Unity project for Android and place the output APK file in the "Builds" folder of your project.

