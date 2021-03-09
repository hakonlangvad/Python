import math, time

def choosingDirToGo(potentials,goalPos,rows,cols,visited):
    '''
    Takes in potential location an object can move to from it's cell and goal locatiion
    returns the location that is closest to the goal cell
    '''
    less = max(rows,cols)**2
    count = 0
    for pos in potentials:
        diff = math.sqrt(abs(pos[0]-goalPos[0])**2 + abs(pos[1]-goalPos[1])**2)
        if diff < less and (pos[0],pos[1]) not in visited:
            returnValue = (pos[0],pos[1])
            less = diff
            count += 1
    if count > 0:
        return returnValue
    else:
        return False
    
def reachablePath(pathGoal,locations):
    '''
    Takes in a path to goal and all the locations on the grid
    Finds all the straight lines that can be walked
    Returns a new list of path to goal which should've been shrinked
    '''
    for index in range(2):
        i = 1
        while i < len(pathGoal):
            lastPos = pathGoal[-i]
            y = 0
            while y < len(pathGoal):
                firstPos = pathGoal[y]
                if firstPos != lastPos:
                    if lastPos[index] == firstPos[index]: # If x-values are the same. Check if reachable straight line
                        checkList = []
                        for loc in locations:
                            if loc[index] == lastPos[index]:
                                checkList.append(loc)
                        checkList = sorted(checkList)
                        straightLine = True
                        start = 0
                        end = len(checkList)-1
                        for x in range(len(checkList)):
                            if checkList[x] == lastPos:
                                start1 = x
                            if checkList[x] == firstPos:
                                end1 = x
                        start = min(start1,end1)
                        end = max(start1,end1)
                        run = False
                        checkList2 = []
                        if index == 0:
                            index2 = 1
                        else:
                            index2 = 0
                        for x in range(abs(start-end)):
                            if checkList[x+start] != startPos:
                                checkList2.append(checkList[x+start])
                            if checkList[x+start] not in pathGoal:
                                run = True
                            if checkList[x+start][index2] != checkList[x+start+1][index2] - 1:
                                straightLine = False
                                break
                        if straightLine and run:
                            value1 = len(pathGoal) - i
                            value2 = y
                            getOtherValues = []
                            for x in range(abs(value1 - value2)):
                                pathGoal.remove(pathGoal[value1 - x])
                            get = False
                            for x in range(len(pathGoal)):
                                if get:
                                    getOtherValues.append(pathGoal[x])
                                if pathGoal[x] == firstPos:
                                    get = True
                            
                            x = 0
                            while x < len(pathGoal):
                                if pathGoal[x] in getOtherValues:
                                    pathGoal.remove(pathGoal[x])
                                else:
                                    x += 1
                            for x in range(len(checkList2)):
                                pathGoal.append(checkList2[x])
                            pathGoal.append(lastPos)
                            for x in range(len(getOtherValues)):
                                pathGoal.append(getOtherValues[x])
                y += 1
            i += 1
    return pathGoal


if __name__ == '__main__':

    locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),
                (0,1),(1,1),(2,1),(3,1),(4,1),(6,1),(9,1),
                (0,2),(1,2),(2,2),(3,2),(4,2),(6,2),(8,2),(9,2),
                (0,3),(1,3),(2,3),(3,3),(4,3),(9,3),
                (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(7,4),(8,4),(9,4),
                (9,5),
                (0,6),(1,6),(2,6),(4,6),(5,6),(6,6),(8,6),(9,6),
                (0,7),(2,7),(3,7),(4,7),(6,7),(9,7),
                (0,8),(2,8),(3,8),(6,8),(7,8),(9,8),
                (0,9),(2,9),(3,9),(5,9),(6,9),(7,9),(8,9),(9,9)]

    ######## Variables ########
    rows = 10
    cols = 10
    goalPos = (0,9)
    startPos = (0,0)
    ###########################

    ######## Constants ########
    relatives = {}
    path = []
    pathGoal = []
    visited = []
    position = startPos
    reachable = True

    ############### Finding connected cells ###############
    for y in range(len(locations)): # Goes through all the cells
        loc = locations[y]
        relatives[loc] = [] # Cells that are reachable will be added here
        dx = [1,-1,0, 0] # North, South, East, West
        dy = [0, 0,1,-1]
        for i in range(len(dx)): # Looping North, South, East, West
            xx = loc[0] + dx[i] 
            yy = loc[1] + dy[i]
            '''
            If the location is within the board and the coordinate is in the locations-list:
            It will be added to the relatives dictionary:
            '''
            if xx >= 0 and xx < rows and yy >= 0 and yy < cols and (xx,yy) in locations:  
                relatives[loc].append((xx,yy))


    ############### Finding the path ###############

    print("\nSTART POSITION: " + str(startPos))
    while True:
        if position not in path:
            path.append(position)
        if position not in visited:
            visited.append(position)
        if position == goalPos:
            break
        potentials = relatives[position]
        toGo = choosingDirToGo(potentials,goalPos,rows,cols,visited)
        if toGo != False:    
            position = toGo
        else:
            # If stuck, start backtracking cell by cell
            if position == path[0]:
                print("It's not possible to reach the goal location")
                reachable = False
                break
            path.remove(path[-1])
            position = path[-1]
        #time.sleep(3)

    ############### Removes round trips ###############
    if reachable:    
        pathGoal = path
        i = 1
        while True:
            pos = path[-i]
            if pos == startPos:
                break
            potentials = relatives[pos]
            for y in range(len(path)):
                for x in range(len(potentials)):
                    if y < len(path):
                        if potentials[x] == path[y] and len(path) - y != i+1 and len(path) - y != i-1:
                            diff = abs(len(pathGoal) - y - i)
                            for z in range(1,diff):
                                pathGoal.remove(pathGoal[y+diff-z])
            i += 1
        
        # Finds straight lines
        pathGoal = reachablePath(pathGoal,locations)

        # Found shortest path
        print("\nSHORTEST PATH IS LOCATIONS:")
        for i in range(len(pathGoal)-1):
            print(pathGoal[i],end=(", "))
        print(pathGoal[-1])

