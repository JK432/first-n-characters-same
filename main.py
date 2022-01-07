# Write a Python function called compare which takes two strings s1 and s2 and an integer n as arguments. The function should return True if first n characters of both the strings are same else the function should return False
def com(a,b,n):
  if(a[0:n]==b[0:n]):
    print("The substrings are equal")
  else:
    print("Not equal")

x=input()
y=input()
z=int(input())
com(x,y,z)