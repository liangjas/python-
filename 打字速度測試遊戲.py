import random
import time

# 隨便的東西
words = ["python", "java", "swift", "javascript", "golang", "ruby", "typescript", "cplusplus"]

def display_welcome_message():
    print("歡迎來到打字速度")
    print("你有30秒的時間來輸入盡可能多的。")
    input("按Enter開始")

def get_random_word():
    return random.choice(words)

def display_word(word):
    print(f"請輸入這個: {word}")

def get_user_input():
    return input("你的輸入: ")

def check_word(user_input, word):
    return user_input == word

def display_result(correct_words):
    print(f"時間到！你總共正確輸入 {correct_words} 。")

def typing_game():
    display_welcome_message()

    start_time = time.time()
    end_time = start_time + 30  # 你有的遊戲時間

    correct_words = 0

    while time.time() < end_time:
        word = get_random_word()
        display_word(word)
        user_input = get_user_input()

        if check_word(user_input, word):
            print("正確！")
            correct_words += 1
        else:
            print("錯誤！")

    display_result(correct_words)

# 開始遊戲
if __name__ == "__main__":
    typing_game()