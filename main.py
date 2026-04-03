# 1
m = lambda a, b: a if a > b else b

print(m(2,10))



# 2
a = lambda x: x if x >= 0 else -x

print(a(-5))

# 3
a = lambda a, b, c: a + b + c

print(a(5, 4, 8))

# 4
q = lambda a, b: a % b

print(q(17, 5))

# 6
m = lambda a, b: 0 if a == b else (a if a < b else b)

print(m(10,25))

# 7
a = lambda x: "juft" if x % 2 == 0 else "toq"

print(a(4))

# 8
a = lambda eni, boyi: eni * boyi

print(a(7, 6))


# 10
a = lambda x: len(str(abs(x)))

print(a(355205))


# 11
a = lambda a, b: a % b == 0

print(a(20, 4))


# 12
a = lambda b: 3.12 * b ** 2

print(a(4))


# 13
a = lambda a, b: (a - b) ** 2

print(a(4, 2))

# 15
a = lambda a, b, c: "teng tomonli" if a== b== c else ("teng yonli" if a==b or b==c or a==c else "oddiy")

print(a(5,7,8))
