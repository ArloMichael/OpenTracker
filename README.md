# OpenTracker

OpenTracker is an open-source project that tracks your face with real-time video captured from your webcam.
This documentation provides instructions on how to use OpenTracker using two methods: running the pre-built executable file or downloading the Python source code and running it manually.

## Method 1: Running the Executable File (Easy)

### Prerequisites

*   Windows operating system
*   Webcam connected to your computer
*   OBS Studio (download from [OBS website](https://obsproject.com/download))
*   OBS Virtual Cam (download from [GitHub](https://github.com/CatxFish/obs-virtual-cam/releases))
  
### Steps

1.  Download the OpenTracker executable file from the GitHub repository
    
2.  Double-click on `OpenTracker.exe` to run the application
    
3.  Use the virtual camera in applications like Zoom and Microsoft Teams. Just change the video feed to `OBS Virtual Camera`
    

## Method 2: Running the Python Source Code (Advanced)

### Prerequisites

*   Python 3.7 or higher installed on your system
*   Webcam connected to your computer
*   OBS Studio (download from [OBS website](https://obsproject.com/download))
*   OBS Virtual Cam (download from [GitHub](https://github.com/CatxFish/obs-virtual-cam/releases))

### Steps

1.  Clone or download the OpenTracker repository from GitHub
    
2.  Open a command prompt or terminal and navigate to the extracted folder
    
3.  Install the required Python dependencies by running the following command:
    
    ``` console
    pip install -r requirements.txt
    ```
    
4.  After the installation, execute the following command to run the OpenTracker script:
    
    ``` console
    python opentracker.py
    ```
    
5.  Use the virtual camera in applications like Zoom and Microsoft Teams. Just change the video feed to `OBS Virtual Camera`
    

## Customization (Advanced)

You can customize OpenTracker according to your requirements. Open the `opentracker.py` file in a text editor to make changes to the following options:

*   Virtual camera dimensions: Modify the `width` and `height` values in the `pyvirtualcam.Camera(width=680, height=480, fps=60)` line to adjust the virtual camera output dimensions
    
*   CascadeClassifier model: Modify the CascadeClassifier to change the type of detection
    

Feel free to explore and customize the code. If you encounter issues or have suggestions, please report them in the GitHub repository's issue tracker. Enjoy using OpenTracker!
