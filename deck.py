from card import Card
import os

class Deck:
    def __init__(self, name = "", cards=[], hasAcespec = False) -> None:
        """Create a new deck"""
        
        self.Pokemon = []
        self.Trainer = []
        self.Energy = []
        self.hasAcespec = hasAcespec
        self.name = name
        self.add_cards(cards)
        
    def add_card(self, card) -> None:
        """Add a card to a deck"""
        if card.isAcespec and self.hasAcespec:
            raise DeckMoreThanOneAceSpecError(f"Can't add {card.name} to {self.name}, the deck already has an AceSpec")
        elif card.isAcespec:
            self.hasAcespec = True
        if card.type == "Pokemon":
            sumCard = Card(card.amount, card.name, card.type, card.set, isAcespec=card.isAcespec, isPrism=card.isPrism, isBasicNrj=card.isBasicNrj)
            for pokemon in [c for c in self.Pokemon if c.name == card.name]:
                sumCard += pokemon
            if sumCard.isValid():
                self.Pokemon.append(card)
            else:
                raise DeckUnvalidCardError(f"There are too many of {sumCard.name} ({sumCard.amount})")
        elif card.type == "Trainer":
            sumCard = Card(card.amount, card.name, card.type, card.set, isAcespec=card.isAcespec, isPrism=card.isPrism, isBasicNrj=card.isBasicNrj)
            for trainer in [c for c in self.Trainer if c.name == card.name]:
                sumCard += trainer
            if sumCard.isValid():
                self.Trainer.append(card)
            else:
                raise DeckUnvalidCardError(f"There are too many of {sumCard.name} ({sumCard.amount})")
        elif card.type == "Energy":
            sumCard = Card(card.amount, card.name, card.type, card.set, isAcespec=card.isAcespec, isPrism=card.isPrism, isBasicNrj=card.isBasicNrj)
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
            
    def exportToTCGO(self) -> None:
        """Export a deck to a ptcgo readable format"""
        if not os.path.isdir("Export"):
            os.mkdir("Export")
        if os.path.isfile(f"Export/{self.name}.txt"):
            answer=input("A deck with the same name already exist, do you want to overwrite it (y/n) ?")[0].lower()
            if answer != "y":
                print("aborted")
                return 0
        with open(f"Export/{self.name}.txt","w") as deck:
            deck.write(f"Pokemon ({self.getNumPokemon()})\n")
            for card in self.Pokemon:
                deck.write(f"{card.amount} {card.name} {card.set} {card.coll_num} \n")
            deck.write(f"Trainer ({self.getNumTrainer()})\n")
            for card in self.Trainer:
                deck.write(f"{card.amount} {card.name} {card.set} {card.coll_num} \n")
            deck.write(f"Energy ({self.getNumEnergy()})\n")
            for card in self.Energy:
                deck.write(f"{card.amount} {card.name} {card.set} {card.coll_num} \n")

class DeckMoreThanOneAceSpecError(Exception):
    pass            

class DeckUnvalidCardError(Exception):
    pass
        
if __name__ == "__main__":
    pikachu = Card(4, "Pikachu", "Pokemon", "XY", 123)
    Juniper = Card(1, "Juniper", "Trainer", "SUM", 12, isAcespec= True)
    pikachu2 = Card(14, "Pikacwhu", "Energy", "BLW", 12, isBasicNrj=True)
   
    
    
    testDeck = Deck("Test",[pikachu,pikachu2,Juniper])
    #testDeck.exportToTCGO()
  