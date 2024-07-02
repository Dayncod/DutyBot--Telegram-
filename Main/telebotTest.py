import random
import pyodbc
import telebot
from telebot import types

bot = telebot.TeleBot('6366348527:AAFcFWXB57aK06gZFdRn-Bdc0YNVcijb0C0')

connect = pyodbc.connect("DRIVER={SQL Server}; SERVER=DESKTOP-SMAKMB9\DIMONSQLSERVER; DATABASE=Customers; UID=DESKTOP-SMAKMB9\dimon; PWD=password")
cursor = connect.cursor()

class Student:
 def __init__(self, id, name, status): 
  self.id = id
  self.name = name
  self.status = str(status)

admins = [1997074173, 1113636604]

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
  std = Student(message.chat.id, message.from_user.first_name, 'user')
  Buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
  if(std.id in admins):
    std.status = 'adm'
    btn1 = types.KeyboardButton('Список присутствующих')
    btn2 = types.KeyboardButton('Кто дежурит')
    btn3 = types.KeyboardButton('Изменить список присутсвующих')
    Buttons.add(btn1, btn2, btn3)
  else:
    btn1 = types.KeyboardButton('Список присутствующих')
    btn2 = types.KeyboardButton('Кто дежурит')
    Buttons.add(btn1, btn2)

  bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я бот-дежурный для группы З-3-9Б-21, что ты хочешь узнать?', reply_markup=Buttons)
  print(f'Пользователь {std.name}: {std.id}, {std.status}')


@bot.message_handler(content_types=['text'])
def choose_duty(message):
  if(message.text == 'Список присутствующих'):
    for i in range(len(students)):
      bot.send_message(message.chat.id, f'{i + 1}. {students[i]}')
  elif(message.text == 'Кто дежурит'):
    duty_pair = random.sample(students, 2)
    bot.send_message(message.chat.id, f"Дежурят: {duty_pair[0]}, {duty_pair[1]}")
  elif(message.text == 'Изменить список присутсвующих'):
    cursor.execute('SELECT * FROM Users')

bot.polling(none_stop=True, interval=0)






