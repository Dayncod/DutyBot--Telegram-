import pyodbc
import csv
import telebot
import re

import PresenceList

from telebot import types

PL = PresenceList.Presence

bot = telebot.TeleBot('6366348527:AAFcFWXB57aK06gZFdRn-Bdc0YNVcijb0C0')

key = "DRIVER={SQL Server}; SERVER=DESKTOP-SMAKMB9\\DIMONSQLSERVER; DATABASE=Customers; Trusted_Connection=yes;"

connect = pyodbc.connect(key)
cursor = connect.cursor()

class Student:
 def __init__(self, id, name): 
  self.id = id
  self.name = name
  self.Presence = True

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
    btn3 = types.KeyboardButton('Скачать таблицу дежурств')
    Buttons.add(btn1, btn2)
    Buttons.add(btn3)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я бот-дежурный для группы З-3-9Б-21, что ты хочешь узнать?', reply_markup=Buttons)
  elif(int(answer2) == 0):
    btn1 = types.KeyboardButton('Список присутствующих')
    btn2 = types.KeyboardButton('Кто дежурит')
    btn3 = types.KeyboardButton('Изменить список присутствующих')
    btn4 = types.KeyboardButton('Скачать таблицу дежурств')
    Buttons.add(btn1, btn2)
    Buttons.add(btn3, btn4)
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
    connect = pyodbc.connect(key)
    cursor.execute("SELECT TOP 2 BUTTON_TEXT FROM Duty_List WHERE Duty_Count = (SELECT MIN(Duty_Count) FROM Duty_List) ORDER BY BUTTON_TEXT")
    answer4 = ""
    for i in cursor.fetchall():
      answer4 += (re.sub("[^А-Яа-я. ]", "", str(i)) + ' и ')

    keyboard = types.InlineKeyboardMarkup()
    saveButton = types.InlineKeyboardButton(text='Сохранить', callback_data='Save')
    keyboard.add(saveButton)
    
    bot.send_message(message.chat.id, f"Сегодня дежурят: *{answer4[:-3]}*", reply_markup=keyboard, parse_mode='Markdown')
    connect.close()

  elif(message.text == 'Скачать таблицу дежурств'):
    bot.send_message(message.chat.id, 'дЕРЖИ')


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
      if(call.data == 'Save'):
        connect = pyodbc.connect(key)
        cursor.execute("SELECT TOP 2 BUTTON_TEXT FROM Duty_List WHERE Duty_Count = (SELECT MIN(Duty_Count) FROM Duty_List) ORDER BY BUTTON_TEXT")
        answer5 = ''
        answer6 = ''
        num = 0
        for i in cursor.fetchall():
          num += 1
          if(num == 1):
            answer5 = (re.sub("[^А-Яа-я. ]", "", str(i)))
            cursor.execute(f"UPDATE Duty_List SET Duty_Count = ((SELECT TOP 1 Duty_Count FROM Duty_List WHERE Duty_Count = 0) + 1) WHERE BUTTON_TEXT = '{answer5}'")
            cursor.commit()
          else:
            answer6 = (re.sub("[^А-Яа-я. ]", "", str(i)))
            cursor.execute(f"UPDATE Duty_List SET Duty_Count = ((SELECT TOP 1 Duty_Count FROM Duty_List WHERE Duty_Count = 0) + 1) WHERE BUTTON_TEXT = '{answer6}'")
            cursor.commit()
        connect.close()
      else:
        Editkeyboard = PL.EditList(call.data)
        bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text='Таблица присутствующих', reply_markup=Editkeyboard)

bot.polling(none_stop=True, interval=0)






