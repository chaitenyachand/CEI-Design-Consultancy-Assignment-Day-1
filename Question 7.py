# Create a program that prints the multiplication table of a given number using while loop

num = int(input("Enter a number to print it's multiplication table: "))
i=1

while i<=10:
  print(f"{num}X{i} = {num * i}")
  i += 1
