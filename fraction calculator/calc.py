# functions

def help():
    print(
        """+ ==> add
        - ==> subtract
        x ==> multiply
        / ==> divide
        help ==> bring this again.
        """
    )

def simplify(N, D):
    hcf = compute_hcf(N, D)
    on =  N / hcf
    od =  D / hcf
    RESULT_LIST = [on, od]
    return RESULT_LIST


def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

def multiply(N1, D1, N2, D2):
    RN = N1 * N2
    RD = D1 * D2
    RESULT_FRACTION_LIST = [RN, RD]
    return RESULT_FRACTION_LIST


def divide(N1, D1, N2, D2):
    RN = N1 * D2
    RD = D1 * N2
    RESULT_FRACTION_LIST = [RN, RD]
    return RESULT_FRACTION_LIST


def add(N1, D1, N2, D2):
    LCM = compute_lcm(D1, D2)

    x_for_d1 = LCM / D1
    x_for_d2 = LCM / D2

    CN1 = N1 * x_for_d1
    CN2 = N2 * x_for_d2

    ON = CN1 + CN2
    RESULT_FRACTION_LIST = [ON, LCM]
    return RESULT_FRACTION_LIST


def subtract(N1, D1, N2, D2):
    LCM = compute_lcm(D1, D2)

    x_for_d1 = LCM / D1
    x_for_d2 = LCM / D2

    CN1 = N1 * x_for_d1
    CN2 = N2 * x_for_d2

    ON = CN1 - CN2
    RESULT_FRACTION_LIST = [ON, LCM]
    return RESULT_FRACTION_LIST


# end


# mainloop
while True:
    # get inputs

    N1 = int(input("numerator 1 -> "))
    D1 = int(input("denominator 1 -> "))

    if D1 == 0:
        print("invalid denominator because it is 0")
        break

    elif D1 == "help":
        help()

    elif D1 == "shud up":
        break

    OP = input("operator (+, -, x, /) -> ")

    if OP != "+" and OP != "-" and OP != "x" and OP != "/":
        print("invalid operator")

    N2 = int(input("numerator 2 -> "))
    D2 = int(input("denominator 2 ->"))


    if D2 == 0:
        print("invalid denominator because it is 0")

    print(f"{N1}/{D1} {OP} {N2}/{D2}\n")

    if OP == "+":
        RESULT_LIST = add(N1, D1, N2, D2)

    elif OP == "x":
        RESULT_LIST = multiply(N1, D1, N2, D2)

    elif OP == "/":
        RESULT_LIST = divide(N1, D1, N2, D2)

    elif OP == "-":
        subtract(N1, D1, N2, D2)

    elif OP == "shud up":
        break


    ON = RESULT_LIST[0]
    OD = RESULT_LIST[1]
    RESULT = f"{ON}/{OD}"
    print(RESULT)
