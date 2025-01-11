class Animal():
   
   def __init__(self) -> None:
      self.no_of_eyes=2
    
   def breathe(self):
      print("inhale,exhale")

class Fish(Animal):
  def __init__(self) -> None:
    super().__init__() 
    #super().__init__() calls the constructor of the parent class, initializing the attributes inherited from the parent class. 
    #In this specific case, it "ensures" that the no_of_eyes attribute from the Animal class is properly initialized in the Fish class
  
  def breathe(self):   
    super().breathe()#what this breathe function first it use the breathe function from the super class and then also print something as well 
    print("when inside water")

fish=Fish()
fish.breathe()
print(fish.no_of_eyes)

