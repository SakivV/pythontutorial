from guizero import App, Text, TextBox, PushButton
def say_crop_name():
    welcome_msg.set(crop_name.get())    

app = App(title="Hello World")
welcome_msg = Text(app,text='Welcome to my App',size=36,font="Verdana")
crop_name = TextBox(app)
update_text = PushButton(app, command=say_crop_name, text="Display my name")
app.display()
