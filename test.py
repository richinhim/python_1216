#1
print("*"*5, end="")

print()
print("="*20)
#2
str = "*"
for i in range(4):
    print("*"*5, end="")
    print()
#3
for i in range(1,6):
    print(str*i, end="")
    print()

print()
print("="*20)

#4

for i in range(5, 0, -1):
    print(str * i, end="")
    print()

print()
print("=" * 20)

empty = " "
for i in range(1, 6):
    print(str * i, end=empty*i)
    print()
