""" 100 Days of Code Python Challenge - Day 1: Band Name Generator """

#############################################################
# Remarks
#############################################################
# 1. This project has been purposefully not been equipped with input
# sanitisation as it is a trivial exercise. Input sanitisation will
# be used later on in the course as the projects demand it.
# 2. This project has been developed to follow closely the intended behaviour
# of the online app: https://appbrewery.github.io/python-day1-demo/
# 3. As a learning project, I use extensive commenting for my code
# in order to develop good habits and make sure the code is as readable
# and understandable as possible.
# 4. For formatting I use flake8 in order to impose PEP 8 linting to my code.
# This is also being done for the development of proper habits and to encourage
# coding in a nice, clean and consistent style.


def main():
    """ Main function of the module. """
    # Print a welcome message to the user.
    print("Welcome to the Band Name Generator.")
    # Prompt the user for their city of birth.
    city_of_birth = input("What's the name of the city you grew up in?\n")
    # Prompt the user for their pet's name.
    pet = input("What's your pet's name?\n")
    # Print the proposed band name to the user.
    print("Your band name could be " + city_of_birth + " " + pet)
    return 0


# Standard python boilerplate code.
if __name__ == "__main__":
    # Store the return value of main in a variable.
    info = main()
    # Print some info about the execution of the program.
    print(f"\nThe program terminated with exit code {info}")
