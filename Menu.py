import Gym_details
import random
from StylisticPrint import stylisticPrint
from StylisticPrint import loadingEffectPrint
import SQL_file


# FUNCTIONS FOR SIGNING IN AND UPDATING BOTH

def firstName():
    return input("Please enter your first name. ").strip()


def lastName():
    return input("Please enter your last name. ").strip()


def contactNumber():
    return input("Please enter your contact number. ").strip()


def program():
    stylisticPrint("PROGRAMS @ Fit n' HIIT")
    for pair in Gym_details.programsList.items():
        print(f"{pair[0]}: {pair[1]}")

    while True:
        programChosen = input("Please chose your program by typing between 1-4. ")
        if int(programChosen) in range(1, 5):
            break

    return Gym_details.programsList[int(programChosen)]


def PTName():
    while True:
        ptGender = input("What should be the desired gender of your personal trainer? Please choose between m and f. ")
        if ptGender.lower().strip() in ("f", "m"):
            break

    personalTrainerName = random.choice(Gym_details.femaleTrainers) if ptGender == "f" else random.choice(
        Gym_details.maleTrainers)

    return personalTrainerName


# FUNCTIONS FOR LOGGING IN
def enterCode():
    while True:
        unqiqueGymCode = input("Enter the unique gym code given to you while signing in. ")
        if SQL_file.validateCode(unqiqueGymCode):
            break
    return int(unqiqueGymCode)


def postLoginMenu(details):
    choices = ("1. Show Records", "2. Change Records", "3. Exit")
    accountDeleted = False

    while True:
        if accountDeleted:
            break

        stylisticPrint("MENU\nPlease choose between 1 and 3. Type 3 or q to quit editor. ")
        for choice in choices:
            print(choice)
        choice = input("Please choose between 1 and 3. Type 3 or q to quit editor. ")
        if choice.lower() == "q":
            loadingEffectPrint("Exiting editor.")
            break

        choice = int(choice)
        if choice == 1:
            SQL_file.retrieveDetails(details["id"])

        if choice == 2:
            editDetails(details)

        if choice == 3:
            loadingEffectPrint("Exiting editor.")
            break




def editDetails(details):
    # Preparing dictionary for option number and corresponding changes
    columns = ("firstName", "lastName", "contactNumber", "program", "PTName")
    numColumns = list(range(1, 6))
    choiceAndColumn = dict(zip(numColumns, columns))

    while True:
        stylisticPrint(f"Please choose between 1 and 5")
        for (key, value) in choiceAndColumn.items():
            print(f"{key}: Change {value}")
        choice = input(f"Please choose between 1 and 5. Type q to save changes and quit editor. ")

        if choice.lower() == "q":
            break

        else:
            choice = int(choice)
            if choice == 1:
                details["firstName"] = firstName()
            if choice == 2:
                details["lastName"] = lastName()
            if choice == 3:
                details["contactNumber"] = contactNumber()
            if choice == 4:
                details["program"] = program()
            if choice == 5:
                details["PTName"] = PTName()
                loadingEffectPrint("making changes")

    SQL_file.updateRecord(details)

