generation = 5 # n
fecundity = 3 # k
prev_young = 1
prev_adult = 0
for i in range(0, generation-1):
	current_adult =  prev_young + prev_adult
	current_young = prev_adult * fecundity
	current_total = current_adult + current_young
	prev_young = current_young
	prev_adult = current_adult
	print current_total, 

