"""
5. Determină dacă un număr dat este palindrom.
Funcția principală: is_palindrome(n) -> bool
Funcția de test: test_is_palindrome()
"""

def citire():
    n = int(input("Dati un numar: "))
    return n

def printMenu():
    print("1. Citire numar. ")
    print("2. Verifica daca numarul dat este palindrom. ")
    print("3. Verifica daca numarul este superprim. ")
    print("4. Verifica daca numarul dat este antipalindrom. ")
    print("x. Iesire. ")

def is_palindrome(n):
    """
    Determina daca un numar dat este palindrom
    :param n: numar intreg
    :return: True, daca numarul dat este palindrom, respectiv False, in caz contrar.
    """
    x = int(n)
    k = 0
    while x > 0:
        k = k * 10 + x % 10
        x = x // 10
    if k == n:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(123) == False
    assert is_palindrome(12321) == True
    assert is_palindrome(12) == False
    assert is_palindrome(6789876) == True

"""
6. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. 
   De exemplu, 233 este superprim, deoarece 2, 23 și 233 sunt toate prime, 
   dar 237 nu este superprim, deoarece 237 nu este prim.
Funcția principală: is_superprime(n) -> bool
Funcția de test: test_is_superprime()
"""

def is_prime(n):
    """
    Verifica daca un numar este superprim, adica, daca toate prefixele sale sunt prime.
    :param n: un numar intreg
    :return: True, daca numarul e superprim, respectiv, False, in caz contrar.
    """
    ok = True
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n % i == 0 and ok == True:
            ok = False
    if ok:
        return True
    else:
        return False

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(3) == True
    assert is_prime(9) == False
    assert is_prime(13) == True

def is_superprime(n):
    copie_n = int(n)
    ok = True
    while copie_n != 0 and ok == True:
        s = is_prime(copie_n)
        copie_n = copie_n // 10
        if s == False:
            ok = False
    return ok

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(1371) == False
    assert is_superprime(11311) == True

"""
7. Determină dacă un număr este antipalindrom: un număr este antipalindrom dacă oricare două cifre
    egal depărtate de extremități sunt diferite (excepție făcând cifra din mijloc dacă avem 
    un număr impar de cifre). De exemplu: 2783 este antipalindrom, iar 2773 nu este.
Funcția principală: is_antipalindrome(n) -> bool
Funcția de test: test_is_antipalindrome()
"""

def is_antipalindrome(n):
    k = 0
    x = int(n)
    aux = 0
    while x != 0:
        k = k + 1
        x = x // 10
    x = int(n)
    while x != 0:
        aux = aux * 10 + x % 10
        x = x // 10
    c = 1
    x = int(n)
    while aux != 0:
        if k % 2 != 0 and c != k // 2 + 1:
            if aux % 10 == x % 10:
                return False
        elif aux % 10 == x % 10:
            return False
        aux=aux//10
        x=x//10
        c = c + 1
    return True

def test_is_antipalindrome():
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False

test_is_palindrome()
test_is_prime()
test_is_antipalindrome()

while True:
    printMenu()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        n = citire()
    elif optiune == "2":
        print(is_palindrome(n))
    elif optiune == "3":
        print(is_superprime(n))
    elif optiune =="4":
        print(is_antipalindrome(n))
    elif optiune == "x":
        break
    else:
        print("Optiune gresita! Reincercati! ")