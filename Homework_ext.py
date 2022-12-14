users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users['Jonathan']['twitter'])
# 2. Get Erik's hometown
print (users["Erik"]["home_town"])
# 3. Get the list of Erik's lottery numbers
print (users ["Erik"] ["lottery_numbers"])
# 4. Get the species of Avril's pet Monty
print (users ["Avril"] ["pets"] [0] ["species"])
# 5. Get the smallest of Erik's lottery numbers
e_numbers = (users ["Erik"] ["lottery_numbers"])
print (min(e_numbers))
# 6. Return an list of Avril's lottery numbers that are even
# a_numbers = (users ["Avril"] ["lottery_numbers"])
# for digits in a_numbers: 
#     if digits % 2 == 0:
#         print(digits)
users ["Avril"] ["lottery_numbers"]
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# e_numbers.append(7)
# print (e_numbers)
users["Erik"]["home_town"] = "Edinburgh"
# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
users["Erik"]
print(users["Erik"]["home_town"])
# 9. Add a pet dog to Erik called "fluffy"
# e_pets = (users["Erik"] ["pets"])
# e_pets.append({"name" : "fluffy"})
# print (e_pets)
users["Erik"]["pets"].append ({"name": "fluffy", "species": "dog"})
# 10. Add another person to the users dictionary
new_user = {
    "twitter": "jennah",
    "lottery_numbers": [2, 4, 6, 8, 12],
    "home_town": "Edinburgh",
    "pets":[
        {
      "name": "gerty",
      "species": "hamster"
        },
        {
      "name": "kirsten",
      "species": "dog"
        },
        ]
    }
users.update(new_user)
print(new_user)