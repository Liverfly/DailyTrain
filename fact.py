import sys  
#tailcall 
def fact(x, acc=1):  
    if x: return fact(x.__sub__(1), acc.__mul__(x))  
    return acc  
sys.stdout.write(str(fact(6)) + '\n') 