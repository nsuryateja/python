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

crics = ("Virat_Kohli","Steve_Smith","Sachin_Tendulkar","Kane_Williamson","Joe_Root","Ab_Devilliers","Babar_Azam")
polis = ("Morarji_Desai","Rajiv_Gandhi","Narendra_Modi","Manmohan_Singh","Atal_Vajpayee")

def paraString(Items):
    """
    Takes in tuple of items and gives a string of paragraphs
    
    """
    
    string = []
    for item in Items:
        string = parser("https://en.wikipedia.org/wiki/" + item) + string
    string = "\n".join(string)
    return string
    
cricket = paraString(crics)
pm = paraString(polis)

def writeTo(content,filename):
    
    """
    Takes in content of string, writes to a file
    """
    
    with open(filename,"w") as f:
        f.write(content)
        
writeTo(cricket,"cricket.txt")
writeTo(pm,"pm.txt")

def printAlt(f1,f2):
    """
    Takes two files and prints them in akterante paragraph manner
    """
    
    with open(f1,"r") as file1, open(f2,"r") as file2:
        for p1,p2 in zip(file1.readlines(),file2.readlines()):
            print("-----first-------")
            print(p1)
            print("-----second------")
            print(p2)
            
printAlt("cricket.txt","pm.txt")

    

