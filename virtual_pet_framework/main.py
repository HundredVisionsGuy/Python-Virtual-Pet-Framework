"""
This is the main virtual pet program. 
TODO: create an interaction loop that provides ways to interact with your pet.
Examples:
* create a pet
* save your pet
* view all pets
* bring out your pet
* play with your pet
* feed your pet
* train your pet
"""

import utilities
import json
from pet import Pet

new_menu = """
Here is your list of options:

    1 - Option 1: Create a new pet
    2 - Option 2: Select your pet to interact with
    3 - Option 3: Save pet data
    4 - Option 4: Quit
"""

def main():
    pet = None
    # Create a menu for pet playground
    
    options = ("1", "2", "3", "4")
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(new_menu, options)
        if choice == "1":
            pet = create_new_pet()
        elif choice == "2":
            pets = get_pets()
            
            # retrieve a pet to play with
            pet = get_pet(pets)

            if not pet:
                print("\nYou have no pets to play with.")
                print("Try creating a new pet.")
                continue

            # TODO Work on function below
            pet = interact_with_pet(pet)

        elif choice == "3":
            if pet:
                pet.store_pet_data()

def interact_with_pet(pet):
    """TODO: write the code to interact with your pet"""
    return pet

def get_pet(pets):
    for pet in pets:
        name = pet.get("name")
        breed = pet.get("breed")
        prompt = f"Would you like to play with {name} the {breed}"
        prompt += "? (y/n) "
        play_with = utilities.get_menu_choice(prompt, ("y", "n"))
        if play_with == "y":
            # create a pet object with the data
            new_pet = Pet.create_pet(pet)
            return pet
    return None

def get_pets() -> list:
    """load the pets from the pets.json file
    
    Returns:
        pets: a list of pet objects
    """
    pets = utilities.get_file_contents("data/", "pets.json")
    pets = json.loads(pets)
    pets = pets.get("pets")
    return pets

def create_new_pet():
    """ creates and returns a new pet object"""
    name = input("Select a name for your pet: ")
    breed = input("Select a pet breed: ")
    pet = Pet(name, breed)
    return pet

    print("\nThanks for playing.")


if __name__ == "__main__":
    main()
