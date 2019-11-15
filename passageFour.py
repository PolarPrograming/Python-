def drawABearWithString(paddingStr,row=18,column=23):
    if row < 18:
        row = 18
    retString = ""
    left, right = 3, 4
    for y in range(row):
        if y < int(row/18)*3: 
            for x in range(column):
                if (x >= left and x <= right) \
                or (x >= column-right-1 and x <= column-left-1):
                    retString += paddingStr[int((x-y)%len(paddingStr))]+" "
                else: 
                    retString += "  "
            retString += "\n"
            left -= 1; right += 1
        elif y >= int(row/18)*3 and y < int(row/18)*(3+9):
            for x in range(column):
                retString += paddingStr[int((x-y)%len(paddingStr))]+" "
            retString += "\n"
        elif y >= int(row/18)*(3+9) and y < int(row/18)*(3+9+6):
            if y % 2 == 0: left += 2; 
            for x in range(column):
                if x >= left and x <= column-left-1: 
                    retString += paddingStr[int((x-y)%len(paddingStr))]+" "
                else: 
                    retString += "  "
            retString += "\n"
    return retString

paddingStr = "Python!"
bear = drawABearWithString(paddingStr)
print(bear)

paddingStr = "Python!"
bear = drawABearWithString(paddingStr,20,28)
print(bear)
