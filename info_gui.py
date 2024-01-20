import PySimpleGUI as sg
from webscrape import crop_info
from language_processor import process

layout = [
    [sg.Text("What do you need to know?",
             background_color="#479e2e",
             font=("Georgia",30))],
    [sg.Multiline(size=(50,2), 
              key="USER",
              expand_y=True,
              expand_x=True,
              font=("Georgia",20))],
    [sg.Button(button_text="Get Answers", 
               size=(10,0.5), 
               enable_events=True, 
               key="QUESTION",
               font=("Georgia",17)),
    sg.Button(button_text="Check Question List", 
               size=(16,0.5), 
               enable_events=True, 
               key="LIST",
               font=("Georgia",17))
    ],
    [sg.Text(size=(60,3), 
             key="OUTPUT",
             background_color="#479e2e",
             font=("Georgia",20))],
    [sg.Button(button_text="Close", 
               size=(5,1), 
               enable_events=True, 
               key="CLOSE",
               font=("Georgia"))]
    ]

window = sg.Window("Stardew Valley Info Guide", 
                   layout, 
                   element_justification="c",
                   background_color="#479e2e")

while True:
    event, values = window.read()
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break
    if event == "QUESTION":
        user_info = (values["USER"]).lower()
        window['OUTPUT'].update(value=process(user_info))
    if event == "LIST":
        layout2 = [[sg.Text("What crop grows during <season>?\nWhat is <crop> used in?\nHow long does <crop> take to grow?How much does <crop> cost?\nHow much does <crop> sell for?\nHow much energy does <crop> give?\nHow much health does <crop> give?",
                            font=("Georgia"))]]
        window2 = sg.Window("List of Applicable Questions",
                            layout2)
        while True:
            eve, val = window2.read()
            if eve == sg.WIN_CLOSED:
                break
        window2.close()
window.close()



