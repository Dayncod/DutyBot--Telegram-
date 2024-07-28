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

    callbackButton1 = types.InlineKeyboardButton(text='Барков В.Е.', callback_data='0')
    callbackButton2 = types.InlineKeyboardButton(text='Берчун Д.А.', callback_data='1')
    callbackButton3 = types.InlineKeyboardButton(text='Гаврилов Н.А.', callback_data='2')
    callbackButton4 = types.InlineKeyboardButton(text='Горяйнов Т.А.', callback_data='3')

    callbackButton5 = types.InlineKeyboardButton(text='Дубицкий Д.С.', callback_data='4')
    callbackButton6 = types.InlineKeyboardButton(text='Зарубайлова А.А.', callback_data='5')
    callbackButton7 = types.InlineKeyboardButton(text='Кабаркдин С.А.', callback_data='6')
    callbackButton8 = types.InlineKeyboardButton(text='Ленков Н.О.', callback_data='7')

    callbackButton9 = types.InlineKeyboardButton(text='Мельников Г.В.', callback_data='8')
    callbackButton10 = types.InlineKeyboardButton(text='Мельниченко Д.В.', callback_data='9')
    callbackButton11 = types.InlineKeyboardButton(text='Новохатько К.А.', callback_data='10')
    callbackButton12 = types.InlineKeyboardButton(text='Пищальноков Д.А.', callback_data='11')

    callbackButton13 = types.InlineKeyboardButton(text='Плащевский Е.К.', callback_data='12')
    callbackButton14 = types.InlineKeyboardButton(text='Русов Г.А.', callback_data='13')
    callbackButton15 = types.InlineKeyboardButton(text='Рябов М.Е.', callback_data='14')
    callbackButton16 = types.InlineKeyboardButton(text='Савин М.А.', callback_data='15')

    callbackButton17 = types.InlineKeyboardButton(text='Селивёрстов А.И.', callback_data='16')
    callbackButton18 = types.InlineKeyboardButton(text='Сидорчук О.В.', callback_data='17')
    callbackButton19 = types.InlineKeyboardButton(text='Фёдоров С.Е.', callback_data='18')
    callbackButton20 = types.InlineKeyboardButton(text='Филиппенко А. Н.', callback_data='19')

    callbackButton21 = types.InlineKeyboardButton(text='Хандримайло Д.В.', callback_data='20')
    callbackButton22 = types.InlineKeyboardButton(text='Чеверда Я.А.', callback_data='21')
    callbackButton23 = types.InlineKeyboardButton(text='Шкурдюк С.А.', callback_data='22')
    callbackButton24 = types.InlineKeyboardButton(text='Шпунтова П.В.', callback_data='23')

    callbackButtonComplete = types.InlineKeyboardButton(text='Подтвердить', callback_data='Confirmation')
    callbackButtonReset = types.InlineKeyboardButton(text='Сбросить', callback_data='Reset')

    callbackList = [callbackButton1, callbackButton2, callbackButton3,
                    callbackButton4, callbackButton5, callbackButton6,
                    callbackButton7, callbackButton8, callbackButton9,
                    callbackButton10, callbackButton11, callbackButton12,
                    callbackButton13, callbackButton14, callbackButton15,
                    callbackButton16, callbackButton17, callbackButton18,
                    callbackButton19, callbackButton20, callbackButton21,
                    callbackButton22, callbackButton23, callbackButton24]
    
    def List():
        keyboard = types.InlineKeyboardMarkup(row_width=3)

        keyboard.add(Presence.callbackList[0], Presence.callbackList[1], Presence.callbackList[2])
        keyboard.add(Presence.callbackList[3], Presence.callbackList[4], Presence.callbackList[5])
        keyboard.add(Presence.callbackList[6], Presence.callbackList[7], Presence.callbackList[8])
        keyboard.add(Presence.callbackList[9], Presence.callbackList[10], Presence.callbackList[11])
        keyboard.add(Presence.callbackList[12], Presence.callbackList[13], Presence.callbackList[14])
        keyboard.add(Presence.callbackList[15], Presence.callbackList[16], Presence.callbackList[17])
        keyboard.add(Presence.callbackList[18], Presence.callbackList[19], Presence.callbackList[20])
        keyboard.add(Presence.callbackList[21], Presence.callbackList[22], Presence.callbackList[23])
        keyboard.add(Presence.callbackButtonComplete)
        keyboard.add(Presence.callbackButtonReset)
        return keyboard
    
    def EditList(callback_data):
        for i in range(len(Presence.students)):
            if(callback_data == str(i)):
                callbackButtonN = types.InlineKeyboardButton(text=f'~|{Presence.students[i]}|~', callback_data=f'-{i}')
                # callbackButtonN = types.InlineKeyboardButton(text= '-1', callback_data=f'-{i}')
                Presence.callbackList[i] = callbackButtonN
                modifiedKeyboard = Presence.List()
                return modifiedKeyboard
            elif(callback_data == '-' + str(i)):
                callbackButtonN = types.InlineKeyboardButton(text=f'{Presence.students[i]}', callback_data=f'{i}')
                # callbackButtonN = types.InlineKeyboardButton(text= '1', callback_data=f'{i}')
                Presence.callbackList[i] = callbackButtonN
                modifiedKeyboard = Presence.List()
                return modifiedKeyboard
        
        
