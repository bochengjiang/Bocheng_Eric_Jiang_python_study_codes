# 8-th homework 2nd question
## Please write a program that requires the user to input an integer n, and then outputs all even numbers from 0 to n. 
## For example, if the user inputs 10, the program should output 0, 2, 4, 6, 8, 10.

n=int(input("please enter a random number that is greater than 0:"))
even_number_list=[]
for even_number in range (0,n+1,2):
    even_number_list.append(even_number)
print (even_number_list)