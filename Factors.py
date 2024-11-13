
def is_prime(number):
    if number < 1:
        return False
    if number < 0:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_factors(number):   
  factors = []
  divider = 2
  while number > 1:
    while number % divider == 0:
      factors.append(divider)
      number //= divider
    divider += 1
  return factors

number = int(input("Enter number: "))

if is_prime(number): 
    print(number, "is prime")
else:
    factors = prime_factors(number) 
    print(factors)

