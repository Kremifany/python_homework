# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def call_dog(self):
#         print(f"Come here, {self.name}!")

#     def speak(self):
#         print("bark bark bark")

# dog1 = Dog("Spot", 2)
# dog1.call_dog()
# dog1.speak()
# print(f"dog1's name is {dog1.name}.")

# dog2 = Dog("Wally", 4)
# dog2.call_dog()
# dog2.age += 1
# print(dog2.age)
# In the above, we have:

# The declaration of a class named Dog. Unlike functions, class names are capitalized in Python.
# An initialization method __init__() that runs automatically when you create a new dog. Here, the method is used to set the initial values of the object's attributes (name and age).
# You can access an object's attributes using dot notation: this includes both instance variables and methods.
# The object's instance variables self.name and self.age store data for each instance of the class.
# The two methods, call_dog() and speak() are always passed the value self, which gives them access to attributes like name or age.
# Notice that we were able to modify dog2's age -- there is nothing truly private about the data stored in an object's attributes. We will say more about this below.
# What is self?
# Within a class definition, self refers to the current instance of the class — the specific object the method is being called on. It can be a little confusing because when defining a method it is always the first parameter, but you don’t actually pass it in as a parameter when invoking the method; Python does that automatically behind the scenes. For instance, above we have dog1.call_dog(), which doesn't include the self argument explicitly.
#############################################################
# Expanding the class: class attributes and class methods
# We can add more bells and whistles to our simple Dog class. For example, suppose we want to count how many dogs have been created. 
# Instead of storing that information in each individual dog, we can store it once at the class level:

# class Dog:
#     _count = 0  

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Dog._count += 1 

#     def call_dog(self):
#         print(f"Come here, {self.name}!")

#     def speak(self):
#         print("bark bark bark")

#     @classmethod
#     def get_dog_count(cls):
#         return cls._count

# # Create a couple of dogs
# dog1 = Dog("Spot", 2)
# dog1.call_dog()
# dog1.speak()
# print(f"dog1's name is {dog1.name}.")

# dog2 = Dog("Wally", 4)
# dog2.call_dog()
# dog2.age += 1
# print(f"dog2's new age: {dog2.age}")



# print(f"Total dogs created: {Dog.get_dog_count()}")  

# ###########################
# # There are quite a few new things going on here:

# # The variable _count is a class variable. Unlike the instance variables like name and age, it belongs to the class itself — not any individual dog. This means it is shared across all Dog objects. You can tell it is a class variables because it is defined outside the __init__() method.
# # The _count variable starts with a single underscore to signal that it’s intended for internal use. This is a common Python convention: it doesn’t make the variable truly private (it is still accessible), but it tells developers that it isn't meant to be directly accessed and modified.
# # The method get_dog_count() is a class method, declared using the @classmethod decorator (we will talk more about decorators below). This tells Python that the method operates on the Dog class rather than individual objects.
# # Instead of taking self as the first parameter, get_dog_count() takes in cls (short for class). cls allows us to access the class-level variable _count.

# # Class inheritance
# # Suppose you want to create a class that’s similar to Dog, but with a few differences — maybe a bigger bark, or a new behavior like fetching. Instead of rewriting everything from scratch, Python (and OOP in general) lets you inherit from an existing class and customize only the parts you want. This is called class inheritance.

# # Here's an example where we create a class BigDog that explicitly inherits from Dog:

# class BigDog(Dog): # inherits from Dog
#     def __init__(self, name, age): 
#         # Call the parent class's __init__ to set name/age
#         super().__init__(name, age) 

#     def fetch(self):
#         print("Got it.")

#     def speak(self):
#         print("Woof Woof Woof") # overrides Dog.speak()

#     def speak_verbose(self):
#         # call Dog.speak(), then BigDog.speak()
#         super().speak()
#         self.speak()

# dog3 = BigDog("Butch", 3)
# dog3.call_dog()
# dog3.speak()
# dog3.speak_verbose()


# # Here, the BigDog class inherits from the Dog class, meaning it gets all of Dog’s methods and attributes unless explicitly changed:

# # The call_dog() method is inherited from Dog, because we didn’t override it.
# # The speak() method is overridden to make big dogs sound different.
# # The speak_verbose() method shows how to call both the original Dog.speak() (using super()) and BigDog.speak().
# # You might try creating a ShyDog class that overrides speak() to say nothing unless prompted by giving it a treat with a method give_treat().

# class ShyDog(Dog): # inherits from Dog
#     def __init__(self, name, age): 
#         # Call the parent class's __init__ to set name/age
#         super().__init__(name, age)
#         self._has_treat = False

#     def fetch(self):
#         print("Got it.")

#     def speak(self):
#         print("Woof Woof Woof") # overrides Dog.speak()

#     def speak_verbose(self):
#         # call Dog.speak(), then BigDog.speak()
#         super().speak()
#         if self._has_treat:
#             print(f"{self.name}  barks after treat... bark!")
#             self._has_treat = False  # The treat is "used up" after speaking
#         else:
#             print("...") # Shy dogs say nothing unless prompted
    
#     def give_treat(self):
#         self._has_treat = True
#         print(f"{self.name} happily takes the treat!")

# dog4 = ShyDog("Shiri", 4)
# dog4.call_dog()
# dog4.speak()
# dog4.give_treat()
# dog4.speak_verbose()


# print(f"\nprints attributes and methods for the Dog class:\n{Dog.__dict__}\n ")
# print(f"\nprints the attributes of the instance and their values.:\n{dog4.__dict__}\n ")

class Shout(str):
   def __new__(cls, content):
      return str.__new__(cls, content.upper())

x = Shout("hello there")
print(x) # prints HELLO THERE