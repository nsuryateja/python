def printIt(items):
    lens = max([len(i) for i in items])
    for i in range(len(items)):
        for j in range(lens):
            if len(items[i]) <= j:
                if j+1 != lens:
                    print("_", end = ",")
                else:
                    print("_")
            else:
                if j+1 != lens:
                    print(items[i][j], end = ",")
                else:
                    print(items[i][j])
printIt(["suneet","two","three","four","sharath"])
