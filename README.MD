# Face Recognition Attendance System

This is a Python-based Face Recognition Attendance System using the Tkinter library for GUI. It allows users to perform various tasks related to face recognition, including training images, recognizing faces, recording attendance, and managing student details. The application uses OpenCV and the LBPH (Local Binary Patterns Histograms) algorithm for face recognition, and integrates modules for handling student information and attendance tracking.

## Features

- **Student Details**: Add and manage student details.
- **Face Recognition**: Recognize faces from live camera feed and match them with the trained dataset.
- **Attendance Management**: Mark attendance based on face recognition results.
- **Training**: Train the face recognition model using LBPH on images stored in the `data` directory.
- **Photos**: Access the folder where all images for training are stored.
- **Exit**: Safely exit the application.

## Prerequisites

- Python 3.x
- Required Libraries: Install the dependencies using pip:
  ```bash
  pip install numpy opencv-python opencv-contrib-python pillow
