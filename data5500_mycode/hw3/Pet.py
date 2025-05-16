class Pet:

    species_lifespans = {"dog": 13, "cat": 15, "rabbit": 9, "parrot": 50}

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

        #calc age in human years
    def age_in_human_years(self):
        if self.species == "dog":
            return self.age * 7
        elif self.species == "cat":
            return self.age * 6
        elif self.species == "rabbit":
            return self.age * 8
        elif self.species  == "parrot":
            return self.age * 5
    
    #avg lifespan
    def get_average_lifespan(self):
        return Pet.species_lifespans.get(self.species, "Unknown lifespan")

#instantiate 3 pets
pet1 = Pet(name="Dolce", age=1, species="dog")
pet2 = Pet(name="Ozzy", age=5, species="cat")
pet3 = Pet(name="Thumper", age=7, species="rabbit")

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet.name} is a {pet.species} and is {pet.age} years old.")
    print(f"Age in human years: {pet.age_in_human_years()}")
    print(f"Average lifespan for a {pet.species}: {pet.get_average_lifespan()} years\n")

#Create a class called Pet with attributes name and age. Implement a method within the class to calculate the age of the pet in equivalent human years. Additionally, create a class variable called species to store the species of the pet. Implement a method within the class that takes the species of the pet as input and returns the average lifespan for that species.Instantiate three objects of the Pet class with different names, ages, and species.Calculate and print the age of each pet in human years.Use the average lifespan function to retrieve and print the average lifespan for each pet's species.

