
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
    
    def __init__(self, amount: int, name: str, type: str, set: str = None, coll_num: int = None ) -> None:
        """Create a new card"""
        self.amount = amount
        self.name = name
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
        """Check if a card is valid (maximum 4 cards with the same name)"""
        if self.type == "Energy":
            return True
        else:
            return self.amount <= 4


class CardTypeError(Exception):
    pass

class CardSetError(Exception):
    pass
