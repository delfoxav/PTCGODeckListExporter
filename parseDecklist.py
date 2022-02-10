from card import Card


from deck import Deck
from deck import Jan2022_Format

def parseTCGODeckListFromFile(filename):
    with open( f"Import/{filename}", "r", encoding="utf-8") as tcgolist:
        contents = tcgolist.read()
        print (contents)
        #return parseTCGODecklist(filename.strip(".txt"), contents)


def parseTCGODecklist(deckName, deckList, format=""):
    deck= Deck(name=deckName)

    #TODO : implement formatting guessing to handle decklists from other sources like LimitlessTCG, etc.

    section = ''

    for line in deckList.split('\n'):
        line = line.strip('\r').rstrip()
        #print ("Line "+line)

        if line.startswith("****** Pokémon Trading Card Game Deck List ******"):
            continue
        
        if line.startswith("##Pokémon") or line.startswith("Pokémon") or line.startswith("Pokemon"):
            section="Pokemon"
            continue
        if line.startswith("##Trainer") or line.startswith("Trainer"):
            section="Trainer"
            continue
        if line.startswith("##Energy") or line.startswith("Energy"):
            section="Energy"
            continue

        if line == "":
            continue

        if line.startswith("Total Cards"):
            break

        amount,first = getAmountCard(line)
        set,last = getSet(line)
        if last is None:
            collnum,last = getCollNum(line)
        else:
            collnum = getCollNum(line)[0]
        card = Card(amount = amount, name = line[first:last], type = section, set = set, coll_num = collnum)
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