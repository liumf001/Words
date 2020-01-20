import os
import shutil
print("""
                      .::::.  
                     .::::::::.  
                    :::::::::::  
                 ..:::::::::::'  
              '::::::::::::'  
                .::::::::::  
           '::::::::::::::..  
                ..::::::::::::.  
              ``::::::::::::::::  
               ::::``:::::::::'        .:::.  
              ::::'   ':::::'       .::::::::.  
            .::::'      ::::     .:::::::'::::.  
           .:::'       :::::  .:::::::::' ':::::.  
          .::'        :::::.:::::::::'      ':::::.  
         .::'         ::::::::::::::'         ``::::.  
     ...:::           ::::::::::::'              ``::.  
    ```` ':.          ':::::::::'                  ::::..  
                       '.:::::'                    ':'````..  
Reciting words is so interesting!Reciting words is so interesting!
Reciting words is so interesting!Reciting words is so interesting!
Reciting words is so interesting!Reciting words is so interesting!""")


def first_run():
    print("WELCOME!")
    print("for the first time using this software, please set a daily target:")
    number = input('The number of words you want recite per day\n:)>>>')
    while not number.isdecimal():
        print("What are you inputting! please input a number:")
        number = input(':)>>>')
    num = int(number)
    with open(".\\src\\number_per_day.txt", mode='w', encoding='utf-8') as f:
        f.write(number)
    print("""
Set target successfully. 
input 'help' to get guidance.
Please enjoy.
    """)
    return num


def get_target():
    with open(".\\src\\number_per_day.txt", 'r', encoding='utf-8') as f:
        number = f.readline()
    return int(number)


def set_target():
    number = input('The number of words you want recite per day\n:)>>>')
    while not number.isdecimal() or int(number) < 1 or int(number) > 2000:
        print("What are you inputting! please input a decimal number(0<number<2001):")
        number = input(':)>>>')
    with open(".\\src\\number_per_day.txt", 'w', encoding='utf-8') as f:
        f.write(number)


def help_command():
    with open('.\\src\\readme.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line, end='')


def start_stuff(num):
    with open('.\\src\\src_words.txt', 'r', encoding='utf-8') as f:
        total_words = f.readlines()
        num = min(num, len(total_words))
        today_words = total_words[:num]
    with open('.\\src\\src_words.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(total_words[num:]))
    flag = True
    for i in range(0, 5):
        if not flag:
            break
        for word in today_words:
            print(word, end='')
            cmd = input('>>>')
            if cmd == '' or cmd == 'continue' or cmd == 'c':
                pass
            elif cmd == 'trash' or cmd == 't':
                today_words.remove(word)
                with open(".\\src\\trash_words.txt", 'a', encoding='utf-8') as f:
                    f.write(word)
            elif cmd == 'help':
                help_command()
            elif cmd == 'break' or cmd == 'b':
                with open('.\\src\\src_words.txt', 'w', encoding='utf-8') as f:
                    f.write(''.join(total_words))
                    flag = False
                break
    with open('.\\src\\review_words.txt', 'a', encoding='utf-8') as f:
        f.write(''.join(today_words))


def reset():
    sure = input('Are you sure you want to reset this software? [y/n]: ')
    if sure == 'y' or sure == '':
        open('.\\src\\number_per_day.txt', 'w').close()
        open('.\\src\\trash_words.txt', 'w').close()
        open('.\\src\\review_words.txt', 'w').close()
        open('.\\src\\done_words.txt', 'w').close()
        os.remove('.\\src\\src_words.txt')
        shutil.copyfile('.\\src\\backup.txt', '.\\src\\src_words.txt')
        print("reset successfully.")
        set_target()


def review_stuff(num):
    if os.stat('.\\src\\review_words.txt').st_size == 0:
        print("There is no word to review")
        return None
    with open(".\\src\\review_words.txt", 'r', encoding='utf-8') as f:
        total_words = f.readlines()
        num = min(num, len(total_words))
        review_words = total_words[:num]
    with open(".\\src\\review_words.txt", 'w', encoding='utf-8') as f:
        f.write(''.join(total_words[num:]))
    flag = True
    for i in range(0, 3):
        if not flag:
            break
        for word in review_words:
            print(word, end='')
            cmd = input('>>>')
            if cmd == '' or cmd == 'continue' or cmd == 'c':
                continue
            elif cmd == 'trash' or cmd == 't':
                review_words.remove(word)
                with open(".\\src\\trash_words.txt", 'a', encoding='utf-8') as f:
                    f.write(word)
            elif cmd == 'help':
                help_command()
            elif cmd == 'break' or cmd == 'b':
                with open('.\\src\\review_words.txt', 'w', encoding='utf-8') as f:
                    f.write(''.join(total_words))
                flag = False
                break
    with open('.\\src\\done_words.txt', 'a', encoding='utf-8') as f:
        f.write(''.join(review_words))


def done_stuff():
    if os.stat('.\\src\\done_words.txt').st_size == 0:
        print("You have not done any word", end='')
        return None
    with open('.\\src\\done_words.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line, end='')


def target_stuff():
    print('Your target is ' + str(get_target()), end='')
    print('Do you want to change it?(y/n):')
    cmd = input(':)>>>')
    if cmd == 'y' or cmd == 'Y' or cmd == '':
        set_target()


def all_stuff():
    with open('.\\src\\src_words.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line, end='')


def main():
    if os.stat('.\\src\\number_per_day.txt').st_size == 0:
        set_target()
    while True:
        cmd = input(':)>>>')
        if cmd == 'help':
            help_command()
        elif cmd == 'end':
            break
        elif cmd == 'start':
            start_stuff(get_target())
        elif cmd == 'reset':
            reset()
        elif cmd == 'review':
            review_stuff(get_target())
        elif cmd == 'done':
            done_stuff()
        elif cmd == 'target':
            target_stuff()
        elif cmd == 'all':
            all_stuff()


if __name__ == '__main__':
    main()
