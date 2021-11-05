N = int(input("Please give us a number: "))
N_even = N%2 == 0
if N_even:
	sum_of_odds = (N/2)**2
	avg_of_evens = N/2 + 1
else:
	sum_of_odds = ((N+1)/2)**2
	avg_of_evens = (N-1)/2 + 1
print("Sum of odds between 1 and {} : {}".format(N,sum_of_odds))
print("Avarage of evens between 1 and {} : {}".format(N,avg_of_evens))