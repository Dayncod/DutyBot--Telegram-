import pyodbc
import telebot
import re

from telebot import types

class Presence:

    students = [
        "Барков В.Е.",
        "Берчун Д.А.", 
        "Гаврилов Н.А.", 
        "Горяйнов Т.А.", 
        "Дубицкий Д.С.", 
        "Зарубайлова А.А.", 
        "Кабаркдин С.А.", 
        "Ленков Н.О.", 
        "Мельников Г.В.", 
        "Мельниченко Д.В.",
        "Новохатько К.А.",
        "Пищальноков Д.А.",
        "Плащевский Е.К.",
        "Русов Г.А.",
        "Рябов М.Е.",
        "Савин М.А.",
        "Селивёрстов А.И.",
        "Сидорчук О.В.",
        "Фёдоров С.Е.",
        "Филиппенко А. Н.",
        "Хандримайло Д.В.",
        "Чеверда Я.А.",
        "Шкурдюк С.А.",
        "Шпунтова П.В."]

    callbackButton1 = types.InlineKeyboardButton(text='Барков В.Е.', callback_data='1')
    callbackButton2 = types.InlineKeyboardButton(text='Берчун Д.А.', callback_data='2')
    callbackButton3 = types.InlineKeyboardButton(text='Гаврилов Н.А.', callback_data='3')
    callbackButton4 = types.InlineKeyboardButton(text='Горяйнов Т.А.', callback_data='4')

    callbackButton5 = types.InlineKeyboardButton(text='Дубицкий Д.С.', callback_data='5')
    callbackButton6 = types.InlineKeyboardButton(text='Зарубайлова А.А.', callback_data='6')
    callbackButton7 = types.InlineKeyboardButton(text='Кабаркдин С.А.', callback_data='7')
    callbackButton8 = types.InlineKeyboardButton(text='Ленков Н.О.', callback_data='8')

    callbackButton9 = types.InlineKeyboardButton(text='Мельников Г.В.', callback_data='9')
    callbackButton10 = types.InlineKeyboardButton(text='Мельниченко Д.В.', callback_data='10')
    callbackButton11 = types.InlineKeyboardButton(text='Новохатько К.А.', callback_data='11')
    callbackButton12 = types.InlineKeyboardButton(text='Пищальноков Д.А.', callback_data='12')

    callbackButton13 = types.InlineKeyboardButton(text='Плащевский Е.К.', callback_data='13')
    callbackButton14 = types.InlineKeyboardButton(text='Русов Г.А.', callback_data='14')
    callbackButton15 = types.InlineKeyboardButton(text='Рябов М.Е.', callback_data='15')
    callbackButton16 = types.InlineKeyboardButton(text='Савин М.А.', callback_data='16')

    callbackButton17 = types.InlineKeyboardButton(text='Селивёрстов А.И.', callback_data='17')
    callbackButton18 = types.InlineKeyboardButton(text='Сидорчук О.В.', callback_data='18')
    callbackButton19 = types.InlineKeyboardButton(text='Фёдоров С.Е.', callback_data='19')
    callbackButton20 = types.InlineKeyboardButton(text='Филиппенко А. Н.', callback_data='20')

    callbackButton21 = types.InlineKeyboardButton(text='Хандримайло Д.В.', callback_data='21')
    callbackButton22 = types.InlineKeyboardButton(text='Чеверда Я.А.', callback_data='22')
    callbackButton23 = types.InlineKeyboardButton(text='Шкурдюк С.А.', callback_data='23')
    callbackButton24 = types.InlineKeyboardButton(text='Шпунтова П.В.', callback_data='24')

    callbackList = [callbackButton1, callbackButton2, callbackButton3,
                    callbackButton4, callbackButton5, callbackButton6,
                    callbackButton7, callbackButton8, callbackButton9,
                    callbackButton10, callbackButton11, callbackButton12,
                    callbackButton13, callbackButton14, callbackButton15,
                    callbackButton16, callbackButton17, callbackButton18,
                    callbackButton19, callbackButton20, callbackButton21,
                    callbackButton22, callbackButton23, callbackButton24]

    callbackButtonComplete = types.InlineKeyboardButton(text='Подтвердить', callback_data='Confirmation')

    
    def List():
        keyboard = types.InlineKeyboardMarkup(row_width=3)

        keyboard.add(Presence.callbackButton1, Presence.callbackButton2, Presence.callbackButton3)
        keyboard.add(Presence.callbackButton4, Presence.callbackButton5, Presence.callbackButton6)
        keyboard.add(Presence.callbackButton7, Presence.callbackButton8, Presence.callbackButton9)
        keyboard.add(Presence.callbackButton10, Presence.callbackButton11, Presence.callbackButton12)
        keyboard.add(Presence.callbackButton13, Presence.callbackButton14, Presence.callbackButton15)
        keyboard.add(Presence.callbackButton16, Presence.callbackButton17, Presence.callbackButton18)
        keyboard.add(Presence.callbackButton19, Presence.callbackButton20, Presence.callbackButton21)
        keyboard.add(Presence.callbackButton22, Presence.callbackButton23, Presence.callbackButton24)
        keyboard.add(Presence.callbackButtonComplete)

        return keyboard
    
    def EditList(callback_data):
        for i in range(23):
            if(callback_data == str(i)):
                keyboard = types.InlineKeyboardMarkup(row_width=3)
                Presence.callbackList[i + 1] = types.InlineKeyboardButton(text=f'~{Presence.students[i]}~', callback_data=f'-{i + 1}')
                keyboard.add(Presence.callbackButton1, Presence.callbackButton2, Presence.callbackButton3)
                keyboard.add(Presence.callbackButton4, Presence.callbackButton5, Presence.callbackButton6)
                keyboard.add(Presence.callbackButton7, Presence.callbackButton8, Presence.callbackButton9)
                keyboard.add(Presence.callbackButton10, Presence.callbackButton11, Presence.callbackButton12)
                keyboard.add(Presence.callbackButton13, Presence.callbackButton14, Presence.callbackButton15)
                keyboard.add(Presence.callbackButton16, Presence.callbackButton17, Presence.callbackButton18)
                keyboard.add(Presence.callbackButton19, Presence.callbackButton20, Presence.callbackButton21)
                keyboard.add(Presence.callbackButton22, Presence.callbackButton23, Presence.callbackButton24)
                keyboard.add(Presence.callbackButtonComplete)
                return keyboard


        
        # if(callback_data == '1'):
        #     keyboard = types.InlineKeyboardMarkup(row_width=3)
        #     Presence.callbackButton1 = types.InlineKeyboardButton(text='~Барков В.Е.~', callback_data='-1')
        #     keyboard.add(Presence.callbackButton1, Presence.callbackButton2, Presence.callbackButton3)
        #     keyboard.add(Presence.callbackButton4, Presence.callbackButton5, Presence.callbackButton6)
        #     keyboard.add(Presence.callbackButton7, Presence.callbackButton8, Presence.callbackButton9)
        #     keyboard.add(Presence.callbackButton10, Presence.callbackButton11, Presence.callbackButton12)
        #     keyboard.add(Presence.callbackButton13, Presence.callbackButton14, Presence.callbackButton15)
        #     keyboard.add(Presence.callbackButton16, Presence.callbackButton17, Presence.callbackButton18)
        #     keyboard.add(Presence.callbackButton19, Presence.callbackButton20, Presence.callbackButton21)
        #     keyboard.add(Presence.callbackButton22, Presence.callbackButton23, Presence.callbackButton24)
        #     keyboard.add(Presence.callbackButtonComplete)
        #     return keyboard
        # elif(callback_data == '-1'):
        #     keyboard = types.InlineKeyboardMarkup(row_width=3)
        #     Presence.callbackButton1 = types.InlineKeyboardButton(text='Барков В.Е.', callback_data='1')
        #     keyboard.add(Presence.callbackButton1, Presence.callbackButton2, Presence.callbackButton3)
        #     keyboard.add(Presence.callbackButton4, Presence.callbackButton5, Presence.callbackButton6)
        #     keyboard.add(Presence.callbackButton7, Presence.callbackButton8, Presence.callbackButton9)
        #     keyboard.add(Presence.callbackButton10, Presence.callbackButton11, Presence.callbackButton12)
        #     keyboard.add(Presence.callbackButton13, Presence.callbackButton14, Presence.callbackButton15)
        #     keyboard.add(Presence.callbackButton16, Presence.callbackButton17, Presence.callbackButton18)
        #     keyboard.add(Presence.callbackButton19, Presence.callbackButton20, Presence.callbackButton21)
        #     keyboard.add(Presence.callbackButton22, Presence.callbackButton23, Presence.callbackButton24)
        #     keyboard.add(Presence.callbackButtonComplete)
        #     return keyboard
        
        
