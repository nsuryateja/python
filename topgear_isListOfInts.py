def isListOfInts(intList):
    """Return True for ints and empty list: False if any character present: Throws Value Error for non-list type"""        
    if not type(intList) == list:
            raise ValueError('arg not of <list> type')
    elif not intList:
            return True
    else:   
        for item in intList:
            if not type(item) == int:
                return False
        return True
