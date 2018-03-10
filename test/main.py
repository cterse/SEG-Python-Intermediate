'''
Created on 13-Feb-2018

@author: DELL
'''
import MainGUI as mainGUI
import Person as person
import House as house
import Item as item

house1 = house.House()
person1 = person.Person(house1)
itemBedsheet = item.Item("3","BEDSHEET")
itemToiletCleaner = item.Item("1","TOILET CLEANER")
itemLamp = item.Item("4","LAMP")
itemUtensil = item.Item("2","UTENSIL")

mainGUI.enterHouseButton.configure(command=person1.enterHouse)
mainGUI.exitHouseButton.configure(command=person1.exitHouse)
mainGUI.placeBedsheetButton.configure(command=lambda: person1.placeItem(itemBedsheet))
mainGUI.placeLampButton.configure(command=lambda: person1.placeItem(itemLamp))
mainGUI.placeToiletCleanerButton.configure(command=lambda: person1.placeItem(itemToiletCleaner))
mainGUI.placeUtensilButton.configure(command=lambda: person1.placeItem(itemUtensil))


mainGUI.createMainGUI()