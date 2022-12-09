# Sample Speed-test Application:

# Reference Video: https://www.youtube.com/watch?v=DIRBUuJZtOM

# Import Required Module
from tkinter import *
from tkinter.ttk import *
from speedtest import Speedtest

def update_text():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10 ** 6), 2)
    upload_speed = round(upload / (10 ** 6), 2)
    down_label.config(text="Download Speed - " + str(download_speed) + "Mbps")
    up_label.config(text="Upload Speed - " + str(upload_speed) + "Mbps")


# Create Object
root = Tk()

# Set Title of the Box:
root.title("Internet Speed Tester")

# Set geometry (widthxheight):
root.geometry('400x400')

## This will create style object
style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).
style.configure('W.TButton', font= ('calibri', 10, 'bold', 'underline'), foreground='green')

# Style will be reflected only on
# this button because we are providing
# style only on this Button.

# btn2 = Button(root, text = 'Click me !', command = None)
# btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

button = Button(root, text="Test Speed",  style = 'W.TButton', width=30, command=update_text)
button.grid(row=1, column=3, pady=10, padx=100)
down_label = Label(root, text="")
down_label.grid()
up_label = Label(root, text="")
up_label.grid()

root.mainloop()
