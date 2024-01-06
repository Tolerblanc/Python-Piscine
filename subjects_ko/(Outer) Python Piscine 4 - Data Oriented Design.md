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

## Ex 00

> `ex00/statistics.py`로 제출
>
> 허용 함수 없음

`*args`로 알 수 없는 수량의 숫자들을 받고, `**kwargs`의 질문을 통해 평균, 중앙값, 사분위수 (1Q, 3Q), 표준 편차 및 분산을 구해야 합니다.
예외 처리가 이루어져야 합니다.

함수 프로토타입은 다음과 같습니다.

```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
	#your code here
```

`tester.py`는 다음과 같습니다.

```python
from statistics import ft_statistics

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
```

예상되는 출력은 다음과 같습니다.

```bash
$> python tester.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
$>
```

## Ex 01

> `ex01/in_out.py`로 제출
>
> 허용 함수 없음

인자를 제곱($x^2$)하여 반환하는 함수, 인자 자신으로 제곱($x^x$)하는 함수, 숫자와 함수를 인자로 받는 함수를 작성하세요. 3번째 함수는 호출하면 인수의 계산 결과를 반환하는 객체를 반환합니다.

함수 프로토타입은 다음과 같습니다.

```python
def square(x: int | float) -> int | float:
	#your code here

def pow(x: int | float) -> int | float:
	#your code here

def outer(x: int | float, function) -> object:
	count = 0
	def inner() -> float:
		#your code here
```

`tester.py`는 다음과 같습니다.

```python
from in_out import outer
from in_out import square
from in_out import pow
my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
```

예상되는 출력은 다음과 같습니다.

```bash
$> python tester.py
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
$>
```

> 💡 전역 스코프 사용이 금지되어 있다는 사실을 잊지 마세요!

## Ex 02

> `ex02/callLimit.py` 로 제출
>
> 허용 함수 없음

함수 호출 수를 인자로 받아, 한도 초과 시 함수 실행을 차단하는 함수를 작성하세요.

함수 프로토타입은 다음과 같습니다.

```python
def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		def limit_function(*args: Any, **kwargs: Any):
			#your code here
```

`tester.py`는 다음과 같습니다.

```python
from callLimit import callLimit

@callLimit(3)
def f():
	print("f()")

@callLimit(1)
def g():
	print("g()")

for i in range(3):
	f()
	g()
```

예상되는 출력은 다음과 같습니다.

```bash
$> python tester.py
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
$>
```

> 💡`Wrapper`가 무엇일까요?

## Ex 03

> `ex03/new_student.py`로 제출
>
> `dataclasses`, `random`, `string` 허용

`name`과 `surname`을 인자로 받고, `active`가 `True`로 설정되는 `dataclass`를 작성하세요. 학생 로그인을 생성 후, `generate_id` 함수로 랜덤 ID를 생성합니다. (주: 원문은 nickname으로 되어 있는데, 예시를 보면 다 surname이라서 surname으로 표기)
클래스의 `__str__`, `__repr__`을 사용해서는 안됩니다.

함수 및 클래스 프로토타입은 다음과 같습니다.

```python
import random
import string
from dataclasses import dataclass, field
def generate_id() -> str:
	return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
	#your code here
```

`tester.py`는 다음과 같습니다.

```python
from new_student import Student

student = Student(name = "Edward", surname = "agle")
print(student)
```

예상되는 출력은 다음과 같습니다. (id는 랜덤입니다.)

```bash
$> python tester.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
$>
```

> 💡 로그인과 ID 는 초기화 할 수 없어야 하며, 초기화를 시도할 경우 반드시 에러를 발생시켜야 합니다.

`tester.py`는 다음과 같습니다.

```python
from new_student import Student

student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)
```

예상되는 출력은 다음과 같습니다.

```bash
$> python tester.py
...
TypeError: Student.__init__() got an unexpected keyword argument 'id'
$>
```
