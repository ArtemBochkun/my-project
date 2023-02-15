easy = {"cat": "кошка", "dog": "собака", "owl": "сова", "dragon": "дракон", "pig": "свинья"} 
medium = {"black": "черный", "white": "белый", "pink": "розовый", "blue": "голубой", "red": "красный"}    
hard = {"mother": "мама", "father": "папа", "brother": "брат", "sister": "сестра", "aunt": "тетя"}

levels = {
    0: "Нулевой",
    1: "Так себе", 
    2: "Можно лучше", 
    3: "Норм", 
    4: "Хорошо",  
    5: "Отлично",
}

result = {}

print("Выберите уровень сложности ")
print("Легкий, Средний, Сложный ")
user_answer = input()

if user_answer == "легкий":
  print("Выбран уровень сложности, мы предложим Вам 5 слов, подберите перевод ") 
  input("Нажмите Enter")

  for words in easy:
    print(f"{words} , {len(easy[words])} букв, начинается на {easy[words][0]}")
    easy_answer = input()
    if easy_answer == easy[words]:
      result[words] = True
      print(f'Верно, {words.title()} это {easy_answer}')
    else : 
      result[words] = False
      print(f'Неверно {words.title()} это {easy[words]}')

if user_answer == "средний":
  print("Выбран уровень сложности, мы предложим Вам 5 слов, подберите перевод ") 
  input("Нажмите Enter")

  for words in medium:
      print(f"{words} , {len(medium[words])} букв, начинается на {medium[words][0]}")
      medium_answer = input()
      if medium_answer == medium[words]:
        result[words] = True
        print(f'Верно, {words.title()} это {medium_answer}')
      else : 
        result[words] = False
        print(f'Неверно {words.title()} это {medium[words]}')

if user_answer == "сложный":
  print("Выбран уровень сложности, мы предложим Вам 5 слов, подберите перевод ") 
  input("Нажмите Enter")

  for words in hard:
      print(f"{words} , {len(hard[words])} букв, начинается на {hard[words][0]}")
      hard_answer = input()
      if hard_answer == hard[words]:
        result[words] = True
        print(f'Верно, {words.title()} это {hard_answer}')
      else : 
        result[words] = False
        print(f'Неверно {words.title()} это {hard[words]}')

score = 0

print(f"Правильно отвеченные слова: ")

for key in result :
  if result[key] == True : 
    score += 1 
    print(key)

print(f"Неправильно отвеченные слова: ")

for key in result :
  if result[key] == False :  
    print(key)

print(f"Ваш ранг: {levels[score]}")

