#<데이터 전처리(Preprocessing) for 데이터 클렌징>
#문자열 바꾸기 => re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)  //횟수는 생략가능ㄴ
#패턴에 '[^]'사용하면 해당 패턴을 만족하지 않는 문자열들을 대상으로 할 수 있음
#.lower().split() => 문자열을 소문자로 바꾼 후에 단어로 쪼갬
#word for word in re.sub().lower().split() if word not in banned => banned에 없는 단어 중에 ~~
#re.sub('[^a-e0-9]',,) => 영소문자, 숫자 빼고
#re.sub(r'[^\w]') =>알파벳대소문자, 숫자 빼고 => ^[0-9a-zA-Z]와 동일
#앞에 r을 사용하는 이유: 이스케이프방지 => \를 한번만 적어도 되게 함

#<Counter로 개수 처리하기>
#collections에 Counter(리스트)
#리스트의 요소 개수를 값과 함께 튜플로 묶어서 딕셔너리로 반환한다. => 당연히 중복 값은 하나로 해줌
#counter.most_common(개수) => 개수만큼 가장 개수가 많은 값을 튜플 형식으로 반환

