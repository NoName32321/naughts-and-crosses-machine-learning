#tic tac toe ai

import random

def displayBoard():
    resString = ""
    for i in curPos:
        if i == '0':
            resString += " "
        elif i == '1':
            resString += "X"
        elif i == '2':
            resString += "O"
    print("")
    print("Current move number: ", curMoveNum)
    print("The current position is:")
    print("当前移动编号是：", curMoveNum)
    print("当前局势为：")
    print("")
    print("    1   2   3")
    print("a  ", resString[0], " ", resString[1], " ", resString[2])
    print("b  ", resString[3], " ", resString[4], " ", resString[5])
    print("c  ", resString[6], " ", resString[7], " ", resString[8])

def playerMove():
    global curPos
    inputValid = False
    while inputValid != True:
        inputValid = True
        print("")
        print("Input position.")
        print("输入位置。")
        print("")
        inputMove = input("    >>> ")
        if not (len(inputMove) == 2 and inputMove[0] in {'a', 'b', 'c'} and inputMove[1] in {'1', '2', '3'}):
            inputValid = False
            print("")
            print("Output invalid, try again.")
            print("位置无效，请重新输入。")
            
        if inputValid == True:
            moveIndex = 0
            if inputMove[0] == 'a':
                moveIndex += 0
            elif inputMove[0] == 'b':
                moveIndex += 3
            elif inputMove[0] == 'c':
                moveIndex += 6
            moveIndex += int(inputMove[1]) - 1
            if curPos[moveIndex] == 0:
                inputValid = False
                print("")
                print("Location invalid, try again.")
                print("位置无效，请重新输入。")
        
        if inputValid == True:
            curPos = curPos[:moveIndex] + '1' + curPos[moveIndex + 1:]
        
def checkWin(sub):
    pWin = False
    if curPos[0] == sub and curPos[3] == sub and curPos[6] == sub:
        pWin = True
    elif curPos[1] == sub and curPos[4] == sub and curPos[7] == sub:
        pWin = True
    elif curPos[2] == sub and curPos[5] == sub and curPos[8] == sub:
        pWin = True
                    
    if curPos[0] == sub and curPos[1] == sub and curPos[2] == sub:
        pWin = True
    elif curPos[3] == sub and curPos[4] == sub and curPos[5] == sub:
        pWin = True
    elif curPos[6] == sub and curPos[7] == sub and curPos[8] == sub:
        pWin = True
                    
    if curPos[0] == sub and curPos[4] == sub and curPos[8] == sub:
        pWin = True
    elif curPos[2] == sub and curPos[4] == sub and curPos[6] == sub:
        pWin = True
    
    return pWin
    
def computerMove():
    global mainStore
    global curPos
    global posRecord
    global moveRecord
    
    if not curPos in mainStore:
        newToken = ""
        for i in curPos:
            if i == '0':
                newToken += "10"
            else:
                newToken += "00"
        mainStore[curPos] = newToken
        
    moveTokens = mainStore[curPos]
    totalTokens = 0
    moveTokensTotal = []
    for i in range(9):
        totalTokens += int(moveTokens[i*2:i*2+2])
        moveTokensTotal.append(moveTokens[i*2:i*2+2])
    randNum = random.randint(0, totalTokens)
    moveIndex = 0
    while randNum > 0:
        randNum -= int(moveTokensTotal[moveIndex])
        moveIndex += 1
    moveIndex -= 1
    moveRecord.append(moveIndex)
    posRecord.append(curPos)
    curPos = curPos[:moveIndex] + '2' + curPos[moveIndex + 1:]
    
    if moveIndex == 0:
        resMove = 'a1'
    elif moveIndex == 1:
        resMove = 'a2'
    elif moveIndex == 2:
        resMove = 'a3'
    elif moveIndex == 3:
        resMove = 'b1'
    elif moveIndex == 4:
        resMove = 'b2'
    elif moveIndex == 5:
        resMove = 'b3'
    elif moveIndex == 6:
        resMove = 'c1'
    elif moveIndex == 7:
        resMove = 'c2'
    elif moveIndex == 8:
        resMove = 'c3'
    
    print("")
    print("Computer played: ", resMove)
    print("电脑下在了：", resMove)

def updateTokens(result):
    global mainStore
    for i in range(len(posRecord)):
        tokenChange = mainStore[posRecord[i]][moveRecord[i] * 2: moveRecord[i] * 2 + 2]
        
        if result == 'Win':
            tokenChange = int(tokenChange) + 5
        elif result == 'Loss':
            tokenChange = int(tokenChange) - 2
        elif result == 'Tie':
            tokenChange = int(tokenChange)
            
        if tokenChange < 1:
            resToken = '01'
        elif tokenChange < 10:
            resToken = '0' + str(tokenChange)
        elif tokenChange > 99:
            resToken = '99'
        else:
            resToken = str(tokenChange)

        mainStore[posRecord[i]] = mainStore[posRecord[i]][:moveRecord[i] * 2] + resToken + mainStore[posRecord[i]][moveRecord[i] * 2 + 2:]


#==========Setup==========

print("Insert priming state: (if none, enter 'NONE')")
print("输入初始状态: (如果没有，输入'NONE')")
print("")
strInpDict = input("    >>> ")

if strInpDict == 'NONE':
    print("")
    print("New state created.")
    print("新状态已生成。")
    mainStore = {}
else:
    print("")
    print("Input accepted, priming:")
    print("输入已被接受，系统初始化中:")

    if 4 % strInpDict.count("'") != 4:
        print("")
        print("Priming state text contains error. Make sure you copied the entire text.")
        print("初始状态文本错误。请确认你是否拷贝了整个文本。")
    else:
        pairTotal = int(strInpDict.count("'") / 4)

    inString = False
    tempKeyStr = ""
    tempValueStr = ""
    isKey = True
    pairCount = 0
    mainStore = {}

    for char in strInpDict:
    
        if char == "'":
            if inString is True:
                isKey = not isKey
            inString = not inString
            
        elif inString is True:
            if isKey is True:
                tempKeyStr += char
            else:
                tempValueStr += char
    
        if char == "'" and inString is False and isKey is True:
            mainStore[tempKeyStr] = tempValueStr
            tempKeyStr = ""
            tempValueStr = ""
            pairCount += 1
            print("Priming state: (", pairCount, "/", pairTotal, ")")

    print("")
    print("Priming complete!")
    print("初始化完毕！")

    print("")
    print("!!!DEBUG!!!")
    print(mainStore)

#========== MAIN BODY ==========
uInput = ''
while uInput != 'END':
    
    print("")
    print("Menu:")
    print("    'START': Starts training.")
    print("    'END': Ends training and prints priming state text.")
    print("    'HELP': Gives help text.")
    print("")
    print("主页面：")
    print("    'START'：开始训练。")
    print("    'END'：结束训练并打印初始状态文本。")
    print("    'HELP'：打印辅导文本")
    print("")
    uInput = input("    >>> ")
    
    if uInput == 'END':
        print("")
        print("Training ended. Here is the priming text:")
        print("训练结束。这是初始化文本：")
        print("")
        print(mainStore)
    
    elif uInput == 'HELP':
        print("")
        print("This is a tic-tac-toe artificial intelligence machine learning trainer based on the matchbox experiment.")
        print("这是一个基于火柴盒实验的井字式人工智能机器学习训练器。")
        print("")
        print("You will be given a 3 by 3 grid marked with a, b, and c on the horizontal axis and 1, 2, and 3 on the vertical axis.")
        print("您将得到一个3乘3的网格，在水平轴上标有a、b和c，在垂直轴上标有1、2和3。")
        print("")
        print("Your marker is the X, the computer's is the O, and you will start first. You will take turns with the computer to move on the grid. You mark the location you want to move by entering the lowercase letter and the number, such as 'a1', or 'c2'.")
        print("你的标记是X，计算机的标记是O，你会先开始。您将轮流使用电脑在网格上下棋。您可以通过输入小写字母和数字来标记要标记的位置，例如'a1'或'c2'。")
    
    #========== MAIN TRAINING ==========
    
    elif uInput == 'START':
        while uInput != 'EXIT':
            print("")
            print("Game started.")
            print("游戏开始。")
            
            curPos = '000000000'
            moveRecord = []
            posRecord = []
            curMoveNum = 0
            isEnd = False
            
            while isEnd == False:
                curMoveNum += 1
                displayBoard()
                playerMove()
                if checkWin('1') == True:
                    isEnd = True
                    print("")
                    print("You win!")
                    print("你赢啦！太棒棒喽！")
                    updateTokens('Loss')
                elif curMoveNum == 5:
                    isEnd = True
                    print("")
                    print("You tied.")
                    print("bro连机器都打不过XD")
                    updateTokens('Tie')
                else:
                    computerMove()
                    if checkWin('2') == True:
                        isEnd = True
                        print("")
                        print("You lost.")
                        print("bro尽然输给了机器XD")
                        updateTokens('Win')
            
            print("")
            print("To exit, enter 'EXIT'; to continue, enter anything.")
            print("要退出，请输入'EXIT'；要继续，请输入任何内容。")
            print("")
            uInput = input("    >>> ")
            
    else:
        print("")
        print("Responce invalid. Check for spelling mistakes and try again.")
        print("响应无效。检查拼写错误，然后重试。")
            
            
            
            
            
            
            
            


