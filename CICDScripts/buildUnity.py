import os
import subprocess
import argparse
import platform

def get_unity_executable_extension(unity_path):
    # Check if .exe extension is already present
    if platform.system() == "Windows":
        return ".exe"
    return ""

def produce_build(unity_path, job_name, workspace, build_number, build_target):
    os.chdir(workspace)
    build_location = os.path.join(workspace, f"Build/{build_target}_{build_number}.apk")
    
    # Get the correct Unity executable extension based on the OS and unity_path
    unity_extension = get_unity_executable_extension(unity_path)
    unity_exe = os.path.join(unity_path, f"Unity{unity_extension}")

    cmd = [
        unity_exe,
        "-quit",
        "-developmentBuild",
        "-batchmode",
        "-logfile",
        "build.log",
        "-executeMethod",
        "Build.PerformBuild",
        "-projectPath",
        workspace,
        "-buildTarget",
        build_target,
        "-buildLocation",
        build_location
    ]
    
    print(f"Running build with the following parameters:")
    print(f"Unity executable path: {unity_exe}")
    print(f"Job name: {job_name}")
    print(f"Workspace: {workspace}")
    print(f"Build number: {build_number}")
    print(f"Build target: {build_target}")
    print(f"Build location: {build_location}")
    
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unity Build Script")
    parser.add_argument("unity_path", help="Path to Unity executable")
    parser.add_argument("job_name", help="Job name")
    parser.add_argument("workspace", help="Workspace path")
    parser.add_argument("build_number", help="Build number")
    parser.add_argument("build_target", help="Target platform for the build")

    args = parser.parse_args()

    # Normalize paths to handle forward slashes and backslashes correctly
    unity_path = os.path.normpath(args.unity_path)
    workspace = os.path.normpath(args.workspace)

    produce_build(unity_path, args.job_name, workspace, args.build_number, args.build_target)
