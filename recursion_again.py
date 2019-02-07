'''
def recurse(cnt):
    if cnt == 5:
        return

    print(cnt)
    recurse(cnt+1)
    print(cnt) //when recurse return, this line works

cnt = 1
def recurse():
    global cnt //if cnt don't declare globally, recurse() function will exceed the limit of stack memory
    if cnt > 5:
        return

    print(cnt)
    cnt += 1
    recurse()

def fib(n):
    if(n==1 or n==2):
        return 1

    return fib(n-1) + fib(n-2)

f = [0 for x in range(50)]
def fibo(n):
    global f
    if f[n] != 0:
        return f[n]

    if(n==1 or n==2):
        return 1
    f[n] = fibo(n-1) + fibo(n-2)
    return f[n]
s = 0
def sm(n):
    global s
    if n==0:
        return

    s += n
    sum(n-1)
    return s
'''

if __name__ == "__main__":
    n = int(input("n: \n"))
    print(sum(n))
