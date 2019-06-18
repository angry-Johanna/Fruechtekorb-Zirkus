

class Frucht:
    frucht=""
    zustand=""
    herkunt=""

    def __init__(self,frucht,zustand,herkunft):
        self.frucht=frucht
        self.zustand=zustand
        self.herkunft=herkunft

    def __str__(self):
        return "Diese Frucht heisst "+self.frucht+" und kommt "+self.zustand+" aus "+self.herkunft+"."
    
    
