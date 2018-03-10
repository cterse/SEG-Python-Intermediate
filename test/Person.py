'''
Created on 12-Feb-2018

@author: DELL
'''
from builtins import str
import House as house   #for testing
import Item as item     #for testing
import logger as log
import GUImanipulator as guiMan
import time

itemRoomMap = {"TOILET CLEANER": "BATHROOM", "UTENSIL": "KITCHEN", "BEDSHEET": "BEDROOM", "LAMP": "HALL"}

class Person:
    house = ""
    currentPos = "";
    itemsToPlace = [];
    
    def __init__(self, house):
        self.house = house
        
        #guiMan.discolorRoom(self.currentPos)
        self.currentPos = self.house.OUTSIDE_HOUSE
        guiMan.colorRoom(self.currentPos)
    
    def setHouse(self, house):
        self.house = house
        
        guiMan.discolorRoom(self.currentPos)
        self.currentPos = self.house.OUTSIDE_HOUSE
        guiMan.colorRoom(self.currentPos)
        
    def getHouse(self):
        if self.house != "":
            return self.house
        else:
            print("No house allotted.")
            return -1
        
    def exitHouse(self):
        log.newLogger.emit("\n********* Leaving House")
        if self.currentPos == self.house.OUTSIDE_HOUSE:
            print("Already outside!")
            log.newLogger.emit("Already outside!")
            return self.currentPos
        elif self.currentPos != self.house.FIRST_ROOM:
            self.goToRoom(self.house.FIRST_ROOM)
        
        print("Leaving house.")
        log.newLogger.emit("Leaving house.")
        
        guiMan.updateGUI()
        time.sleep(1)
        
        guiMan.discolorRoom(self.currentPos)
        self.currentPos = self.house.OUTSIDE_HOUSE
        guiMan.colorRoom(self.currentPos)
        
        print("Current position: " + self.currentPos)
        log.newLogger.emit("Current position: " + self.currentPos)
        return self.currentPos
    
    def enterHouse(self):
        log.newLogger.emit("\n********* Entering House")
        if self.currentPos == self.house.OUTSIDE_HOUSE:
            guiMan.discolorRoom(self.currentPos)
            self.currentPos = self.house.FIRST_ROOM
            guiMan.colorRoom(self.currentPos)
            
            print("Entered inside.")
            log.newLogger.emit("Entered inside")
            print("Current position: " + self.currentPos)
            log.newLogger.emit("Current position: " + self.currentPos)
            return 1
        else:
            print("Already inside!")
            log.newLogger.emit("Already inside!")
            print("Current position: " + self.currentPos)
            log.newLogger.emit("Current position: " + self.currentPos)
            return self.currentPos
    
    def goToRoom(self, destinationRoom):
        log.newLogger.emit("\n********* Going to room: " + destinationRoom)
        if self.currentPos == self.house.OUTSIDE_HOUSE:
            print("Enter house first!")
            log.newLogger.emit("Enter house first!")
            return self.currentPos
        if self.currentPos == destinationRoom:
            print("Already in " + destinationRoom)
            log.newLogger.emit("Already in " + destinationRoom)
            return self.currentPos
        
        print("Current position: " + self.currentPos)
        log.newLogger.emit("Current position: " + self.currentPos)
        while self.currentPos != destinationRoom:
            if self.house.areRoomsConnected(self.currentPos, destinationRoom) == True:
                #print("Rooms are connected")
                print("Entering room: " + str(destinationRoom))
                log.newLogger.emit("Entering room: " + str(destinationRoom))
                
                guiMan.updateGUI()
                time.sleep(1)
                
                guiMan.discolorRoom(self.currentPos)
                self.currentPos = destinationRoom
                guiMan.colorRoom(self.currentPos)
                
                print("Reached destination.")
                log.newLogger.emit("Reached destination.")
            else:
                #print("Rooms are not connected")
                roomsConnectedToCurrent = self.house.getConnectedRooms(self.currentPos)
                roomsConnectedToDestination = self.house.getConnectedRooms(destinationRoom)
                
                commonRoomFound = None
                for i in range(len(roomsConnectedToCurrent)):
                    if roomsConnectedToCurrent[i] in roomsConnectedToDestination:
                        commonRoomFound = roomsConnectedToCurrent[i]
                        print("Entering room: " + str(roomsConnectedToCurrent[i]))
                        log.newLogger.emit("Entering room: " + str(roomsConnectedToCurrent[i]))
                        
                        guiMan.updateGUI()
                        time.sleep(1)
                        
                        guiMan.discolorRoom(self.currentPos)
                        self.currentPos = roomsConnectedToCurrent[i]
                        guiMan.colorRoom(self.currentPos)
                        
                
                if commonRoomFound is None:
                    print("Entering room: " + str(roomsConnectedToCurrent[0]))
                    log.newLogger.emit("Entering room: " + str(roomsConnectedToCurrent[0]))
                    
                    guiMan.updateGUI()
                    time.sleep(1)
                    
                    guiMan.discolorRoom(self.currentPos)
                    self.currentPos = roomsConnectedToCurrent[0]
                    guiMan.colorRoom(self.currentPos)
        
    def placeItem(self, item):
        log.newLogger.emit("\n********* Placing item: " + item.getItemName())
        if self.currentPos == self.house.OUTSIDE_HOUSE:
            print("Enter house first!")
            log.newLogger.emit("Enter house first!")
            return self.currentPos
        
        itemName = item.getItemName()
        itemRoomName = itemRoomMap[itemName.upper()]
        print("Placing item: " + itemName + " in room: " + itemRoomName)
        log.newLogger.emit("Placing item: " + itemName + " in room: " + itemRoomName)
        
        if self.currentPos != itemRoomName:
            self.goToRoom(itemRoomName)
        print(itemName + " placed in room " + itemRoomName)
        log.newLogger.emit(itemName + " placed in room " + itemRoomName)
        
    def getCurrentRoom(self):
        #roomName = self.house.getRoomName(self.currentPos)
        return self.currentPos


#newEnv = house.House()
#p1 = Person(newEnv)
#p1.exitHouse()
#p1.enterHouse()
#print("Starting room: " + p1.getCurrentRoom())
#p1.placeItem(item.Item(1, "UTENSIL"))
#p1.placeItem(item.Item(1, "BEDSHEET"))
#p1.goToRoom(3)
#p1.goToRoom(0)