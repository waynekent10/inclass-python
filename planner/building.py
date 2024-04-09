import datetime

class Building:
    def __init__(self, address, stories):
        self.address = address
        self.stories = stories
        self.designer = "Bruce"
        self.date_constructed = ''
        self.owner = ''

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        self.owner = buyer
# Create 5 building instances
buildings = [
    Building("100 Punk Street", 5),
    Building("200 Jabroni Avenue", 8),
    Building("300 Stone Cold Street", 10),
    Building("400 Viper Avenue", 15),
    Building("500 Pizza Lane", 12)
]

agent = "Hollywood"

for building in buildings:
    building.purchase(agent)
    building.construct()

for building in buildings:
    print(f"{building.address} was purchased by {building.owner} on {building.date_constructed.strftime('%m/%d/%Y')} and has {building.stories} stories.")
