# Problem 3

# Iterative
n = 100
mysum = 0
for i in range(1, n + 1):
    mysum = mysum + i
    i = + 1

print(mysum)


# Recursive
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(100))
