class Bird:
    def intro(self):
        print("There are many kind of birds")
        
    def flight(self):
        print("Most birds cannot fly")
        
class Parrot(Bird):
    def flight(self):
        print("most parrots can fly")
        
class Penguin(Bird):
    def flight(self):
        print("Penguins can hardly fly")
        
obj_bird = Bird()
obj_parr = Parrot()
obj_peng = Penguin()

obj_bird.intro()
obj_bird.flight()

obj_parr.intro()
obj_parr.flight()

obj_peng.intro()
obj_peng.flight()
