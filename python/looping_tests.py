
for i in range(35):
	print("* ", end=" ")
	
	if i == 10:
		print("")
	if i == 15:
		print("")

print()

for j in range(5):
	for k in range(20):
		print("* ", end=" ")
	print()

print()

for a in range(10):
	for b in range(a):
		print(b, end="_")
	print()

print()

for c in range(10,0,-1):
	for e in range(10 - c):
		print("_", end="_")
	for d in range(c):
		print(d, end="_")
	print()

print()

for i in range(1,10):
	for j in range(1,10):
		if j * i > 9:
			print(j * i, end="_")
		else:
			print(j * i, end="__")
	print()

print()

for i in range(1, 10):
	for l in range(10 - i):
		print("_", end="_")
	for j in range(1, i):
		print(j, end="_")
	for k in range(i,0,-1):
		print(k, end="_")
	print()