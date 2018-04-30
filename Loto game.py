
# coding: utf-8

import random

#create a list of empty cells  
def empty_cells():
    empty_cell = []
    for i in range(4):
        number_cell = random.randint(1,9)
        while number_cell in empty_cell:
                number_cell = random.randint(1,9)
        empty_cell.append(number_cell)
    return empty_cell

#cheak if element in a card   
def check_card(card, cell):
    in_card = False
    for line in card:
        if cell in line:
            return True
    return False
       
#creation of cards
def create_card():
    card = [[0 for j in range(9)] for i in range(3)]
    for i in range(3):
        empty_cell = empty_cells()
        cell_list = []
        for j in range(5):
            cell = random.randint(1,90)
            in_card = check_card(card, cell)
            while cell in cell_list or  in_card:
                cell = random.randint(1,90)
                in_card = False
                in_card = check_card(card, cell)
            cell_list.append(cell)
        cell_list.sort()
        g = 0
        for k in range(1,10):
            if k in empty_cell:
                card[i][k-1] = '  '
            else:
                card[i][k-1] = cell_list[g]
                g += 1
    return card
card = create_card()

def output_card(card):
    for line in card:
        for element in line:
            if len(str(element)) < 2:
                print(' {} '.format(element), end = '')
            else:
                print('{} '.format(element), end = '')
        print('\n')


def cross_number(card, number):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == number:
                card[i][j] = '--'

# game process
def loto_game(card_plr, card_cmp):

    right_answer_plr = 0
    right_answer_cmp = 0
    list_lato = []
    for i in range(90):
        print('Ваша карточка')
        output_card(card_plr)
    
        print('Карточка компьютера')
        output_card(card_cmp)
    
        number = random.randint(1,90)
        while number in list_lato:
            number = random.randint(1,90)
        list_lato.append(number)
        print('Новый бочонок: {} (осталось {})'.format(number, 90-len(list_lato)))
        
        while True:
            try:
                answer = int(input('1.Зачеркнуть\n'
                                  '2.продолжить'))
                break 
            except ValueError:
                print('Неверный формат вода')
             

        if answer == 1 and check_card(card_plr, number):
            right_answer_plr += 1
            cross_number(card_plr, number)
        elif answer == 1 and not check_card(card_plr, number):
            print('Вы проиграли')
            break
        elif answer == 2 and check_card(card_plr, number):
            print('Вы проиграли')
            break
                
        if check_card(card_cmp, number):
            right_answer_cmp += 1
            cross_number(card_cmp, number)
            
        if right_answer_cmp == 15 and right_answer_plr == 15:
            print('Ничья')
            break
        elif right_answer_plr == 15:
            print('Игрок победил')
            break
        if right_answer_cmp == 15:
            print('Компьютер победил')
            break         
                

card_plr = create_card()

card_cmp = create_card()

loto_game(card_plr, card_cmp)

