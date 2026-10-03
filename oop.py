class Person:
 def __init__(self, name, age):
    self.name = name
    self.age = age
 def getAge(self):
   return self.age 
  

person1=Person("junior",30)
# accessing the values
print(person1.name)
print(person1.age)
# modifying the value
person1.age=32
print(person1.age)

# adding new properties
person1.city="ikeja"
person1.nationality="nigerian"

# getting the values
print(person1.city)
print(person1.nationality)
print(person1.getAge())



class Playlist:
  def __init__(self,name):
    self.name=name
    self.songs=[]
  def Add_song(self,song):
    self.songs.append(song)
    print(f"{song} was added")
  def Delete_Song(self,song):
    if song in self.songs:
       self.songs.remove(song)
       print(f"{song} have been deleted successfully!")
  def Show_Songs(self):
      print(f"playlist name:{self.name}")
      for song in self.songs:
        print(song)
Playlist1=Playlist("jamz")
Playlist1.Add_song("update")
Playlist1.Show_Songs()
Playlist1.Add_song("heaven baby")
Playlist1.Show_Songs()
Playlist1.Add_song("Plaintain Seller")
Playlist1.Show_Songs()
Playlist1.Delete_Song("update")

class Employee(Person):
  pass

employee1=Employee("emeka",35)
print(employee1.name)
print(employee1.age)
