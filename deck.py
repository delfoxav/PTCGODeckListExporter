from card import Card
import os
import format

Jan2022_Format = format.Jan2022_Format

class Deck:
    
    def __init__(self, name = "", cards=[], hasAcespec = False) -> None:
        """Create a new deck"""
        
        self.Pokemon = []
        self.Trainer = []
        self.Energy = []
        self.hasAcespec = hasAcespec
        self.name = name
        self.add_cards(cards)
        self.format=self.setFormat(Jan2022_Format)
        
    def add_card(self, card) -> None:
        """Add a card to a deck"""
        if card.isAcespec and self.hasAcespec:
            raise DeckMoreThanOneAceSpecError(f"Can't add {card.name} to {self.name}, the deck already has an AceSpec")
        elif card.isAcespec:
            self.hasAcespec = True
        if card.type == "Pokemon":
            sumCard = Card(card.amount, card.name, card.type, card.set, isAcespec=card.isAcespec, isPrism=card.isPrism)
            for pokemon in [c for c in self.Pokemon if c.name == card.name]:
                sumCard += pokemon
            if sumCard.isValid():
                self.Pokemon.append(card)
            else:
                raise DeckUnvalidCardError(f"There are too many of {sumCard.name} ({sumCard.amount})")
        elif card.type == "Trainer":
            sumCard = Card(card.amount, card.name, card.type, card.set, isAcespec=card.isAcespec, isPrism=card.isPrism)
            for trainer in [c for c in self.Trainer if c.name == card.name]:
                sumCard += trainer
            if sumCard.isValid():
                self.Trainer.append(card)
            else:
                raise DeckUnvalidCardError(f"There are too many of {sumCard.name} ({sumCard.amount})")
        elif card.type == "Energy":
            sumCard = Card(card.amount, card.name, card.type, card.set, isAcespec=card.isAcespec, isPrism=card.isPrism)
            for energy in [c for c in self.Energy if c.name == card.name]:
                sumCard += energy
            if sumCard.isValid():
                self.Energy.append(card)
            else:
                raise DeckUnvalidCardError(f"There are too many of {sumCard.name} ({sumCard.amount})")
            
    def add_cards(self, cards) -> None:
        """Add multiple cards to a deck"""
        
        for card in cards:
            self.add_card(card)
    
    def isEmpty(self) -> None:
        """Check if a deck is empty"""
        return self.Pokemon == [] and self.Trainer == [] and self.Energy == []
    
    def isComplete(self) ->None:
        """Check if a deck is complete (has 60 cards)"""
        return self.getNumPokemon() + self.getNumEnergy() + self.getNumTrainer() == 60
            
    def getNumPokemon(self) ->int:
        nbPokemon=0
        for card in self.Pokemon:
            nbPokemon += card.amount
        
        return nbPokemon
    
    def getNumTrainer(self) ->int:
        nbTrainer=0
        for card in self.Trainer:
            nbTrainer += card.amount
        
        return nbTrainer
    
    def getNumEnergy(self) ->int:
        nbEnergy=0
        for card in self.Energy:
            nbEnergy += card.amount
        
        return nbEnergy
    
    def setFormat(self,format_list:list[str]) -> str:
        """Set the format of the deck, required a list of the different format. Use only the pokemon cards"""
        decksets=[pokemon.getSet() for pokemon in self.Pokemon]
        found=False
        for format in format_list:
            found = True
            for set in decksets:
                if set not in format.sets:
                    found=False
            if found:
                return format.name
        
                
            
        
            
    def exportToTCGO(self) -> None:
        """Export a deck to a ptcgo readable format"""
        filepath = f"Export/{self.format}/{self.name}.txt"
        if not os.path.isdir("Export"):
            os.mkdir("Export")
        if not os.path.isdir(f"Export/{self.format}"):
            os.mkdir(f"Export/{self.format}")
        if os.path.isfile(filepath):
            answer=input("A deck with the same name already exist, do you want to overwrite it (y/n) ?")[0].lower()
            if answer != "y":
                print("aborted")
                return 0
        with open(filepath,"w") as deck:
            deck.write(f"Pokemon ({self.getNumPokemon()})\n")
            for card in self.Pokemon:
                deck.write(f"{card.amount} {card.name} {card.set} {card.coll_num}\n")
            deck.write(f"\n")
            deck.write(f"Trainer ({self.getNumTrainer()})\n")
            for card in self.Trainer:
                deck.write(f"{card.amount} {card.name} {card.set} {card.coll_num}\n")
            deck.write(f"\n")
            deck.write(f"Energy ({self.getNumEnergy()})\n")
            for card in self.Energy:
                if card.set is not None:
                    deck.write(f"{card.amount} {card.name} {card.set} {card.coll_num}\n")
                else:
                    deck.write(f"{card.amount} {card.name} {card.coll_num}\n")

        return os.path.abspath(filepath)

class DeckMoreThanOneAceSpecError(Exception):
    pass            

class DeckUnvalidCardError(Exception):
    pass
        
if __name__ == "__main__":
    pikachu = Card(4, "Pikachu {*}", "Pokemon", "BLW", 123)
    Juniper = Card(1, "Juniper", "Pokemon", "SUM", 12, isAcespec= True)
    pikachu2 = Card(14, "Water Energy Energy", "Energy", "BLW", 12)
    
    

    
    
    testDeck = Deck("Test",[pikachu,pikachu2,Juniper])
    print(testDeck.format)
    #testDeck.exportToTCGO()
  