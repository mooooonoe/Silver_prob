# 16120 PPAP

# ppap 문자열 p에서 시작하여 문자열 내의 p를 ppap 로 바꾸는 과정을 반복하여 만들 수있는 문자열

def check(str_i):
    stack = []
    ori = 'PPAP'

    for char in str_i:
        stack.append(char)
        if ''.join(stack[-4:]) == ori:
            del stack[-4:]
            stack.append('P')

    result = ''.join(stack)
    return result


str_i = input()
result = check(str_i)

if result=='P':
    print('PPAP')
else:
    print('NP')
