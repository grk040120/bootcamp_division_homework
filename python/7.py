"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    year=int(input('연도 입력 : '))
    month=int(input('월 입력 : '))
    if month==4 or month==6 or month==9 or month==11 :
        days=30
    if month==2:
        if (year%4==0 and year%100!=0) or year%400==0 :
             days=29
        else :
            days=28
    else :
        days=31
    print(days)

    return


if __name__ == '__main__':
    main()
