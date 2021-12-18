import PySimpleGUI as sg
import pymysql.cursors
from userFunctions import addUser

cancel = False
def loginscreen(cur):
    sg.theme("LightBlue2")
    layout = [  [sg.Text('Log In', size=(15, 1), font=40)],
                [sg.Text('Username', size=(15, 1), font=16), sg.InputText(key='-usernm-', font=16)],
                [sg.Text('Password', size=(15, 1), font=16), sg.InputText(key='-psswrd-', password_char='*', font=16)],
                [sg.Button('Login')], [sg.Button('Create Account')]    ]
    window = sg.Window("Log In", layout, size=(1000, 720))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            cancel = True
            break
        else:
            if event == "Login":
                cur.execute("select password, user_id from users where username = '{}';".format(values['-usernm-']))
                output = cur.fetchall()
                if values['-psswrd-'] == output[0][0]:
                    window.close()
                    return True, output[0][1]
                    break
                elif values['-psswrd-'] != output[0][0]:
                    sg.popup("Incorrect username and/or password. Try again")
            elif event == "Create Account":
                createAccount(cur)

def createAccount(cur):
    sg.theme("LightBlue2")
    layout = [  [sg.Text('New Account', size=(15, 1), font=40)],
                [sg.Text('Username', size=(15, 1), font=16), sg.InputText(key='-usernm-', font=16)],
                [sg.Text('Password', size=(15, 1), font=16), sg.InputText(key='-psswrd-', password_char='*', font=16)],
                [sg.Button('Create Account')], [sg.Button('Cancel')]    ]
    window = sg.Window("New Account", layout, size=(1000, 720))

    event, values = window.read()
    if event != sg.WIN_CLOSED:
        if event == "Create Account":
            addUser(values['-usernm-'], values['-psswrd-'], cur)
    window.close()
