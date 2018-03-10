import MainGUI as mainGUI

roomColorMap = {"KITCHEN":"red", "HALL":"green", "BEDROOM":"yellow", "BATHROOM":"blue"}

def colorRoom(roomName):
    if roomName == "KITCHEN":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.kitchen, fill=roomColorMap[roomName])
        mainGUI.mainDiagramCanvas.coords(mainGUI.personImageOnCanvas, 95, 120)
    elif roomName == "HALL":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.hall, fill=roomColorMap[roomName])
        mainGUI.mainDiagramCanvas.coords(mainGUI.personImageOnCanvas, 190, 120)
    elif roomName == "BEDROOM":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.bedroom, fill=roomColorMap[roomName])
        mainGUI.mainDiagramCanvas.coords(mainGUI.personImageOnCanvas, 95, 220)
    elif roomName == "BATHROOM":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.bathroom, fill=roomColorMap[roomName])
        mainGUI.mainDiagramCanvas.coords(mainGUI.personImageOnCanvas, 200, 220)
    elif roomName == "OUTSIDE":
        mainGUI.mainDiagramCanvas.coords(mainGUI.personImageOnCanvas, 190, 20)
    else:
        print("wrong room")
        
def discolorRoom(roomName):
    if roomName == "KITCHEN":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.kitchen, fill="white")
    elif roomName == "HALL":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.hall, fill="white")
    elif roomName == "BEDROOM":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.bedroom, fill="white")
    elif roomName == "BATHROOM":
        mainGUI.mainDiagramCanvas.itemconfig(mainGUI.bathroom, fill="white")
    elif roomName == "OUTSIDE":
        None
    else:
        print("wrong room")

def updateGUI():
    mainGUI.root.update()