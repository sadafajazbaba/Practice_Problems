
def hello():
    print("I am tired")
hello()
def greet(fx):
    def mfx(*args,**kwargs):
     print("Good Evening")
     fx(*args, **kwargs)
     print("Thanks for using this function.")
    return mfx
@greet
def Roy():
  print("I love Arundhati Roy")
@greet
def add(a,b):
    print(a+b)
    
add(6,6)
Roy()