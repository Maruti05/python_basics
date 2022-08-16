#1.Local variable 2.Global variable

#1.Local Variable
#Local variables are the variables that declared inside the function and have scope within the function.
b=45   #global variable
def add():
    a=10 #local variable
    print(a)
    print(b)


add()
del b #delete variable
print(b)    

