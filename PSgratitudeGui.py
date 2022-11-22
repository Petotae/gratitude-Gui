# Peter Savinelli

# This program requires PyQt6, so make sure you have that if it doesn't work

# Imports "sys", it is necessary for the program to actually appear as a window
import sys

# Imports all the object types that I am going to use throughout the program, including buttons, the textbox,
# the non-editable text, the layout, the and the app itself.
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit

# Creates a new "QApplication" object called "gratitude", it is responsible for being the underlying roots that hold
# all the other objects together
gratitude = QApplication([])

# New "QLabel" is created, it is seen as a block of text by the user
label = QLabel("Please enter your name: ")

# A "QLineEdit" object is made, it acts as an empty block of text that the user can give input to
line = QLineEdit()

# A new "enterButton" object is created, it is seen by the user as a button that can be clicked
enterButton = QPushButton("Enter")

# A "QGridLayout" is then created, and all the previous widgets are added to it. The "QGridLayout" object type
# dictates how the various widgets added to it are organized, it allows the user can see them.
layout = QGridLayout()
layout.addWidget(label)
layout.addWidget(line)
layout.addWidget(enterButton)

# Creates a new "QWidget", this widget serves as the window that contains a layout full of other widgets
window = QWidget()
# Sets the title bar on top of the window
window.setWindowTitle("For who I'm grateful for...")
# Sets the size of the window
window.setGeometry(500, 300, 500, 100)
# Assigns the previously made layout to the window
window.setLayout(layout)

# A new window is made, this window is the one that is shown with the message for the user
outWindow = QWidget()
# A new label is made that will later contain the user's message
outLabel = QLabel()
# A new layout is made, the "outLabel" label is assigned to it, and then the layout is assigned "outWindow" widget
outLayout = QGridLayout()
outLayout.addWidget(outLabel)
outWindow.setLayout(outLayout)


# Function that displays the message for the user
def thankuser():
    # Saves user's textbox input to a variable
    text = line.text()

    # Capitalizes the user's input, then saves it in a new variable. This is used for when one of the special names
    # are entered. It allows these if statements to be case-insensitive.
    uptext = text.upper()

    # Checks if the user entered something in the text box, if they did the if statement returns as true
    if text == "":
        outLabel.setText("Input your name please :(")

        # Calls the window the error message
        outWindow.show()
    elif uptext == "DIANE":
        outLabel.setText("I love you, mom")

        # Calls the window that displays the thank-you message for my mom
        outWindow.show()
    elif uptext == "PETER":
        outLabel.setText("I'm great")

        # Calls the window that displays the egotistical message for me
        outWindow.show()
    else:
        # The "outLabel" text is updated to a message depending on what the "text" variable is assigned to
        outLabel.setText("I am so grateful for you, " + text + ", you're amazing <3")

        # Calls the window that displays the message for the user
        outWindow.show()


# When the button is pressed by the user, the "thankuser" function is called
enterButton.pressed.connect(thankuser)

# Displays the first window for the user
window.show()

# Allows program to be quit properly with operating system's close button
sys.exit(gratitude.exec())
