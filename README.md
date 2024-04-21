# speach-recognition-project
a small AI-based project that generates response in the form of speach and takes input from user in the form of speach
Description

This project is a speech recognition and response system built with Python. It uses the speech_recognition and pyttsx3 libraries to convert spoken language into written text and then generate a spoken response. The application has a simple GUI built with wxPython that allows the user to interact with the system.

Installation

To install and run this project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python 3.6 or above installed. You can download Python here.
3. Install the necessary dependencies by running the following command in your terminal:

 
pip install 



• speech_recognition
• pyttsx3
• wxPython
• g4f
Additionally, you will need to install pyinstaller to run the file
Usage

To use this project, follow the following steps:
1. Navigate to the directory of the python code file in command prompt
2. Run the following command: pyinstaller speach_recognition.py --windowed
3. Wait for a few minutes. A folder named  dist will appear in the same directory where the code is saved. It will contain the exe file.


A GUI will appear with a 'Speak' button. Click the button and speak into your microphone. The program will transcribe your speech into text, generate a response, and then speak the response.

Troubleshooting

If you encounter any issues while installing or running this project, please check the following:

• Ensure you have the correct version of Python installed.
• Make sure all dependencies are installed correctly.
• Check your microphone is working properly.
