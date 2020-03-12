global testCases
global currentCase
global index
global numServers
global requiredP
global compPower
global currentL
global currentR
global totalP
global currentWasteP
global bestWasteP
global bestL
global bestR
global outputString

inputFile = open("input.txt","r")
lines = inputFile.readlines()
inputFile.close()

testCases = int(lines[0])
lines.pop(0)

for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
    lines[i] = lines[i].split(' ')

def initialiseVariables():
    global currentCase, index, numServers, requiredP, compPower, currentL, currentR, totalP, currentWasteP, bestWasteP, bestL, bestR, outputString
    currentCase = int(lines[0][0])
    index = ((currentCase-1)*3)
    numServers = int(lines[index+1][0])
    requiredP = int(lines[index+1][1])
    compPower = lines[index+2]
    for j in range(len(compPower)):
        compPower[j] = int(compPower[j])
    currentL = 0
    currentR = 0
    totalP = 0
    currentWasteP = 0
    bestWasteP = 100000000000000000000000000
    bestL = 0
    bestR = 0
    outputString = ""

initialiseVariables()

##MAKE CHECKING CODE A FUNCTION, RETURN AND INPUT? GLOBAL VAR?

def checkIfBest(b):
    global currentCase, index, numServers, requiredP, compPower, currentL, currentR, totalP, currentWasteP, bestWasteP, bestL, bestR, outputString
    if totalP >= requiredP:
        currentR = b
        b = numServers+1
        currentWasteP = totalP - requiredP
        if currentWasteP < bestWasteP:
            bestL = currentL
            bestR = currentR
            bestWasteP = currentWasteP
        elif currentWasteP == bestWasteP:
            if currentL < bestL:
                bestL = currentL
                bestR = currentR
    return b

def doIteration():
    global currentCase, index, numServers, requiredP, compPower, currentL, currentR, totalP, currentWasteP, bestWasteP, bestL, bestR, outputString
    for a in range(numServers):
        currentL = a
        currentR = 0
        totalP = 0
        if currentL == numServers-1:
            totalP = compPower[numServers-1]
        else:
            for b in range(a, numServers-1):
                totalP += compPower[b]
                b = checkIfBest(b)
                if totalP >= requiredP:
                    break

doIteration()

outputString += "Case #" + str(currentCase) + ": " + str(bestL) + " " + str(bestR)

print(outputString)

#print(testCases)
#print(currentCase)
#print(index)
#print(numServers)
#print(requiredP)
#print(compPower)
#print(bestL)
#print(bestR)
