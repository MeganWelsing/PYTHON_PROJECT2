import qrcode
import PySimpleGUI as sg
import os

# Creating the GUI layout
layout = [
    [sg.Text('Enter text:'), sg.InputText(key='text')],
    [sg.Text('Select QR code size:'), sg.Slider(range=(1, 20), orientation='h', default_value=5, key='size')],
    [sg.Text('Select QR code color:')],
    [sg.Radio('Black', "COLOR", default=True, key='color_black'), sg.Radio('Red', "COLOR", key='color_red')],
    [sg.Text('Select background color:')],
    [sg.Radio('White', "BG_COLOR", default=True, key='bg_color_white'), sg.Radio('Yellow', "BG_COLOR", key='bg_color_yellow')],
    [sg.Button('Generate QR Code')],
    [sg.Image(key='image')]
]

# Creating  the window
window = sg.Window('QR Code Generator', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Generate QR Code':
        # Get the user input and generate the QR code image
        qr = qrcode.QRCode(version=1, box_size=values['size'], border=4)
        qr.add_data(values['text'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='bblack' if values['color_black'] else 'blue',
                            back_color='white' if values['bg_color_white'] else 'yellow')

        # Save the QR code image to a file
        img_file = 'qrcode.png'
        path = os.path.join(os.getcwd(), img_file)
        img.save(path)

        # Update the window to display the QR code image
        window['image'].update(filename=path)


window.close()