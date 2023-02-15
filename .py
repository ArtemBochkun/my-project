import random

MORZE_CODES = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

words = ["cat", "dog", "house", "counter", "penis"]

answer = [] 


def morse_encorde(word) : 
    """
    переводит слово на английском языке в подследовательность точек и тире 
    return: строка морзянки
    """
    word_encoded = []

    for letter in word :
        word_encoded.append(MORZE_CODES.get(letter, ""))

    return " ".join(word_encoded)     


def get_word() :
    """
    Получает случайное число из списка 
    return: строка слова 
    """
    return random.choice(words)


def print_statistics(answer) : 
    """
    На основе списка answer True False выводит статистику 
    """
    total = len(answer)
    correct = sum(answer)
    incorrect = total - correct 

    print(f"Всего задачек {total}")
    print(f"Отвечено верно {correct}")
    print(f"Отвечено неверно {incorrect}")


def main () :

    print("Сегодня мы потренериуемся расшифрововать азбку Морза")
    print("Нажмите ENTER и начнем")
    input()

    for i in range (1, len(words)+1): 

        current_word = get_word()   
        current_encoded = morse_encorde(current_word)

        print(f"Слово {i} - {current_encoded}")

        user_input = input()

        if user_input.lower() == current_word :
            print(f"Верно {current_word}")
            answer.append(True)
        else :
            print(f"Неверно {current_word}")    
            answer.append(False)

    print(print_statistics(answer))


# main()            