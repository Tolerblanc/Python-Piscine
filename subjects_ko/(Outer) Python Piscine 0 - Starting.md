# Subject 번역

## General Rules

-   VM을 사용하여 클러스터 컴퓨터에서 모듈을 렌더링해야 합니다.
    -   가상 머신에 사용할 OS를 선택할 수 있습니다.
    -   가상 머신에 프로젝트를 구현하는 데 필요한 모든 소프트웨어가 있어야 합니다. 이 소프트웨어를 구성하고 설치해야 합니다.
-   또는 도구를 사용할 수 있는 경우, 컴퓨터에 직접 설치할 수 있습니다.
    -   세션에 필요한 모든 모듈을 설치할 수 있는 공간이 있는지 확인합니다. (캠퍼스에 있는 경우 goinfre 사용)
    -   평가 전에 모든 모듈을 설치해야 합니다.
-   함수들은 예상치 못하게 종료되면 안됩니다. (segmentation fault, bus error, double free 등) 예상치 못한 종료가 일어난다면, 당신의 프로젝트는 비 기능적인 것으로 간주되며 0점을 받게 됩니다.
-   프로젝트에 대한 테스트 프로그램을 만드는 것을 강력 권장합니다.
    -   제출할 필요가 없고, 채점되지 않습니다.
    -   이렇게 하면 자신의 작업과 동료의 작업을 쉽게 테스트할 수 있습니다. 특히, 디펜스 시 유용합니다.
    -   실제로 디펜스 하는 동안, 자신의 테스트 및 평가하는 동료의 테스트를 자유롭게 사용할 수 있습니다.
-   당신의 모든 작업을 git 레포지토리에 제출하세요. git 레포지토리에 제출된 작업물만 점수를 받을 수 있습니다. 만약 Deepthought이 작업물을 채점하게 되어있다면, 동료평가를 마친 뒤 자동으로 채점될 것입니다. Deepthought은 작업물의 에러를 발견한 순간 채점을 중지합니다.
-   반드시 `Python 3.10` 을 사용해야 합니다.
-   각 예제에서 금지되지 않은 모든 빌트인 함수를 사용할 수 있습니다.
-   모든 라이브러리 import는 명시적이여야 합니다.
    -   `import numpy as np` 형식으로 사용해야 하며,
    -   `from pandas import *` 와 같은 형식은 허용되지 않습니다.
    -   허용되지 않은 import 형식을 사용할 경우, 0점을 받게 됩니다.
-   전역 변수를 사용해서는 안됩니다.

## Ex 00

> `ex00/Hello.py`로 제출.
>
> 허용 함수 없음

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

위 코드에서 각 자료형 안에 들어있는 문자열을 수정하여, 아래와 같이 출력되도록 하세요.

```bash
$>python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'Korea!')$
{'Hello', 'Seoul!'}$
{'Hello': '42Seoul!'}$
$>
```

## Ex 01

> `ex01/format_ft_time.py`로 제출.
>
> 허용 함수: `time`, `datetime` 또는 날짜를 받을 수 있는 다른 라이브러리

아래 형식으로 날짜를 출력하는 스크립트를 작성하세요. 당연하게도 실제 출력결과는 예시와 다를 수 있습니다. 하지만 같은 포맷으로 출력 돼야 합니다.

```bash
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

## Ex 02

> `ex02/find_ft_type.py` 로 제출.
>
> 허용 함수 없음.

객체 타입을 출력하고 42를 반환하는 함수를 작성하세요.

프로토타입은 다음과 같습니다.

```python
def all_thing_is_obj(object: any) -> int:
	#your code here
```

`tester.py`는 다음과 같습니다.

```python
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

print(all_thing_is_obj(10))
```

예상되는 출력은 다음과 같습니다.

```bash
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

함수만 단독으로 실행하는 것은 아무 동작도 하지 않습니다.

```bash
$>python find_ft_type.py | cat -e
$>
```

## Ex 03

> `ex03/NULL_not_found.py` 로 제출
>
> 허용 함수 없음

모든 타입의 "Null" 값을 출력하는 함수를 작성하세요.
아무런 문제 없이 잘 동작한다면 0을, 문제가 있다면 1을 반환해야 합니다.
당신의 함수는 모든 타입의 NULL 값을 출력해야 합니다.

프로토타입은 다음과 같습니다.

```python
def NULL_not_found(object: any) -> int:
	#your code here
```

`tester.py`는 다음과 같습니다.

```python
from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ’’
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

```

예상되는 출력은 다음과 같습니다.

```bash
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Garlic: nan <class 'float'>$ #서브젝트에는 Cheese로 되어 있는데, 오타인듯?
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not found$
1$
$>
```

함수만 단독으로 실행하는 것은 아무 동작도 하지 않습니다.

```bash
$>python NULL_not_found.py | cat -e
$>
```

## Ex 04

> `ex04/whatis.py`로 제출
>
> `sys` 또는 인자(`args`)를 받을 수 있는 라이브러리 허용

숫자를 인자로 받아서, 홀수 또는 짝수를 판별하고 결과를 출력하는 스크립트를 작성하세요.
만약 하나 이상의 인자가 주어지거나, 주어지는 인자가 숫자가 아닐 경우 `AssertionError`를 출력합니다.

예상되는 출력은 다음과 같습니다.

```text
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

## 추가되는 규칙

-   전역 스코프 사용을 금지합니다. 함수를 사용하세요!
-   각 프로그램은 반드시 `main()`함수가 있어야 하며, 단순한 스크립트가 아니여야 합니다.

```python
def main():
	# 테스트와 에러 헨들링

if __name__ == "__main__":
	main()
```

-   _catch_ 되지 않은 `exception`의 발생은 해당 예제의 점수를 0점으로 처리합니다. 테스트하기 위해 의도적으로 발생시키는 `exception` 또한 이 규칙이 적용됩니다.
-   당신의 모든 함수는 문서화되어야 합니다. (`__doc__`)
-   당신의 코드는 반드시 `norm`을 지켜야 합니다.
    -   `pip install flake8`
    -   `alias norminette = flake8`

## Ex 05

> `ex05/building.py` 로 제출
>
> `sys` 또는 인자(`args`)를 받을 수 있는 라이브러리 허용

이번에는 `main`을 통해, 완전히 자동화된 프로그램을 만들어 볼 것입니다. 하나의 문자열 인자를 받아서,글자수와 대문자 개수 및 소문자 개수, 문장부호 개수, 숫자와 공백 개수를 출력해야 합니다.

-   `None`이 주어지거나 아무것도 주어지지 않는다면, 유저로 부터 문자열을 입력 받습니다.
-   두 개 이상의 인자가 주어진다면, `AssertionError`를 출력합니다.

예상되는 출력은 다음과 같습니다.

```bash
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backwardcompatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
```

예상되는 출력은 다음과 같습니다. (캐리지 리턴은 공백으로 취급되며, 이를 고려하지 않으려면 EOF를 통해 입력을 종료합니다.)

```bash
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

> 💡 바퀴를 재발명 하지 마세요. 언어의 기능을 사용하세요.

## Ex 06

> `ex06` 폴더 안에 `ft_filter.py`, `filterstring.py` 로 제출
>
> `sys` 또는 인자(`args`)를 받을 수 있는 라이브러리 허용

### Part 1: filter 함수 재구현

당신만의 `ft_filter` 함수를 재구현하세요. 빌트인 `filter` 함수와 같은 동작을 해야합니다. (`print(filter.__doc__)` 반환값 또한 일치해야 합니다.), 재구현 시 반드시 `list comperhension` 를 사용하세요.

당연하게도, 빌트인 `filter`함수의 사용은 금지됩니다.

> 💡Part 1 만 해결해도 이 예제는 통과가 가능합니다. 하지만, 추후 프로젝트를 진행하는 데 알아야 할 것들이 있으므로 추가로 진행하는 것을 강력히 권장합니다.

### Part 2: 프로그램

문자열(S)과 정수(N), 2개의 인자를 받는 프로그램을 작성하세요. 프로그램은 **S** 에서 길이가 **N** 보다 긴 단어의 리스트를 출력해야 합니다.

-   단어들은 공백 문자를 통해 구분됩니다.
-   문자열은 문장 기호나 안보이는 문자 같이 특수 문자를 포함하지 않습니다.
-   프로그램은 반드시 하나의 `list comprehension`과 하나의 `lambda`를 포함해야 합니다.
-   만약 인자 개수가 2가 아니거나 타입이 다르다면, `AssertionError`를 출력합니다.

예상되는 출력은 다음과 같습니다.

```bash
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
$> python filterstring.py 'Hello the World' 99
[]
$>
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

## Ex 07

> `ex07/sos.py` 로 제출
>
> `sys` 또는 인자(`args`)를 받을 수 있는 라이브러리 허용

문자열을 인자로 받아 [모스 부호](https://en.wikipedia.org/wiki/Morse_code)로 인코딩하는 프로그램을 작성하세요.

-   프로그램은 공백문자와 알파벳/숫자 를 지원합니다.
-   알파벳/숫자 들은 `.`과 `-`로 표현됩니다.
-   각 모스 부호들은 하나의 공백으로 구분됩니다.
-   공백 문자는 `/` 로 표현됩니다.

모스 부호들을 보관하기 위해 반드시 `dictionary` 를 사용해야 합니다.

```python
NESTED_MORSE = { " ": "/ ",
				"A": ".- ",
				...
}
```

인자의 개수가 1이 아니거나 타입이 다르다면, `AssertionError`를 출력합니다.

```bash
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

## Ex 08

> `ex08/Loading.py` 로 제출
>
> 허용 함수 없음

`ft_tqdm` 함수를 만들어 봅시다.
`yield` 연산자를 통해 `tqdm` 함수를 복사합니다.

프로토타입은 다음과 같습니다.

```python
def ft_tqdm(lst: range) -> None:
	#your code here
```

`tester.py`는 다음과 같습니다. (원래의 `tqdm`과 비교해보세요.)

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
	sleep(0.005)
print()
for elem in tqdm(range(333)):
	sleep(0.005)
print()
```

예상되는 출력은 다음과 같습니다. (원래의 `tqdm`과 가능한 한 유사해야 합니다.)

```text
$> python tester.py
100%|[===============================================================>]| 333/333
100%| | 333/333 [00:01<00:00, 191.61it/s]
```

## Ex 09

> `ex09` 폴더 안에 `*.py`, `*.txt`, `*.toml`, `README.md`, `LICENSE` 제출
>
> `PyPI` 또는 패키지 생성 라이브러리

원하는 방식으로, 파이썬에서 첫 번째 패키지를 만드세요.
`pip list` 명령을 입력하면 설치된 패키지 목록에 패키지가 나타납니다.
`pip show -v ft_package` 명령을 입력하면 패키지의 특성이 나타납니다.

```bash
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

이 패키지는 다음의 명령어를 사용하여 `pip`를 통해 설치 되어야 합니다.

-   `pip install ./dist/ft_package-0.0.1.tar.gz`
-   `pip install ./dist/ft_package-0.0.1-py-none-any.whl`
    당신의 패키지는 스크립트에서 아래와 같은 방식으로 호출할 수 있어야 합니다.

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```
