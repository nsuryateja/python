"""Write a code to read  the data from  input file called input.txt 
and count the number of characters per line, number of words per line 
and write these into output file called as output.txt"""
contents = [line.rstrip('\n') for line in open('input.txt','r')]
f = open('output.txt','a')
f.write('characters_per_line:')
for item in contents:
        f.write(len(item))
        print(' ',end = '')
print('\n')        
f.write('no_of_words_per_line:')
for item in contents:
        f.write(len(item.split(' ')))
        print(' ',end = '')
f.close()
