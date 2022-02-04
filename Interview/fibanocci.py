def febanocci():
    a = 0
    b = 1
    temp = 0
    i=0
    while True:
        b = a + b
        a=b
        b=temp
        print(temp)
        print(f"*********{i}**")
        i+= 1


# febanocci()

def prime(a):

    for i in range(2,a):
        if a%i == 0:
            print("not prime")
            break
    else:
        print("prime")

