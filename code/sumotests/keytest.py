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

app = App("Display Sensor", layout="auto")

key_w = TextBox(app)

key_w.when_key_pressed = read_key()


text = Text(app, text ="", visible=True)

#button4.after(3, clear)


app.display()
