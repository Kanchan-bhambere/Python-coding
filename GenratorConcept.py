def prime_genrator(n):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,(int(num ** 0.5)+1)):
            if num % i==0:
                return False
        return True

    count=0
    num=2
    while count<n:
        if is_prime(num):
            yield num
            count += 1
        num+=1

prime_gen = prime_genrator(int(input("enter number: ")))
for i in prime_gen:
    print(i)

