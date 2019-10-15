def diamond():
    n  = 5
    k = 1
    i = -1
    j = (n-1)/2
    while i < n-2:
        i = i + 2
        print((j-1) * " "),
        print(i * "*")
        j = j - 1
    i = i + 2
    print(i*"*")
    i = i - 2
    while i >= 1:
        print((k-1)*" "),
        print(i * "*")
        i = i - 2
        k = k+1


diamond()