using UnityEngine;
using UnityEditor;

public class Build
{
    public static void PerformBuild()
    {
        // Check if Oculus XR plugin is enabled
        bool isOculusXRPluginEnabled = UnityEditor.EditorApplication.ExecuteMenuItem("Assets/Oculus/XR/Plugins/OculusXRPlugin/Editor/Oculus XR Plugin.menu");

        // Disable the Oculus XR plugin if it's enabled
        if (isOculusXRPluginEnabled)
        {
            UnityEditor.EditorApplication.ExecuteMenuItem("Assets/Oculus/XR/Plugins/OculusXRPlugin/Editor/Oculus XR Plugin.unmenu");
        }

        // Get Command Line Arguments to use for build variables
        string[] commandLineArgs = System.Environment.GetCommandLineArgs();
        string buildTarget = "";
        string buildLocation = "";

        for (int i = 0; i < commandLineArgs.Length; i++)
        {
            if (commandLineArgs[i] == "-buildTarget") //What plaform do you want to build? Android, StandaloneWindows64
            {
                buildTarget = commandLineArgs[i + 1];
            }

            if (commandLineArgs[i] == "-buildLocation") //Where should the output go? *.apk, *.exe
            {
                buildLocation = commandLineArgs[i + 1];
            }
        }

        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
        EditorBuildSettingsScene[] scenes = EditorBuildSettings.scenes;

        // Get the scenes from build settings
        string[] scenePaths = new string[scenes.Length];
        for (int i = 0; i < scenes.Length; i++)
        {
            scenePaths[i] = scenes[i].path;
        }

        // Set Build Player Options based on variables above
        buildPlayerOptions.scenes = scenePaths;
        buildPlayerOptions.locationPathName = buildLocation;
        buildPlayerOptions.target = (BuildTarget)System.Enum.Parse(typeof(BuildTarget), buildTarget);
        buildPlayerOptions.options = BuildOptions.Development | BuildOptions.AllowDebugging;

        // Make the build
        BuildPipeline.BuildPlayer(buildPlayerOptions);
    }
}
