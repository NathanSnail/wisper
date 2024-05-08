from core import prettify, compute, time_eval

target = input("target: ")
if target.find("."):
	bounds = [int(x) for x in target.split(".")]
	upper = max(bounds)
	lower = min(bounds)
else:
	itarget = int(target)
	upper = itarget
	lower = itarget

count = input("find: ")
if count == "":
	count = "100"
count = int(count)

#time_eval(10000)
prettify(compute(lower, upper, count))
