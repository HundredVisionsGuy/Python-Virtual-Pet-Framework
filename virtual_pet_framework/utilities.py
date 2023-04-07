""" utilities.py
a set of functions to be used to make the program more useful and be used in
other similar projects."""

# import statements

def get_menu_choice(menu: str, legal_choices: tuple) -> str:
    """displays a menu of options, and asks the user to make a choice.

    Args:
        menu: a formatted string of choices for the user
        legal_choices: a tuple of only choices that the user is allowed
            to make

    Returns:
        user_choice: a single character that must be one of the legal choices
    """

    user_choice = ""
    while user_choice not in legal_choices:
        print(menu)
        user_choice = input("Your Choice: ")
        # Give feedback if user didn't use proper choice
        if user_choice not in legal_choices:
            print("Sorry, that is not an option, please select one of the following: ")
            print(legal_choices)
    return user_choice

if __name__ == "__main__":
    menu = "\nHere is your list of options:\n\n\t1 - Option #1\n"
    menu += "\t2 - Option #2\n\t3 - Option #3\n\n"
    selection = get_menu_choice(menu, ("1", "2", "3"))

    print(f"\nYou selected {selection}")

    new_menu = """
    Here is your list of options:

        1 - Option 1: Play with your pet.
        2 - Option 2: Feed your pet.
        3 - Option 3: Post a video of your pet on Instagram
        4 - Option 4: Pet your pet.
    """
    options = ("1", "2", "3", "4")
    new_choice = get_menu_choice(new_menu, options)
    print("you selected: " + new_choice)