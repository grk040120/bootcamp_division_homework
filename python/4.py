"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    score=int(input("점수 : "))
    if score >= 90 :
        grade='A'
    elif score >= 80 : 
        grade='B'
    elif score >= 70 :
        grade='C'
    elif score >= 60 :
        grade='D'
    else :
        grade='F'
    print('등급 : ', grade)

    return


if __name__ == '__main__':
    main()
