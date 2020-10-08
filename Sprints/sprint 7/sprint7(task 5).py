class LeafElement: 
    def __init__(self, *args): 
        self.position = args[0]
    def showDetails(self): 
        print("\t", end = "")
        print(self.position)
class CompositeElement: 
    def __init__(self, *args): 
        self.position = args[0]
        self.children = []
    def add(self, child): 
        self.children.append(child)
    def remove(self, child): 
        self.children.remove(child)
    def showDetails(self): 
        print(self.position)
        for child in self.children:
            print("\t", end = "")
            child.showDetails()
 