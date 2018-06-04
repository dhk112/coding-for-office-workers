# 미니 과제 2. 클래스 만들어 보기\
# 방금 배운 클래스를 복습해 봅시다.
# 학교 클래스를 만들어주세요.
# 학교 클래스는 이름, 설립연도, 주소라는 정보를 가지고 있어야 합니다.
# 클래스를 활성화 할 때, 위의 3가지 데이터를 반드시 입력하도록 처리해 봅시다.

##### learn variables
school = "ABCcollege"
Establish = "1988"
address = "Seoul"
view_count = 0

# class Learn:
#     school = "ABCcollege"
#     Establish = "1988"
#     address = "Seoul"
#     view_count1 = 0

# learn1 = Learn()
# print(article1.school)
# learn2 = Learn()
# print(learn2.Establish)
# learn3 = Learn()
# print(learn3.address)

# learn1.school = "University"
# print(learn1.school)
# print(learn2.school)

##### Lrean class with__init__
class Learn:
    Establish = "1988"
    view_count = 0

    def __init__(self, school, address):
        self.school = school
        self.address = address

    def read(self):
        self.view_count = self.view_count + 1

learn = Learn("ABCcollege", "Seoul")

# print(learn.view_count)
# learn.read()
# print(learn.view_count)

##### learn class inheritance 속성 복습
class CodingClass(Learn):
    name = "DanielK"

    def read(self):
        self.view_count = self.view_count + 5

coding_class = CodingClass("ABCcollege", "Seoul")
print(coding_class.school)
print(coding_class.name)
print(coding_class.view_count)
coding_class.read()
print(coding_class.view_count)
