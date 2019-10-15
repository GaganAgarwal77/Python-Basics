def diamond(n,c):
    k = 1
    i = -1
    j = int((n-1)/2)
    while i < n-2:
        i = i + 2
        print((j-1) * " "),
        print(i * c)
        j = j - 1
    i = i + 2
    print(i*c)
    i = i - 2
    while i >= 1:
        print((k-1)*" "),
        print(i * c)
        i = i - 2
        k = k+1


diamond()