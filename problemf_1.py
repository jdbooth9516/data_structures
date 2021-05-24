import random


def find_pi_day():
    months = [("Jan", "no"), ("Feb", "no"), ("Mar", "yes"), ("Apl", "no"), ("Jun", "no"), ("Jul", "no"), ("Aug", "no"), ("Sep", "no"), ("Oct", "no"), ("Dec", "no"), ]

    for i in months: 
        if i[1] == 'yes':
            print(i[0])

print("Problem 1 a.")
find_pi_day()
print()

def birthday_locations():
    locations = {'Arizona', "Tennesse", "Korea"}
    locations.add("Sedona" )
    locations.add("Ireland")
    locations.add("Italy")

    for i in locations:
        print(i)

print("Problem 1 b.")
birthday_locations()
print()

def sweepstakes():
    contestants = [
        {
        "firstname": "John",
        "lastname": "Doe"
        },
        {
        "firstname": "Jane",
        "lastname": "Doe"
        },
        {
        "firstname": "BiJohnl",
        "lastname": "Doe"
        },
        {
        "firstname": "Ryan",
        "lastname": "Doe"
        },
        {
        "firstname": "Alice",
        "lastname": "Doe"
        }
    ]

    winning_number = random.randint(1, 5) - 1 
    winner =contestants[winning_number]
    winner_first = winner.get("firstname")
    winner_last = winner.get("lastname")
    print(f"The Winner is {winner_first} {winner_last}.")
    

print("Problem 1 C.")
sweepstakes()
print()

