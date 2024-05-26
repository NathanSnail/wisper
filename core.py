import math
import random
import time

mods = {
	"chain spell": -30,
	"reduce lifetime": -42,
	"phasing / true orbit": 80,
	"increase lifetime": 75,
	"orbit / ping pong": 25,
	"spiral": 50,
	"null shot": 280,
}


def div_eval(vals):
	t = {
		0: 0,
		1: 1,
		2: 2,
		3: 2,
		4: 2,
		5: 2,
		6: 3,
		7: 3,
		8: 3,
		9: 3,
		10: 3,
		11: 2,
		12: 3,
		13: 4,
		14: 4,
		15: 4,
		16: 4,
		17: 5,
		18: 5,
		19: 5,
		20: 4,
		21: 3,
		22: 4,
		23: 5,
		24: 5,
		25: 5,
	}
	score = sum([t[x] if x in t.keys() else math.ceil(x / 5) for x in vals])
	return score


inv = {v: k for k, v in mods.items()}

all = [x for k, x in mods.items()]
negative = [x for k, x in mods.items() if x < 0]
positive = [x for k, x in mods.items() if x > 0]


def compute(lower, upper, count):
	frontier = [(0, [])]
	sols = []
	searched = set()
	done = 0

	def new_case(value, stack, elem):
		n = [x for x in stack] + [elem]
		frontier.append((value + elem, n))

	while True:
		e = frontier[0]
		value = e[0]
		stack = e[1]
		stack.sort()
		frontier.pop(0)
		key = tuple(e[1].count(x) for x in all)
		if key in searched:
			continue
		searched.add(key)
		if value > upper:
			for elem in negative:
				new_case(value, stack, elem)
		elif value < lower:
			for elem in positive:
				new_case(value, stack, elem)
		else:
			# if target_ranged:
			# 	if upper != e[0]:
			for elem in positive:
				new_case(value, stack, elem)
			# 	if lower != e[0]:
			for elem in negative:
				new_case(value, stack, elem)
			done += 1
			sols.append(key)
			if done >= count:
				break

	sols.sort(key=lambda x: -div_eval(x))
	return sols


def prettify(sols):
	sols = [
		", ".join([f"{x} * {inv[all[k]]}" for k, x in enumerate(sol) if x > 0])
		+ f" (estimated {div_eval(sol)} spells) for "
		+ f"{sum([x * all[k] for k, x in enumerate(sol)])}f"
		for sol in sols
	]
	print("\n".join(sols))


# prettify(compute(lower, upper, count))


def time_eval(n):
	start = time.time()
	for i in range(n):
		base = random.randint(-400, -30)
		if i % 100 == 0:
			print(i)
		compute(base - 7, base + 7, 100)
	print(time.time() - start)
