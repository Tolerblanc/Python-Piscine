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

> `ex00/S1E9.py`로 제출
> 허용 함수 없음

첫 번째 파라미터로 `first_name`을, 두 번째 파라미터로 `is_alive`를 받는 추상 클래스 `character`를 만드세요. 두 번째 파라미터는 필수가 아니며, 기본적으로 `True`로 설정됩니다. `is_alive`를 `True`에서 `False`로 변경하는 메서드가 존재합니다.
그리고, 이 클래스를 상속하는 `stark` 클래스를 작성하세요.

프로토타입은 다음과 같습니다.

```python
from abc import ABC, abstractmethod

class Character(ABC):
	"""Your docstring for Class"""
	@abstractmethod
		#your code here

class Stark(Character):
	"""Your docstring for Class"""
		#your code here
```

`tester.py`는 다음과 같습니다.

```python
from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print（"---"）
Lyanna = Stark("Lyanna", False)
print (Lyanna.__dict__)
```

예상되는 출력은 다음과 같습니다. (docstring은 다를 수 있습니다.)

```bash
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>
```

> 💡 추상클래스를 사용하였는지 꼭 확인하세요. 아래의 코드에서 에러가 발생해야 합니다.

```python
from S1E9 import Character

hodor = Character("hodor")

# TypeError: Can't instantiate abstract class Character with abstract method
```

## Ex 01

> `ex01` 폴더 안에 이전 예제의 파일들 + `S1E7.py`로 제출
>
> 허용 함수 없음

`Character`를 상속하는 2개의 클래스를 작성하세요. `Character`클래스 없이 인스턴스화 할 수 있습니다. `__str__` 과 `__repr__`이 객체가 아닌 문자열을 반환하는 방법을 찾아보세요. 캐릭터들을 체인으로 생성하는 클래스 메서드를 작성하세요. (??) (원문: Write a Class method to create characters in a chain.)

클래스 프로토타입은 다음과 같습니다.

```python
from S1E9 import Character

class Baratheon(Character):
	#your code here

class Lannister(Character):
	#your code here

	#decorator
	def create_lannister(your code here):
		#your code here
```

`tester.py`는 다음과 같습니다.

```python
from S1E7 import Baratheon, Lannister
Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
```

예상되는 출력은 다음과 같습니다. (docstring은 다를 수 있습니다.)

```bash
$> python tester.py
{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: {'Lannister', 'blue', 'light'}>
True
---
Name : ('Jaine', 'Lannister'), Alive : True
$>
```

## Ex 02

> `ex02` 폴더 안에 이전 예제의 파일들 + `DiamondTrap.py`로 제출
>
> 허용 함수 없음

이 예제에서는 `Joffrey Baratheon`이라는 괴물을 만들겁니다. 이건 너무 위험해요!
이 새로운 **가짜** 왕에게는 뭔가 모순되는 점이 있습니다.
**속성**을 사용하여 새로운 왕의 물리적 특성을 바꿔야 합니다.

클래스 프로토타입은 다음과 같습니다.

```python
from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	#your code here
```

`tester.py`는 다음과 같습니다.

```python
from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
```

예상되는 출력은 다음과 같습니다. (docstring은 다를 수 있습니다.)

```bash
$> python tester.py {'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$>
```

> 💡파이썬 2.3 부터, 언어는 다이아몬드 상속 문제에 대응하기 위하여 C3 선형화를 사용합니다.

## Ex 03

> `ex03/ft_calculator.py` 로 제출
>
> 허용 함수 없음

벡터와 스칼라의 사칙 연산이 가능하게 하는 `calculator`클래스를 작성하세요.

클래스 프로토타입은 다음과 같습니다.

```python
class calculator:
#your code here
	def __add__(self, object) -> None:
		#your code here
	def __mul__(self, object) -> None:
		#your code here
	def __sub__(self, object) -> None:
		#your code here
	def __truediv__(self, object) -> None:
		#your code here
```

`tester.py`는 다음과 같습니다.

```python
from ft_calculator import calculator
v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
Print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
Print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
```

예상되는 출력은 다음과 같습니다. (docstring은 다를 수 있습니다.)

```bash
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
```

> 💡 `ZeroDivisionError`를 제외하고, 아무 에러도 핸들링할 필요 없습니다.

## Ex 04

> `ex04/ft_calculator.py`로 제출
>
> 허용 함수 없음

두 벡터간 내적, 덧셈, 뺄셈을 가능하게하는 `calculator` 클래스를 작성하세요.
벡터들은 항상 같은 크기이므로, 예외처리 하지 않아도 됩니다.
이 클래스를 인스턴스화하지 않고 `calculator` 클래스의 메서드를 사용할 수 있도록 도와주는 데코레이터를 찾아야 합니다.

클래스 프로토타입은 다음과 같습니다.

```python
class calculator:
#your code here
	# decorator
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		#your code here
	# decorator
	def add_vec(V1: list[float], V2: list[float]) -> None:
		#your code here
	# decorator
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		#your code here
```

`tester.py` 는 다음과 같습니다.

```python
from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calcluator.sous_vec(a, b)
```

예상되는 출력은 다음과 같습니다. (docstring은 다를 수 있습니다.)

```bash
$> python tester.py
Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
$>
```

> 💡에러 핸들링을 하지 않아도 됩니다. 만약 벡터나 행렬 계산에 대해 더 알아보고 싶다면, 이 피신이 끝난 후 `matrix`프로젝트에 도전해보세요!
