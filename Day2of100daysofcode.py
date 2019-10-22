contents = """This program counts the number of words in the given sentence
even though it has new lines"""
def replacer(text):
    helper = ""
    for i in text:
        if i == "\n":
            helper = helper + " "
            continue
        helper = helper + i
    return helper
def counter(text):
    text = replacer(text)
    return len(text.split())
print(counter(contents))
