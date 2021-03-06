from tkinter.constants import S
import pymysql.cursors
from searchFunctions import searchFunction
from connection import getConnection
from userFunctions import getUserTable, addMovie
from login import loginscreen
import PySimpleGUI as sg
import csv

user_id = -1

def dbprog(cur):
    # gui startup
    open("output.csv", "w").close()
    sg.theme('Default1')
    layout = [  [sg.Text('Search Movies: '), sg.InputText()],
                [sg.Button('Search')], [sg.Button('My Movie List')], [sg.Button('Add to list')] ]
    window = sg.Window('Movie List', layout, size=(1800, 720), element_justification='c')

    while (True):
        event, values = window.read()
        output = "Empty"
        if event == "Search":
            #Parse the input of the values we got from the search bar (window.read) to a function that turns them into MySql queries
            #so "Movie Name" becomes a "Select title from movie where title = Movie_Name"
            values = searchFunction(values, cur)
            try:
                cur.execute(values[0])
                output = cur.fetchall()
            except pymysql.err.OperationalError as e:
                output = "Empty"
        elif event == "My Movie List":
            values = getUserTable("usertable{}".format(user_id), cur)
            try:
                cur.execute(values)
                output = cur.fetchall()
            except pymysql.err.OperationalError as e:
                output = "Empty"
        elif event == "Add to list":
            layout = [  [sg.Text('Title'), sg.InputText()],
                        [sg.Text('Status'), sg.InputText()],
                        [sg.Text('My Rating out of 10'), sg.InputText()],
                        [sg.Button('Add')] ]
            window.close()
            window = sg.Window('Movie List', layout, size=(1800, 720), element_justification='c')
            event, values = window.read()
            if event == "Add":
                addMovie("usertable{}".format(user_id), values[0], values[1], values[2], cur)
                window.close()
                layout = [  [sg.Text('Search Movies: '), sg.InputText()],
                            [sg.Button('Search')], [sg.Button('My Movie List')], [sg.Button('Add to list')] ]
                window = sg.Window('Movie List', layout, size=(1800, 720), element_justification='c')
            continue
        if output != "Empty":
            with open("output.csv", "w", encoding='utf-8') as outfile:
                csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
                writer = csv.writer(outfile, dialect="custom")
                for tup in output:
                    writer.writerow(tup)
            data = []
            header_list = []
            with open("output.csv", "r", encoding='utf-8') as infile:
                reader = csv.reader(infile)
                data = list(reader)
                header_list = ['column' + str(x) for x in range(len(data[0]))]
            sg.set_options(element_padding=(0, 0))
            layout = [  [sg.Text('Search Movies: '), sg.InputText()],
                        [sg.Button('Search')], [sg.Button('My Movie List')],
                        [sg.Table(values=data,
                                headings=header_list,
                                max_col_width=25,
                                auto_size_columns=True,
                                justification='right',
                                # alternating_row_color='lightblue',
                                num_rows=min(len(data), 20))] ]
            window.close()
            window = sg.Window('Movie List', layout, size=(1800, 720), element_justification='c')
        else:
            sg.set_options(element_padding=(0, 0))
            layout = [  [sg.Text('Search Movies: '), sg.InputText()],
                        [sg.Button('Search')], [sg.Button('My Movie List')],
                        [sg.Text('Empty List')] ]
            window.close()
            window = sg.Window('Movie List', layout, size=(1800, 720), element_justification='c')


if __name__ == "__main__" :
    cur = getConnection()
    tf, user_id = loginscreen(cur)
    if (tf):
        dbprog(cur)
