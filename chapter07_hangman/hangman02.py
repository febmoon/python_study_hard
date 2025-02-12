import random

word_list = ["apple","banana","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# todo -1 : 비어 있는 list인 display를 만드시오.
#  chosen_word의 각 문자 개수마다 "_"를 추가하시오. 예를 들어 chosen_word == "apple"이라면
#  display = ["_","_","_","_","_"]이 되어야 합니다. 즉, chosen_word의 문자개수만큼
#  "_" 가 생깁니다.

display = []
# 일반 for 문
# for _ in range(len(chosen_word)):   # 변수가 사용되지 않으므로 i가 아니라 _로 명시함.
#     display.append("_")
#
# print(display)

# 향상된 for 문
for i in chosen_word:
    display.append("_")
print(display)

# todo-2 :chosen_word의 각 문자들을 반복시키세요.
#  만약 그 위치의 문자가 guess와 일치하면, 해당인덱스의 display에서 해당문자를 공개하세요.
#  ex) 사용자가 "p"를 입력했고, chosen word 가 "apple" 이라면  display = ['_','p','p','_','_']로
#  바뀌어야 합니다.

guess = input("알파벳을 입력하시오>>>").lower()


for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = guess
print(display)