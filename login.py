import PySimpleGUI as sg
import pymysql.cursors

cancel = False
def loginscreen(cur):
    sg.theme("LightBlue2")
    layout = [  [sg.Text('Log In', size=(15, 1), font=40)],
                [sg.Text('Username', size=(15, 1), font=16), sg.InputText(key='-usernm-', font=16)],
                [sg.Text('Password', size=(15, 1), font=16), sg.InputText(key='-psswrd-', password_char='*', font=16)],
                [sg.Button('Login')]    ]
    window = sg.Window("Log In", layout, size=(1000, 720))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            cancel = True
            break
        else:
            if event == "Login":
                cur.execute("select password from users where username = '{}';".format(values['-usernm-']))
                output = cur.fetchall()
                print(output[0][0])
                print(values['-psswrd-'])
                if values['-psswrd-'] == output[0][0]:
                    window.close()
                    return True
                    break
                elif values['-psswrd-'] != output[0][0]:
                    sg.popup("Incorrect username and/or password. Try again")
