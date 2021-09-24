
a = 10
def test_func():
    print(a)


test_func()
print(a)

print("__________________________")

def test_func2():
    b = 10
    print(b)
test_func2()
#print(b)

print("______________")
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

print("_______________________-")
#Same name
def spam():
    eggs = 'spam local'
    print(eggs)    # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)    # prints 'bacon local'
    spam()
    print(eggs)    # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)        # prints 'global'

print("_____________________")
#Global statement
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)