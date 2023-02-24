class File:
  def __init__(self, name,surname ,age):
      self.name = name
      self.surname = surname
      self.ageeee= age

      
  def get_payment(self):
      return self.pay
  
  def get_name(self):
      return self.name+" "+self.surname
  
  def set_name(self, new_name):
      self.name = new_name  
#   def set_name(self, new_name):
#       self.name = new_name
  
  def __eq__(self, other):
      return self.name == other.name and self.surname == other.surname
  
  def __str__(self):
      return f"File name: {self.name}, File size: {self.size}"
  
  def __lt__(self, other):
      return self.size < other.size

class hourly_worker1(File):
    # File("hamza","konac",21)
    def __init__(self, name: str, surname: int, age: int,hour):
        # super().__init__(name, surname,age)
        # self.category = category
        self.paymnet=0
        self.hou=hour
        
    def calculate_payment(self):
        self.paymnet=self.hou*15
        # print(self.name)
    def get_payment(self):
        return self.paymnet

        
class weekly_worker(File):
    def __init__(self, name: str, surname: int, age: int,day):
        super().__init__(name, surname,age)
        # self.category = category
        self.paymnet=0
        self.day=day
        
    def calculate_payment(self):
        self.paymnet=self.day*90
    def get_payment(self):
        return self.paymnet


worker1=hourly_worker1("hamza","konac",21,15)
worker2=weekly_worker("mehmet","veli",22,15)
worker1.calculate_payment()
worker2.calculate_payment()
print(f"{worker1.get_name()}   {worker1.get_payment()}")
print(f"{worker2.get_name()}   {worker2.get_payment()}")

worker3=File("hamza","konac",21)
# worker3.ca

# if(worker1.__eq__(worker2)):
#     print("equal")
# else:
#     print("not equal")
# worker1.set_name("mehmet")

# print(worker1.get_name())

# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)
# worker=File("hamza","konac",21,3009)



# if __name__ == '__main__':
#   file1 = File('hello.txt', 10)
#   file2 = File('hello.txt', 10)
#   print(file1) # Should print 'File name: hello.txt, File size: 10'

#   file3 = File('bybye.md', 20)
#   print(file3) # Should print 'File name: bybye.md, File size: 20'

#   print(file1 == file3) # Should print False
#   print(file1 == file2) # Should print True
