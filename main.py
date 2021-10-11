def is_prime(n):
    '''
    Determina daca un numar este prim sau nu.
    - n : intreg
    - prim: bool care va fi true daca numarul este prim, respectiv
    false daca numarul nu este prim
    '''
    prim = True
    if n < 2:
        prim = False
    for i in range(2, n):
        if n % i == 0:
            prim = False
    return prim


def get_largest_prime_below(n):
    '''
    Determina cel mai mare numar prim mai mic decat n
    Input:
    - n: intreg
    Output:
    - cel mai mare numar prim mai mic decat n
    '''

    for i in range(n, 2, -1):
        check = is_prime(i)
        if check == True:
            return i


def is_leap(year):
    '''
    Determina daca un an dat este bisect sau nu
    Input:
    - year: intreg care reprezinta anul introdus
    Output:
    - False daca anul introdus nu este bisect, respectiv True, daca anul introdus este bisect
    '''
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def get_leap_years(start, end):
    '''
    Determina folosind functia is_leap toti anii bisecti dintr-un interval dat
    Input:
    -start,end : intregi care reprezinta capetele intervalului
    Output:
    -leapYears: o lista de intregi care contine toti anii bisecti din intervalul [start,end]
    '''
    leapYears = []
    for i in range(start, end + 1):
        if is_leap(i):
            leapYears.append(str(i))
    for i in range(0, len(leapYears)):
        leapYears[i] = int(leapYears[i])
    return leapYears


def test_is_leap():
    assert is_leap(1964) == True
    assert is_leap(1968) == True
    assert is_leap(1972) == True
    assert is_leap(1973) == False
    assert is_leap(2100) == False
    assert is_leap(1700) == False
    assert is_leap(2020) == True
    assert is_leap(2030) == False


def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(1) == None


test_get_largest_prime_below()
test_is_leap()


def main():
    while True:
        print('1.Cel mai mare numar prim mai mic decat un numar dat.')
        print('2.Afiseaza toti anii bisecti intre doi ani dati')
        print('x. Exit')
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            nr = int(input('Dati un numar: '))
            C = get_largest_prime_below(nr)
            print(f'Cel mai mare numar prim mai mic decat {nr} este {C}')
        elif optiune == '2':
            nr1 = int(input('Dati primul an: '))
            nr2 = int(input('Dati al doilea an: '))
            print(f'Anii bisecti din intervalul {nr1} , {nr2} este {get_leap_years(nr1, nr2)}')

        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

main()