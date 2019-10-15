N =int(input("Enter your amount: "))
a = N%200
b = a%50
c = b%10
d = c%5
e = d%25
n_200 = (N - (N % 200)) / (200)
n_50 = (a - (a % 50)) / (50)
n_10 = (b - (b % 10)) / (10)
n_5 = (c - (c % 5)) / (5)
n_2 = (d - (d % 2)) / (2)
n_1 = (e - (e % 1)) / (1)
total =  n_1 + n_2 +n_5 +n_10 + n_50 +n_200
if a == 0:
    print(f"{total} notes")
else:
    if b== 0:
        print(f"{total} notes")
    else:
        if c==0:
            print(f"{total} notes")
        else:
            if d==0:
                print(f"{total} notes")
            else:
                if e==0:
                    print(f"{total} notes")
                else:
                    print(f"{total} notes")



