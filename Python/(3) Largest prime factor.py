the_number = 600851475143
i = 2

while i * i <= the_number:
    if the_number % i:
        i += 1
    else:
        the_number //= i # floor division. Ex: 10/4 = 2.5 is division, 10/4 = 2 is floor division
print(the_number)
