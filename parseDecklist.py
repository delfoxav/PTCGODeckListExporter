from numpy import number
from card import Card


from deck import Deck
def parseTCGODecklist(filename):
    deck= Deck(name=filename)
    with open(filename, "r", encoding="utf-8") as tcgolist:
        while line :=tcgolist.readline():
            if line[:9] == "##Pokémon":
                tcgolist.readline()
                while line !="\n":
                    line=tcgolist.readline()
                    if line !="\n":
                        amount,first = getAmountCard(line)
                        set,last = getSet(line)
                        collnum = getCollNum(line)
                        card = Card(amount = amount, name = line[first:last], type = "Pokemon", set = set, coll_num = collnum)
                        deck.add_card(card)
            if line[:9] == "##Trainer":
                tcgolist.readline()
                while line !="\n":
                    line=tcgolist.readline()
                    if line !="\n":
                        amount,first = getAmountCard(line)
                        set,last = getSet(line)
                        collnum = getCollNum(line)
                        card = Card(amount = amount, name = line[first:last], type = "Trainer", set = set, coll_num = collnum)
                        deck.add_card(card)
            if line[:8] == "##Energy":
                tcgolist.readline()
                while line !="\n":
                    line=tcgolist.readline()
                    if line !="\n":
                        amount,first = getAmountCard(line)
                        set,last = getSet(line)
                        collnum = getCollNum(line)
                        card = Card(amount = amount, name = line[first:last], type = "Energy", set = set, coll_num = collnum)
                        deck.add_card(card)
    return deck    
        
            
            
            

def getAmountCard(line):
    amount = []
    numbers = "0123456789"
    letter = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(line)):
        if line[i] in numbers:
            amount.append(line[i])
        if line[i].lower() in letter:
            break
    if amount !=[]:
        return (int("".join(amount)),i)

def getCollNum(line):
    collNum = []
    numbers ='0123456789'
    letter = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(line)-1,0,-1):
        if line[i] in numbers:
            collNum.insert(0,line[i])
        if line[i].lower() in letter:
            break
        
    return int("".join(collNum))

def getSet(line):
    set = []
    for i in range(len(line)-1,0,-1):
        if line[i].isupper() and line[i].isalpha():
            set.insert(0,line[i])
        if line[i] == " " and line[i+1] in set:
            break
    return ("".join(set),i+1)

if __name__ == "__main__":
    parseTCGODecklist("testlist.txt").exportToTCGO()