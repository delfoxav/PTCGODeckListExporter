from card import Card
sets=Card.sets
del Card

class Format:
    """Define a format"""
    def __init__(self, name, sets) -> None:
        self.name = name
        self.sets = sets
        
def create_Formats_list(names: list[str], setList: list[list[str]] )-> list[Format]:
    """Create a list of formats"""
    listFormats=[]
    assert len(names) == len(setList),f"The number of names doesn't fit the number of set list. {len(names)} and {len(setList)}"
    
    for name,sets in zip(names,setList):
        listFormats.append(Format(name,sets))

    return listFormats


Jan2022_Format_Names=[f"STD_20{i}_{i+1}"for i in range(11,22)]
Jan2022_Format_Names.append("Expanded")
Jan2022_Format_Names.append("Unlimited")
Jan2022_Format_SetList=[sets[sets.index("HS"):sets.index("DEX")+1],
                        sets[sets.index("BLW"):sets.index("PLF")+1],
                        sets[sets.index("NXD"):sets.index("FLF")+1],
                        sets[sets.index("BCR"):sets.index("ROS")+1],
                        sets[sets.index("XY"):sets.index("STS")+1],
                        sets[sets.index("PRC"):sets.index("BUS")+1],
                        sets[sets.index("BKT"):sets.index("CES")+1],
                        sets[sets.index("SUM"):sets.index("UNB")+1],
                        sets[sets.index("UPR"):sets.index("RCL")+1],
                        sets[sets.index("TEU"):sets.index("CRE")+1],
                        sets[sets.index("SSH"):],
                        sets[sets.index("BLW"):],
                        sets]

Jan2022_Format = create_Formats_list(Jan2022_Format_Names, Jan2022_Format_SetList)
