def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def concatenare_nr_pozitive(l):
    '''
    Determina nr obtinut prin concatenarea tuturor nr pozitive din lista
    :param l: o lista de int-uri
    :return: nr obtinut prin concatenarea tuturor nr pozitive din l
    '''
    rezultat=''
    for x in l:
        if x>0:
            nr_in_string=str(x)
            rezultat+=nr_in_string
    return int(rezultat)


def test_concatenare_nr_pozitive():
    assert concatenare_nr_pozitive([0, 8, 23, -13, 25])==82325
    assert concatenare_nr_pozitive([0, -1,-562,23,56]) == 2356
    assert concatenare_nr_pozitive([0, 8,-5]) == 8

def suma_mic_mare(l):
    '''
    Determina suma dintre cel mai mare număr din listă și cel mai mic număr din listă.
    :param l: o lista de int-uri
    :return: suma dintre cel mai mare număr din l și cel mai mic număr din l
    '''
    nr_max=l[0]
    nr_min=l[0]
    for x in l:
        if x>nr_max:
            nr_max=x
        elif x<nr_min:
            nr_min=x
    return nr_max+nr_min


def test_suma_mic_mare():
    assert suma_mic_mare([10, -3, 25, -1, 3, 25, 18])==22
    assert suma_mic_mare([10, -3, 0]) == 7
    assert suma_mic_mare([-1,-8,-10]) == -11


def suma_cifrelor(n):
    '''
    determina suma cifrelor unui nr
    :param n: un nr intreg
    :return: suma cifrelor lui n
    '''
    rezultat=0
    while n>0:
        rezultat=rezultat+n%10
        n=n//10
    return rezultat


def test_suma_cifrelor():
    assert suma_cifrelor(2)==2
    assert suma_cifrelor(223) == 7
    assert suma_cifrelor(111111) == 6


def suma_cifrelor_mai_mari_decat_n(l,n):
    '''
     Afișeaza toate numerele care au suma cifrelor mai mare sau egală decat un număr n citit de la tastatură.
    :param l:o lista de int-uri
    :param n:un nr citit de la tastatura
    :return:toate numerele, din l, care au suma cifrelor mai mare sau egală decat n
    '''
    rezultat=[]
    for x in l:
        if suma_cifrelor(x)>=n:
            rezultat.append(x)
    return rezultat


def test_suma_cifrelor_mai_mari_decat_n():
    assert suma_cifrelor_mai_mari_decat_n([25, 11, 10, 24, 39],7)==[25,39]
    assert suma_cifrelor_mai_mari_decat_n([1, 2, 3, 4], 5) == []
    assert suma_cifrelor_mai_mari_decat_n([1, 2, 3, 4, 40], 4) == [4,40]

def main():
    test_suma_mic_mare()
    test_concatenare_nr_pozitive()
    test_suma_cifrelor()
    test_suma_cifrelor_mai_mari_decat_n()
    l=[]
    while True:
        print("1. Citire lista")
        print("2.Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.")
        print("3.Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă.")
        print("4.Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n "
              "citit de la tastatură.")
        print("5.Afișarea listei obținute din lista inițială în care numerele pătrat perfect "
              "sunt înlocuite cu radicalul acestora.")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune=="2":
            print(concatenare_nr_pozitive(l))
        elif optiune=="3":
            print(suma_mic_mare(l))
        elif optiune=="4":
            n=int(input("Dati un nr:"))
            print(suma_cifrelor_mai_mari_decat_n(l,n))
        elif optiune=="a":
            print(l)
        elif optiune=="x":
            break
        else:
            print("Optinue gresita!Reincercati!")


if __name__ == '__main__':
  main()
