
greeting = "Hello"
name = "Renato"

def greet_2():
     global greeting
     greeting = "Goodbye"
     name= "Sara"

     message = f"{greeting} , {name}"

     print(message)

greet_2()
print(name)
print(greeting)
 