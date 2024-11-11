"""
1. wprowadzenie liczb po przecinku
2. wprowadzenie pustego pola
3. wielkosci znaków
4. uzycie interpunkcji
"""
def is_polindrome(text):
    
    assert all(znak.isalpha() or znak.isdigit() for znak in text), "Tekst zawiera niedozwolone znaki, uzyj tylko liter lub cyfr"
    print("nie zaweira znakow spec")
    if text.isalpha():
        print("ciag tekstowy")
    elif text.isdigit():
        print("ciag liczbowy")
    else:
        print("ciag mieszany") 
    return text == text[::-1]
    
text = input("Wprowadz polindrom:")
assert text, "pole nie moze byc puste"

if is_polindrome(text):
    print("to jest polindrom")
else:
    print("to nie jest polindrom")
