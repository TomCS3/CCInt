"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out"basis.
People must adopt either the "oldest"(based on arrival time) of all animals at the shelter, or they can select 
whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select 
which specific animal they would like. Create the data structures to maintain this system and implement operations 
such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.
"""

from random import randint

class Shelter:

    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if animal == "dog":
            self.dogs.append(animal)
        elif animal == "cat":
            self.cats.append(animal)
        else:
            raise ValueError "animal must be either a dog or a cat"
    
    def dequeueDog(self):
        if self.dogs.isEmpty():
            print("No dogs in the Shelter")
            return None
        return self.dogs.pop(0)
    
    def dequeueCat(self):
        if self.cats.isEmpty():
            print("No cats in the Shelter")
            return None
        return self.cats.pop(0)

    def dequeAny(self):
        if self.dogs.isEmpty() and self.cats.isEmpty():
            print("No animals in the Shelter")
            return None
        elif self.dogs.isEmpty():
            return self.cats.pop(0)
        elif self.cats.isEmpty():
            return self.dogs.pop(0)
        else:
            random  = randint(0,1)
            if random = 0:
                return self.dogs.pop(0)
            else:
                return self.cats.pop(0)

    
