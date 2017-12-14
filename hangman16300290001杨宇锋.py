from datetime import datetime
import hangmanlib16300290001杨宇锋 as hm
import random
import csv
import os


def make_WordDict(file):
    '''
    读取txt文档，制作一个list存放着每个单词
    :param file:
    :return: list
    '''
    with open(file, 'r') as f:
        lines = f.readline()
        lines = lines.split(' ')
    return lines

    # print(lines[:800])


def count_total_time(start_time_compact):
    '''

    :param start_time_compact:
    :return: total_time(s)
    '''

    end_time = datetime.now().strftime("%H:%M:%S")
    e_d = int(end_time[0:2]) * 3600 + int(end_time[3:5]) * 60 + int(end_time[6:])
    s_t = int(start_time_compact[0:2]) * 3600 + int(start_time_compact[3:5]) * 60 + int(start_time_compact[6:])
    total_time = e_d - s_t
    return total_time


def game(dict):
    '''
    游戏的主函数
    从word list中随机选取一个单词放入word_chosen变量中，再创建word_list变量存放相同个数的下划线
    :param dict:
    :return: none
    '''

    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    start_time_compact = datetime.now().strftime("%H:%M:%S")

    word_chosen = dict[random.randint(0, len(dict) - 1)]
    #word_chosen = 'smart'                                   ##WIN时的测试单词
    word_chosen=list(word_chosen)
    jiaoshoujia_step = 0
    word_list = ['_'*int((i+1)/(i+1)) for i in range(len(word_chosen))]


    ##游戏主循环， 到绞首架第六步后自动退出循环
    while jiaoshoujia_step < 7:
        print('*'*60)
        print('mistakes:', jiaoshoujia_step)
        if word_list == word_chosen:
            print('YOU WIN')
            break
        while True:
            letter = input('请输入一个小写字母:')
            if 'a' <= letter <= 'z':
                if letter in word_list:
                    print('这个字母你已经输过了，请重新输入')
                else:
                    break

            else:
                print('输入有误，请重新输入...')

        ##若字母存在，把下划线改成该字母，若不存在，绞首架多加一笔
        if letter in word_chosen:
            for j in range(len(word_chosen)):
                if word_chosen[j] == letter:
                    word_list[j] = letter
            new_word_list = ' '.join(word_list)
            hm.print_hangman(new_word_list, jiaoshoujia_step)

        else:
            new_word_list = ' '.join(word_list)
            jiaoshoujia_step += 1
            hm.print_hangman(new_word_list, jiaoshoujia_step)
            if jiaoshoujia_step == 6:
                print('YOU LOSE')
                break

    return [start_time, count_total_time(start_time_compact), ''.join(word_chosen), ' '.join(word_list)]


def main():
    '''
    先判断csv文件是否存在，再分情况循环game函数
    :return:
    '''
    word_dict = make_WordDict('words.txt')
    if os.path.exists(os.getcwd() + '/guess.csv') == True :
        with open('guess.csv', 'a') as guess_file:
            while True:
                info = game(word_dict)
                writer = csv.writer(guess_file)
                writer.writerow(info)

                continue_game = input('Do you want to play again?(y/n)')
                if continue_game == 'y' or continue_game == 'Y':
                    continue
                else:
                    break

    else:
        with open('guess.csv', 'w') as guess_file:
            n = -1
            while True:
                n += 1
                info = game(word_dict)
                writer = csv.writer(guess_file)
                if n < 1:
                    fileHeader = ['游戏开始的时间', '单次游戏使用的时间(s)', '猜测的单词', '用户猜测的字符序列']
                    writer.writerow(fileHeader)
                writer.writerow(info)

                continue_game = input('Do you want to play again?(y/n)')
                if continue_game == 'y' or continue_game == 'Y':
                    continue
                else:
                    break


if __name__ == '__main__':
    main()
