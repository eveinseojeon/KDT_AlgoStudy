## 진법

- 파이썬은 기본 10진법이다. 2진법, 8진법, 16진법으로 표현할 때는 접두어가 붙는다.

  - 2진법 : 0b
  - 8진법 : 0o
  - 16진법 : 0x

- 진법을 변환하는 파이썬 내장함수

  - 2진법 : bin()
  - 8진법 : oct()
  - 16진법 : hex()

- 출력할 때

  - 8진법

    ```python
  print('%o'%n) # n에 저장되어 있는 값을 8진수(octal) 형태 문자열로 출력
    ```

  - 16진법
  
    ```python
  print('%x'%n) # n에 저장되어 있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력
    print('%X'%n) # n에 저장되어 있는 값을 16진수(hexadecimal) 대문자 형태 문자열로 출력
  ```




##  유니코드 관련 함수

- ord() : 문자 -> 정수(유니코드 값)
- chr() : 정수(유니코드 값) -> 문자



## 나눗셈 연산자

- // : 몫
- % : 나머지



## 실수의 자릿수

- format()

  ```python
  format(실수, '.2f') # 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다.
  ```



## 불 대수(boolean algebra)

- bool()

  ```python
  bool() # 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해 준다.
  ```



## 비트단위(bitwise) 연산자

- << (bitwise left shift)

  ```python
  n<<a # n의 2**a배
  ```

- \>\> (bitwise left shift)

  ```python
  n>>a # n의 2**(-a)배
  ```

- ~ (bitwise not)

  ```python
  ~n # -n-1
  ```

- & (bitwise and)

- | (bitwise or)

- ^ (bitwise xor)

