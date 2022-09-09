# Description

이 프로젝트는 "life is funny"라는 슬로건을 기준삼아 만들어진 패키지이다.
우리가 좀더 편하게 살수있기를 바라면서 여러 코드를 작성했으며 사용해보면 정말 재밌고 편리하다.(내기준)
이 패키지를 사용하고싶다면 아래 README를 읽는걸 추천한다.

## History

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

## Examples
```python
from jhfunny import jhfunny

a = jhfunny.funny()

a.starpix(5) # 피라미드 형태의 별찍기가 출력된다. 
a.starpix(5, "down") # 뒤집힌 피라미드 형태의 별찍기 default vlaue => "up"
```
```python
from jhfunny import jhfunny

a = jhfunny.funny()

a.pypi("hello") # pypi("package_name")
```
pypi에 업로드하기위한 자료구조를 그대로 생성하여 쉽게 패키지를 배포할수있는 함수이다.
[링크](https://imagine-village.tistory.com/entry/PyPi%EC%97%90-%ED%8C%A8%ED%82%A4%EC%A7%80%EB%A5%BC-%EC%97%85%EB%A1%9C%EB%93%9C-%ED%95%98%EB%8A%94-%EB%B2%95)를 클릭하면 pypi에 업로드하는 방식의 코드들이 나와있으니 참고하면 좋다.