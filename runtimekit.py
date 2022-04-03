###########
#난해한 언어 키트
#이 키트는 퍼블릭 도메인에 의해 배포됩니다.
#수정하실 분은 수정하시고, 언제든 다른 언어로 번역하실 자원봉사자분들도 환영합니다!
#이 구문은 파이썬3으로 열어야 합니다.(파이썬2 이용시, input()->raw_input())
import sys
#줄 번호를 나타내는 변수
li=0
#파일 확장자 지정
fileext=""
#파일 확장자 에러 시 지정문구
fileexterror=""
#파일 맞는지 여부
file_correct=False
#파일 이름
filename=""
#필수 문구가 맞지 않으면 나타나는 에러
SEerror=""
#코드 리스트
command_list=[]
#처음/끝 필수 문구 지정
start=""
end=""
#변수 선언 구문 지정(ex. "정"으로 지정하면 "정"이 있어야만 변수로 읽힘)
v1=""
#포인팅 변수 지정(ex. "안"으로 지정하면 "안"이 몇개인지를 세어 ("안"의개수)번째 변수를 조작.리스트로 하는것을 추천.
v2=[]
#변수 리스트
var_list=[0]
#증가 연산자
add=""
#감소 연산자
sub=""
#곱하기 연산자
mul=""
#print문
printvar=""
#곱하기 연산자 지정
##################
#if문 정의 구문 사용법
#(변수1)(if문 정의 구문)(변수2)(같다면/아니라면 구문)(실행문)
#변수는 변수 선언과 포인팅 변수 지정구문에 따름.
#if문 정의 구문 지정
ifvar=""
#같다면 구문(if문 정의 구문 필수)
eqvar=""
#아니라면 구문(if문 정의 구문 필수)
notvar=""
#if문 오류시 메시지
iferror=""
#jump문 구문
jmp=""
#return(exit) 구문
ret=""
#exit 메시지
exitmsg=["",""]
#input 구문
inputvar=""
#문자열오류(문자는 표현 가능하지만, 문자열은 표현 불가능)
strerror=""
#형변환구문
casting=""
#무한루프 기준값
error=10000
#무한루프시 오류메시지
inflooperr=""
#####################
#v2 추가내용
#배열 변수 추가
#배열 뒤에 무언가를 추가하거나 삭제하는 함수
array_list=[[0]]
#배열 선언 문자
arrayvar=""
#배열 포인터 구분자
arraypointer=""
#배열 끝 구분자(자료 대입용)
EOA=""
#배열 원소 추가
concat=""
#배열 원소 제거
remove=""
#배열원소 제거 시 에러메시지(배열 길이가지충분하지 않을 때)
removeerror=""
#배열 원소 포인팅 에러
arraypointingerr=""
#시스템 인수 읽기
for j in range(len(sys.argv)):
    if fileext in sys.argv[j]:
        file_correct=True
        filename=sys.argv[j].split("\n")[0]
        break
#확장자 검사 구문
if not file_correct:
    print(fileexterror)
    sys.exit(1)
#메인구문
with open(filename,"r") as f:
    command_list=f.readlines()
    for c in range(len(command_list)):
        command_list[c]=command_list[c].split("\n")[0]
    if command_list[0]!=start or command_list[-1]!=end:
        print(SEerror)
        sys.exit(-1)
    while li<len(command_list):
        error-=1
        if error<0:
            print(inflooperr)
            sys.exit(3)
        cnt=0
        result=False
        code=command_list[li]
        for i in v2:
            cnt+=code.count(i)
        if arrayvar in code:
            try:
                while True:
                    if len(array_list)>cnt:
                        break
                    else:
                        array_list.append([0])
                cnt2=code.count(add)-code.count(sub)
                cnt4=0
                if arraypointer in code:
                    l,r=code.split(arraypointer)
                    point,right=r.split(EOA)
                    value=0
                    if mul in right:
                        right2=right.split(mul)
                        for rr in right2:
                            value*=rr.count(add)-rr.count(sub)
                    if mul in point:
                        point2=point.split(mul)
                        for rr in point2:
                            cnt3*=rr.count(add)-rr.count(sub)
                    for ii in v2:
                        cnt4+=l.count(ii)
                    cnt3=point.count(add)-point.count(sub)
                    if value==0:
                        value+=right.count(add)-right.count(sub)
                    array_list[cnt4][cnt3]+=value
                if remove in code:
                    del array_list[cnt][cnt2]
                elif concat in code:
                    array_list.append(cnt2)
            except ValueError:
                print(removeerror)
                sys.exit(-1)
            except IndexError:
                print(arraypointingerr)
                sys.exit(-2)
        if v1 in code:
            while True:
                if len(var_list)>cnt:
                    break
                else:
                    var_list.append(0)
            try:
                var_list[cnt]=int(var_list[cnt])
                if not mul in code:
                    var_list[cnt]+=code.count(add)-code.count(sub)
                else:
                    l,r=code.split(mul)
                    var_list[cnt]+=(l.count(add)-l.count(sub))*(r.count(add)-r.count(sub))
            except ValueError:
                a=ord(var_list[cnt])+code.count(add)-code.count(sub)
                if a>0:
                    var_list[cnt]=chr(a)
            li+=1
        if ifvar in code:
            l_,r_=code.split(ifvar)
            c_l=0
            c_r=0
            for i in v2:
                c_l+=l_.count(i)
                c_r+=r_.count(i)
            l=var_list[c_l]
            r=var_list[c_r]
            if l==r and eqvar in code:
                result=True
            elif l!=r and notvar in code:
                result=True
            elif not (notvar in code or eqvar in code ):
                print(iferror)
                sys.exit(2)
            if not result:
                li+=1
        if printvar in code:
            cnt=0
            for i in v2:
                cnt+=code.count(i)
        if casting in code:
            try:
                var_list[cnt]=int(var_list[cnt])
                if var_list[cnt]>0:
                    var_list[cnt]=chr(var_list[cnt])
            except ValueError:
                var_list[cnt]=ord(var_list[cnt])
        if inputvar in code:
            a=input()
            b=0
            for i in v2:
                cnt+=code.count(i)
            if a.isnumeric():
                b=int(a)
            elif len(a)==1:
                b=a
            else:
                print(strerror)
                sys.exit(3)
            var_list[cnt]=b
            li+=1
        if result:
            if jmp in code:
                code=code.split(jmp)[1]
                cnt=code.count(add)-code.count(sub)
                if cnt==0:
                    for i in v2:
                        cnt+=code.count(i)
                    cnt=var_list[cnt]
                    li=cnt
                else:
                    li=cnt
            if ret in code:
                cnt=code.count(add)-code.count(sub)
                if cnt==0:
                    for i in v2:
                        cnt+=code.count(i)
                    cnt=var_list[cnt]
                print(exitmsg[0]+str(cnt)+exitmsg[1])
                sys.exit(0)