def resolve():
    '''
    code here
    '''
    S = input()
    
    is_1st = False
    if S[2] == S[3]:
        is_1st = True

    is_2nd = False
    if S[4] == S[5]:
        is_2nd = True

    is_ans = False
    if is_1st and is_2nd:
        is_ans = True
    
    print('Yes') if is_ans else print('No')
    
if __name__ == "__main__":
    resolve()
