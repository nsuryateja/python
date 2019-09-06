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
        print(x)
        print(y)
        
virat = parser("https://en.wikipedia.org/wiki/Virat_Kohli")
smith = parser("https://en.wikipedia.org/wiki/Steve_Smith")
sachi = parser("https://en.wikipedia.org/wiki/Sachin_Tendulkar")
willi = parser("https://en.wikipedia.org/wiki/Kane_Williamson")
root  = parser("https://en.wikipedia.org/wiki/Joe_Root")
abd   = parser("https://en.wikipedia.org/wiki/Ab_Devilliers")
azam  = parser("https://en.wikipedia.org/wiki/Babar_Azam")

cricket = virat+smith+sachi+willi+root+abd+azam

cricket = "\n".join(cricket)
f = open('cricket.txt','w',encoding='UTF-8')
f.write(cricket)

desa  = parser("https://en.wikipedia.org/wiki/Morarji_Desai")
rajiv = parser("https://en.wikipedia.org/wiki/Rajiv_Gandhi")
modi  = parser("https://en.wikipedia.org/wiki/Narendra_Modi")
mohan = parser("https://en.wikipedia.org/wiki/Manmohan_Singh")
atal  = parser("https://en.wikipedia.org/wiki/Atal_Vajpayee")

pm = desa+rajiv+modi+mohan+atal

pm = "\n".join(pm)
p = open('pm.txt','r+',encoding='UTF-8')
p.write(pm)


#Printing paragraphs??
printPara(?)
