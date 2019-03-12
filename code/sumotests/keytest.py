from guizero import TextBox, App, Text

def read_key(event_data):
    print("Read : " + event_data.key)

def forward():
    print('F')

def backwards():
    print('B')

def right():
    print('R')

def left():
    print('L')

app = App("Key Testing", layout="auto")

key_w = TextBox(app)



text = Text(app, text ="S", visible=True)

key_w.when_key_pressed = read_key




app.display()
