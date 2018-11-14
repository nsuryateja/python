def subsequences(text):
        if len(text) == 1:
                return 1
        elif len(text) == 2:
                return 3
        else:
                return subsequences(text[1:len(text)])*2+1
no_of_subs = subsequences('abcdef')
print(no_of_subs)
