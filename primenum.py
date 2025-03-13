def primes():
    n = 2
    while True:
        flag = 1
        for i in range(2,n):
            if n % i == 0:
                flag = 0
                break
        if(flag):
            yield n
        n+=1 

primes = primes()
print([next(primes) for _ in range(10)])

lst = [0,3,5,23,4,6,32,5,46,8]

even = list(filter(lambda x :  x % 2 == 0 , lst))
even = [x for x in lst if x % 2 == 0]

print(even)