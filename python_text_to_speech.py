import PySimpleGUI as sg
import pyttsx3


engine = pyttsx3.init()

# Code to create the layout 
layout = [
    [sg.Text('Enter Text ', font=('Arial', 15)), sg.InputText(key='-INPUT-', font=('Arial', 15)), sg.Button('Speak', font=('Arial', 15))],
    [sg.Text('Choose a Voice:', font=('Arial', 15)), sg.Radio('Male', "RADIO1", default=True, font=('Arial', 15), key='-MALE-'), sg.Radio('Female', "RADIO1", font=('Arial', 15), key='-FEMALE-')],
    [sg.Text('Adjust the Volume:', font=('Arial', 15)), sg.Slider(range=(0, 100), default_value=50, orientation='h', size=(20, 15), font=('Arial', 15), key='-VOLUME-')],
    [sg.Text('Adjust the Speed:', font=('Arial', 15)), sg.Slider(range=(100, 500), default_value=200, orientation='h', size=(20, 15), font=('Arial', 15), key='-SPEED-')],
    [sg.Button('Exit',font=('Arial', 15))]
]

# Code to create the GUI window
window = sg.Window('Text-to-Speech App', layout )

# Defining a function for speaking the text
def speak(text, volume, speed):
    # Setting the voice based on the user's choice
    if values['-MALE-']:
        voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    else:
        voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_id)

   
    engine.setProperty('volume', volume / 100)
    engine.setProperty('rate', speed)

    
    engine.say(text)
    engine.runAndWait()


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break

    if event == 'Speak':
        text = values['-INPUT-']
        volume = values['-VOLUME-']
        speed = values['-SPEED-']
        speak(text, volume, speed)

window.close()