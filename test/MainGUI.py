'''
Created on 11-Feb-2018

@author: DELL
'''

import os
import sys
import tkinter as tk
import constants as constants

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

root = tk.Tk()
root.title(constants.ROOT_TITLE)

#Canvas
mainDiagramCanvas = tk.Canvas(root, bg="white")
kitchen = mainDiagramCanvas.create_rectangle(10+50, 10+50, 100+50, 100+50)
hall = mainDiagramCanvas.create_rectangle(100+50, 10+50, 200+50, 100+50)
bathroom = mainDiagramCanvas.create_rectangle(100+50, 100+50, 200+50, 200+50)
bedroom = mainDiagramCanvas.create_rectangle(10+50, 100+50, 100+50, 200+50)

#Images
#logo = tk.PhotoImage(file="python_logo_small.gif")
mainDoorImage = tk.PhotoImage(file=resource_path("main_door_small.png"))
horizontalDoorImage = tk.PhotoImage(file=resource_path("door_small.png"))
verticalDoorImage = tk.PhotoImage(file=resource_path("door_2_small.png"))
personImage = tk.PhotoImage(file=resource_path("person.png"))
personImageOnCanvas = mainDiagramCanvas.create_image(10, 20, image=personImage)

#Labels
mainDoorLabel = tk.Label(root, image=mainDoorImage)
horizontalDoorLabel = tk.Label(root, image=horizontalDoorImage)
horizontalDoorLabel2 = tk.Label(root, image=horizontalDoorImage)
verticalDoorLabel = tk.Label(root, image=verticalDoorImage)

#hallLabelFrame = tk.LabelFrame(mainDiagramCanvas, text="HALL")
#hallLabel = tk.Label(hallLabelFrame, text="HALL")
#bedroomLabelFrame = tk.LabelFrame(mainDiagramCanvas, text="BEDROOM")
#bedroomLabel = tk.Label(bedroomLabelFrame, text="BEDROOM")
#bathroomLabelFrame = tk.LabelFrame(mainDiagramCanvas, text="BATHROOM")
#bathroomLabel = tk.Label(bathroomLabelFrame, text="BATHROOM")
#kitchenLabelFrame = tk.LabelFrame(mainDiagramCanvas, text="KITCHEN")
#kitchenLabel = tk.Label(kitchenLabelFrame, text="KITCHEN")

#Buttons
enterHouseButton = tk.Button(root, text=constants.ENTER_HOUSE_BUTTON)

placeLampButton = tk.Button(root, text=constants.PLACE_LAMP)
placeBedsheetButton = tk.Button(root, text=constants.PLACE_BEDSHEET)
placeToiletCleanerButton = tk.Button(root, text=constants.PLACE_TOILET_CLEANER)
placeUtensilButton = tk.Button(root, text=constants.PLACE_UTENSIL)

exitHouseButton = tk.Button(root, text=constants.EXIT_HOUSE_BUTTON)

#Text and Scrollbar
logText = tk.Text(root, wrap="word")
scrollb = tk.Scrollbar(root, command=logText.yview)
logText.configure(yscrollcommand=scrollb.set)

def createMainGUI():
    
    #Placement
    mainDiagramCanvas.grid(row="0", column="0", rowspan="4", columnspan="4")
    enterHouseButton.grid(row="1", column="7")
    placeUtensilButton.grid(row="3", column="6")
    placeLampButton.grid(row="3", column="7")
    placeBedsheetButton.grid(row="3", column="8")
    placeToiletCleanerButton.grid(row="3", column="9")
    exitHouseButton.grid(row="5", column="7")
    
    logText.grid(row="6", column="0", columnspan="10")
    scrollb.grid(row="6", column="9", sticky="ns")

    mainDiagramCanvas.create_window(170, 60, window=mainDoorLabel, anchor='w')
    mainDiagramCanvas.create_window(170, 150, window=horizontalDoorLabel, anchor='w')
    mainDiagramCanvas.create_window(70, 150, window=horizontalDoorLabel2, anchor='w')
    mainDiagramCanvas.create_window(130, 205, window=verticalDoorLabel, anchor='w')
    
    mainDiagramCanvas.coords(personImageOnCanvas, 190, 20)
    
    mainDiagramCanvas.create_text(180, 100, text="HALL", anchor='w')
    mainDiagramCanvas.create_text(170, 200, text="BATHROOM", anchor='w')
    mainDiagramCanvas.create_text(80, 100, text="KITCHEN", anchor='w')
    mainDiagramCanvas.create_text(70, 200, text="BEDROOM", anchor='w')
    
    root.mainloop()

#createMainGUI()