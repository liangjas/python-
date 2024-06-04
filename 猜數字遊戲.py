import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("歡迎來到猜數字遊戲！")

    while guess != number_to_guess:
        guess = int(input("請輸入你猜的數字（1到100）："))
        attempts += 1

        if guess < number_to_guess:
            print("太小了，再試一次！")
        elif guess > number_to_guess:
            print("太大了，再試一次！")
    
    print(f"恭喜你！你在 {attempts} 次嘗試後猜中了數字 {number_to_guess}！")

if __name__ == "__main__":
    guess_number()