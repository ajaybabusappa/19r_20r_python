#Pro
#In general - variables or functions (methods)
class Calculator:
    company_name = "Casio"
    total_count = 0
    price = 10000
    def __init__(self, id1, name1):
        self.id = id1
        self.name = name1
        Calculator.total_count += 1
        print("Calculator constructor called")
        
    def show_id_name(self):
        print(self.id, self.name)
        
        
    @classmethod
    def reset_count_name(cls, new_name):
        cls.total_count = 0
        cls.company_name = new_name
        print("Total count is reset to zero")
        
    @classmethod
    def set_price(cls, new_price):
        cls.price = new_price
        
    
    @staticmethod
    def connect_to_database():
        print("Connecting to database")
        


calc1 = Calculator(2, "Normal calculator")
calc1.show_id_name()
calc1.created_date = "02-05"
calc2 = Calculator(3, "Advanced calculator")
calc2.show_id_name()

print(vars(calc1))
print(vars(calc2))


#Variables - class or static varaible and instance variable
#Methods - Class methods, static methods and instance methods are differernt


print(calc1.company_name)

#print(Calculator.id)
print(Calculator.company_name)
print(Calculator.total_count)



Calculator.reset_count_name('My Casio')

print(Calculator.company_name)
print(Calculator.total_count)

print(Calculator.connect_to_database())


#4 pillars - Inheritance, Polymorphism, Encapsulation, Abstraction


#Inheritance - 