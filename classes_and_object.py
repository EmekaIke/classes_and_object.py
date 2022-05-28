class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("My name is", self.name, "my age is ", self.age, "my tracks are ", self.tracks, "and my score is ", self.score)
        
    #new method
    def change_name(self, name):
        self.name= "Peter"
        print("My name has changed to ", self.name)
        
    #new method
    def change_age(self, age):
        self.age = age
        print("My age has changed to ", self.age)
        
    #new method
    def add_track(self, track):
        self.track = track
        print("I want to add a new track called", self.track)
        
    #new method
    def get_score(self, score):
        self.score = score
        print("My score is ", self.score)
    
#calling class
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score(22))
