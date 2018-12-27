def returnOnceDigit(num):
        div = 1
        for i in range(1,len(str(num))):
                div = div * 10
        num = int(num)
        while(not num < 10):
                num = num % div
                div = div/10
        return int(num)
print('enter a num:')
print(returnOnceDigit(input()))
