class Player:
    def __init__(self, name) -> None:
        
        self.name = name
        self.health = 20 
        self.vitality = 0
        self.strength = 0
        self.agility = 0
        self.defense = 0
    
    def get_class(self):
        player_class = input("Choose your class: \n(a) Knight \n(b) Rouge ")
        if player_class == "a":
            self.vitality += 15
            self.strength += 17
            self.agility += 12
            self.defense += 16
        elif player_class == "b":
            self.vitality += 13
            self.strength += 15
            self.agility += 17
            self.defense += 14
        else:
            print("Invalid selection")
            player_one.get_class()

print("\n")
print("Adventure Person: The Deep Cave".center(100))
input("Press 'Enter' to start\n".center(100))

player_one = Player(input("Hello adventurer. Please enter your name: "))

print("Welcome {},".format(player_one.name))
player_one.get_class()










