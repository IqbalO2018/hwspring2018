import random
import collections
input = raw_input(" enter 9 random characters ")
d = collections.defaultdict(int)

if len(input) > 9:
	print("please run the code again")

for c in input:
	d[c] += 1

found = False

for c in sorted(d, key = d.get, reverse=True):
	if d[c] > 1 and not found:
		found = True
		print ("Run the code again and include a string without repetition of the characters")

g1r1c1 = input[0]
g1r1c2 = input[1]
g1r1c3 = input[2]
g2r1c1 = input[3]
g2r1c2 = input[4]
g2r1c3 = input[5]
g3r1c1 = input[6]
g3r1c2 = input[7]
g3r1c3 = input[8]

r1 = []

r1.append(g1r1c1)
r1.append(g1r1c2)
r1.append(g1r1c3)
r1.append(g2r1c1)
r1.append(g2r1c2)
r1.append(g2r1c3)
r1.append(g3r1c1)
r1.append(g3r1c2)
r1.append(g3r1c3)

g1r2c1 = input[3]
g1r2c2 = input[4]
g1r2c3 = input[5]
g2r2c1 = input[6]
g2r2c2 = input[7]
g2r2c3 = input[8]
g3r2c1 = input[0]
g3r2c2 = input[1]
g3r2c3 = input[2]

r2 = []

r2.append(g1r2c1)
r2.append(g1r2c2)
r2.append(g1r2c3)
r2.append(g2r2c1)
r2.append(g2r2c2)
r2.append(g2r2c3)
r2.append(g3r2c1)
r2.append(g3r2c2)
r2.append(g3r2c3)

g1r3c1 = input[6]
g1r3c2 = input[7]
g1r3c3 = input[8]
g2r3c1 = input[0]
g2r3c2 = input[1]
g2r3c3 = input[2]
g3r3c1 = input[3]
g3r3c2 = input[4]
g3r3c3 = input[5]

r3 = []

r3.append(g1r3c1)
r3.append(g1r3c2)
r3.append(g1r3c3)
r3.append(g2r3c1)
r3.append(g2r3c2)
r3.append(g2r3c3)
r3.append(g3r3c1)
r3.append(g3r3c2)
r3.append(g3r3c3)

g1r4c1 = input[1]
g1r4c2 = input[2]
g1r4c3 = input[3]
g2r4c1 = input[4]
g2r4c2 = input[5]
g2r4c3 = input[6]
g3r4c1 = input[7]
g3r4c2 = input[8]
g3r4c3 = input[0]

r4 = []

r4.append(g1r4c1)
r4.append(g1r4c2)
r4.append(g1r4c3)
r4.append(g2r4c1)
r4.append(g2r4c2)
r4.append(g2r4c3)
r4.append(g3r4c1)
r4.append(g3r4c2)
r4.append(g3r4c3)

g1r5c1 = input[4]
g1r5c2 = input[5]
g1r5c3 = input[6]
g2r5c1 = input[7]
g2r5c2 = input[8]
g2r5c3 = input[0]
g3r5c1 = input[1]
g3r5c2 = input[2]
g3r5c3 = input[3]

r5 = []

r5.append(g1r5c1)
r5.append(g1r5c2)
r5.append(g1r5c3)
r5.append(g2r5c1)
r5.append(g2r5c2)
r5.append(g2r5c3)
r5.append(g3r5c1)
r5.append(g3r5c2)
r5.append(g3r5c3)

g1r6c1 = input[7]
g1r6c2 = input[8]
g1r6c3 = input[0]
g2r6c1 = input[1]
g2r6c2 = input[2]
g2r6c3 = input[3]
g3r6c1 = input[4]
g3r6c2 = input[5]
g3r6c3 = input[6]

r6 = []

r6.append(g1r6c1)
r6.append(g1r6c2)
r6.append(g1r6c3)
r6.append(g2r6c1)
r6.append(g2r6c2)
r6.append(g2r6c3)
r6.append(g3r6c1)
r6.append(g3r6c2)
r6.append(g3r6c3)

g1r7c1 = input[2]
g1r7c2 = input[3]
g1r7c3 = input[4]
g2r7c1 = input[5]
g2r7c2 = input[6]
g2r7c3 = input[7]
g3r7c1 = input[8]
g3r7c2 = input[0]
g3r7c3 = input[1]

r7 = []

r7.append(g1r7c1)
r7.append(g1r7c2)
r7.append(g1r7c3)
r7.append(g2r7c1)
r7.append(g2r7c2)
r7.append(g2r7c3)
r7.append(g3r7c1)
r7.append(g3r7c2)
r7.append(g3r7c3)

g1r8c1 = input[5]
g1r8c2 = input[6]
g1r8c3 = input[7]
g2r8c1 = input[8]
g2r8c2 = input[0]
g2r8c3 = input[1]
g3r8c1 = input[2]
g3r8c2 = input[3]
g3r8c3 = input[4]

r8 = []

r8.append(g1r8c1)
r8.append(g1r8c2)
r8.append(g1r8c3)
r8.append(g2r8c1)
r8.append(g2r8c2)
r8.append(g2r8c3)
r8.append(g3r8c1)
r8.append(g3r8c2)
r8.append(g3r8c3)


g1r9c1 = input[8]
g1r9c2 = input[0]
g1r9c3 = input[1]
g2r9c1 = input[2]
g2r9c2 = input[3]
g2r9c3 = input[4]
g3r9c1 = input[5]
g3r9c2 = input[6]
g3r9c3 = input[7]

r9 = []

r9.append(g1r9c1)
r9.append(g1r9c2)
r9.append(g1r9c3)
r9.append(g2r9c1)
r9.append(g2r9c2)
r9.append(g2r9c3)
r9.append(g3r9c1)
r9.append(g3r9c2)
r9.append(g3r9c3)

b = random.randint(1,5)


if(b ==1):
	print (r1)
	print (r2)
	print (r3)
	print (r4)
	print (r5)
	print (r6)
	print (r7)
	print (r8)
	print (r9)

elif(b == 2):
	print (r2)
        print (r1)
        print (r3)
        print (r5)
        print (r4)
        print (r6)
        print (r8)
        print (r7)
        print (r9)

elif(b == 3):
        print (r3)
        print (r2)
        print (r1)
        print (r6)
        print (r5)
        print (r4)
        print (r9)
        print (r8)
	print (r7)

elif(b == 4):
	print (r3)
        print (r1)
        print (r2)
        print (r6)
        print (r4)
        print (r5)
        print (r9)
        print (r7)
        print (r8)

elif(b == 5):
	print (r1)
        print (r3)
        print (r2)
        print (r4)
        print (r6)
        print (r5)
        print (r7)
        print (r9)
        print (r8)
else:
	print( "This went wrong")
