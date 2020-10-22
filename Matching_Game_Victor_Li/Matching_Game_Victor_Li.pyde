""" Victor Li
VARIABLE MAP
NAME                     PURPOSE                             TYPE         RANGE
imageListNames           list of all images                  List         N/A
photoList                list of all loaded images           List         N/A
loadedVariableList       list of all variables(String)       List         N/A
variableList             list of all variables(int)          List         N/A
activePhotoList          list of active images,location,size List         N/A
bkx                      background width                    Int          800
bky                      background height                   Int          800
allBoundaries            list of all clickable areas         Int          N/A
gameBoard                list of "IMG 1" or "IMG 2"          List         N/A
startSquareX             x refrence point for create grid    Int          0
startSquareY             y refremce point for create grid    Int          0
sqaureXShow              x point for each row                Int          0-600
squareYShow              y point for each collume            Int          0-600
squareHeight             height of each square               Int          200
squareWidth              width of each square                Int          200
numSquares               number of squares per row           Int          4
numCards                 total number of squares/cards       Int          16
numImages                total number of 1 type of images    Int          8
removeSquare             makes Square unclickable            Bool         T/F
whichSquare              which square did u click            Int          (-1)-15
imageList                lables the images                   List          N/A
numberOfImages           determines # of dif type of IMG     Int           2
numberOfGameSpace        number of games spaces              Int           16
clickCounter             number of times clicked             Int           0-2
activeSquares            number of clickable areas           List          N/A
time                     time                                Int           Infinity
finishedSquares          the matched cards                   List          N/A
"""
import random
import time 

def setup():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, removeSquare, startSquareX, startSquareY
    global bkx, bky, numCards, time
    global imageList, gameBoard, numberOfImages, gameBoard, numberOfGameSpaces, numImages, photoList
    global clickCounter, activePhotoList, finishedSquares
    
    imageListNames = loadImageNames()
    photoList = loadImages( imageListNames )
    loadedVariableList = loadVariables()
    variableList = stringtoint(loadedVariableList)

    activePhotoList = []

    bkx = variableList[0]
    bky = variableList[1]
    
    allBoundaries = []
    gameBoard = []
    
    startSquareX = variableList[2]
    startSquareY = variableList[3]
    squareXShow = startSquareX
    squareYShow = startSquareY
    
    squareHeight = variableList[4]
    squareWidth = variableList[5]
    numSquares = variableList[6]
    numCards = variableList[7]
    numImages = variableList[8]
    removeSquare = True
    whichSquare = variableList[9]
    
    ##Load real Images
    imageList = ["a","b"]
    numberOfImages = len(imageList)
    numberOfGameSpaces = len(gameBoard)
    
    clickCounter = variableList[10]
    
    size ( 800, 900 )
    
    activeSquares = [ True for i in range( numCards ) ]
    loadSquaresToBoard()
    
    time = frameCount
    finishedSquares = []
    
def loadImageNames():
    
    file = open("images.txt")
    fileList = []                  #Start with an empty list
    text = file.readlines()
     
    for line in text:
        line = line.strip() #Gets rid of end-of-line markers, etc.
        row = ""
        for c in line:
            row = row + c
        rowList = row.split( ",")
    file.close
    return ( rowList )

def loadImages( imageListNames ):
     
    numImages = len( imageListNames )
    imageList = [ "" for i in range( numImages ) ]
    for i in range( numImages ):
        imageList[ i ] = loadImage( imageListNames[ i ] )

    return( imageList )

def loadSquaresToBoard():
    global imageList, gameBoard, numberOfImages, gameBoard, numImages, numberOfGameSpaces, photoList
    global allBoundaries
    for i in range (numberOfImages):
        for j in range (numImages):
            gameBoard.append(imageList[i])

    random.shuffle(gameBoard)
    numberOfGameSpaces = len(gameBoard)
    print(gameBoard)
    
def loadVariables():
    
    file = open("variables.txt")
    fileList = []                  #Start with an empty list
    text = file.readlines()
     
    for line in text:
        line = line.strip() #Gets rid of end-of-line markers, etc.
        row = ""
        for c in line:
            row = row + c
        rowList = row.split( ",")
    file.close

    return ( rowList )

def stringtoint(List):
    newList = []
    for i in range (len(List)):
         newList.append(int(List[i]))
    return( newList )
    
def resetTime():
    global time
    time = frameCount % 60
    return time
    
def loadPhotosToBoard():
    global activePhotoList, squareWidth, squareHeight, time, finishedSquares, activeSquares
    
    if len(activePhotoList) == 2:
        for i in range (len(activePhotoList)):
            image(activePhotoList[i][0], activePhotoList[i][1], activePhotoList[i][2], squareWidth, squareHeight)
        correct = checkCards(activePhotoList[0][0], activePhotoList[1][0])
        activeSquares = [ False for i in range( numCards ) ]
                        
        if time == 0:
            if correct:
                for i in range (len(activePhotoList)):
                    finishedSquares.append(activePhotoList[i][3])
            activeSquares = [ True for i in range( numCards ) ]
            for i in range (len(finishedSquares)):
                activeSquares[finishedSquares[i]] = False
       
            
            activePhotoList = []
    else:
        for i in range (len(activePhotoList)):
            image(activePhotoList[i][0], activePhotoList[i][1], activePhotoList[i][2], squareWidth, squareHeight)

    
def cardClicked(loc):
    global imageList, gameBoard, numberOfImages, gameBoard, numImages, numberOfGameSpaces, photoList
    global allBoundaries, squareWidth,squareHeight, activePhotoList, activePhotoList, activeSquares, whichSquare
        
    if gameBoard [loc] == "a":
        photoVar = [photoList[0], allBoundaries[loc][0][0], allBoundaries[loc][0][1],whichSquare]
        activePhotoList.append (photoVar)
    else:
        photoVar = [photoList[1], allBoundaries[loc][0][0], allBoundaries[loc][0][1],whichSquare]
        activePhotoList.append (photoVar)

               

def createGameArea (x ,y):
    global numSquares, startSquareX, startSquareY ,squareXShow ,squareYShow ,squareHeight ,squareWidth 
    for i in range( numSquares ):
        upperLeft =  [ x,y ]
        lowerRight = [ x  + squareWidth, y + squareHeight ]
        clickBoundary = [ upperLeft, lowerRight ]
        fill(225)
        rect( x , y, squareWidth, squareHeight )
        allBoundaries.append( clickBoundary )
    
        x = x + squareWidth
        

def checkCards(a,b):
    if a == b:
        return True
    else:
        return False        
    
    
def loadFinishedArea():
    global finishedSquares, allBoundaries, squareWidth, squareHeight
    fill(0)
    for i in range (len(finishedSquares)):
        rect(allBoundaries[finishedSquares[i]][0][0], allBoundaries[finishedSquares[i]][0][1], squareWidth, squareHeight)
        

def finishGame():
    global finishedSquares, numCards, activeSquares, activePhotoList, gameBoard
    if len(finishedSquares) == numCards:
        activeSquares = [ True for i in range( numCards ) ]
        activePhotoList = []
        finishedSquares = []
        random.shuffle(gameBoard)
        
        
        
def mouseReleased():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numCards
    
#  all Boundaries is a list of tuples,  each tuple is the upper left and lower right of each box
#  if removeSquare is True, you will not be able to click again in that square again as that place in activeSquares will be turned to False
    whichSquare = - 1
    for i in range( numCards ):
        if activeSquares[ i ]:
            validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
            validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
            validLocation = validXRange and validYRange
            if validLocation:
                whichSquare = i
                break
        else:
            validLocation = False
    if validLocation and removeSquare:
        activeSquares[ whichSquare ] = False
    
    if whichSquare > -1:
        cardClicked(whichSquare)
    print(whichSquare)
    

    

        


def draw():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, removeSquare, startFill, startSquareX, startSquareY
    global bkx, bky, numCards, whichSquare, activePhotoList
    resetTime()
    background(255)
    for i in range(numSquares):
        createGameArea(startSquareX, startSquareY + squareHeight * i)
    
    # createMenuArea()
    # createMenu()
   
    loadPhotosToBoard()
    loadFinishedArea()
    finishGame()
    

        

    
   
            
