# Setting Up Appium for Mobile Automation Testing

## Installing Appium

1. **Install Appium globally:**
   ```bash
   npm i -g appium
   ```

2. **Installing Android SDK**
   - If you have already installed Android Studio, you can skip this part.
   - Download and install Android Studio on your device or just install command-line tools for Android SDK.
   - [Download Android Studio](https://developer.android.com/studio)
   - If you download the command-line tools, unzip it to a folder and navigate to the bin folder where `sdkmanager` is located. Run these two commands in this folder using cmd:
     ```bash
     sdkmanager "platform-tools" "platforms;android-33"
     sdkmanager build-tools;34.0.0
     ```

3. **Set Environment variables:**
   - Set `ANDROID_HOME` to the path where `platform-tools` and `build-tools` are located.
   - Append these paths to Environmental path:
     - `%ANDROID_HOME%platform-tools`
     - `%ANDROID_HOME%build-tools/34.0.0`

4. **Install JDK**
   - [Download JDK](https://www.oracle.com/java/technologies/downloads/#java17)
   - Set up the `JAVA_HOME` environment variable to point to the JDK home directory, which will contain the `bin`, `include`, and other directories.

5. **Connect the Mobile device:**
   - Make sure your mobile device is in developer mode and USB debugging is on.

6. **Open the command prompt and type:**
   ```bash
   adb devices
   ```
   If your phone is shown in the result, then you are ready to go.

7. **Check if Python and pip are installed:**
   ```bash
   python --version
   pip --version
   ```
   If they are not installed, download and install Python.

8. **Install The Appium Python Client:**
   ```bash
   pip install Appium-Python-Client
   ```

9. **Finally, run the code `bkash_check_balance.py`.**
