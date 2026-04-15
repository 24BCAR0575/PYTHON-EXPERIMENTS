# 1. CLASS AND OBJECT
class Animal:
    def __init__(self, name):
        self.name = name  # Attribute

    # 2. METHOD
    def speak(self):
        print("Animal makes a sound")

# 3. SINGLE INHERITANCE
class Dog(Animal):
    # 4. METHOD OVERRIDING (Polymorphism)
    def speak(self):
        print(f"{self.name} says: Woof Woof!")

# 5. MULTILEVEL INHERITANCE
class WorkingDog(Dog):
    def work(self):
        print(f"{self.name} is now working.")

# 6. MULTIPLE INHERITANCE
class Friendly:
    def greet(self):
        print("This animal is friendly.")

class PetDog(Dog, Friendly): # Inherits from Dog AND Friendly
    pass

# 7. METHOD OVERLOADING (Using default arguments)
class Calculator:
    def add(self, a, b, c=0): 
        print(f"Sum is: {a + b + c}")

# --- DISPLAYING EVERYTHING ---

print("--- 1 & 2: Class, Object, and Method ---")
my_animal = Animal("Generic")
my_animal.speak()

print("\n--- 3 & 4: Single Inheritance and Overriding ---")
my_dog = Dog("Buddy")
my_dog.speak()

print("\n--- 5: Multilevel Inheritance ---")
my_worker = WorkingDog("Rex")
my_worker.speak() # From Dog
my_worker.work()  # From WorkingDog

print("\n--- 6: Multiple Inheritance ---")
my_pet = PetDog("Max")
my_pet.speak() # From Dog
my_pet.greet() # From Friendly

print("\n--- 7: Method Overloading ---")
calc = Calculator()
calc.add(5, 10)       # Two arguments
calc.add(5, 10, 20)   # Three arguments