"""class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + "가 짖습니다!")

my_dog = dog("뽀삐","골든 리트리버")

my_dog.bark()"""

# 실습과제 1

class 붕어빵:
    def __init__(self, name):
        self.name = name

    def 팔다(self):  # def 명령어를 사용해 함수를 생성
        print(self.name + " 붕어빵이 판매되었습니다.")

    def 먹다(self):
        print(self.name + " 붕어빵을 먹습니다.")

# 겍체생성
붕어빵맛 = 붕어빵(input("붕어빵의 맛을 입력하세요: ")) # input 함수를 이용해 매개변수를 사용자에게 입력 받도록 설정 후 객체에 저장

# 명령어 사용
붕어빵맛.팔다() # 함수 사용
붕어빵맛.먹다()


# ---------------- 실습과제 2 ----------------

class 붕어빵:
    def __init__(self, 이름, 가격, total=0): # 이름, 가격, 총합을 받는 매개변수 생성후 self 매개변수을 사용
        self.이름 = 이름
        self.가격 = 가격
        self.total = total

    def 팔다(self): #  def를 이용하여 팔다 라는 함수 생성
        print(self.이름 + "을 " + str(self.가격) + "에 팔았습니다.") # 자료타입이 다르므로 str함수를 이용하여 정수형 자료형을 문자형 자료형으로 변환 후 문자를 결합
            self.total = self.total + self.가격 # 입력받은 붕어빵의 가격을 total에 저장

# 객체 생성
팥 = 붕어빵("팥붕어삥", 1000)
슈크림 = 붕어빵("슈크림붕어빵", 1500)

# 명령어 사용
팥.팔다()
팥.팔다()
print(팥.total)


# ---------------- 추가 문제 ----------------

class 교수님:                          # class 명령어 이용해 교수님 이라는 클래스 생성
    def __init__(self, 학번, 이름):    # 매개변수를 객체에 데이터로 저정하는 __init__ 함수 사용, 매개변수 입력 후 self 객체 내의 속성 및 함수에 접근
        self.학번 = 학번               # 각 매개변수에 객체 생성
        self.이름 = 이름

    def 수업이(self):                  # def 명령어를 이용해 '수업이' 라는 함수 생성
        print("안녕하십니까 교수님 " + self.학번 + "_" + self.이름 + "이라고 합니다. 수업 내용은 어렵지만 그래도 재밌습니다!") # print 명령어로 출력값 출력

# 객체 생성
학번 = input("학번을 입력해주세요: ") # input : 사용자로부터 입력값을 받는 함수
이름 = input("이름을 입력해주세요: ")
클래스호출객체 = 교수님(학번, 이름)

# 메소드 호출
클래스호출객체.수업이()
