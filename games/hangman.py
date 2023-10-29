from random import choice

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

max_wrong = len(HANGMAN) - 1
WORDS = ("аист", "акула", "баран", "барсук", "бобр", "бык", "верблюд", "волк", "воробей", "ворон", "выдра", "голубь", "гусь", "жаба", "зебра")  # Слова для угадывания

word = choice(WORDS)  # Слово, которое нужно угадать
so_far = "*" * len(word)  # Одна звездочка для каждой буквы в слове, которое нужно угадать
wrong = 0  # Количество неверных предположений, сделанных игроком
used = []  # Буквы уже угаданы

while wrong < max_wrong and so_far != word:
    print(HANGMAN[wrong])  # Вывод висельника по индексу
    print("\nВы использовали следующие буквы:\n", used)
    print("\nНа данный момент слово выглядит так:\n", so_far)

    guess = input("\n\nВведите свое предположение: ")  # Пользователь вводит предполагаемую букву

    while guess in used:
        print("Вы уже вводили букву", guess)  # Если буква уже вводилась ранее, то выводим соответствующее сообщение
        guess = input("Введите свое предположение: ")  # Пользователь вводит предполагаемую букву

    used.append(guess)  # В список использованных букв добавляется введённая буква

    if guess in word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
        print("\nДа!", guess, "есть в слове!")
        new = ""
        for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nИзвините, буквы \"" + guess + "\" нет в слове.")  # Если буквы нет, то выводим соответствующее сообщение
        wrong += 1

if wrong == max_wrong:  # Если игрок превысил кол-во ошибок, то его повесили
    print(HANGMAN[wrong])
    print("\nТебя повесили!")
else:  # Если кол-во ошибок не превышено, то игрок выиграл
    print("\nВы угадали слово!")

print("\nЗагаданное слово было \"" + word + '\"')
