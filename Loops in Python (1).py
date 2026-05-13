# loops : while

# Youssef
i = 1 #We choose any variable name and assign it any value.

while  i<=5:
	i+=1 # To prevent unlimited text repetition, we set limits for the value of i.
	print("Youssef")
print ("*"*10)

# 0 2 4 6 8 10
i = 0
while i<=10:
	print(i)
	i+=2
print ("*"*5)
# 1 3 5 7 9
i  = 1
while i<=9:
	i+=1
	print(i)
	
print ("*"*10)

limit = int(input("Enter the limit Number: "))
Choice = input("even or odd: ")

if Choice == "even":
	i=0
elif Choice == "odd":
	i=1
while i<=limit:
	print(i)
	i+= 2