from bs4 import BeautifulSoup
import requests
def parser(link):
    """
    This function takes the URL of the wikipedia page and returns the list of all paragraphs
    """
    source = requests.get(link).text
    soup =  BeautifulSoup(source,'lxml')
    content = soup.find("div", id = "mw-content-text")
    plist = [para.text for para in content.find_all("p") if not para.text == "\n"]
    return plist
def printPara(list1,list2):
    """
    This function takes two lists and prints paragraphs picking alternatively
    """
    for x,y in zip(list1,list2):
        print("------STEVE-------")
        print(x)
        print("------BILL-------")
        print(y)
# Takes only the first six paragraphs
steve = parser("https://en.wikipedia.org/wiki/Steve_Jobs")[:6]
bill = parser("https://en.wikipedia.org/wiki/Bill_Gates")[:6]
#Printing paragraphs
printPara(steve,bill)
