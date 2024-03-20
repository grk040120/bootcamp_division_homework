"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    number=int(input('12 이하의 자연수 입력 : '))
    s=1
    for i in range(1,number+1) :
        s=s*i

    print('{}! = {}'.format(number,s))


    return


if __name__ == '__main__':
    main()
