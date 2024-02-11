#설탕배달

#(시행착오1)단순히 나머지x 5와 3으로 딱 나누어 떨어지게 만들어야 하므로
#(시행착오2)5로 나눈 나머지에 따라 값을 정하기... 시도는 좋았으나 XXX

while True:
    N = int(input())
    if N < 3 or N > 5000:
        print("입력하는 수의 범위는 3 이상 5000 이하 입니다. 다시 입력해주세요")
        continue
    break

count = 0
x = N
i = N//5  # 5로 나눌 때 몫
#5로 나누고 나머지가 1이상일때 3으로 나누어 떨어질때까지 5로 나눈 몫을 낮추어 3으로 나누기를 시도한다.

while x > 0 or i >= 0:
    x = N-(5*i)  # 3이 처리해야할 값(=5로 나눈 나머지)
    if x == 0:
        count = i
        break
    elif x % 3 == 0:
        count = i+(x//3)
        break
    i -= 1

if i < 0:
    count = -1

print(count)