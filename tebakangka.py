import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("Tidak ada skor tertinggi")
    else:
        print("Skor tertinggi adalah {} percobaan".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Halo teman, selamat datang dalam permainan tebak angka!")
    player_name = input("Siapa namamu? ")
    wanna_play = input("Hai, {}, maukah kamu bermain tebak angka? (Ketik Ya/Tidak) ".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "ya":
        try:
            guess = input("Pick a number between 1 and 10: ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Maukah kamu bermain lagi? (Ketik Ya/Tidak): ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "tidak":
                    print("Baiklah, sampai jumpa lagi!")
                    break
            elif int(guess) > random_number:
                print("Terlalu tinggi")
                attempts += 1
            elif int(guess) < random_number:
                print("Terlalu rendah")
                attempts += 1
        except ValueError:
            print("Oh tidak! angka yang kamu pilih tidak valid")
    else:
        print("Baiklah, sampai jumpa lagi!")
if __name__ == '__main__':
    start_game()
