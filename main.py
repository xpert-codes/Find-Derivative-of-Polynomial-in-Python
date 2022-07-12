import random


def derivativeTerm(pTerm, val):

    # Get coefficient
    coeffStr = ""

    i = 0
    while (i < len(pTerm) and
           pTerm[i] != 'x'):
        coeffStr += (pTerm[i])
        i += 1

    coeff = int(coeffStr)

    # Get Power (Skip 2 characters
    # for x and ^)
    powStr = ""
    j = i + 2
    while j < len(pTerm):
        powStr += (pTerm[j])
        j += 1

    power = int(powStr)

    # For ax^n, we return
    # a(n)x^(n-1)
    return (coeff * power *
            pow(val, power - 1))

list1 = ["x^4+2x^3-3", "4x^3+6x^2-6",
             "x^2+2x+3", "x^4+2x^3-2x^2+6"]

def derivativeVal(poly, val):

    ans = 0
    i = 0
    stSplit = poly.split("+")

    while (i < len(stSplit)):
        ans = (ans +
               derivativeTerm(stSplit[i],
                              val))
        i += 1

    return ans


# Driver code
if __name__ == "__main__":

    st = input("Enter correct polynomial(Like: 4x^3 + 3x^1 + 2x^2): ")
    val = 2
    
    print(random.choice(list1))
    print(derivativeVal(st, val))
