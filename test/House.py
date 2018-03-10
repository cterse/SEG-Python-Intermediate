'''
Created on 13-Feb-2018

@author: DELL
'''

class House:
    #connectivityMatrix = [[1,0,1,0], [0,1,0,1], [1,0,1,1], [0,1,1,1]]
    connectivityMatrix = [[1,0,0,1], [0,1,1,0], [0,1,1,1], [1,0,1,1]]
    roomMap = {0: "KITCHEN", 1: "HALL", 2: "BATHROOM", 3: "BEDROOM", -1: "OUTSIDE"}
    
    OUTSIDE_HOUSE = "OUTSIDE"
    FIRST_ROOM = "HALL"
    
    def getConnectivityMatrix(self):
        return self.connectivityMatrix
    
    def getRoomMap(self):
        return self.roomMap
    
    def getRoomName(self, roomCode):
        return self.roomMap[roomCode]
    
    def getRoomCode(self, roomName):
        for i in self.roomMap.keys():
            if self.roomMap[i] == roomName:
                return i
        
        return None
    
    def areRoomsConnected(self, roomA, roomB):
        roomACode = self.getRoomCode(roomA)
        roomBCode = self.getRoomCode(roomB)
        if roomACode is None or roomBCode is None:
            print("Custom Error: House:areRoomsConnected(): room(s) does not exist")
            return None
        
        if self.connectivityMatrix[roomACode][roomBCode] == 1:
            return True
        else:
            return False
    
    def getConnectedRooms(self, roomName):
        connectedRoomsList = []
        roomCode = self.getRoomCode(roomName)
        if roomCode is None:
            print("Custom Error: House:getConnectedRooms(): room(s) does not exist")
            return None
        
        for counter in range(len(self.connectivityMatrix)):
            if self.connectivityMatrix[roomCode][counter] == 1:
                connectedRoomsList.append(self.getRoomName(counter))
        
        if connectedRoomsList.count(roomName) > 0:
            connectedRoomsList.remove(roomName)
        return connectedRoomsList
    
    
    
#h = House()
#print(h.getRoomCode("gibberish"))
#print(h.getRoomCode(""))
#listroom = h.getConnectedRooms("BEDROOM")
#print(listroom)
