print("""Welcome to the Tic toc toe game!
This is a two player game: Player 1 and Player 2""")
P1 = input("@Player1 - Please select X or O: ").upper()
P2 = "O" if P1 == "X" else "X"
Inputs = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
win = [(0,1,2),(0,3,6),(0,4,8),(3,4,5),(1,4,7),(2,4,6),(2,5,8),(6,7,8)]
def winner(Inp, listy):
    for tup in listy:
        if (Inp[tup[0]] + Inp[tup[1]] + Inp[tup[2]]).upper() == P1*3:
            return P1
        if (Inp[tup[0]] + Inp[tup[1]] + Inp[tup[2]]).upper() == P2*3: 
            return P2
    return "Not Decided"  
player = ["@Player1","@Player2"]  

def play():
    val = 0
    while(winner(Inputs,win)) == "Not Decided":
        
        pos = int(input(f"{player[val]} - Please select the position (1-9) :"))
        while not pos in list(range(1,10)) or not Inputs[pos-1] == " ":
             print("Already choosen or INVALID: Choose another")
             pos = int(input(f"{player[val]} - Please select the position (1-9) :"))
        Inputs[pos-1] = P1 if val == 0 else P2
        print(Inputs)
        print(f"""
     |     |     
  {Inputs[6]}  |  {Inputs[7]}  |  {Inputs[8]}  
     |     |     
------------------
     |     |     
  {Inputs[3]}  |  {Inputs[4]}  |  {Inputs[5]}  
     |     |     
------------------
     |     |     
  {Inputs[0]}  |  {Inputs[1]}  |  {Inputs[2]}  
     |     |      
""")
        if winner(Inputs,win) == P1 or winner(Inputs,win) == P2:
            print(f"Congratulations {player[val][1:-1] + ' ' + player[val][-1]} Wins")
            break
        val = 1 - val
play()
