answer = 0

"""
'answer' variable is the sum of
all the multiples of 3 or 5 below 1000
"""

for i in range(1000):  # cycle for find the sum
    if i % 3 == 0 or i % 5 == 0:
        answer += i    # '+=' same as 'answer = answer + i'
print(answer)

# https://projecteuler.net/problem=1 => problem description
