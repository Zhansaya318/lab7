n = int(input("="))

#1 task
print("task 1")
for i in range(1,n+1):
    print(i*i, end=" ")
print()
#2 task
print("task 2")
for i in range(1,n+1, 2):
    print(i, end=" ")
print()

#3 task
print("task 3")
for i in range(1, n+1):
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
print()

#4 task
print("task 4")
a = 5
b = 9
for i in range(a, b+1):
    print(i*i, end=" ")
print()

#5 task
print("task 5")
for i in range(n, 0, -1):
    print(i, end=" ")

