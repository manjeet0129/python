#B#class that store information
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
