"""
filename: pet.py
Author: Chris Winikka
Description: A virtual pet complete with pet emotions and behavior.
"""
import json
import uuid
import utilities
import random

class Pet:
    """A virtual pet (can be used as a base class for other pet types).

    Attributes:
        name: str
        breed: str
        nickname: list (a list strings of given nicknames for your pet)
        happiness: int how happy is the pet from 0-10 (10 being happiest)
        hunger: int how hungry our pet is (the higher the number, the 
            hungrier the pet)
        health: int how healthy is our pet
    """
    # constructor method
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.ID = uuid.uuid1().hex
        self.breed = breed
        self.nicknames = []
        self.happiness = 5
        self.hunger = 4
        self.health = 50
        self.tiredness = 0

        self.store_pet_data()

    def store_pet_data(self) -> None:
        """ Insert pet information into the pets.json file"""
        # TODO:
        # add some error handling in case the file doesn't exist

        # get the contents of the pets
        pets_text = utilities.get_file_contents("data/", "pets.json")
        pets_dictionary = json.loads(pets_text)

        # create a pet dictionary object and append it to the pet_dictionary
        this_pet = {
            "name": self.name,
            "ID": self.ID,
            "breed": self.breed,
            "nicknames": self.nicknames,
            "happiness": self.happiness,
            "hunger": self.hunger,
            "health": self.health,
            "tiredness": self.tiredness
        }

        # TODO:
        # Only append the pet if it isn't already there.

        pets_dictionary["pets"].append(this_pet)
        pets_json = json.dumps(pets_dictionary)

        # Save to pets.json
        with open("data/pets.json", "w") as outfile:
            outfile.write(pets_json)

    def load_data(self) -> None:
        """Grab pet data from the pets.json file and get the attributes"""

        # Get all pets from pets.json
        print("Loading")


    def play(self):
        """let the user choose how to play with the pet"""
        menu = f"\nChoose an option for playing with {self.name}:\n"
        menu += "\n\t1 - fetch\n\t2 - chase the laser pointer"
        menu += "\n\t3 - tug of war\n\t4 - quit\n"

        choice = ""
        description = ""
        while choice != "4":
            choice = utilities.get_menu_choice(menu, ("1", "2", "3", "4"))
            if choice == "1":
                description = f"{self.name} runs after the toy you toss. "
                if random.choice("01") == "1":
                    description += f"Once {self.name} grabs the toy, "
                    description += f"{self.name} runs away with it. "
                    self.happiness += 1
                    # quit since the pet ran off with the toy
                    choice = "4"
                else:
                    description += f"{self.name} runs after the toy and picks"
                    description += " it up and brings it back to you. "
                    description += f"{self.name} seems to really like this game. "
                    self.happiness += 2
            elif choice == "4":
                description = f"{self.name} goes back to their favorite spot."
                description += " You are done playing."
            else:
                description = f"{self.name} says 'weee!!!'"
                self.happiness += 1
            
            # How play affects other attributes
            self.hunger += 1
            self.tiredness += 1

            # keep happiness capped at 10
            if self.happiness > 10:
                self.happiness = 10
            print(description)

            # provide update
            description = f"{self.name}'s happiness is at {self.happiness}."
            print(description)


# global scope
if __name__ == "__main__":
    # Construct 2 pet instances
    fluffy = Pet("Fluffy", "rock")
    fluffy.play()