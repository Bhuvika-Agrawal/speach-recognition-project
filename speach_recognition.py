import threading
import speech_recognition as sr
import g4f
import pyttsx3
import wx

converter = pyttsx3.init()
voices = converter.getProperty('voices')
for voice in voices:
    if 'female' in voice.name or 'female' in voice.id:
        converter.setProperty('voice', voice.id)
        converter.setProperty('rate', 120)
        converter.setProperty('volume', 1)
        break
convo = []

# Define the main window class
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.sizer.Add(self.text_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        self.btn = wx.Button(self.panel, label='Speak')
        self.sizer.Add(self.btn, 0, wx.ALL | wx.CENTER, 5)
        self.btn.Bind(wx.EVT_BUTTON, self.on_click_speak)
        self.panel.SetSizer(self.sizer)
        self.Show()

    def on_click_speak(self, event):
        # Disable the button
        self.btn.Disable()
        # Start the speech recognition in a new daemon thread
        threading.Thread(target=self.on_speak, daemon=True).start()

    def on_speak(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.text_ctrl.AppendText("Say something...\n")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                self.text_ctrl.AppendText(f"Recognized text: {text}\n")
            except sr.UnknownValueError:
                self.text_ctrl.AppendText("Couldn't understand what you said.\n")
                wx.CallAfter(self.btn.Enable) 

            except sr.RequestError as e:
                self.text_ctrl.AppendText(f"Sorry, there was an error with the service; {e}\n")
                wx.CallAfter(self.btn.Enable) 

        # Generate AI response
        response = self.generate_ai_response(text)
        self.text_ctrl.AppendText(f"AI Response: {response}\n")

        # Speak out the response
        self.speak(response)

        # Re-enable the button
        wx.CallAfter(self.btn.Enable)

    def generate_ai_response(self, text):
        def GPT4(prompt):
            convo.append({"role": "user", "content": prompt})
            answer = g4f.ChatCompletion.create(messages=convo, model='gpt-3.5-turbo', provider=g4f.Provider.You)
            convo.append({"role": "assistant", "content": answer})
            return answer

        return GPT4(text)

    def speak(self, text):
        converter.say(text)
        converter.runAndWait()

# Run the application
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None, 'Speech Recognition App')
    app.MainLoop()