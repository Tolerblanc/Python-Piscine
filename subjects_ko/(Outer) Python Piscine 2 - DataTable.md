# Subject 번역

## General Rules

- VM을 사용하여 클러스터 컴퓨터에서 모듈을 렌더링해야 합니다.
	- 가상 머신에 사용할 OS를 선택할 수 있습니다.
	- 가상 머신에 프로젝트를 구현하는 데 필요한 모든 소프트웨어가 있어야 합니다. 이 소프트웨어를 구성하고 설치해야 합니다.
- 또는 도구를 사용할 수 있는 경우, 컴퓨터에 직접 설치할 수 있습니다.
	- 세션에 필요한 모든 모듈을 설치할 수 있는 공간이 있는지 확인합니다. (캠퍼스에 있는 경우 goinfre 사용)
	- 평가 전에 모든 모듈을 설치해야 합니다.
- 함수들은 예상치 못하게 종료되면 안됩니다. (segmentation fault, bus error, double free 등) 예상치 못한 종료가 일어난다면, 당신의 프로젝트는 비 기능적인 것으로 간주되며 0점을 받게 됩니다.
- 프로젝트에 대한 테스트 프로그램을 만드는 것을 강력 권장합니다.
	- 제출할 필요가 없고, 채점되지 않습니다. 
	- 이렇게 하면 자신의 작업과 동료의 작업을 쉽게 테스트할 수 있습니다. 특히, 디펜스 시 유용합니다.
	- 실제로 디펜스 하는 동안, 자신의 테스트 및 평가하는 동료의 테스트를 자유롭게 사용할 수 있습니다.
- 당신의 모든 작업을 git 레포지토리에 제출하세요. git 레포지토리에 제출된 작업물만 점수를 받을 수 있습니다. 만약 Deepthought이 작업물을 채점하게 되어있다면, 동료평가를 마친 뒤 자동으로 채점될 것입니다. Deepthought은 작업물의 에러를 발견한 순간 채점을 중지합니다.
- 반드시 `Python 3.10` 을 사용해야 합니다.
- 각 예제에서 금지되지 않은 모든 빌트인 함수를 사용할 수 있습니다.
- 모든 라이브러리 import는 명시적이여야 합니다. 
	- `import numpy as np` 형식으로 사용해야 하며,
	- `from pandas import *`  와 같은 형식은 허용되지 않습니다.
	- 허용되지 않은 import 형식을 사용할 경우, 0점을 받게 됩니다.
- 전역 변수를 사용해서는 안됩니다.

## 추가되는 규칙

- 전역 스코프 사용을 금지합니다. 함수를 사용하세요!
- 각 프로그램은 반드시 `main()`함수가 있어야 하며, 단순한 스크립트가 아니여야 합니다.
```python
def main():
	# 테스트와 에러 헨들링

if __name__ == "__main__":
	main()
```
- _catch_ 되지 않은 `exception`의 발생은 해당 예제의 점수를 0점으로 처리합니다. 테스트하기 위해 의도적으로 발생시키는 `exception` 또한 이 규칙이 적용됩니다.
- 당신의 모든 함수는 문서화되어야 합니다. (`__doc__`)
- 당신의 코드는 반드시 `norm`을 지켜야 합니다.
	- `pip install flake8`
	- `alias norminette = flake8`

이번 모듈에서는 FREE SCHOOL MATERIALS FROM GAPMINDER.ORG, CC-BY LICENSE. 의 데이터를 사용할 것입니다.

데이터 조작이나 데이터 시각화를 연습 하고 싶다면 사용 가능한 데이터를 살펴보는 것이 좋습니다.

## Ex 00
> `ex00/load_csv.py`로 제출
> `pandas` 또는 모든 데이터셋 조작 라이브러리 허용

경로를 인자로 받아서 데이터셋의 차원을 출력하고 반환하는 함수를 작성하세요.
경로가 이상한 경우와 같은 에러 케이스를 핸들링하고, `None`을 반환하세요.

프로토타입은 다음과 같습니다.
```python
def load(path: str) -> Dataset: (You have to adapt the type of return according to your library)
	#your code here
```

`tester.py`는 다음과 같습니다.
```python
from load_csv import load

print(load("life_expectancy_years.csv"))
```

예상되는 출력은 다음과 같습니다.
```bash
$> python tester.py 
Loading dataset of dimensions (195, 302) 
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100 
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8 
	... 
$>
```
데이터셋 출력 방식은 자유입니다.

## Ex 01

> `ex01` 폴더 안에 `load_csv.py`, `aff_life.py`로 제출
> `matplotlib`, `seaborn` 또는 데이터 시각화를 위한 모든 라이브러리 허용

이전 예제에서의 `load` 함수를 호출하여  `life_expectancy_years.csv` 를 로드하고, 당신의 캠퍼스의 지역 정보를 표시하는 프로그램을 만드세요.
그래프에는 제목과 범례가 있어야 합니다.
예를 들어, 프랑스의 4 2캠퍼스 같은 경우 다음과 같은 결과를 출력할 수 있습니다.
![[Pasted image 20240104210226.png]]

## Ex 02

> `ex02` 폴더 안에 `load_csv.py`, `aff_pop.py`로 제출
> `matplotlib`, `seaborn` 또는 데이터 시각화를 위한 모든 라이브러리 허용

1번 예제에서의 `load` 함수를 호출하여  `population_total.csv` 를 로드하고, 당신의 캠퍼스의 지역 정보와 특정 캠퍼스의 정보를 표시하는 프로그램을 만드세요.
그래프에는 제목과 범례가 있어야 합니다.
1800년대 부터 2050년대를 출력해야 합니다.
예를 들어, 프랑스의 42 캠퍼스 같은 경우 다음과 같은 결과를 출력할 수 있습니다.
![[Pasted image 20240104210433.png]]

## Ex 03

> `ex03` 폴더 안에 `load_csv.py`, `projection_life.py`로 제출
> `matplotlib`, `seaborn` 또는 데이터 시각화를 위한 모든 라이브러리 허용

1번 예제에서의 `load` 함수를 호출하여 `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` 와 `life_expectancy_years.csv`를 로드하고, 각 국가의 1900년 국민 총생산 대비 기대 수명을 표시하는 프로그램을 만드세요.
그래프에는 제목과 범례가 있어야 합니다.
반드시 1900년을 표시해야 합니다.
![[Pasted image 20240104210810.png]]

>💡두 변수의 상관관계가 보이나요?

