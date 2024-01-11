for i in range(5):
    # print("Hello")
    print(i, end="")

print()
for i in range(2, 5):
    print(i, end=" ")

print()
for i in range(1, 5, 2):
    print(i, end=" ")

print()
print()
for i in range(1, 5, 1):
    print(i, end=" ")

print()
for i in range(-1, 5, 2):
    print(i, end=" ")

print()
start, end = 1, 10
for i in range(start, end + 1):
    print(i,end=" ")

print()
start, end = 1, 10
for i in range(end, start - 1, -1):
    print(i, end=" ")

print()
start, end = 1, 10
for i in range(end, start - 1, -2):
    print(i, end=" ")

print()
for value in 2, "hello", 2.5, "world", True:
    print(value)