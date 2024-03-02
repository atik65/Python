class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound of a " + self.name)

    def show_info (self):
        print("Name: " + self.name + " Species: " + self.species)


class Dog(Animal):
    def __init__(self,name, species,bread):
        super().__init__(name, species)
        self.bread = bread

    def make_sound_dog(self):
       super().make_sound()





class GermanShepherd(Dog):
    def __init__(self, name, species, bread, color):
        super().__init__(name, species, bread)
        self.color = color

    def make_sound_GermanShepherd(self):
        super().make_sound_dog()



germenShepherd1 = GermanShepherd("Rex", "Dog", "German Shepherd", "Black")        


germenShepherd1.make_sound_GermanShepherd()




