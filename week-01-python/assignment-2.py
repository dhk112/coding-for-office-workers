# 과제2 - 회사 조직도 만들기
# 구현 내용
# 사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# 직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.
# 힌트
# 클래스와 상속을 활용합니다.
# 사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때, 입력을 받을 수 있도록 합시다.
# 직장 동료의 기본 직급은 "대리"로 지정합니다.
# (고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서, 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.

### workers variables
# name1 = "DanielKIM"
# old1 = "31"
# gender1 = "남자"

# name2 = "Lisa"
# old2 = "29"
# gender2 = "여자"

### workers class with __init__
class Workers:

    def __init__(self, name, old, gender):
        self.name = name
        self.old = old
        self.gender = gender

worker1 = Workers("DanielKIM", "31", "남자")
worker2 = Workers("Lisa", "29", "여자")

# print(worker1.name)
# print(worker1.old)
# print(worker1.gender)
# print(worker2.name)
# print(worker2.old)
# print(worker2.gender)

### workers class inheritance
class CompanyWorkers(Workers):

    def __init__(self, name, old, gender, position):
        super().__init__(name, old, gender)
        self.position = position

company_workers1 = CompanyWorkers("DanielKIM", "31", "남자", "substitute")
company_workers2 = CompanyWorkers("Lisa", "29", "여자", "substitute")
# print(company_workers1.name)
# print(company_workers1.old)
# print(company_workers1.gender)
# print(company_workers2.name)
# print(company_workers2.old)
# print(company_workers2.position)
# print(company_workers2.gender)

print(company_workers1.__dict__)
print(company_workers2.__dict__)
