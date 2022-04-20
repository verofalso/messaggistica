import PySimpleGUI as sg
import telegram
import cv2

sg.theme('DarkBlue')

layout = [  [sg.Text('Invia il tuo messaggio:')],
          sg.FileBrowse('Immagine', target='img', 
              file_types=(("JPEG", "*.jpg"),("PNG", "*.png"),))
            [sg.Multiline('Messaggio...',size =(40,10),no_scrollbar=True)],
            [sg.Button('invia',key='invia'),sg.Button('immagine',key='immagine')]]

chat = 'xxx'
bot = 'XXX'

window = sg.Window('Teleponti',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    elif event == 'invia':
      telegram.Bot(token=bot).send_message(chat_id=chat,testo=values[0])
      message= values['msg'].strip()
      if len(message) == 0:
       sg.popup('inserisci del testo')
    elif event == 'immagine':
      image = cv2.imread(values)
      image = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 65])
      telegram.Bot(bot=bot).send_photo(chat=chat, photo=image.tobytes())
window.close()