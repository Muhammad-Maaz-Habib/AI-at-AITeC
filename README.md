# Object Tracking with OpenCV

## Description
This project demonstrates a simple object tracking system using OpenCV's `TrackerCSRT` algorithm. The script captures video from your webcam, allows you to select an object to track, and then continuously tracks the object, displaying its position and the tracking status.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Contact Information](#contact-information)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Muhammad-Maaz-Habib/Tracker-using-OPEN-CV.git
    ```
2. Navigate to the project directory:
  
3. Install the required dependencies:
    ```bash
    pip install opencv-python
    ```

## Usage
1. Run the script:

2. A window will open showing the live feed from your webcam. Use your mouse to select the object you want to track and press Enter. The script will start tracking the selected object.

3. The video feed will display the tracking status and the frames per second (FPS). Press 'q' to quit the application.

## Configuration
- The script uses the `cv2.TrackerCSRT_create()` method to create a CSRT tracker. You can modify the tracker type by changing this method to other OpenCV trackers if needed.

## Contributing
Feel free to open issues or submit pull requests for improvements. Please ensure your contributions adhere to the project's coding standards and provide clear documentation for any changes.


## Acknowledgements
- The object tracking functionality is powered by OpenCV's `TrackerCSRT` algorithm.

## Contact Information
For questions or feedback, please contact me at [maazhabib2k4@gmail.com].
