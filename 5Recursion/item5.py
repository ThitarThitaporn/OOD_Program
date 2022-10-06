def staircase(n, r=0):
    if abs(n) - 1 == r:
        if n > 0:
            return "#" * (r + 1)
        elif n < 0:
            return "_" * (abs(n) - 1) + "#"
        elif n == 0:
            return "Not Draw!"
    else:
        if n > 0:
            return "_" * (n - r - 1) + "#" * (r + 1) + "\n" + staircase(n, r + 1)
        elif n < 0:
            return "_" * (r) + "#" * (abs(n) - r) + "\n" + staircase(n, r + 1)
        elif n == 0:
            return "Not Draw!"


print(staircase(int(input("Enter Input : "))))
