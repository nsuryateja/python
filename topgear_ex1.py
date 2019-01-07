def returnOnceDigit(no):
        """Returns once digit og a given number
           Input : Integer
           Output: Once digit of that integer"""
           
        div = 1
        for i in range(1,len(str(no))):
                div = div * 10
        no = int(no)
        while(not no < 10):
                no = no % div
                div = div/10
        return int(no)
#Ruler function        
def ruler(num):
        """Prints the ruler
        Input: Integer
        Output: Ruler"""
        
        if num%9:
            inches = num//9
        else:
            inches = num//9 -1
        for i in range(1,inches+1):
                print(' '*9, end = '')
                print(i,end = '')
        print('\n')
        length = 0
        while(not length==num):
                print(returnOnceDigit(length+1),end='')
                length = length +1
#Calling the function to print for 80
ruler(80)
