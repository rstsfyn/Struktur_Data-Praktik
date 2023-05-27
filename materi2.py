import random
import os
import re

def check_play_status():
    valid_respon= ['iya', 'tidak']
    while True:
        try:
            respon = input("Apakah kamu ingin memainkan lagi? (Iya atau Tidak): ")
            if respon.lower() not in valid_respon:
                raise ValueError('hanya Iya atau Tidak')
            
            if respon.lower() == 'iya':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Terimakasih telah Memainkan Permainan Suit Ini!")
                exit()
        except ValueError as err:
            print(err)

def play_suit():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Orang, Gajah, Semut - Suit!')
        
        user_choice = input('Silahkan Pilih Senjatamu'  
                            '[O]rang, [G]ajah, atau [S]emut: ')
        
        if not re.match('[OoGgSs]', user_choice):
            print('Pilih huruf terlebih dahulu untuk bertarung')
            print('[O]rang, [G]ajah, atau [S]emut:')
            continue
        
        print(f'Pilihanmu : {user_choice}')
        
        choices = ['O', 'G', 'S']
        opp_choice = random.choice(choices)
        
        print(f'Pilihanku: {opp_choice}')
        
        if opp_choice == user_choice.upper():
            print('Tidak ada yang menang(Tie)')
            play = check_play_status()
        elif opp_choice == 'O' and user_choice.upper() == 'S':
            print('Orang Mengalahkan Semut, Aku Menang!')
            play = check_play_status()
        elif opp_choice == 'G' and user_choice.upper() == 'O':
            print('Gajah Mengalahkan Orang, Aku Menang!')
            play = check_play_status()
        elif opp_choice == 'S' and user_choice.upper() == 'G':
            print('Semut Mengalahkan Gajah, Aku Menang!')
            play = check_play_status()
        else:
            print('Kamu Menang!\n')
            play = check_play_status()

if __name__ == '__main__':
    play_suit()