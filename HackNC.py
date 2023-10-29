"""HackNC - Presidents Game."""

__author__ = "Ana Restrepo", "Wenyu Xie", "Xiangling Chen", "Rital Patel"

from random import randint

dad: str = "\U0001F64B"
no: str = "\U0001F645"
yes: str = "\U0001F646"
# all lists will go here
name_list: list[str] = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Burn", "William Henry Harrison", "John Tyler"]
start_year: list[str] = ["1789", "1797", "1801", "1809", "1817", "1825", "1829", "1837", "1841", "1841"]

end_year: list[str] = ["1797", "1801", "1809","1817", "1825", "1829", "1837", "1841", "1841", "1845"]

count_0: int = 1

print("Welcome to the Presidents game designed for people who want to test out for their knowledge on U.S. presidents.")
print("The idea of this game is based off one of our authors' childhood. She was told to recite all the U.S. presidents at the age of 7 by her dad.")
print("Please write both the first and last name, capitalizing both the first letters.")

while count_0 < 4:
    print(" ")
    print(f"=== Round {count_0}/3 ===")
    # idx for the idx corresponding to the lists
    idx: int = randint(0, 9)
    # secret is the name of the president based on the idx of the list

    secret: str = name_list[idx]

    guess: str = input(f"Who is the No.{idx+1} U.S. president? ")

    if guess == secret:
        print("Horray you got it you smarty pants!")
        print("You succeeded in 1 turn!")
        print(f"Good job! On to the next round!{yes}")
    else:
        print(f"That is incorrect. This president was in office from {start_year[idx]} to {end_year[idx]}. ")
        print("You have 3 turns remaining.")
        count: int = 1
        while count < 4:
            guess = input("Guess again! ")
            if guess == secret:
                print("Horray you got it smarty pants!")
                print(f"You succeeded in {count + 1} turns!")
                print(f"Good job! On to the next round!{yes}")
                count = 5
            count += 1
        if count == 4:
            print(f"Try again next time!{no}")
            exit()
    count_0 += 1
print(f"Horray you won the Presidents game! My dad would be proud!{dad}")
print("**Based on a true story**")