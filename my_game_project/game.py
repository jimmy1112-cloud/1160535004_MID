import random
def play_game():
    target_number = random.randint(1, 100)
    attempts = 0
    print("=== 歡迎來到猜數字遊戲 ===")
    print("我已經想好了一個 1 到 100 之間的數字。")

    while True:
        try:
            guess = int(input("請輸入你猜的數字: "))
            attempts += 1

            if guess < target_number:
                print("太小了！再試一次。")
            elif guess > target_number:
                print("太大了！再試一次。")
            else:
                print(f"恭喜你！你花了 {attempts} 次猜中了！")
                break
        except ValueError:
            print("請輸入有效的整數。")

if __name__ == "__main__":
    play_game()