f = open('a.txt', 'r')
lines=f.readlines()
f.close()

f2 = open('b.txt', 'w')
for line in lines:
    line = line.replace("java", "python")
    f2.write(line)
f.close()
