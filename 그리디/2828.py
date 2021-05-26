''' 
플레이어는 게임을 하는 중에 바구니를 왼쪽이나 오른쪽으로 이동할 수 있다. 
하지만, 바구니는 스크린의 경계를 넘어가면 안 된다. 가장 처음에 바구니는 왼쪽 M칸을 차지하고 있다.
*입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M < N ≤ 10) 둘째 줄에 떨어지는 사과의 개수 J가 주어진다. (1 ≤ J ≤ 20) 
다음 J개 줄에는 사과가 떨어지는 위치가 순서대로 주어진다.
*출력
모든 사과를 담기 위해서 바구니가 이동해야 하는 거리의 최솟값을 출력한다.
'''
#스크린길이:N, 바구니길이:M
#이동 거리는 M들의 뺄셈의 절대값
#바구니 길이로 커버치기-> 사과위치-현재위치의 절대값<=바구니길이면 이동안해도 됨

NM=list(map(int,input().split()))
J=int(input())
left=1
right=left+NM[1]-1
move=0
apple=[]

for i in range(J):
    apple.append(int(input()))
#바구니가 커버치는 구간: current~current+M-1 (길이M)
#사과가 바구니 앞/뒤로 떨어지는 경우 나눠서 생각

for i in range(J):
    if apple[i]<left:
        right-=left-apple[i]
        move+=left-apple[i]
        left=apple[i]
    elif apple[i]>right:
        left+=apple[i]-right
        move+=apple[i]-right
        right=apple[i]

print(move)

