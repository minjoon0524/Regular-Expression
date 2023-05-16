import re


# re.search() 메소드를 사용하여 문자열의 시작 부분에서 패턴과 일치하는 부분을 찾는 예시입니다.
def check_pattern(pattern, text):
  match = re.search(pattern, text)
  if match:
    print('The string matches the pattern.')
  else:
    print('The string does not match the pattern.')


pattern = r'Hello'
text = 'Hello, how are you?'
check_pattern(pattern, text)


# re.match() 메소드를 사용하여 문자열의 전체 부분에서 패턴과 일치하는 부분을 찾는 예시입니다.
def match_pattern(pattern, string):
  match = re.match(pattern, string)
  if match:
    print(match.group())  # Print the matched string
  else:
    print("No match found.")


pattern = r'^hello'
string = 'Hello, world!'
match_pattern(pattern, string)


# re.findall() 메소드를 사용하여 문자열에서 패턴과 일치하는 모든 부분을 찾는 예시입니다.
def find_pattern(pattern, string):
  matches = re.findall(pattern, string)
  return matches


pattern = r'\d+'
string = 'There are 12 apples and 20 oranges.'
result = find_pattern(pattern, string)
print(result)


# re.finditer() 메소드를 사용하여 문자열에서 패턴과 일치하는 모든 부분에 대한 반복자(iterator)를 반환하는 예시입니다.
def find_all_patterns(pattern, string):
  matches = re.finditer(pattern, string)
  for match in matches:
    print(match.group())


pattern = r'\d+'
string = 'There are 12 apples and 20 oranges.'
find_all_patterns(pattern, string)


# re.sub() 메소드를 사용하여 문자열에서 패턴과 일치하는 부분을 다른 문자열로 대체하는 예시입니다.
def substitute_pattern(pattern, replacement, string):
  new_string = re.sub(pattern, replacement, string)
  return new_string


pattern = r'\d+'
replacement = '잘렸어'
string = 'There are 12 apples and 20 oranges.'
new_string = substitute_pattern(pattern, replacement, string)
print(new_string)


# subn() 함수는 sub() 함수와 비슷하지만, 대체된 횟수를 함께 반환하는 점에서 차이가 있습니다.
def substitute_numbers(pattern, replacement, string):
  new_string, count = re.subn(pattern, replacement, string)
  return new_string, count


pattern = r'\d+'
string = 'There are 12 apples and 20 oranges.'

new_string, count = substitute_numbers(pattern, 'X', string)
print(new_string)  # 출력: There are X apples and X oranges.
print(count)  # 출력: 2


# 입력된 문장에서 이메일 주소를 추출하는 예시입니다.
def extract_emails(text):
  pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
  emails = re.findall(pattern, text)
  return emails


def main():
  sentence = "Please contact me at minjoon0524@example.com or mj0524@example.co.uk for further information."
  extracted_emails = extract_emails(sentence)
  print(extracted_emails
        )  # 출력: ['minjoon0524@example.com', 'mj0524@example.co.uk']


if __name__ == '__main__':
  main()


# 텍스트 데이터에서 HTML 태그를 제거하고, 공백을 처리하며, 특정 문자를 제거하고, 대소문자를 변환하는 작업을 수행하는 예시입니다.
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


def main():
  html_text = '<p>This is an <b>example</b> text.</p>'
  cleaned_text = clean_text(html_text)
  print(cleaned_text)  # 출력: this is an example text


if __name__ == '__main__':
  main()


# 문장을 단어로 분할하는 토큰화 작업을 수행하는 예시입니다.
def tokenize_text(text):
  # 정규표현식 패턴을 사용하여 문장을 단어로 분할
  tokens = re.findall(r'\b\w+\b', text)
  return tokens


def main():
  sentence = "I love natural language processing!"
  tokens = tokenize_text(sentence)
  print(tokens)  # 출력: ['I', 'love', 'natural', 'language', 'processing']


if __name__ == '__main__':
  main()
