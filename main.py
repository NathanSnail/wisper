from core import compute, prettify, time_eval
import sys

args = sys.argv
if len(args) > 1:
	target = args[1]
else:
	target = input("target: ")
if target.find("."):
	bounds = [int(x) for x in target.split(".")]
	upper = max(bounds)
	lower = min(bounds)
else:
	itarget = int(target)
	upper = itarget
	lower = itarget

count = "100"
if len(args) == 1:
	count = input("find: ")
else:
	if len(args) > 2:
		count = args[2]
count = int(count)

# time_eval(10000)
prettify(compute(lower, upper, count))
