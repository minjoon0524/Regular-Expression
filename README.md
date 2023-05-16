# 1. 정규 표현식 (Regular Expression)

### 목차

- 정규표현식 조사 및 필요이유
- 파이썬에서의 기본 사용법
- 코드예제

## 정규표현식 조사 및 필요이유

### 1. 정규표현식이란

![1](https://github.com/minjoon0524/Regular-Expression/assets/118280086/85c420e9-cbd8-449f-bb00-92c5d827f410)

- **정규표현식**은 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어입니다 주로 프로그래밍 언어나 텍스트 에디터 등에서 문자열의 검색과 치환을 위한 용도로 쓰이고 있습니다.

출처 - [정규표현식(Regular Expression)을 소개합니다. (nextree.co.kr)](https://www.nextree.co.kr/p4327/)

### 2. 정규표현식 필요 이유

- 정규표현식이 필요한 이유는 정규 표현식을 사용하면 복잡하거나 반복적인 문자열 처리 작업을 매우 간단하고 효율적으로 수행할 수 있기 때문입니다.

추가적인 예시로 설명을 들면 

1. **문자열 검색과 매칭**: 이메일 주소, 전화번호, URL 등과 같은 특정 형식의 문자열을 찾을 수 있습니다. 이를 통해 입력 데이터의 유효성을 검사하거나 원하는 정보를 추출할 수 있습니다.
2. **데이터 정제 및 가공**: 텍스트 데이터에서 HTML 태그를 제거하거나, 공백을 처리하거나, 특정 문자를 제거하거나, 대소문자를 변환하는 등의 작업을 수행할 수 있습니다.
3. **토큰화와 텍스트 분석**: 자연어 처리(Natural Language Processing) 분야에서 정규표현식은 텍스트를 토큰화(tokenization)하는 데 사용됩니다. 토큰화는 문장이나 문서를 단어 또는 구절로 분할하는 작업으로, 텍스트 분석, 기계 번역, 정보 검색 등에 활용됩니다.
4. **패턴 기반 작업**:  문자열 내에서 날짜, 시간, 숫자, 주소 등과 같은 패턴을 추출하거나 대체하는 작업에 유용합니다.
5. **로그 파일 분석**: 시스템 로그 파일이나 웹 서버 로그 파일과 같은 대용량 텍스트 파일을 분석할 때, 정규표현식은 특정 패턴을 검색하거나 원하는 정보를 추출하는 데 사용됩니다. 이를 통해 로그 파일의 통계 분석, 오류 검출, 보안 감사 등을 수행할 수 있습니다.

출처 - ChatGPT

---

## 파이썬에서의 기본 사용

### ****1. 정규식 표현 방법****

- Python에서는 정규식의 사용을 위해 re 모듈을 기본적으로 제공합니다. 즉, 정규식을 사용하고 싶다면 **re 모듈**을 먼저 import 해야합니다.
- 패턴 객체는 re.compile() 함수를 이용하여 정규식을 컴파일 하면 생성됩니다.

![정규표현식 작성방법 1](https://github.com/minjoon0524/Regular-Expression/assets/118280086/f33546d6-d44c-433b-957b-4c3c090a01cc)

### 2****. 정규식 사용 방법(관련API)****

![정규표현식 작성방법 2](https://github.com/minjoon0524/Regular-Expression/assets/118280086/86566fa3-f55e-4925-af6d-59974e3286ac)

패턴 객체의 search() 메소드와 match() 메소드가 반환하는 **매치 객체는 다음과 같은 메소드들을 제공합니다.** 

![정규표현식 작성방법 3](https://github.com/minjoon0524/Regular-Expression/assets/118280086/54795b1a-7e95-4717-98d1-a46978f81fa7)

기본적으로 re 모듈은 정규식을 컴파일 하고 그 결과에 해당하는 패턴 객체의 메소드를 호출하는 방식으로 사용이 됩니다. 그러나 re 모듈은 이러한 두 단계를 하나의 단계로 합쳐 더욱 간단하게 코딩을 할 수 있도록 다음과 같은 간편 함수들까지 제공합니다. 위에서 설명한 패턴 객체의 메소드들과 일대일로 대응됩니다.

출처 - [https://it-eldorado.tistory.com/135](https://it-eldorado.tistory.com/135)

---

## 코드 예제

### 1. 기본예제

1. **`re.search()`** 메소드를 사용하여 문자열의 시작 부분에서 패턴과 일치하는 부분을 찾는 예시입니다.

```python
import re

pattern = r'Hello'
text = 'Hello, how are you?'

match = re.search(pattern, text)
if match:
    print('문자열이 패턴과 일치합니다.')
else:
    print('문자열이 패턴과 일치하지 않습니다.')
```

1. **`re.match()`** 메소드를 사용하여 문자열의 전체 부분에서 패턴과 일치하는 부분을 찾는 예시입니다.

```python
import re

pattern = r'^hello'
string = 'Hello, world!'

match = re.match(pattern, string)
if match:
    print(match.group()) # 출력: Hello
```

 3. **`re.findall()`** 메소드를 사용하여 문자열에서 패턴과 일치하는 모든 부분을 찾는 예시입니다.

```python
import re

pattern = r'\d+'
string = 'There are 12 apples and 20 oranges.'

matches = re.findall(pattern, string)
print(matches) # 출력: ['12', '20']
```

4 . **`re.finditer()`** 메소드를 사용하여 문자열에서 패턴과 일치하는 모든 부분에 대한 반복자(iterator)를 반환하는 예시입니다.

```python
import re

pattern = r'\d+'
string = 'There are 12 apples and 20 oranges.'

matches = re.finditer(pattern, string)
for match in matches:
    print(match.group()) # 출력: 12, 20
```

1. **`re.sub()`** 메소드를 사용하여 문자열에서 패턴과 일치하는 부분을 다른 문자열로 대체하는 예시입니다.

```python
import re

pattern = r'\d+'
string = 'There are 12 apples and 20 oranges.'

new_string = re.sub(pattern, '잘렸어', string)
print(new_string)  # 출력: There are 잘렸어 apples and 잘렸어 oranges.
```

1. **`subn()`** 함수는 **`sub()`** 함수와 비슷하지만, 대체된 횟수를 함께 반환하는 점에서 차이가 있습니다.

```python
import re

pattern = r'\d+'
string = 'There are 12 apples and 20 oranges.'

new_string, count = re.subn(pattern, 'X', string)
print(new_string) # 출력: There are X apples and X oranges.
print(count)      # 출력: 2
```

### 2. 심화예제

1. 입력된 문장에서 이메일 주소를 추출하는 예시입니다.

```python
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

sentence = "Please contact me at minjoon0524@example.com or mj0524@example.co.uk for further information."
extracted_emails = extract_emails(sentence)
print(extracted_emails)  # 출력: ['minjoon0524@example.com', 'mj0524@example.co.uk']
```

1. 텍스트 데이터에서 HTML 태그를 제거하고, 공백을 처리하며, 특정 문자를 제거하고, 대소문자를 변환하는 작업을 수행하는 예시입니다. 

```python
import re

def clean_text(text):
    # HTML 태그 제거
    cleaned_text = re.sub(r'<.*?>', '', text)

    # 공백 처리
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    # 특정 문자 제거
    cleaned_text = re.sub(r'[!@#$%^&*(),.?":{}|<>]', '', cleaned_text)

    # 대소문자 변환
    cleaned_text = cleaned_text.lower()

    return cleaned_text

html_text = '<p>This is an <b>example</b> text.</p>'
cleaned_text = clean_text(html_text)
print(cleaned_text)  # 출력: this is an example text
```

1. 문장을 단어로 분할하는 토큰화 작업을 수행하는 예시입니다. 

```python
import re

def tokenize_text(text):
    # 정규표현식 패턴을 사용하여 문장을 단어로 분할
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

sentence = "I love natural language processing!"
tokens = tokenize_text(sentence)
print(tokens)  # 출력: ['I', 'love', 'natural', 'language', 'processing']
```

출처 - ChatGPT

---
