import random
print('enter your age:')
age = int(input())
disease = ['cancer','laughter','jumping off a building','the worst disease ever discovered']
print('you are born in: '+ str(2018 -age),end = ' ')
print( 'and you will turn 100 years in: '+ str(100-age+2018))
print('if and only if you dont die of ' + disease[random.randint(0,3)] + ' in: '+ str(random.randint(2018,100-age+2018)))
