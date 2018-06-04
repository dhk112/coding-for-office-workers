import random
#미니 과제 1. 랜덤뽑기

# * 개발자에게 필수적인 구글 검색(구글링) 능력을 키워봅시다.
# * 리스트나 튜플에서 임의로 하나의 값을 뽑으려면 어떻게 해야할까요? 
# * [1, 2, 3, 4, 5] 라는 리스트 중에 임의의 값을 하나 뽑아주세요.
# * 필수 과제는 아닙니다.
# * 다 하신 분은 채팅방에 결과 공유해주세요 :)

# 답 : https://docs.python.org/2/library/random.html?highlight=choice#random.choice

# random.choice([1, 2, 3, 4, 5])
# 1, 2, 3, 4, 5 중에 하나의 값을 리턴한다.

print(random.choice([1, 2, 3, 4, 5]))

# random.randint(1, 5)
# 1 이상 5이하의 정수(int)를 리턴한다.
# random, randrange 함수와는 달리 마지막 숫자가 포함되는 것이 특이하다.
#import random
# random.randint([1, 2, 3, 4, 5])
