
class Card:
    types = ["Pokemon","Trainer","Energy"]
    sets = ["HS", #TODO Check if the name are right
            "UL",
            "UD",
            "TM",
            "CL",
            "BLW",
            "EPO",
            "NVI",
            "NXD",
            "DEX",
            "DRX",
            "DRV",
            "BCR",
            "PLS",
            "PLF",
            "PLB",
            "LTR",
            "KSS",
            "XY",
            "FLF",
            "FFI",
            "PHF",
            "PRC",
            "DCR",
            "ROS",
            "AOR",
            "BKT",
            "BKP",
            "GEN",
            "FCO",
            "STS",
            "EVO",
            "SUM",
            "GRI",
            "BUS",
            "SLG",
            "CIN",
            "UPR",
            "FLI",
            "CES",
            "DRM",
            "LOT",
            "TEU",
            "DET",
            "UNB",
            "UNM",
            "HIF",
            "CEC",
            "SSH",
            "RCL",
            "DAA",
            "CPA",
            "VIV",
            "SHF",
            "BST",
            "CRE",
            "EVS",
            "CEL",
            "FST",
            "BRS"]
    
    basicEnergies =["Water Energy",
                    "Grass Energy",
                    "Lightning Energy",
                    "Fire Energy",
                    "Fighting Energy",
                    "Dark Energy",
                    "Psychic Energy",
                    "Metal Energy",
                    "Fairy Energy",
                    ]
    
    
    
    def __init__(self, amount: int, name: str, type: str, set: str = None, coll_num: int = None, isAcespec = False, isPrism = False, isBasicNrj = False ) -> None:
        """Create a new card"""
        self.amount = amount
        self.name = name
        self.isAcespec = isAcespec
        self.isPrism = isPrism
        self.isBasicNrj = isBasicNrj
        if type in Card.types:
            self.type = type
        else:
            raise CardTypeError(f"I don't know the type {type}")
        if set in Card.sets:
            self.set = set
        else:
            raise CardSetError(f"I don't know the set {set}")
        self.coll_num = coll_num
        
    def isValid(self) -> None:
        """Check if a card is valid (maximum 4 cards with the same name and only one AceSpec/Prism)"""
        if self.isBasicNrj:
            return True
        elif self.isAcespec or self.isPrism:
            return self.amount <= 1
        else:
            return self.amount <= 4
    
    def __add__(self, other):
        """addition for cards, sum the amount of cards with the same name"""
        if self.name != other.name:
            raise CardDifferentNameError(f"I wasn't able to sum {self.name} and {other.name} please sum only cards with the same name.")
        return Card(amount=self.amount+other.amount, name= self.name, type=self.type, set=self.set, isAcespec=self.isAcespec, isPrism=self.isPrism, isBasicNrj=self.isBasicNrj)

    def __iadd__(self, other):
        return self+other

class CardTypeError(Exception):
    pass

class CardSetError(Exception):
    pass

class CardDifferentNameError(Exception):
    pass

