from dokusan import generators
import numpy as np
import time
print("Hello and welcome to Atharva's sudoku generator")
print()
time.sleep(2)
print("one thing to remember is that whatever sudoku ")
print("this program generators there the 0 mean empty spaces")
print()
while True:
    time.sleep(5)
    do=input("do you want to genrte a sudoku yes|no: ")
    print()
    if(do=="yes"):
        time.sleep(2)
        arra=np.array(list(str(generators.random_sudoku(avg_rank=150))))
        print(arra.reshape(9,9))  
        print() 
    elif(do=="no"):
        time.sleep(2)
        break     
    else:
      print("invalid text")
      print()
print("goodbey!")
print()
time.sleep(3)