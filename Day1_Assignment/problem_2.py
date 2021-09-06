#Problem_2 : Write a program which accept principle, rate and time from user and print the simple interest.

p = int(input("principle: "))
r = int(input("Rate: "))
t = int(input("Time: "))
print(f"Simple_Interest = {(p*r*t)/100}")