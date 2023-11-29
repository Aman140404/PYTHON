a = int(input("enter the number of elements you want to enter in the list"))
s = []
for i in range(0, a):
    b = int(input("enter the next element of the list"))
    s.append(b)
d = len(s)
temp = s[d-1]
s[d-1] = s[0]
s[0] = temp
for i in range(0, len(s)):
    print(s[i])
