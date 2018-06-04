# 과제1 - 맛집 고르기
# 구현내용
# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
# 힌트
# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.

import random
print("오늘의 맛집추천!")
KOREAN_FOOD = ("김치", "불고기", "된장찌개")
CHINIESE_FOOD = ("짜장면", "짬뽕", "탕수육")
JAPANECE_FOOD = ("초밥", "라멘", "덴뿌라")
food = input("한식, 중식, 일식 중 한가지를 골라주세요.\n")
if food == "한식":
    print(random.choice(KOREAN_FOOD))
elif food == "중식":
    print(random.choice(CHINIESE_FOOD))
elif food == "일식":
    print(random.choice(JAPANECE_FOOD))
else:
    print("다시 골라주세요~!")
