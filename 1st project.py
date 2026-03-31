# PROJECT 1 
# FAKE NEWS HEADLINE GENERATOR
# CONCEPT
# 1 LISTS : to store groups of words like names,action,and place.
# 2 Random Choice() : to pick one item randomly from a list.
# 3 print() : to show the fake headline a screen.
# 4 while loops : to repeat the process untill the user sat to string concatenation or f string .


# CREATE SUBJECTS
Subjects = {
    "sharukhan",
    "virat kholi",
    "babar Azam",
    "a mumbai cat",
    "a group of company",
    "a prime minister of mudi",
    "auto rishkaw driver from delhi"
}

Action = {
    "lunches",
    "cancels",
    "dance with",
    "cats",
    "orders",
    "celebrates",
    "enjoy"
}
Place_or_Thing = {
    "a red fort",
    "in mumbai local train",
    "a plot of samosa",
    "inside parlement",
    "at ganga chat",
    "ipl mathche",
    "at india cat"
}
import random

# CREATE SUBJECTS
subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Babar Azam",
    "a Mumbai cat",
    "a group of company",
    "the Prime Minister of Modi",
    "an auto rickshaw driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "cats",
    "orders",
    "celebrates",
    "enjoys"
]

places_or_things = [
    "the Red Fort",
    "in Mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga ghat",
    "IPL match",
    "at India Gate"
]

# START THE HEADLINE GENERATOR LOOP
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

# print goodbye message
print("\nThanks for using the fake news headline generator. Have a fun day!")



    



