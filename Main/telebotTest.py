import random
import pyodbc
import telebot
import re

import PresenceList

from telebot import types

bot = telebot.TeleBot('6366348527:AAFcFWXB57aK06gZFdRn-Bdc0YNVcijb0C0')

key = "DRIVER={SQL Server}; SERVER=DESKTOP-SMAKMB9\DIMONSQLSERVER; DATABASE=Customers; Trusted_Connection=yes;"

PL = PresenceList.Presence

connect = pyodbc.connect(key)
cursor = connect.cursor()

class Student:
 def __init__(self, id, name): 
  self.id = id
  self.name = name
  self.Presence = True

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
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я бот-дежурный для группы З-3-9Б-21, что ты хочешь узнать?', reply_markup=Buttons)
  elif(int(answer2) == 0):
    btn1 = types.KeyboardButton('Список присутствующих')
    btn2 = types.KeyboardButton('Кто дежурит')
    btn3 = types.KeyboardButton('Изменить список присутствующих')
    Buttons.add(btn1, btn2)
    Buttons.add(btn3)
    bot.send_message(message.chat.id, f'Здравствуйте, Администратор {message.from_user.first_name}', reply_markup=Buttons)

  connect.close()
  


@bot.message_handler(content_types=['text'])
def choose_command(message):

  std = Student(message.chat.id, message.from_user.first_name)

  connect = pyodbc.connect(key)
  cursor.execute(f"SELECT CASE WHEN EXISTS(SELECT 1 FROM Users WHERE USER_STATUS = 'user' and ID = {std.id}) THEN 1 ELSE 0 END")
  answer3 = re.sub("[^0-9]", "", str(cursor.fetchall()))
  connect.close()

  if(message.text == 'Список присутствующих'):
    StdString = PL.ShowStringList()
    bot.send_message(message.chat.id, f'{StdString}')
    # bot.edit_message_text(chat_id = message.chat.id, message_id = message.message_id, text=f'{StdString}')


  elif(message.text == 'Кто дежурит'):
    duty_pair = random.sample(students, 2)
    bot.send_message(message.chat.id, f"Дежурят: {duty_pair[0]}, {duty_pair[1]}")
  elif(message.text == 'Изменить список присутствующих'):

    if(int(answer3) == 0):
      keyboard = PL.List()
      bot.send_message(message.chat.id, 'Таблица присутствующих', reply_markup=keyboard)
    else:
      bot.send_message(message.chat.id, 'Недостаточно прав доступа')   

  else:
    bot.send_message(message.chat.id, 'Неизвестная команда') 

  @bot.callback_query_handler(func=lambda call: True)
  def callback(call):
      Editkeyboard = PL.EditList(call.data)
      bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text='Таблица присутствующих', reply_markup=Editkeyboard)

bot.polling(none_stop=True, interval=0)






