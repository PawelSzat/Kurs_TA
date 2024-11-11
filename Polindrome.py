"""
1. wprowadzenie liczb po przecinku
2. wprowadzenie pustego pola
3. wielkosci znaków
4. uzycie interpunkcji
"""
def is_polindrome(data):
    
    assert all(znak.isalpha() or znak.isdigit() for znak in data), "Tekst zawiera niedozwolone znaki, uzyj tylko liter lub cyfr"
    print("nie zaweira znakow spec")
    if data.isalpha():
        print("ciag tekstowy")
    elif data.isdigit():
        print("ciag liczbowy")
    else:
        print("ciag mieszany") 
    return data == data[::-1]
    
data = input("Wprowadz polindrom:")
assert data, "pole nie moze byc puste"

if is_polindrome(data):
    print("to jest polindrom")
else:
    print("to nie jest polindrom")
