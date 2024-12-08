f = open("/Users/eshasantosh/Desktop/day1.txt", "r")
l = []
r = []
total = 0
n = 0

for i in f:
    l.append(i[0:5])
    r.append(i[8:13])
l.sort()
r.sort()

for x in range(len(l)):
     c = abs(int(r[x])-int(l[x]))
     total += c
print(total)

for x in l:
    c = int(x) * r.count(x)
    total += c
print(total)