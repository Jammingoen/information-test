#1. 컴퓨터 프로그래밍 __ p.110
#1 프로그램: 문제를 해결하기 위한 처리방법과 순서를 논리적으로 정리하여 컴퓨터에서 실행될수 있는 명령문의 집합으로 구성한 것

#생활속의 다양한 프로그램
#컴퓨터: 우리 생활속에서 다양하게 활용할수있는 프로그램
#스마트 워치: 몸 상태를 확인할수있는 프로그램
#스마트폰: 전화나 메시지를 이용할수있는 프로그램
#자율주행 자동차: 목적지까지 스스로 찾아가는 프로그램
#2 프로그램을 만드는 과정

#문제 이해하고 분석하기
#알고리즘 설계하기
#프로그램 작성하고 실행하기
#수정 및 보완하기
#3 프로그램 언어

#번역 프로그램: 작성된 프로그램을 컴퓨터가 이해할 수 있는 기계 언어로 변환시켜주는 프로그램
#컴파일러 방식: 프로그램을 실행할꺠 모든 코드를 한꺼번에 번역하여 실행하는 방식
#인터프리터 방식: 코드를 할줄씩 번역하여 실행하는 방식

#1 파이선(Phton): 초보자부터 전문가까지 다양한 사람들이 사용하는 텍스트 기반 프로그래밍 언어(텍스트 기반 프로그래밍 언어)

#파이선(Python)을 배오고 사용하기 쉬운 언어이다.
#파이선은 바로 사용이 가능한 명령어들이 많이 저장된 언어이다.
#파이선은 다양한 프로그램을 만들 수 있는 강력한 언어이다.

#import ColabTurtlePlus.Turtle as turtle   #코랩은 웹 환경에서 작동하기에 윈도우에 직접 설치해서 실행시키는 방법과 다르게 모듈을 다룬다.
import turtle   # jupyter notebook, visual studio code, python 에서는 import turtle 로 모듈 불러 오기
turtle.clearscreen()

t=turtle.Turtle() # 거북이 만들기

t.forward(100)      # 거북이 전진하기, 단위:픽셀
t.left(90)        # 왼쪽으로 90도 회전하기
t.forward(100)
t.left(90)

#그리지 않고 움직이기
turtle.initializeTurtle()

t.forward(50)
t.left(90)
t.penup()       #펜을 들어 그리지 않도록 한다.
t.forward(50)
t.right(90)
t.pendown()     #펜을 내려 그리기 시작한다.
t.forward(50)

# 정사각형 그리기
turtle.initializeTurtle()

t.forward(80) # 한 변의 길이를 설정
t.left(90)    # 정사각형의 한 내각의 크기만큼 왼쪽을 회전하기
# 정각형의 나머지 부분을 그리는 코드를 아래에 작성하여 그림을 완성해 보세요.

t.forward(80) # 한 변의 길이를 설정
t.left(90)
t.forward(80) # 한 변의 길이를 설정
t.left(90)
t.forward(80) # 한 변의 길이를 설정
t.left(90)
t.forward(80) # 한 변의 길이를 설정
t.left(90)

# 하나의 캔버스에 2개의 거북이로 도형 그리기
turtle.initializeTurtle()

t1 = turtle.Turtle()      # t1이라는 이름의 거북이 준비
t2 = turtle.Turtle()      # t2라는 이름의 거북이 준
t2.left(180)              # t2 거북이의 방향을 180도 돌려서 뒤를 바라보게 설정
t1.forward(200)
t2.forward(100)     #변의 길이
t1.right(120)       #각도는 원하는 180-(원하는 도형 내각)
t2.right(120)
# 정삼각형의 나머지 부분을 그리는 코드를 아래에 작성하여 그림을 완성해 보세요.
t1.forward(200)
t2.forward(100)
t1.right(120)
t2.right(120)
t2.forward(100)
t2.right(120)
t2.forward(100)
t1.forward(200)

# 색 바꾸기
# 색 이름 이용하기
turtle.initializeTurtle()

t.color('skyblue')  #색을 녹색으로 지정
t.circle(50)    #반지름이 50인 원 그리기

# RGB 색상 비율 이용하기
# color(0,0,0) ~ color(255,255,255): color(Red,Green,Blue), 0: 불끔. 255.가잘 밝은 빛을 냄
# import turtle 에서는 0~1 값으로 빛의 밝기를 정함.

turtle.initializeTurtle()

t.color(128, 0, 0)
t.forward(100)
t.left(90)
t.color(255, 0, 0)
t.forward(100)
t.left(90)
t.color(0, 128, 255)
t.forward(100)
t.left(90)
t.color(128, 128, 128)
t.forward(100)
t.left(90)

#RGB 색상값 이용
# "#000000" ~ "#ffffff": R-16진수 두자리, G-16진수 두자리, B-16진수 두자리
# 10진수-16진수: 10-a, 11-b, 12-c, 13-d, 14-e, 15-f, ... 254-fe, , 255-ff
turtle.initializeTurtle()

t.color("#ff0000")#빨간색
t.forward(100)
t.left(120)
t.color("#00ff00")#연두색
t.forward(100)
t.left(120)
t.color("#90cdaa")#어두운초록색
t.forward(100)
t.left(120)

# 도형 색칠하기
turtle.initializeTurtle()

t.color('orange')
t.begin_fill()#채우기끝
t.circle(50)
t.end_fill()#채우기끝