playerA = {
    "Ap1" : True,
    "Ap2" : True,
    "Ap3" : True,
    "Ap4" : True,
    "Ap5" : True,
}
playerB = {
    "Bp1" : True,
    "Bp2" : True,
    "Bp3" : True,
    "Bp4" : True,
    "Bp5" : True,
}

posA = {
    "Ap1" : "00",
    "Ap2" : "01",
    "Ap3" : "02",
    "Ap4" : "03",
    "Ap5" : "04",
}

posB = {
    "Bp1" : "40",
    "Bp2" : "41",
    "Bp3" : "42",
    "Bp4" : "43",
    "Bp5" : "44",
}

status = True
playerentry = True
currentPlayer = "playerA"

matrix = [
        ["-","-","-","-","-"],
        ["-","-","-","-","-"],
        ["-","-","-","-","-"],
        ["-","-","-","-","-"],
        ["-","-","-","-","-"],]



while(status):
    # ?\ when player enter on a game
    if(playerentry):
        print("player 1 enters")
        matrix[0] = ["Ap1","Ap2","Ap3","Ap4","Ap5"]
        print(matrix)
        print("player 2 enters")
        matrix[4] = ["Bp1","Bp2","Bp3","Bp4","Bp5"]
        print(matrix)
        playerentry = False
    else:
        userInput = input("Enter your input"+currentPlayer)
        if(userInput == "out"):
            status = False
            break
        if(currentPlayer == "playerA"):
            temp = posA.get(userInput)
            matrix[int(temp[0])][int(temp[1])] = "-"
            matrix[int(temp[0])+1][int(temp[1])] = userInput
            newpos = str(int(temp[0])+1) + "" + temp[1]
            posA.update({userInput : newpos})
            print(matrix,posA)
            currentPlayer = "playerB"
        else:
            tmep = posB.get(userInput)
            matrix[int(temp[0])][int(temp[1])] = "-"
            matrix[int(temp[0])-1][int(temp[1])] = userInput
            newpos = str(int(temp[0])-1) + "" + temp[1]
            posB.update({userInput : newpos})
            print(matrix,posB)
            currentPlayer = "playerA"
        
    
    
    
        
    
    
    
    
    
    
    
    
        
    
    
    
    
    
