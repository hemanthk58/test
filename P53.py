n = 7
fibonic_series= [0,1]
'''
for i in range(2,n):
    next_term =fibonic_series[-1] + fibonic_series[-2]
    fibonic_series.append(next_term)
print(fibonic_series)
'''
while len(fibonic_series) < n:
    next_term =fibonic_series[-1] + fibonic_series[-2]
    fibonic_series.append(next_term)
print(fibonic_series)
