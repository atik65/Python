from abc import abstractmethod

class CricketTeam:
    def __init__(self, teamName, captain):
        self.teamName = teamName
        self.captain = captain
   

    @abstractmethod
    def get_squad(self):
        pass

class AsiaCupTeam(CricketTeam):
    def __init__(self, teamName, captain):
        super().__init__(teamName, captain)
        self.players = []

    def add_player(self, name, role):
        player = Player(name, role)
        self.players.append(player)

    def get_squad(self):
        return self.players
    

class Player:
    def __init__(self,name, role):
        self.name = name
        self.role = role



teamBd = AsiaCupTeam("Bangladesh", "Shakib Al Hasan")
teamBd.add_player("Liton Kumar Das", "Opening Batsman")
teamBd.add_player("Mushfiqur Rahim", "Middle Order Batsman")
teamBd.add_player("Taskin Ahamed", "Right Arm Fast Bowler") 


print(f"Team: {teamBd.teamName}")
print(f"Captain: {teamBd.captain}")
print("Squad:")
for player in teamBd.get_squad():
    print(f"Name: {player.name}   Role:{player.role}")