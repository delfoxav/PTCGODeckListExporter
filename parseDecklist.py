from card import Card


from deck import Deck
from deck import Jan2022_Format
def parseTCGODecklist(filename):
    deck= Deck(name=filename)
    with open( f"Import/{filename}", "r", encoding="utf-8") as tcgolist:
        while line :=tcgolist.readline():
            if line[:9] == "##Pokémon":
                tcgolist.readline()
                while line !="\n":
                    line=tcgolist.readline()
                    if line !="\n":
                        amount,first = getAmountCard(line)
                        set,last = getSet(line)
                        collnum = getCollNum(line)[0]
                        card = Card(amount = amount, name = line[first:last], type = "Pokemon", set = set, coll_num = collnum)
                        deck.add_card(card)
            if line[:9] == "##Trainer":
                tcgolist.readline()
                while line !="\n":
                    line=tcgolist.readline()
                    if line !="\n":
                        amount,first = getAmountCard(line)
                        set,last = getSet(line)
                        collnum = getCollNum(line)[0]
                        card = Card(amount = amount, name = line[first:last], type = "Trainer", set = set, coll_num = collnum)
                        deck.add_card(card)
            if line[:8] == "##Energy":
                tcgolist.readline()
                while line !="\n":
                    line=tcgolist.readline()
                    if line !="\n":
                        amount,first = getAmountCard(line)
                        set,last = getSet(line)
                        if last is None:
                            collnum,last = getCollNum(line)
                        else:
                            collnum = getCollNum(line)[0]
                        card = Card(amount = amount, name = line[first:last], type = "Energy", set = set, coll_num = collnum)
                        deck.add_card(card)
    #retest the format as new cards have been added
    deck.format =deck.setFormat(Jan2022_Format)
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
        
    return (int("".join(collNum)),i+1)

def getSet(line):
    set = []
    for i in range(len(line)-1,0,-1):
        if line[i].isupper() and line[i].isalpha() or line[i] =="-":
            set.insert(0,line[i])
        if line[i] == " " and line[i+1] in set:
            break
        #Handle basics Energies without set
        if set == ["E"]:
            return None,None
    return ("".join(set),i)

def remove_spaces(text):
    """Return a copy of text without spaces and newline. Use String translate method
    
    param text: text to translate to a non space version
    type text: str
    """
    #Uses the ascii code for white spaces here as " ","\n" and "\r\n" do not find anything
    translation={32:"",13:"",10:"",9:""}
    return(text.translate(translation))

if __name__ == "__main__":
    parseTCGODecklist("Import/turbo_dark.txt").exportToTCGO()