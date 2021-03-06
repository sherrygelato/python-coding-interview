# python-coding-interview

> 3/21 (mon)

<br/>

# 문자열 조작

<br/>

## # 문자열 조작
- 문자열을 변경하거나 분리하는 등의 여러 과정을 뜻함
- 문자열 자료형과 문자열을 조작하기 위한 다양한 기능들이 있음
> #### 문자열 처리와 관련된 대표적인 분야
> - 정보처리 분야 : 키워드로 웹 페이지 탐색
> - 통신 시스템 분야 : 문자 메시지나 이메일 등 데이터 전송
> - 프로그램 시스템 분야 : 컴파일러나 인터프리터 등은 문자열을 해석하고 처리하여 기계어로 변환함

<br/><br/>

# 01. 유효한 팰린드롬 [Valid palindrome](https://leetcode.com/problems/valid-palindrome/)
주어진 문자열이 팬린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

<br/>

## # '팰린드롬'이란?
- 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장
- 회문이라고도 부름
- 예) '소주 만 병만 주소'

<br/>

### # 예제 1
- 입력
```"A man, a plan, a canal: Panama"```
- 출력
```True```

### # 예제 2
- 입력
```"race a car"```
- 출력
```False```

<br/><br/>

# 02. 문자열 뒤집기 [Reverse String](https://leetcode.com/problems/reverse-string/)
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

<br/>

### # 예제 1
- 입력
```["h", "e", "l", "l", "o"]```
- 출력
```["o", "l", "l", "e", "h"]```

### # 예제 2
- 입력
```["H", "a", "n", "n", "a", "h"]```
- 출력
```["h", "a", "n", "n", "a", "H"]```

<br/><br/>

# 03. 로그파일 재정렬 [Reorder Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

<br/>

### # 예제 1 
- 입력
```logs = ["digl 8 1 5 l","letl art can","dig2 3 6","let2 own kit dig","let3 art zero"]```
- 출력
```["letl art can%"let3 art zero","let2 own kit dig","digl 8 1 5 l","dig2 3 6"]```

<br/><br/>

## # 문법 : + 연산자 동작
- 문자열 값이 차례대로 이어진다.

```
a = [1, 2, 3]
b = [4, 5, 6]

a + b
> [1, 2, 3, 4, 5, 6]

b + a
> [4, 5, 6, 1, 2, 3]
```

<br/><br/>

## # 문법 : 람다 표현식
- 식별자 없이 실행 가능한 함수로, 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현 가능하다.

- sorted()로 정렬
    ```python
    s = ['2 A', '1 B', '4 C', '1 A']

    sorted(s)
    > ['1 A', '1 B', '2 A', '4 C']
    ```

- 그러나 우리가 원하는 결과는, 각 요소의 변호 순 정렬이 아닌 그 뒤의 문자 순 정렬을 원함
- 즉, 문자가 동일한 경우에만 그 앞 번호순으로 정렬되는 형태를 희망
- 이때 리스트의 각 요소를 풀어서 별도 처리해줘야 하는데, 이 때 람다 표현식을 사용한다.
- 람다는 간단한 함수를 쉽게 선언하는 방법이다.

- 람다를 사용하지 않고 직접 함수를 선언한다면
    ```python
    def func(x):
        return x.split()[1], x.split()[0]

    s.sorted(key=func)
    s
    > ['1 A', '2 A', '1 B', '4 C']
    ```

- 람다 표현식을 사용한다면
    ```python
    s.sort(key=lambda x: (x.split()[1], x.split()[0]))
    ```
    - 주의 : 코드가 길어지고, map이나 filter와 함께 섞어서 사용하면 가독성이 매우 떨어진다.

<br/><br/>

# 04. 가장 흔한 단어 [Most Common Word](https://leetcode.com/problems/most-common-word/)
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

<br/>

### # 예제 1 
- 입력
```paragraph = "Bob hit a ball, the hit BALL flew far after it was hit. banned = ["htt"]```
- 출력
```“ball"```

<br/><br/>

# 05. 그룹 애너그램 [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

<br/>

### # 예제 1 
- 입력
```["eat", ''tea", "tan", "ate", ''nat', “bat"]```
- 출력
```[["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]```

<br/>

### # 참고 : '애너그램'이란 
- 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
- 다른 말 : 어구전철
- 예) 문전박대 -> 대박전문

<br/><br/>

### # 여러 가지 정렬 방법
1. sorted()
- 리스트 정렬
    ```python
    a = [2, 5, 1, 9, 7]

    sorted(a)
    > [1, 2, 5, 7, 9]
    ```
- 문자열 정렬
    ```python
    b = 'zdaf'

    sorted(b)
    > ['a', 'b', 'd', 'f', 'z']

    # 다시 문자열로 결합
    "".join(sorted(b))
    > 'abdfz'
    ```
- key=옵션으로 정렬 위한 키 또는 함수를 별도로 지정 할 수 있다.
    ```python
    c = ['ccc', 'aaaa', 'd', 'bb']

    sorted(c, key=len)
    > ['d', 'bb', 'ccc', 'aaaa']
    ```
- 함수 이용해 키를 정의하는 방법
    ```python
    d = ['cde', 'cfc', 'abc']

    def fn(s):
        return s[0], s[-1]

    print(sorted(d, key=fn))
    > ['abc', 'cfc', 'cde']
    ```
    ```python
    d = ['cde', 'cfc', 'abc']

    sorted(a, key=lambda s: (s[0], s[-1]))
    > ['abc', 'cfc', 'cde']
    ```
2. sort() : 리스트 자체 정렬, In-place Sort 제자리 정렬
- 입력을 출력으로 덮어 쓰기 때문에 별도의 추가 공간이 필요하지 않으며, 리턴값이 없다.
    ```python
    alist.sort() # 리스트 자체를 제자리 정렬
    ```

<br/>

### # 파이썬 : 정렬 알고리즘과 팀소트
- 가장 인기 있는 정렬 알고리즘 : 존 폰 노이만이 설꼐한 병합 정렬 (Merge sort)
    - 퀵 정렬이 데이터에 따라 편차가 큰 반면, 병합 정렬은 일정하게 O(n log n)의 안정적인 성능을 보임
    - 안정 정렬(Stable Sort)
- 파이썬의 정렬 : Timsort 팀소트를 사용함
    - '실제 데이터는 대부분 이미 정렬되어 있을 것이다'라고 가정하고 실제 데이터에서 고성능을 낼 수 있게 설계한 알고리즘
    - 데이터가 엉망으로 뒤죽박죽 섞여 있는 일은 없을 거라 가정
    - 삽입 정렬과 병합 정렬을 휴리스틱하게 적절히 조합했다.
- 정렬이 필요 시 대부분의 경우 파이썬의 정렬 함수를 사용하는 것이 가장 빠르다. 파이썬의 내장 함수로서 저수준의 언어를 이용해 신중하게 작성되었기 때문이다. 
- 병합 정렬과 퀵 정렬을 제치고 현업에서 가장 널리 쓰이는 정렬 알고리즘이다.

<br/><br/>

# 06. 가장 긴 팰린드롬 부분 문자열 [Longest Palindrome Substring](https://leetcode.com/problems/longest-palindromic-substring/)
가장 긴 팰린드롬 부분 문자열을 출력하라.

<br/>

### # 예제 1
- 입력
```"babad"```
- 출력
```"bab", "aba"```

### # 예제 2
- 입력
```"cbbd"```
- 출력
```"bb"```

<br/><br/>

### # 유니코드와 UTF-8
- ASCII 인코딩 : 초기에 문자를 표현, 1바이트에 모든 문자 표현, 1비트는 체크섬으로 제외하여 7비트(128글자)로 문자 표현.
    - 한글, 한자와 같은 문자는 2개 이상의 특수 문자를 합쳐서 표현
- 유니코드 : 2~4바이트 공간에 여유있게 문자를 할당하고자 함
    - 1바이트로 표현 가능한 영문자도 2바이트 이상의 공간 사용으로 메모리 낭비가 심하다
- UTF-8 : 가변 길이 문자 인코딩 방식
- 파이썬 3부터 문자열이 모두 유니코드 기반으로 전환됐다. 다국어 출력하는데 아무런 불편함이 없다.

<br/>

### # 파이썬 : 유니코드 인코딩
- 인덱스를 통해 개별 문자에 접근하기 어렵기 때문에 파이썬 내부적으로 UTF-8 인코딩을 사용하지 않는다.
- 각 문자열에 포함된 문자 범위에 따라 서로 다른 고정 인코딩 방식을 선택하여, 내부적으로 파이썬은 문자열 슬라이싱을 포함한 원하는 인덱스에 빠르게 접근할 수 있게 한다.