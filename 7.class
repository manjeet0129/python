#A#class that store information
class student:
  def info(self, studname,studaddress, studclass):
     print("name:", studname)
     print("address:",studaddress)
     print("class:", studclass)
obj=student()
obj.info('veda','airoli', 'syit')

#B##implement the concept of inheritance 
class st:
    def s1(self):
        print("base class")

class st1(st):
    def s2(self):
        print("derived class")

# Create an object of st1
t = st1()

# Call the method from base class
t.s1()

# Call the method from derived class
t.s2()


#c) Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a constructor which takes the parameters x and y (these should all be numbers).
 class Numbers:
    MULTIPLIER=3
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    @classmethod
    def multiply(cls,a):
        return cls.MULTIPLIER*a
    @staticmethod
    def subtract(b,c):
        return b-c
    @property
    def value(self):
        return(self.x,self.y)
    @value.setter
    def value(self,xy_tuple):
        self.x,self.y=xy_tuple
    @value.deleter
    def value(self):
        del self.x
        del self.y
T=Numbers(2,4)
print(T.add())
print(T.multiply(2))
print(Numbers.subtract(4,3))
