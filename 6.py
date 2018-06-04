for x in range(1,6):
    print("AAA")

for x in range(1,11):
    print(x)

fruits = ["apple","banana","peach","orange"]
for x in fruits:
    print(x)

for x in range(0,21,2):
    print(x)

username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("valid user")
else:
    print("invalid user")

username = "user"
password = "admin123"

if username == "admin" or password == "admin123":
    print("valid user")
else:
    print("invalid user")

username = "user"
password = "user123"

if username == "admin" or password == "admin123":
    print("valid user")
else:
    print("invalid user")

counter = 0
while counter <= 10:
    print(counter)
    counter +=1
