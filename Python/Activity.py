import bitmex
import json

class Tick():
    def __init__(self,time, price):
        self.time = time
        self.price = price
class PriceChecker():
    # Constructor
    def __init__(self):
        self.levelsList = []    # call the @levelList.setter method and pass it an empty list
        self.currentPrice = 0.0    #call the @currentPrice.setter method and pass it 0.0
        self.BitmexClient = bitmex.bitmex(test=False)

    # Properties
    # A property is defined like a method, but you use it in your
    # code like a variable (no parentheses need to followed it when used in your code)
    # Refer: https://www.youtube.com/watch?v=jCzT9XFZ5bw
    # Refer BP411 slides: Week 2 - Chapter 10 - Slides about Encapsulation and properties
    @property
    def levelsList(self):           #Return the value of __levelsList
        return self.__levelsList

    @levelsList.setter
    def levelsList(self, newValue):
        self.__levelsList = newValue    # set the value of __levelsList

    @property
    def currentPrice(self):
        return self.__currentPrice

    @currentPrice.setter
    def currentPrice(self,newValue):
        self.__currentPrice = newValue

        # Class Methods

    # =============

    # Method: Sort and Display the levelsList
    def displayList(self):
        print(chr(27) + "[2J")  # Clear the screen
        print("Price Levels In The List")
        print("========================")

        # Sort the list in reverse order
        self.levelsList.sort(reverse=True)
        # Print the items in the list (Based on the above sort, numbers should appear from large to small.)
        for value in self.levelsList:
            print('$' + str(value));

            # Display the menu and get user input about what methods to execute next

    def displayMenu(self):
        min = 0
        max = 4
        errorMsg = "Please enter a valid option between " + str(min) + " and " + str(max)
        print("MENU OPTIONS")
        print("============")
        print("1. Add a price level")
        print("2. Remove a price level")
        print("3. Remove all price levels")
        if(self.currentPrice > 0):
                print("4. Display the current Bitcoin price here: " f"${self.currentPrice:,}")
        else:
                print("4. Display the current Bitcoin price here:")
        print("0. Exit the program")
        print(" ")

        # Get user input. Keep on requesting input until the user enters a valid number between min and max
        selection = 99
        while selection < min or selection > max:
            try:
                selection = int(input("Please enter one of the options: "))
            except:
                print('please enter value')  # user did not enter a number
                continue  # skip the following if statement
            if (selection < min or selection > max):
                print("errorMsg")  # user entered a number outside the required range
        return selection  # When this return is finally reached, selection will have a value between (and including) min and max

    # Method: Append a new price level to the levelsList
    def addLevel(self):
        while userInput == 1:
            try:
                value = float(input("Enter the price level to add: "))
                checkingObj.levelsList.append(value)
                break
                # Let the user enter a new float value and append it to the list
            except:
                # Print and error message if the user entered invalid input
                print("Please enter a valid value")
                continue

    # Method: Remove an existing price level from the levelsList
    def removeLevel(self):
        while userInput == 2:
            try:
                # Let the user enter a new float value. If found in the list, remove it from the list
                value = float(input("Enter the price level to remove :"))
                checkingObj.levelsList.remove(value)
                break
            except:
                # Print and error message if the user entered invalid input
                print("Please enter a valid value")
                continue

    # Method: Set levelsList to an empty list
    def removeAllLevels(self):
        # Set levelsList to an empty list
        checkingObj.levelsList.clear()

    # Method: Load levelsList using the data in levelsFile
    def readLevelsFromFile(self):
        try:
            # Set levelsList to an empty list
            self.levelsList = []
            # Open the file
            fout = open("myFile.txt", "r")
            # Use a loop to read through the file line by line
            for line in fout:

                # if the last two characters in the line is "\n", remove them
                if (line.find('\n')):
                    line = line[:-1]

                # Append the line to levelsList

                self.levelsList.append(float(line))
            # Close the file

            fout.close()
        except:
            return

    # Method: Write LevelsList to levelFile (override the existing file)
    def writeLevelsToFile(self):
        # Open the file in a way that will override the existing file (if it already exists)
        # ...
        fout = open("myFile.txt", "w")
        # Use a loop to iterate over levelsList item by item
        # ...
        for i in self.levelsList:
            fout.write("%s\n" % i)
            # Convert everything in the item to a string and then add \n to it- before writing it to the file
        # ...
        # Close the file
        # ...
        fout.close()

    # Function: Display the Bitcoin price in the menu item - to assist the user when setting price levels
    def updateMenuPrice(self):
        # Get the latest Bitcoin info(as a Tick object) from getBitmexprice(). name it tickobj.
        tickObj = self.getBitmexPrice()
        # Update the currentPrice property with the Bitcoin price in tickObj.
        self.currentPrice=tickObj.price
       

    # Function: call the bitmex exchange
    def getBitmexPrice(self):
        # send a request to exchange for bitcoin's data in $USD ('XBTUSD').
        # Te json response is converted into a tuple which we name responseTuple.
        responseTuple = self.BitmexClient.Instrument.Instrument_get(filter=json.dumps({'symbol': 'XBTUSD'})).result()
        # the tuple consists of the bitcoin information(in the form of a dictionary with key>value pairs) plus
        # some additional meta data received from the exchange.
        # extract only the dictionary (bitcoin information) from the tuple
        responseDictionary = responseTuple[0:1][0][0]
        # create a tick object and set its variables to the timestamp and lastPrice data from the dictionary.
        return Tick(responseDictionary["timestamp"], responseDictionary['lastPrice'])

# *************************************************************************************************
#                                           Main Code Section
# *************************************************************************************************


# Create an object based on the PriceChecker class
checkingObj = PriceChecker()

# Load levelsList from from the records in levelFile
checkingObj.readLevelsFromFile()

# Display the levelsList and Menu; and then get user input for what actions to take
userInput = 99
while userInput != 0:
    checkingObj.displayList()
    userInput = checkingObj.displayMenu()
    if (userInput == 1):
        checkingObj.addLevel()
        checkingObj.writeLevelsToFile()
    elif (userInput == 2):
        checkingObj.removeLevel()
        checkingObj.writeLevelsToFile()
    elif (userInput == 3):
        checkingObj.removeAllLevels()
        checkingObj.writeLevelsToFile()
    elif (userInput == 4):
        checkingObj.updateMenuPrice()

