name1='samsung galaxy g4'
name2='samsung galaxy g2'
name3='battle of thrones'
name4='savitor the flash in the season last'
name5='donning it in style'
name6='style donning it in'
def matchString(str1,str2):
    lst1=str1.split()
    lst2=str2.split()
    lst1.sort()
    lst2.sort()
    print('return values are ')
    if len(str1)>25:
        return 0
    elif len(str2)>25:
        return 1
    elif lst1==lst2:
        return 2
    else:
        return 3
def matchStr(str3,str4):
    print(str3+str4)
returnVal1=matchString(name1,name2)
returnVal2=matchString(name3,name4)
returnVal3=matchString(name5,name6)
