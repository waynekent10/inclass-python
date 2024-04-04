import datetime  # This helps work with dates and times.

#
class Building:
    def __init__(self, address, stories):
        # Setting up the requirements for the buildings
        self.address = address  # The address where the building is located.
        self.stories = stories 
        self.designer = "Bruce Bruce" 
        self.date_constructed = None
        self.owner = None  # The person who buys the building will become the owner.

    def construct(self):
        # This method tells me when the building was built.
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        # This method helps me know who bought the building.
        self.owner = buyer

# Create buildings
buildings = []

# Create the buildings and give them addresses and stories.
buildings.append(Building("100 Main Street", 5))
buildings.append(Building("200 Broad Avenue", 8))
buildings.append(Building("300 Elm Street", 10))
buildings.append(Building("400 Pine Avenue", 15))
buildings.append(Building("500 Oak Lane", 20))

# Potential buyers
buyer_names = ["Daun", "Abby", "Maria", "Frank"]

# For each building, 
for building, buyer in zip(buildings, buyer_names):
    building.purchase(buyer)  # Someone buys the building.
    building.construct()  # We note down when it's built.

# Now, let's print out the details of each building.
for building in buildings:
    print("Address:", building.address)  # Print the building's address.
    print("Owner:", building.owner)  # Print the name of the owner.
    print("Stories:", building.stories)  # Print how many floors the building has.
    print("Date Constructed:", building.date_constructed)  # Print when it was built.
    print()
