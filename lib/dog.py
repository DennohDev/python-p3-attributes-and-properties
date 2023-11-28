#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = 'kinuthia', breed = None):
       
        if  name == "" or not (isinstance(name, str) and (1 <= len(name) <=25)):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name
        
        if breed is not None and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    def get_name(self):
        print ("Getting name")
        return self._name
    
    def get_breed(self):
        print("Getting breed")
        return self._breed

    
    name = property(get_name )
    breed = property(get_breed )

