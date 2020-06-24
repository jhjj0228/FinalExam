def Counting_pi(self, input):

    pi = 0
    sign = 1

    for i in range(1, input,2):

        pi += sign*(1 / (i))
        sign = -sign

    output = pi*4

    return output


if __name__ == '__main__':

    print ("i             m(i)")

    for k in range(1, 1000,100):
        print(("{}             {}").format(k, Counting_pi(k,10000)))
