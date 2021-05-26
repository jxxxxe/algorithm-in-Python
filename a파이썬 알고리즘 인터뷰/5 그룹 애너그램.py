#''.join(리스트) : 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 합쳐 반환
#'구분자'.join(리스트) : 리스트의 요소를 구분자로 이어서 하나의 문자열로 합쳐 반환
from collections import defaultdict
import sys

anagrams=defaultdict(list)

strs=sys.stdin.readline().split()

for str in strs:
    anagrams[''.join(sorted(str))].append(str)

print(anagrams.values())