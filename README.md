# My_YT_Downloader 🚀

A simple and efficient YouTube downloader that allows users to download videos in various formats and resolutions. The app fetches metadata, provides a seamless experience, and allows users to download YouTube content quickly.

---

## **Table of Contents** 📋
1. [Prerequisites](#prerequisites-)
2. [Setup Instructions](#setup-instructions-)
   - [Create a Virtual Environment](#create-a-virtual-environment-)
   - [Activate the Virtual Environment](#activate-the-virtual-environment-)
   - [Install Dependencies](#install-dependencies-)
3. [Running the Application](#running-the-application-)
4. [Features](#features-)
5. [Troubleshooting](#troubleshooting-)
6. [Contributing](#contributing-)
7. [License](#license-)
8. [Acknowledgements](#acknowledgements-)

---

## **Prerequisites** 🔧

Before you begin, you need to ensure that the following are installed on your system:

### **1. Install FFmpeg** 🎬
This application relies on **FFmpeg** for video processing. Follow the instructions below based on your operating system:

- **Windows**: Use the following command to install FFmpeg using `winget` (Windows Package Manager):
  ```bash
  winget install "FFmpeg (Essentials Build)"
# YouTube Downloader Application

## Prerequisites 📋

Before you begin, make sure you have the following installed:

- **Python**: Version 3.6 or higher
- **FFmpeg**: FFmpeg is required for video/audio processing.

### FFmpeg Installation 🔧

- **Windows**: You can download FFmpeg from the official [FFmpeg Downloads](https://ffmpeg.org/download.html). After downloading, add FFmpeg to your system's PATH.

- **macOS/Linux**: Install FFmpeg using your system's package manager:

  - **macOS (Homebrew)**:
    ```bash
    brew install ffmpeg
    ```

  - **Linux (Ubuntu/Debian)**:
    ```bash
    sudo apt-get install ffmpeg
    ```

Ensure that FFmpeg is properly installed and added to your system's PATH.

---

## Setup Instructions 🛠️

### 1. Create a Virtual Environment 🐍

- Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux).
- Create the virtual environment:
    ```bash
    python -m venv enter_your_virtualenv_name
    ```
    Example:
    ```bash
    python -m venv .venv
    ```
    This will create a virtual environment in a folder named `.venv`.

### 2. Activate the Virtual Environment ✅

- **Windows**: Run the following command to activate the virtual environment:
    ```bash
    .\venv\Scripts\activate
    ```
- **macOS/Linux**: Use the following command:
    ```bash
    source venv/bin/activate
    ```

Once activated, your terminal prompt should change to indicate you're working within the virtual environment.

### 3. Install Dependencies 📦

Now that your virtual environment is activated, install the required Python packages from `requirements.txt`:

- Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

This will install all the necessary libraries and modules required for the application to run.

---

## Running the Application 🏃‍♂️

Once you've set up everything, you're ready to run the application:

- Run the application:
    ```bash
    python app.py
    ```

This will start the application, and you can interact with the UI to download YouTube videos.

---

## Features 🌟

- **YouTube Video Downloading**: Download YouTube videos in various formats (MP4, MP3, etc.).
- **Multiple Resolutions**: Select your preferred resolution for downloading (720p, 1080p, etc.).
- **Metadata Fetching**: Fetch video metadata such as title, description, and thumbnail before downloading.
- **Responsive User Interface**: User-friendly and responsive interface that makes it easy to navigate.

---

## Troubleshooting 🌟

If you encounter issues while running the application, here are some common problems and solutions:

### 1. Missing Modules or Libraries
- **Problem**: You receive an error regarding missing modules or libraries.
- **Solution**: Ensure all dependencies are installed by running:
    ```bash
    pip install -r requirements.txt
    ```

### 2. FFmpeg Not Recognized
- **Problem**: FFmpeg is not recognized by the system.
- **Solution**: Make sure FFmpeg is properly installed and that its path is added to your system's environment variables. Check by running:
    ```bash
    ffmpeg -version
    ```

### 3. Application Errors
- **Problem**: The application throws errors when attempting to fetch resolutions or download videos.
- **Solution**: Check if the YouTube URL is correct and ensure the video is publicly accessible.

If you're still encountering issues, feel free to raise an issue on the GitHub repository or contact the project maintainer.

---

## Contributing 🤝

We welcome contributions to improve this project! Here's how you can contribute:

1. **Fork the repository**: Click on the "Fork" button at the top of this page to create your own copy of the project.
2. **Create a new branch**: For your changes, create a new branch using:
    ```bash
    git checkout -b your-feature-branch
    ```
3. **Make your changes**: Implement the changes you want to contribute.
4. **Commit your changes**: Commit your changes with a meaningful commit message.
    ```bash
    git commit -m "Add feature/bugfix description"
    ```
5. **Push your changes**: Push your changes to your forked repository.
    ```bash
    git push origin your-feature-branch
    ```
6. **Create a pull request**: Once your changes are pushed, submit a pull request to the original repository.

---

## License 📄

This project is licensed under the MIT License - see the LICENSE file for more details.

---

## Acknowledgements 🙏

- **FFmpeg**: Thanks to FFmpeg for providing powerful video processing tools.
- **Open-source Community**: Inspiration from various open-source YouTube downloaders and contributions from the community.

