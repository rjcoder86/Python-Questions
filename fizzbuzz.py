def myfizzBuzz(self, n: int) -> list[str]:
    l = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            l.append('FizzBuzz')
        elif i % 3 == 0:
            l.append('Fizz')
        elif i % 5 == 0:
            l.append('Buzz')
        else:
            l.append(str(i))
    return l


def fizzbuzz(n):
    list_of_output = ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,n+1)]
    return list_of_output

print(fizzbuzz(15))
