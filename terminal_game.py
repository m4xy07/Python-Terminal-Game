def start_game():
    print("Welcome to 'Murder at the Mansion'!")
    print("You are Detective James, and you have been called to investigate a murder at the wealthy businessman, Richard Langley's mansion.")
    print("You arrive at the mansion and find the body of Richard Langley in his study.")
    print("You have two options:")
    print("A) Question the butler, Jenkins")
    print("B) Investigate the study for clues")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        question_jenkins()
    elif choice.lower() == 'b':
        investigate_study()
    else:
        print("Invalid choice. Please try again.")
        start_game()


def question_jenkins():
    print("You decide to question the butler, Jenkins.")
    print("Jenkins seems nervous and fidgety, but he tells you that he didn't see or hear anything suspicious.")
    print("You have two options:")
    print("A) Press Jenkins for more information")
    print("B) Let Jenkins go and investigate the rest of the mansion")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        press_jenkins()
    elif choice.lower() == 'b':
        investigate_mansion()
    else:
        print("Invalid choice. Please try again.")
        question_jenkins()


def press_jenkins():
    print("You press Jenkins for more information, and he finally cracks under the pressure.")
    print("He tells you that he saw one of the guests, Mrs. White, arguing with Richard Langley earlier that night.")
    print("You have two options:")
    print("A) Confront Mrs. White about the argument")
    print("B) Investigate Mrs. White's alibi")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        confront_mrs_white()
    elif choice.lower() == 'b':
        investigate_alibi()
    else:
        print("Invalid choice. Please try again.")
        press_jenkins()


def investigate_study():
    print("You decide to investigate the study for clues.")
    print("You find a piece of paper on the floor with a cryptic message: 'The killer was someone who stood to gain from Richard's death.'")
    print("You have two options:")
    print("A) Investigate Richard's business partners")
    print("B) Investigate Richard's family members")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        investigate_partners()
    elif choice.lower() == 'b':
        investigate_family()
    else:
        print("Invalid choice. Please try again.")
        investigate_study()


def investigate_mansion():
    print("You decide to investigate the rest of the mansion.")
    print("You find a suspicious-looking letter opener in the library.")
    print("You have two options:")
    print("A) Investigate the library further")
    print("B) Show the letter opener to Jenkins")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        investigate_library()
    elif choice.lower() == 'b':
        show_letter_opener()
    else:
        print("Invalid choice. Please try again.")
        investigate_mansion()


def confront_mrs_white():
    print("You confront Mrs. White about the argument, and she breaks down in tears.")
    print("She confesses to the crime, and you arrest her.")
    print("Congratulations, you solved the case!")


def investigate_alibi():
    print("You investigate Mrs. White's alibi, and it checks out.")
    print("You realize that you were mistaken about Mrs. White's involvement.")
    print("You have to start over from the beginning.")
    start_game()


def investigate_partners():
    print("You investigate Richard's business partners, and you find a suspicious transaction.")
    print("You have two options:")
    print("A) Confront the business partner about the transaction")
    print("B) Investigate the transaction further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        confront_partner()
    elif choice.lower() == 'b':
        investigate_transaction()
    else:
        print("Invalid choice. Please try again.")
        investigate_partners()


def investigate_family():
    print("You investigate Richard's family members, and you find a suspicious letter.")
    print("You have two options:")
    print("A) Confront the family member about the letter")
    print("B) Investigate the letter further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        confront_family()
    elif choice.lower() == 'b':
        investigate_letter()
    else:
        print("Invalid choice. Please try again.")
        investigate_family()


def investigate_library():
    print("You investigate the library further, and you find a book about poisons.")
    print("You have two options:")
    print("A) Investigate the book further")
    print("B) Show the book to Jenkins")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        investigate_book()
    elif choice.lower() == 'b':
        show_book()
    else:
        print("Invalid choice. Please try again.")
        investigate_library()


def show_letter_opener():
    print("You show the letter opener to Jenkins, and he recognizes it as one of Richard's personal items.")
    print("You have two options:")
    print("A) Investigate the letter opener further")
    print("B) Investigate the study further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        investigate_letter_opener()
    elif choice.lower() == 'b':
        investigate_study()
    else:
        print("Invalid choice. Please try again.")
        show_letter_opener()


def confront_partner():
    print("You confront the business partner about the transaction, and they confess to the crime.")
    print("Congratulations, you solved the case!")


def investigate_transaction():
    print("You investigate the transaction further, and you find evidence of fraud.")
    print("You have two options:")
    print("A) Confront the business partner about the fraud")
    print("B) Investigate the business partner further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        confront_partner()
    elif choice.lower() == 'b':
        investigate_partner()
    else:
        print("Invalid choice. Please try again.")
        investigate_transaction()


def confront_family():
    print("You confront the family member about the letter, and they confess to the crime.")
    print("Congratulations, you solved the case!")


def investigate_letter():
    print("You investigate the letter further, and you find evidence of a motive.")
    print("You have two options:")
    print("A) Confront the family member about the motive")
    print("B) Investigate the family member further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        confront_family()
    elif choice.lower() == 'b':
        investigate_family()
    else:
        print("Invalid choice. Please try again.")
        investigate_letter()


def investigate_book():
    print("You investigate the book further, and you find evidence of a motive.")
    print("You have two options:")
    print("A) Investigate the library further")
    print("B) Investigate the study further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        investigate_library()
    elif choice.lower() == 'b':
        investigate_study()
    else:
        print("Invalid choice. Please try again.")
        investigate_book()


def show_book():
    print("You show the book to Jenkins, and he recognizes it as one of Richard's personal items.")
    print("You have two options:")
    print("A) Investigate the book further")
    print("B) Investigate the study further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        investigate_book()
    elif choice.lower() == 'b':
        investigate_study()
    else:
        print("Invalid choice. Please try again.")
        show_book()


def investigate_letter_opener():
    print("You investigate the letter opener further, and you find evidence of a motive.")
    print("You have two options:")
    print("A) Investigate the letter opener further")
    print("B) Investigate the study further")


    choice = input("What would you like to do? (A/B) ")


    if choice.lower() == 'a':
        investigate_letter_opener()
    elif choice.lower() == 'b':
        investigate_study()
    else:
        print("Invalid choice. Please try again.")
        investigate_letter_opener()


start_game()