import secrets


def main():
    caras_dado = [1,2,3,4,5,6]
    tiros = {}
    for i in range(10):
        cara = secrets.choice(caras_dado)

        if cara in tiros:
            tiros[cara] += 1
        else:
            tiros[cara] = 0

        print(f"El dado cayo en: {cara}")

    print(tiros)

if __name__=='__main__':
    main()