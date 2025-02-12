import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list =["apple",'banana','camel']
chosen_word = random.choice(word_list)
display =[]
lives =6
end_of_game = False
for i in chosen_word:
    display.append("_")
while not end_of_game:
    guess = input("알파벳을 입력하시오>>>").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i]== guess:
            display[i] = guess
        # else:
        #     lives -=1
        #     print(f"당신 기회는 {lives}번 남았습니다")
        #     if lives == 0:
        #         print("모든 기회 잃었습니다.")
        #         break
        #         end_of_game = True
        # 라고 작성하시면 안됩니다. -> 알파벳을 하나 입력할 때마다 모든 단어에서 알파벳이 맞는지
        # 확인하는 조건문이 실행되기 때문에
        #-> 즉, 반복문 내부에 조건문 있기 때문에 geuss를 한번 만 입력하고도
        #lives -=1 이루어짐
# 이상을 이유로 for 반복문 바깥에서 (즉, 들여쓰기 적용X) guess가 chosen_word에 속하지 않는지를 확인하는
# 조건문을 작성해야 함
    if guess not in chosen_word:
        lives -=1
        print(stages[lives])
        print(f"당신의 기회는 {lives}번 남아있습니다")
    if lives == 0:
        print("모든 기회 잃었습니다.")
        end_of_game = True
        print(f"정답은 {chosen_word}입니다.")
    if "_" not in display:
        print("정답입니다")
        end_of_game = True
        # break

    print(" ".join(display))
    print(stages[lives])


print("반복문이 종료된 경우 실행되는 코드입니다.")

# 여기까지 작성했을 때 주의할 점
# 1. 로고
# 2. word_list가 부족하다
# 3. 혹시 테스트 해보고 유지 보수 및 리팩토링 지점이 있는지 확인할 필요가 있음. -> 함수화
