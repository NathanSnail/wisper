import copy
frontier = [(0,[])]

mods = {"chain spell": -30,
        "reduce lifetime": -42,
        "phasing / true orbit": 80,
        "increase lifetime": 75,
        "orbit / ping pong": 25,
        "spiral": 50,
        "null shot": 280
        }

inv = {v: k for k,v in mods.items()}

negative = [x for k,x in mods.items() if x < 0]
positive = [x for k,x in mods.items() if x > 0]

target = int(input("target: "))
count = input("find: ")
if count == "":
	count = "100"
count = int(count)
sols = []
searched = set()
done = 0
while True:
	e = frontier[0]
	frontier.pop(0)
	e[1].sort()
	tstr = f"{len(e[1])} total: {', '.join([inv[x] for x in e[1]])}"
	if tstr in searched:
		continue
	searched.add(tstr)
	if e[0] > target:
		for elem in negative:
			n = copy.copy(e[1])
			n.append(elem)
			frontier.append((e[0]+elem,n))
	elif e[0] < target:
		for elem in positive:
			n = copy.copy(e[1])
			n.append(elem)
			frontier.append((e[0]+elem,n))
	else:
		e[1].sort()
		done += 1
		sols.append(tstr)
		if done >= count:
			break

sols.reverse()
print("\n".join(sols))