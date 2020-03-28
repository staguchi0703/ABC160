def resolve():
    '''
    code here
    '''
    X = int(input())
    res = (X//500)*1000
    X -= (X//500)*500
    res += (X//5)*5

    print(res)

if __name__ == "__main__":
    resolve()
