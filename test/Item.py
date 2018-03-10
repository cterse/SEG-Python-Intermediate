'''
Created on 13-Feb-2018

@author: DELL
'''

class Item:
    name = None
    code = None
    
    def __init__(self, itemCode, itemName):
        self.code = itemCode
        self.name = itemName
    
    def setItemName(self, itemName):
        self.name = itemName
    
    def getItemName(self):
        return self.name
        
    def getItemCode(self):
        return self.code
    