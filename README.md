# fun function index
1. [starpix - 별 찍기를 함수 하나로 완성](#starpix)
1. [pypi - pypi 업로드를 좀 더 단순하게](#pypi)
1. [tentobin - 소수까지 십진수를 이진수로](#tentobin)

# Description

이 프로젝트는 "life is funny"라는 슬로건을 기준삼아 만들어진 패키지이다.
우리가 좀더 편하게 살수있기를 바라면서 여러 코드를 작성했으며 사용해보면 정말 재밌고 편리하다.(내기준)
이 패키지를 사용하고싶다면 아래 README를 읽는걸 추천한다.

## History

> ### version 1.4.1
- fix package to module change and docs update

> ### version 1.4.0
- feat demical to binary add

> ### version 1.3.1
- fix package and module name modify
- package bug fixes

> ### version 1.2.0
- create pypi function
- package bug fixes

> ### version 1.1.0
- install bug fixes

> ### version 1.0.0
- create jhfunnycode package 

## Installation
설치방법은 아래와 같다.
```
pip install jhfunnycode
```
또는 [링크](https://pypi.org/project/jhfunnycode/)에 접속해서 직접 다운받을 수 있다.

<br>



# starpix
프로그래밍의 대표적인 반복문 예제인 별찍기를 함수로 단순화 시켰다.
우리는 이중반복문 과제로부터 해방되었다.

### Examples
```python
import jhfunnycode

jhfunnycode.starpix(5) # 피라미드 형태의 별찍기가 출력된다. 
jhfunnycode.starpix(5, "down") # 뒤집힌 피라미드 형태의 별찍기 default vlaue => "up"
```

<br>

# pypi
본인이 만든 패키지를 남들이 사용할 수 있게 하고싶다. 그런경우 여러가지 방법이 있지만 그중 하나인 유명한 패키지 저장소 PyPi가 있다.
여기에 올리기위해 여러가지 해야할 방법이 있는데 그 방법을 조금 더 단순화 시켰다.

### Examples
```python
import jhfunnycode

jhfunnycode.pypi("hello") # pypi("package_name")
```
pypi에 업로드하기위한 자료구조를 그대로 생성하여 쉽게 패키지를 배포할수있는 함수이다.
[링크](https://imagine-village.tistory.com/entry/PyPi%EC%97%90-%ED%8C%A8%ED%82%A4%EC%A7%80%EB%A5%BC-%EC%97%85%EB%A1%9C%EB%93%9C-%ED%95%98%EB%8A%94-%EB%B2%95)를 클릭하면 pypi에 업로드하는 방식의 코드들이 나와있으니 참고하면 좋다.

<br>

# tentobin
십진수를 이진수로 변경하기위해선 bin()함수를 사용하면 되지만 이는 float까지 변경하지 않는다. 그렇기에 float 자료형까지 이진수로 변경하는 함수를 만들었다. 그리고 이것은 순환소수 여부도 알아낼 수 있다. 즐겁게 사용하길 바란다.

### Examples
```python
import jhfunnycode

jhfunnycode.tentobin(10)
jhfunnycode.tentobin(10.625)
```