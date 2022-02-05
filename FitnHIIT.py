import Menu
import SQL_file


from StylisticPrint import stylisticPrint
from StylisticPrint import loadingEffectPrint

from time import sleep


def main_program():
    entryMode = welcomeUser()
    if entryMode == "s":
        userDetails = signUp()
        SQL_file.createRecord(userDetails)


    else:
        login()




def welcomeUser():
    """
        This function welcomes the user and asks them about their login or signup preference

        Returns:
                entryMode : choice for signing up or logging in
    """

    stylisticPrint("Hello, Welcome to Fit n' HIIT Gym! get the pun in our name ;)")
    while True:
        entryMode = input("Login (l) or SignUp (s) ? Please choose between l and s. ")
        if entryMode.lower().strip() in ("l", "s"):
            break

    return entryMode



def signUp():
    """
            This function is used to perform the sign up of a new user.
            The user enters their information.
            Their record is created in the table

            Returns:
                uniqueGymCode : user uses uniqueGymCode for future logins
    """
    # columnList = ["firstName", "lastName", "contactNumber", "program", "PTName"]
    details = {}

    details["firstName"] = Menu.firstName()
    details["lastName"] = Menu.lastName()
    details["contactNumber"] = Menu.contactNumber()
    details["program"] = Menu.program()
    details["PTName"] = Menu.PTName()

    loadingEffectPrint("account getting created")
    stylisticPrint("Fantastic! your account has been created.\nHere is your information for a review")

    for (key, value) in details.items():
        print(f"{key}: {value}")

    uniqueGymCode = SQL_file.createRecord(details)

    stylisticPrint(f"Your UNIQUE GYM CODE IS {uniqueGymCode}. \nKeep it handy while logging in next time and don't share with anyone")
    quit()




def login():
    """
            This function is used to perform the login.
            The user enters their uniqueGymCode to retrieve their information.
    """

    columnList = ["firstName", "lastName", "contactNumber", "program", "PTName"]

    stylisticPrint("Welcome Back!!")

    uniqueGymCode = Menu.enterCode()

    loadingEffectPrint("logging you in")
    details = SQL_file.retrieveDetails(uniqueGymCode)

    # while True:

    choice = Menu.postLoginMenu(details)












#
#     # All the things about signing up
#     # Typing information
#     firstName = input("Please enter your first name.")
#     secondName = input("Please enter your first name")
#     #userCreated()

