def factorial(n):
    assert n >= 0 and  int(n) == n, 'The number must be positive integer only.'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) 


###### Head Reacursion ######
def count(val):
    if val == 4:
        return 
    val += 1
    print("value is", val)
    count(val)

val = 0
print(count(val))


###### Tail Reacursion ######
def count(val):
    if val == 4:
        return
    val += 1
    count(val)
    print("value is", val)
val = 0
print(count(val))


def Print(x, n):
    if n == 0:return 0
    print(x)
    Print(x-1, n-1)
    
Print(10, 4)