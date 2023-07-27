import os
import subprocess
import argparse

def produce_build(unity_path, job_name, workspace, build_number):
    os.chdir(workspace)
    build_location = os.path.join(workspace, f"Build/Android_{build_number}.apk")
    unity_exe = os.path.join(unity_path, "Editor/Unity.exe")
    
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
        "Android",
        "-buildLocation",
        build_location
    ]
    
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unity Build Script")
    parser.add_argument("unity_path", help="Path to Unity.exe")
    parser.add_argument("job_name", help="Job name")
    parser.add_argument("workspace", help="Workspace path")
    parser.add_argument("build_number", help="Build number")

    args = parser.parse_args()

    produce_build(args.unity_path, args.job_name, args.workspace, args.build_number)
