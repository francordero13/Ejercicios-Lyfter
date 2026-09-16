hotel= {
    "name":"Hotel San Jose",
    "stars": 5,
    "rooms": [
        {
            "number" : 111,
            "floor" : 3,
            "price_per_nigth": 80
        },
         {
            "number" : 222,
            "floor" : 4,
            "price_per_nigth": 90
        },
         {
            "number" : 333,
            "floor" : 5,
            "price_per_nigth": 100
        }
    ]
}

print(hotel["rooms"][2]["price_per_nigth"])