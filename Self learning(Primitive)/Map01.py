def demo01():
    fruit = {'mango', 'apple', 'longan'}
    fruit2 = list(map(str.capitalize, fruit))
    fruit3 = [f.capitalize() for f in fruit]

    print(fruit2)
    print(fruit3)


def usd2thb(usd):
    return usd * 33


def demo02():
    priceUsd = [10, 20, 30, 40, 50]
    priceThb = [n * 33 for n in priceUsd]
    priceThb2 = list(map(lambda n: n * 33, priceUsd))
    priceThb3 = list(map(usd2thb, priceUsd))

    print(priceThb)
    print(priceThb2)
    print(priceThb3)


def area():
    f = input("rai-ngan-sawah : ").split('-')
    Lst_f = list(map(int, f))
    rai, ngan, sqwah = list(map(int, f))
    # print(f)
    print(Lst_f)
    #print(rai, ngan, sqwah)


if __name__ == '__main__':
    # demo01()

    # demo02()
    area()
