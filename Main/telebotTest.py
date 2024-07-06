import random
import pyodbc
import telebot
import re
from telebot import types

bot = telebot.TeleBot('6366348527:AAFcFWXB57aK06gZFdRn-Bdc0YNVcijb0C0')

key = "DRIVER={SQL Server}; SERVER=DESKTOP-SMAKMB9\DIMONSQLSERVER; DATABASE=Customers; Trusted_Connection=yes;"

connect = pyodbc.connect(key)
cursor = connect.cursor()

class Student:
 def __init__(self, id, name): 
  self.id = id
  self.name = name

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
  "Шпунтова П.В."
          ]

@bot.message_handler(commands=['start'])
def choose_start(message):
  connect = pyodbc.connect(key)

  std = Student(message.chat.id, message.from_user.first_name)
  Buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

  cursor.execute(f"SELECT CASE WHEN EXISTS(SELECT 1 FROM Users WHERE id = {std.id}) THEN 1 ELSE 0 END")
  answer = re.sub("[^0-9]", "", str(cursor.fetchall()))
  if(int(answer) == 0):
    cursor.execute(f"INSERT Users(ID, MAIN_NAME, USER_STATUS) VALUES ({std.id}, '{std.name}', 'user')")
    cursor.commit()
    connect.close()
    print(f"Регистрация Пользователя {std.name}: [{std.id}, user] прошла успешно")
  elif(int(answer) == 1):
    cursor.execute(f"SELECT CASE WHEN EXISTS(SELECT 1 FROM Users WHERE USER_STATUS = 'user' and ID = {std.id}) THEN 1 ELSE 0 END")
    answer1 = re.sub("[^0-9]", "", str(cursor.fetchall()))
    if(int(answer1) == 1):
      connect.close()
      print(f'Пользователь {std.name}: [{std.id}, user] уже зарегистрирован')
    elif(int(answer1) == 0):
      cursor.execute(f"UPDATE Users SET USER_STATUS = 'adm' WHERE ID = {std.id}")
      cursor.commit()
      connect.close()
      print(f'Пользователь {std.name}: [{std.id}, adm] уже зарегистрирован')

  connect = pyodbc.connect(key)
  cursor.execute(f"SELECT CASE WHEN EXISTS(SELECT 1 FROM Users WHERE USER_STATUS = 'user' and ID = {std.id}) THEN 1 ELSE 0 END")
  answer2 = re.sub("[^0-9]", "", str(cursor.fetchall()))
  if(int(answer2) == 1):
    btn1 = types.KeyboardButton('Список присутствующих')
    btn2 = types.KeyboardButton('Кто дежурит')
    Buttons.add(btn1, btn2)
  elif(int(answer2) == 0):
    btn1 = types.KeyboardButton('Список присутствующих')
    btn2 = types.KeyboardButton('Кто дежурит')
    btn3 = types.KeyboardButton('Изменить список присутствующих')
    Buttons.add(btn1, btn2)
    Buttons.add(btn3)
  connect.close()
  bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я бот-дежурный для группы З-3-9Б-21, что ты хочешь узнать?', reply_markup=Buttons)


@bot.message_handler(content_types=['text'])
def choose_duty(message):

  std = Student(message.chat.id, message.from_user.first_name)

  connect = pyodbc.connect(key)
  cursor.execute(f"SELECT CASE WHEN EXISTS(SELECT 1 FROM Users WHERE USER_STATUS = 'user' and ID = {std.id}) THEN 1 ELSE 0 END")
  answer3 = re.sub("[^0-9]", "", str(cursor.fetchall()))
  if(message.text == 'Список присутствующих'):
    StdString = ''
    for i in range(len(students)):
      StdString += (str((i + 1)) + '. ' + students[i] + ' \n')
    bot.send_message(message.chat.id, f'{StdString}')     
  elif(message.text == 'Кто дежурит'):
    duty_pair = random.sample(students, 2)
    bot.send_message(message.chat.id, f"Дежурят: {duty_pair[0]}, {duty_pair[1]}")
  elif(message.text == 'Изменить список присутствующих'):
    if(int(answer3) == 0):
      keyboard = types.InlineKeyboardMarkup(row_width=4)

      callbackButton1 = types.InlineKeyboardButton(text='Барков В.Е.', callback_data='test')
      callbackButton2 = types.InlineKeyboardButton(text='Берчун Д.А.', callback_data='test')
      callbackButton3 = types.InlineKeyboardButton(text='Гаврилов Н.А.', callback_data='test')
      callbackButton4 = types.InlineKeyboardButton(text='Горяйнов Т.А.', callback_data='test')

      callbackButton5 = types.InlineKeyboardButton(text='Дубицкий Д.С.', callback_data='test')
      callbackButton6 = types.InlineKeyboardButton(text='Зарубайлова А.А.', callback_data='test')
      callbackButton7 = types.InlineKeyboardButton(text='Кабаркдин С.А.', callback_data='test')
      callbackButton8 = types.InlineKeyboardButton(text='Ленков Н.О.', callback_data='test')

      callbackButton9 = types.InlineKeyboardButton(text='Мельников Г.В.', callback_data='test')
      callbackButton10 = types.InlineKeyboardButton(text='Мельниченко Д.В.', callback_data='test')
      callbackButton11 = types.InlineKeyboardButton(text='Новохатько К.А.', callback_data='test')
      callbackButton12 = types.InlineKeyboardButton(text='Пищальноков Д.А.', callback_data='test')

      callbackButton13 = types.InlineKeyboardButton(text='Плащевский Е.К.', callback_data='test')
      callbackButton14 = types.InlineKeyboardButton(text='Русов Г.А.', callback_data='test')
      callbackButton15 = types.InlineKeyboardButton(text='Рябов М.Е.', callback_data='test')
      callbackButton16 = types.InlineKeyboardButton(text='Савин М.А.', callback_data='test')

      callbackButton17 = types.InlineKeyboardButton(text='Селивёрстов А.И.', callback_data='test')
      callbackButton18 = types.InlineKeyboardButton(text='Сидорчук О.В.', callback_data='test')
      callbackButton19 = types.InlineKeyboardButton(text='Фёдоров С.Е.', callback_data='test')
      callbackButton20 = types.InlineKeyboardButton(text='Филиппенко А. Н.', callback_data='test')

      callbackButton21 = types.InlineKeyboardButton(text='Хандримайло Д.В.', callback_data='test')
      callbackButton22 = types.InlineKeyboardButton(text='Чеверда Я.А.', callback_data='test')
      callbackButton23 = types.InlineKeyboardButton(text='Шкурдюк С.А.', callback_data='test')
      callbackButton24 = types.InlineKeyboardButton(text='Шпунтова П.В.', callback_data='test')

      callbackButtonComplete = types.InlineKeyboardButton(text='Подтвердить', callback_data='text')

      keyboard.add(callbackButton1, callbackButton2, callbackButton3, callbackButton4)
      keyboard.add(callbackButton5, callbackButton6, callbackButton7, callbackButton8)
      keyboard.add(callbackButton9, callbackButton10, callbackButton11, callbackButton12)
      keyboard.add(callbackButton13, callbackButton14, callbackButton15, callbackButton16)
      keyboard.add(callbackButton17, callbackButton18, callbackButton19, callbackButton20)
      keyboard.add(callbackButton21, callbackButton22, callbackButton23, callbackButton24)

      keyboard.add(callbackButtonComplete)
      bot.send_message(message.chat.id, 'Измените список присутствующих', reply_markup=keyboard)
    else:
      bot.send_message(message.chat.id, 'Недостаточно прав доступа')   
  else:
    bot.send_message(message.chat.id, 'Неизвестная команда') 
 # @bot.callback_query_handler()

bot.polling(none_stop=True, interval=0)






