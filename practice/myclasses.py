# class Student:
#     name="leo"
#     sait_id="1234"
#     age="18"
    
#     def moves():
#         print ("moves")
        
#     def say_your_name():
#         print(f"my name is {Student.name}")    
    
#     # moves()
#     # eats()
      
# print(Student.name)        
# Student.moves()      
# Student.say_your_name()



# this is class method
class Car:
    color=""
    model=""
    @staticmethod
    def color():
        print("Color")
    
    @staticmethod    
    def moves():
        print("it moves")    
        
print(Car.color)  
# print(Car.model)
Car.moves()      
 
# this is object method   
class Car:
    engine_type = "gas"
    
    def __init__(self , model, color):
        self.model = model
        self.color = color
    
    def get_color(self):
        print("my color is" + self.color + "my engine type is" + Car.engine_type)
            
        
Car("Red").get_color
Car("Green").get_color  
         
        #  to specify the modeltype
def __init__(self, model="BMW", year ="2008"):
        self.model = model
Car("BMW", "2008").get_model
# same as above
Car().get_model
         