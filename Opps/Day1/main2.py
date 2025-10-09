# Constructor

class Factory:
    def __init__(self,materials,zips,pockets):
        self.materials = materials
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Hello World {self.materials},{self.pockets},{self.zips}")    

reebok = Factory("Leather","3 Zips","2 Pockets")
campus = Factory("nylon",3,2)

print(reebok.pockets)
print(campus.pockets)

reebok.show()
campus.show()