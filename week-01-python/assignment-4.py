# 과제 4 - 컴퓨터 공학도 기분을 내보자 2! 다이아몬드 그리기
# 구현 내용
# 아래 도형을 구현 합니다.
# 00100
# 01110
# 11111
# 01110
# 00100
# 도형을 설명하면 5x5 좌표에, 다이아몬드를 그리고 있습니다.
# 힌트
# 반복문(for-loop)을 사용해야 합니다.

# 1
# 11
# 111
# 1111
# 11111

# for a in range(1, 6):
#     print("1" * a)

# 10000
# 11000
# 11100
# 11110
# 11111

# for a in range(1, 6):
#     print("1" * a + "0" * (5 - a))

# 00100
# 01110
# 11111
# 01110
# 00100

for a in range(1, 6):
    a = a - 3
    if a < 0:
        a = -a
    print("0" * a + "1" * (5 - a * 2) + "0" * a)
