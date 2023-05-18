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
from pet import Pet

def main():
    active_pets = []
    # Create a menu for pet playground
    new_menu = """
    Here is your list of options:

        1 - Option 1: Create a new pet
        2 - Option 2: Select your pet to interact with
        3 - Option 3: Save pet data
        4 - Option 4: Quit
    """
    options = ("1", "2", "3", "4")
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(new_menu, options)
        if choice == "1":
            pet = create_new_pet()
            active_pets.append(pet)
        elif choice == "2":
            if not active_pets:
                print("\nYou have no pets to play with.")
        elif choice == "3":
            if active_pets:
                for pet in active_pets:
                    pet.store_pet_data()

def create_new_pet():
    """ creates and returns a new pet object"""
    name = input("Select a name for your pet: ")
    breed = input("Select a pet breed: ")
    pet = Pet(name, breed)
    return pet

    print("\nThanks for playing.")


if __name__ == "__main__":
    main()
