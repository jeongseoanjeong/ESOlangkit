# ESOlangkit
난해한 언어 키트(파이썬 구현)
License: Public domain License. free to use!
# HOW TO USE(For english users)
imagine code is any line of script.
## You must not to change value of these.
1. li:integer
2. file_correct:boolean
3. var_list:list of integers or characters.
## Operator
1. (IMPORTANT) YOU Need to use Python 3. but if you don't want, fix input() to raw_input() or etc.
2. fileext:String
   * example: ".jsc" => then it finds file that has ".jsc" in file.
3. v1:String
  * if code includes v1's value, it'll read as an variable.
4. v2:list of string
  * if code includes v2's value, it'll move pointers of variables
  * (ex. if v1="h" and v2=["a"] then the variable aaaaah gets fifth variable in variable list.)
  * (it can be one or more values...)
5. start:string
  * if script is not start with start's value, this will be error.
6. end:string
  * if script is not end with end's value, this will be error.
7. add:String
  * if code includes add's value,and code includes variable, then variable is variable + 1 (can be used with pointing)
  * it can be used for jump function.
8. sub:String
  * if code includes sub's value,and code includes variable, then variable is variable - 1 (can be used with pointing)
  * it can be used for jump function,but it must bigger than 0.
9. mul:String
  * if code includes mul's value, then this will split into two of these and multiplies value of left and right and adds into variables pointing.
10. printvar:string
  * if code include printvar's value, then it'll print variables (with pointing)
11. ifvar:string
  * if code includes ifvar's value, then it'll compare variables.
  * if this code includes 
    * eqval's value: execute commands after this code if values are equal.
    * notvar's value: execute commands after this code if values are __not__ equal
12. eqvar:String
13. notvar:string
14. jmp:string
  * if code includes jmp's value, this will be jump into line (add's count)-(sub's count) __or__ variables .
15. ret:string
  * if code includes ret's value this will be
16. exitmsg:list of two Strings
  * initially it is composed two strings, but you can add more or just one string, but you need to fix code.
17. inputvar:string
  * if code includes inputvar's value, it will scan input into variables.
  * but if input is string, this will be error.
18. casting:string
  * if code includes casting's value, variable's type will be switched int to char or char to int by using ASCII code 
19. error:integer
  * default setting is 10000, but you can increase or decrease this value.
## error messages
1. fileexterror:String 
  * if extensions of file is not correct,then this error will be thrown.
2. SEError:strin
  * if code is not starts with variable "start" or not ends with variable "end",then this error will be thrown.
3. strerror:string
  * this runtime only handles char and integer variables. but type of variable is string,then this error will be thrown.
4. inflooperr:string
  * if program loops over (error's value) times then this error will be thrown
# Examples:
  ```python
###########
#난해한 언어 키트
#이 키트는 퍼블릭 도메인에 의해 배포됩니다.
#수정하실 분은 수정하시고, 언제든 다른 언어로 번역하실 자원봉사자분들도 환영합니다!
#이 구문은 파이썬3으로 열어야 합니다.(파이썬2 이용시, input()->raw_input())
import sys
#줄 번호를 나타내는 변수
li=0
#파일 확장자 지정
fileext=".jslang"
#파일 확장자 에러 시 지정문구
fileexterror="파일불안"
#파일 맞는지 여부
file_correct=False
#파일 이름
filename=""
#필수 문구가 맞지 않으면 나타나는 에러
SEerror="걍 정서불안"
#코드 리스트
command_list=[]
#처음/끝 필수 문구 지정
start="#정서안정"
end="#정서불안"
#변수 선언 구문 지정(ex. "정"으로 지정하면 "정"이 있어야만 변수로 읽힘)
v1="정"
#포인팅 변수 지정(ex. "안"으로 지정하면 "안"이 몇개인지를 세어 ("안"의개수)번째 변수를 조작.리스트로 하는것을 추천.
v2=["아","안"]
#변수 리스트
var_list=[0]
#증가 연산자
add="<"
#감소 연산자
sub=">"
#곱하기 연산자
mul=""
#print문
printvar="트롤"
#곱하기 연산자 지정
##################
#if문 정의 구문 사용법
#(변수1)(if문 정의 구문)(변수2)(같다면/아니라면 구문)(실행문)
#변수는 변수 선언과 포인팅 변수 지정구문에 따름.
#if문 정의 구문 지정
ifvar="가천"
#같다면 구문(if문 정의 구문 필수)
eqvar="?"
#아니라면 구문(if문 정의 구문 필수)
notvar="!"
#if문 오류시 메시지
iferror="복정 잡대"
#jump문 구문
jmp="연세"
#return(exit) 구문
ret="귀찮다"
#exit 메시지
exitmsg=["다 귀찮음[","]"]
#input 구문
inputvar="입"
#문자열오류(문자는 표현 가능하지만, 문자열은 표현 불가능)
strerror="너무 길어 정서불안"
#형변환구문
casting="불"
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
        cnt=0
        result=False
        code=command_list[li]
        for i in v2:
            cnt+=code.count(i)
        if v1 in code:
            while True:
                if len(var_list)>cnt:
                    break
                else:
                    var_list.append(0)
            if str(var_list[cnt]).isdigit():
                if not mul in code:
                    var_list[cnt]+=code.count(add)-code.count(sub)
                else:
                    l,r=code.split(mul)
                    var_list[cnt]+=(l.count(add)-l.count(sub))*(code.count(add)-code.count(sub))
            else:
                var_list[cnt]=chr(ord(var_list[cnt])+code.count(add)-code.count(sub))
            
        if ifvar in code:
            l_,r_=code.split(ifvar)
            c_l=0
            c_r=0
            for i in v2:
                c_l+=l.count(i)
                c_r+=l.count(i)
            l=var_list[c_l]
            r=var_list[c_r]
            if l==r and eqvar in code:
                result=True
            elif l!=r and notvar in code:
                result=True
            elif not (notvar in code or eqvar in code ):
                print(iferror)
                sys.exit(2)
        if printvar in code:
            for i in v2:
                cnt+=code.count(i)
            print(var_list[cnt])
        if casting in code:
            if str(var_list[cnt]).isdigit():
                var_list[cnt]=chr(var_list[cnt])
            else:
                var_list[cnt]=ord(var_list[cnt])
        if inputvar in code:
            a=input()
            b=0
            for i in v2:
                cnt+=code.count(i)
            if a.isdigit():
                b=int(a)
            elif len(a)==1:
                b=a
            else:
                print(strerror)
                sys.exit(3)
            var_list[cnt]=b
        if result:
            if jmp in code:
                cnt=code.count(add)-code.count(sub)
                if cnt==0:
                    for i in v2:
                        cnt+=code.count(i)
                    cnt=var_list[cnt]
                else:
                    i=cnt
            if ret in code:
                cnt=code.count(add)-code.count(sub)
                if cnt==0:
                    for i in v2:
                        cnt+=code.count(i)
                    cnt=var_list[cnt]
                else:
                    i=cnt
                print(exitmsg[0]+str(cnt)+exitmsg[1])
                sys.exit(0)
        li+=1
   ```
in script file:
```
#정서안정
입정
트롤정
불정
트롤정
#정서불안
```
this will be printed
```
a
a
97
```
# Contact me
if you're hard to make your own code,or have an idea or contact me,etc...(Thanks! No problem!) -> go to https://discord.gg/PUHW5tsjtY
