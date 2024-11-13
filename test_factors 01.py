
# poprawne zaimportowanie 
def test_import_factors():
    try:
        from Factors import prime_factors
        assert callable(prime_factors), "prime_factors not callable"
    except ImportError as error:
        assert False, error
# sprawdzenie czy podana wartosc jest liczba pierwsza 
def test_is_prime():
        from Factors import is_prime
        result = is_prime(2)  #jak zaimplemetowac liczbe podana przez uzytkownika
        assert result == True, f"error {result}"
# sprawdzenie czy podana wartosc nie jest ujemna     
def test_is_prime_less_1():
    test_cases = [0, -1, -5, -7, -11]
    from Factors import is_prime
    for number in test_cases:
        result = is_prime(number)
        assert result == False, f"jest ujemna" #zawsze zgłasza test ok.

    
if __name__ == '__main__':
    for test in (
        test_import_factors, test_is_prime, test_is_prime_less_1
        ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)
