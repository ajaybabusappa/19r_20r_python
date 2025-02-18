# class Calc:
#     def __init__(self, id1, name1):
#         self.id = id1
#         self.name = name1
#         print("Calc object is created", self.id, self.name)

#     def sum (self, a, b):
#         return a  + b
    
#     def sub (self, a, b):
#         return a - b

# #Inheritance - By default only methods gets inherited. 

# class SciCalc(Calc):
#     def __init__(self, id1, name1):
#         super().__init__(id1, name1)
#         print("SciCalc object created")


# sci_calc_1 = SciCalc(2, 'Sci1')
# print(sci_calc_1.sum(5, 6))
# print(sci_calc_1.id)





# #We types in Inheritance - Mutliple and Multilevel


# class Human:
#     pass
#     #talk, walk

# class Child(Human):
#     pass


# class Student(Child):
#     pass



# #Multiple Inheritance

# # class Lion:
# #     pass
# #     #Hunt, Walk and Talk


# # class Tiger:
# #     pass
# #     #Hunt, walk, Talk

# # class Liger(Lion, Tiger):
# #     pass



class Lion:
    def _init__(self):
        print("Lion called")
    #Hunt, Walk and Talk

    def hunt(self):
        print("Lion hunt function called")


class Tiger:
    def __init__(self, name):
        self.name = name
        print("Tiger called")
    #Hunt, Walk and Talk

    def hunt(self):
        print("Tiger hunt function called")

class Liger( Lion, Tiger):
    def __init__(self, name):
        self.name = name

    def compare (self, other):
        if self.name == other.name:
            print("Both are same ligers")
        else:
            print("Both are not same ligers")

    def hunt(self, *b):
        print("Liger hunt function is being called")

    def hunt(self, predator):
        print("New hunt function")

    def __add__(self, other):
        return self.name + other.name
    
    def __xor__(self, other):
        print("I will not do xor")


liger1 = Liger('Simbha')
liger2 = Liger('Simbha')
tiger1 = Tiger('Simbha')


liger1.compare(liger2)
liger1.compare(tiger1)
#liger2.compare(liger1)

# liger1.hunt()


#Method resolution order (MRO)

# print(Liger.mro())
#print(__mro__(liger1))




#Polymorphism - Duck typing and Operator overloading

#Method overriding.
#Method overloading
#Polymorphism - 

#Ducktyping


#operator overloading - 


print(2 + 3)
num1 = 2
print(num1.__add__(3))
print("Ab" + "Bc")
print(liger1 + liger2)
liger1 ^ liger2


print (2 - 3)




#Encapsulation


class Human:
    def __init__(self, id1, name1, dob1, bg1):
        self.id = id1
        self._name = name1
        self.dob = dob1
        self.__blood_group = bg1


        # def get_name(self):
        #     print(self.name)

        #Setters
    def set_name(self, new_name):
        self.name = new_name

    def get_bg(self):
        print(self.__blood_group)

human1 = Human(1, 'Suman', '12/12/12', 'O+')
print(human1)

#print(human1.name)
#human1.get_name()


#Variables - public, private, protected


print(human1.id)
print(human1.dob)
human1.get_bg()
print(human1.__blood_group)





private variables only in class deinitio
public variables u can use them any where






