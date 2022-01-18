from card import Card
import os

class Deck:
    def __init__(self, name = "", cards=[]) -> None:
        """Create a new deck"""
        
        self.Pokemon = []
        self.Trainer = []
        self.Energy = []
        self.name = name
        self.add_cards(cards)
        
    def add_card(self, card) -> None:
        """Add a card to a deck"""
        
        if card.type == "Pokemon":
            self.Pokemon.append(card)
        elif card.type == "Trainer":
            self.Trainer.append(card)
        elif card.type == "Energy":
            self.Energy.append(card)
            
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
            
            
        
        
if __name__ == "__main__":
    pikachu = Card(4, "Pikachu", "Pokemon", "XY", 123)
    Juniper = Card(3, "Juniper", "Trainer", "SUM", 12)
    
    testDeck = Deck("Test",[pikachu,Juniper])
    testDeck.exportToTCGO()