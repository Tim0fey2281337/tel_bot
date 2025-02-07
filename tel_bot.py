from telegram import ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import random
from class_answers import Otveti

# Задаём константы для этапов теста
QU1, QU2, QU3, QU4, QU5, QU6, QU7, QU8, M1, M2, M3, M4 = range(12)
W1, W2, W3, W4, P1, P2, P3, P4 = range(12, 20)


# Задаём клавиатуру для начала беседы
def st_key():
    start_keyboard = [['/go', '/help', '/commands']]
    start_key = ReplyKeyboardMarkup(start_keyboard, resize_keyboard=True)
    return start_key


# Задаём клавиатуру с вариантами ответов для 1 общего вопроса
def q_o_1():
    q_board = [[Otveti.q_o1[0]], [Otveti.q_o1[1]], [Otveti.q_o1[2]]]
    qo1_key = ReplyKeyboardMarkup(q_board, resize_keyboard=True)
    return qo1_key


# Задаём клавиатуру с вариантами ответов для 2 общего вопроса
def q_o_2():
    q2_board = [[Otveti.q_o2[0]], [Otveti.q_o2[1]], [Otveti.q_o2[2]]]
    qo2_key = ReplyKeyboardMarkup(q2_board, resize_keyboard=True)
    return qo2_key


# Задаём клавиатуру с вариантами ответов для 3 общего вопроса
def q_o_3():
    q3_board = [[Otveti.q_o3[0]], [Otveti.q_o3[1]]]
    qo3_key = ReplyKeyboardMarkup(q3_board, resize_keyboard=True)
    return qo3_key


# Задаём клавиатуру с вариантами ответов для 4 общего вопроса
def q_o_4():
    q4_board = [[Otveti.q_o4[0]], [Otveti.q_o4[1]], [Otveti.q_o4[2]]]
    qo4_key = ReplyKeyboardMarkup(q4_board, resize_keyboard=True)
    return qo4_key


# Задаём клавиатуру с вариантами ответов для 5 общего вопроса
def q_o_5():
    q5_board = [[Otveti.q_o5[0]], [Otveti.q_o5[1]], [Otveti.q_o5[2]]]
    qo5_key = ReplyKeyboardMarkup(q5_board, resize_keyboard=True)
    return qo5_key


# Задаём клавиатуру с вариантами ответов для 6 общего вопроса
def q_o_6():
    q6_board = [[Otveti.q_o6[0]], [Otveti.q_o6[1]], [Otveti.q_o6[2]]]
    qo6_key = ReplyKeyboardMarkup(q6_board, resize_keyboard=True)
    return qo6_key


# Задаём клавиатуру с вариантами ответов для 7 общего вопроса
def q_o_7():
    q7_board = [[Otveti.q_o7[0]], [Otveti.q_o7[1]], [Otveti.q_o7[2]]]
    qo7_key = ReplyKeyboardMarkup(q7_board, resize_keyboard=True)
    return qo7_key


# Задаём клавиатуру с вариантами ответов для 8 общего вопроса
def q_o_8():
    q8_board = [[Otveti.q_o8[0]], [Otveti.q_o8[1]], [Otveti.q_o8[2]]]
    qo8_key = ReplyKeyboardMarkup(q8_board, resize_keyboard=True)
    return qo8_key


# Задаём клавиатуру с вариантами ответов для 1 вопроса про монстров
def m_1():
    m1_board = [[Otveti.m_q1[0]], [Otveti.m_q1[1]], [Otveti.m_q1[2]]]
    m1_key = ReplyKeyboardMarkup(m1_board, resize_keyboard=True)
    return m1_key


# Задаём клавиатуру с вариантами ответов для 2 вопроса про монстров
def m_2():
    m2_board = [[Otveti.m_q2[0]], [Otveti.m_q2[1]], [Otveti.m_q2[2]]]
    m2_key = ReplyKeyboardMarkup(m2_board, resize_keyboard=True)
    return m2_key


# Задаём клавиатуру с вариантами ответов для 3 вопроса про монстров
def m_3():
    m3_board = [[Otveti.m_q3[0]], [Otveti.m_q3[1]], [Otveti.m_q3[2]]]
    m3_key = ReplyKeyboardMarkup(m3_board, resize_keyboard=True)
    return m3_key


# Задаём клавиатуру с вариантами ответов для 4 вопроса про монстров
def m_4():
    m4_board = [[Otveti.m_q4[0]], [Otveti.m_q4[1]], [Otveti.m_q4[2]]]
    m4_key = ReplyKeyboardMarkup(m4_board, resize_keyboard=True)
    return m4_key


# Задаём клавиатуру с вариантами ответов для 1 вопроса про колдунов
def w_1():
    w1_board = [[Otveti.w_q1[0]], [Otveti.w_q1[1]], [Otveti.w_q1[2]]]
    w1_key = ReplyKeyboardMarkup(w1_board, resize_keyboard=True)
    return w1_key


# Задаём клавиатуру с вариантами ответов для 2 вопроса про колдунов
def w_2():
    w2_board = [[Otveti.w_q2[0]], [Otveti.w_q2[1]], [Otveti.w_q2[2]]]
    w2_key = ReplyKeyboardMarkup(w2_board, resize_keyboard=True)
    return w2_key


# Задаём клавиатуру с вариантами ответов для 3 вопроса про колдунов
def w_3():
    w3_board = [[Otveti.w_q3[0]], [Otveti.w_q3[1]], [Otveti.w_q3[2]]]
    w3_key = ReplyKeyboardMarkup(w3_board, resize_keyboard=True)
    return w3_key


# Задаём клавиатуру с вариантами ответов для 4 вопроса про колдунов
def w_4():
    w4_board = [[Otveti.w_q4[0]], [Otveti.w_q4[1]], [Otveti.w_q4[2]]]
    w4_key = ReplyKeyboardMarkup(w4_board, resize_keyboard=True)
    return w4_key


# Задаём клавиатуру с вариантами ответов для 1 вопроса про потусторонних
def p_1():
    p1_board = [[Otveti.p_q1[0]], [Otveti.p_q1[1]], [Otveti.p_q1[2]]]
    p1_key = ReplyKeyboardMarkup(p1_board, resize_keyboard=True)
    return p1_key


# Задаём клавиатуру с вариантами ответов для 2 вопроса про потусторонних
def p_2():
    p2_board = [[Otveti.p_q2[0]], [Otveti.p_q2[1]], [Otveti.p_q2[2]]]
    p2_key = ReplyKeyboardMarkup(p2_board, resize_keyboard=True)
    return p2_key


# Задаём клавиатуру с вариантами ответов для 3 вопроса про потусторонних
def p_3():
    p3_board = [[Otveti.p_q3[0]], [Otveti.p_q3[1]], [Otveti.p_q3[2]]]
    p3_key = ReplyKeyboardMarkup(p3_board, resize_keyboard=True)
    return p3_key


# Задаём клавиатуру с вариантами ответов для 4 вопроса про потусторонних
def p_4():
    p4_board = [[Otveti.p_q4[0]], [Otveti.p_q4[1]], [Otveti.p_q4[2]]]
    p4_key = ReplyKeyboardMarkup(p4_board, resize_keyboard=True)
    return p4_key


# Функция начала работы бота
def start(update, context):
    # Приветственное сообщение
    update.message.reply_text('Привет!\nЧтобы узнать, какой ты монстр, '
                              'нажми /go или узнай больше о боте, нажав /help',
                              reply_markup=st_key())


# Функция начинающая тест
def go(update, context):
    # Сообщение с первым вопросом и вызов клавиатуры для него
    update.message.reply_text('Готов узнать, какой ты монстр? Тогда начинаем!\n'
                              'Какая сила тебе больше'
                              ' всего нравится?', reply_markup=q_o_1())
    # Переходим к этапу QU1
    return QU1


# Записываем в словарь данные о пользователе, чтобы определить
# потом к какому классу он относится
def zap_ans_ob(update, context):
    user = update.message.from_user.id
    ans_ob[user] = {'Монстры': 0,
                    'Колдуны и колдуньи': 0,
                    'Потусторонние': 0}


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu1(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o1[0]:
        ans_ob[user]['Монстры'] += 1
    if update.message.text == Otveti.q_o1[1]:
        ans_ob[user]['Колдуны и колдуньи'] += 1
    if update.message.text == Otveti.q_o1[2]:
        ans_ob[user]['Потусторонние'] += 1


# Функция проверяющая ответ на 1 вопрос и задающая следующий
def qu1(update, context):
    user = update.message.from_user.id
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o1:
        # Если пользователя нет в словаре добаляем его туда:
        if user not in ans_ob:
            # Добавляем его в словарь
            zap_ans_ob(update, context)
            # Вызов функции обрабатывающей ответ
            prov_qu1(update, context)
            # Сообщение со следующем вопросом
            update.message.reply_text('Ты ночное или дневное существо?',
                                      reply_markup=q_o_2())
            # Переходим к этапу QU2
            return QU2
        # Если он уже в словаре то занулюем его значения ответов
        else:
            # Добавляем его в словарь
            zap_ans_ob(update, context)
            # Функция обрабатывающая корректный ответ и добаляющая
            # +1 к одному из классов
            prov_qu1(update, context)
            # Сообщение со следующем вопросом
            update.message.reply_text('Ты ночное или дневное существо?',
                                      reply_markup=q_o_2())
            # Переходим к этапу QU2
            return QU2
    else:
        # Отправляем пользователю сообщение о том что его ответ не корректен
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_1())
        # Возвращаемя к этапу QU1
        return QU1


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu2(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o2[0]:
        ans_ob[user]['Монстры'] += 1
    if update.message.text == Otveti.q_o2[1]:
        ans_ob[user]['Колдуны и колдуньи'] += 1
    if update.message.text == Otveti.q_o2[2]:
        ans_ob[user]['Потусторонние'] += 1


# Функция проверяющая ответ на 2 вопрос и задающая следующий
def qu2(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o2:
        # Вызов функции обрабатывающей ответ
        prov_qu2(update, context)
        # Отправляем сообщение со следующим вопросом
        update.message.reply_text('Тебе нравится использовать свою силу и '
                                  'чувствовать власть над этими людишками?',
                                  reply_markup=q_o_3())
        # Переходим к этапу QU3
        return QU3
    else:
        # Отправляем пользователю сообщение о том что его ответ не корректен
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_2())
        # Возвращаемя к этапу QU2
        return QU2


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu3(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o3[0]:
        ans_ob[user]['Монстры'] += 1
        ans_ob[user]['Колдуны и колдуньи'] += 1
    if update.message.text == Otveti.q_o3[1]:
        ans_ob[user]['Потусторонние'] += 1


# Функция проверяющая ответ на 3 вопрос и задающая следующий
def qu3(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o3:
        # Вызов функции обрабатывающей ответ
        prov_qu3(update, context)
        # Отправляем сообщение со следующим вопросом
        update.message.reply_text('Как думаешь, тебе легко причинить'
                                  ' вред или убить?', reply_markup=q_o_4())
        # Переходим к этапу QU4
        return QU4
    else:
        # Отправляем пользователю сообщение о том что его ответ не корректен
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_3())
        # Возвращаемя к этапу QU3
        return QU3


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu4(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o4[0]:
        ans_ob[user]['Колдуны и колдуньи'] += 1
    if update.message.text == Otveti.q_o4[1]:
        ans_ob[user]['Монстры'] += 1
    if update.message.text == Otveti.q_o4[2]:
        ans_ob[user]['Потусторонние'] += 1


# Функция проверяющая ответ на 4 вопрос и задающая следующий
def qu4(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o4:
        # Вызов функции обрабатывающей ответ
        prov_qu4(update, context)
        # Отправляем сообщение со следующим вопросом
        update.message.reply_text('Ты социализирован?', reply_markup=q_o_5())
        # Переходим к этапу QU5
        return QU5
    else:
        # Отправляем пользователю сообщение о том что его ответ не корректен
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_4())
        # Возвращаемя к этапу QU4
        return QU4


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu5(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o5[0]:
        ans_ob[user]['Монстры'] += 1
    if update.message.text == Otveti.q_o5[1]:
        ans_ob[user]['Потусторонние'] += 1
    if update.message.text == Otveti.q_o5[2]:
        ans_ob[user]['Колдуны и колдуньи'] += 1


# Функция проверяющая ответ на 5 вопрос и задающая следующий
def qu5(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o5:
        # Вызов функции обрабатывающей ответ
        prov_qu5(update, context)
        # Отправляем сообщение со следующим вопросом
        update.message.reply_text('Можешь ли ты сказать, что живёшь уже долго'
                                  ' и многое повидал/а?', reply_markup=q_o_6())
        # Переходим к этапу QU6
        return QU6
    else:
        # Отправляем пользователю сообщение о том что его ответ не корректен
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_5())
        # Возвращаемя к этапу QU5
        return QU5


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu6(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o6[0]:
        ans_ob[user]['Колдуны и колдуньи'] += 1
    if update.message.text == Otveti.q_o6[1]:
        ans_ob[user]['Монстры'] += 1
    if update.message.text == Otveti.q_o6[2]:
        ans_ob[user]['Потусторонние'] += 1


# Функция проверяющая ответ на 6 вопрос и задающая следующий
def qu6(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o6:
        # Вызов функции обрабатывающей ответ
        prov_qu6(update, context)
        # Отправляем сообщение со следующим вопросом
        update.message.reply_text('Ты знаешь чего ты хочешь?',
                                  reply_markup=q_o_7())
        # Переходим к этапу QU7
        return QU7
    else:
        # Отправляем пользователю сообщение о том что его ответ не корректен
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_6())
        # Возвращаемя к этапу QU6
        return QU6


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu7(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o7[0]:
        ans_ob[user]['Монстры'] += 1
    if update.message.text == Otveti.q_o7[1]:
        ans_ob[user]['Потусторонние'] += 1
    if update.message.text == Otveti.q_o7[2]:
        ans_ob[user]['Колдуны и колдуньи'] += 1


# Функция проверяющая ответ на 7 вопрос и задающая следующий
def qu7(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o7:
        # Вызов функции обрабатывающей ответ
        prov_qu7(update, context)
        # Отправляем сообщение со следующим вопросом
        update.message.reply_text('Ты чувствуешь, что тебя что-то держит в '
                                  'этом мире и не даёт покоя?',
                                  reply_markup=q_o_8())
        # Переходим к этапу QU8
        return QU8
    else:
        # Отправляем пользователю сообщение о том что его ответ не корректен
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_7())
        # Возвращаемя к этапу QU7
        return QU7


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из классов
def prov_qu8(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.q_o8[0]:
        ans_ob[user]['Монстры'] += 1
    if update.message.text == Otveti.q_o8[1]:
        ans_ob[user]['Потусторонние'] += 1
    if update.message.text == Otveti.q_o8[2]:
        ans_ob[user]['Колдуны и колдуньи'] += 1


# Функция возращающая текст перехода к классу монстров и 1 вопрос про них
def per_m():
    tkm = ('Ты монстр, но пока не понятно какой...\nТы привередлив к еде?')
    return tkm


# Функция возращающая текст перехода к классу колдунов и 1 вопрос про них
def per_w():
    tkw = ('Ты колдун/колдунья, но пока не поятно какой/какая...\n'
           'Ты любишь заключать контракты?')
    return tkw


# Функция возращающая текст перехода к классу потусторонние и 1 вопрос про них
def per_p():
    tkp = ('Ты какая-то астральная сущность, но пока не'
           ' понятно какая.... \nТы злючка?')
    return tkp


# Функция проверяющая ответ на 8 вопрос и задающая следующий
def qu8(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.q_o8:
        # Вызов функции обрабатывающей ответ
        prov_qu8(update, context)
        # Записываем в переменную результат работы функции для
        # отпределения к какому классу относится пользователь
        t_ob = chek_ob(update, context)
        # Проверка по ключу, тоесть если результат chek_ob(update, context) -
        # Монстры, то пользователь отправляется к лассу монстров и будет опреде
        # лятся какой именно он монстр. Аналогично с Колдунами и Потусторонними
        if t_ob == 'Монстры':
            # Отправляем пользователю сообщение, что он монстр и переходим
            # к классу монстров
            update.message.reply_text(per_m(), reply_markup=m_1())
            # Записываем в словарь по монстрам пользователя
            zap_v_ans_m(update, context)
            # Переходим к этапу M1
            return M1
        if t_ob == 'Колдуны и колдуньи':
            # Отправляем пользователю сообщение, что он колдун и переходим
            # к классу колдунов
            update.message.reply_text(per_w(), reply_markup=w_1())
            # Записываем в словарь по колдунам пользователя
            zap_v_ans_w(update, context)
            # Переходим к этапу W1
            return W1
        if t_ob == 'Потусторонние':
            # Отправляем пользователю сообщение, что он потустороннее существо
            # и переходим к классу потусторонних
            update.message.reply_text(per_p(), reply_markup=p_1())
            # Записываем в словарь по потусторонним пользователя
            zap_v_ans_p(update, context)
            # Переходим к этапу P1
            return P1
    else:
        # Если ответ не корректен, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=q_o_8())
        # Возвращаемя к этапу QU8
        return QU8


# Функция определяющая какой из ключей набрал больше всего поинтов и
# возвращающая эток ключ, по которому в дальнейшем происходит переход к
# тому или иному типу монтсров
def chek_ob(update, context):
    user = update.message.from_user.id
    max_p = 0
    point_n = []
    # Проверяем ключи в словаре пользователя и записываем тот, который набрал
    # большее количество поинтов
    # Если два типа набрало равное кол-во поинтов, то выдаём случайное из них
    for i in ans_ob[user].keys():
        if ans_ob[user][i] == max_p:
            max_p = ans_ob[user][i]
            point_n.append(i)
        if ans_ob[user][i] > max_p:
            max_p = ans_ob[user][i]
            point_n.clear()
            point_n.append(i)
    us_p = random.choice(point_n)
    return us_p


# Функция записывающая в словарь с монстрами пользователя
def zap_v_ans_m(update, context):
    user = update.message.from_user.id
    if user not in ans_m:
        ans_m[user] = {
            'Шейпшифтер': 0,
            'Гуль': 0,
            'Вампир': 0
        }
    else:
        ans_m[user] = {
            'Шейпшифтер': 0,
            'Гуль': 0,
            'Вампир': 0
        }


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из монстров
def prov_mu1(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.m_q1[0]:
        ans_m[user]['Гуль'] += 1
    if update.message.text == Otveti.m_q1[1]:
        ans_m[user]['Вампир'] += 1
    if update.message.text == Otveti.m_q1[2]:
        ans_m[user]['Шейпшифтер'] += 1


# Функция проверяющая ответ на 1 вопрос о монстрах и задающая следующий
def mu1(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.m_q1:
        # Вызов функции обрабатывающей ответ
        prov_mu1(update, context)
        # Отправка пользователю сообщения со 2 вопросом о монстрах
        update.message.reply_text('Тебе нравится часто менять свой имидж?',
                                  reply_markup=m_2())
        # Переход к этапу M2
        return M2
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=m_1())
        # Возвращаемя к этапу M1
        return M1


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из монстров
def prov_mu2(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.m_q2[0]:
        ans_m[user]['Шейпшифтер'] += 1
    if update.message.text == Otveti.m_q2[1]:
        ans_m[user]['Вампир'] += 1
    if update.message.text == Otveti.m_q2[2]:
        ans_m[user]['Гуль'] += 1


def mu2(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.m_q2:
        # Вызов функции обрабатывающей ответ
        prov_mu2(update, context)
        # Отправка пользователю сообщения с 3 вопросом о монстрах
        update.message.reply_text('Ты одиночка?', reply_markup=m_3())
        # Переход к этапу M3
        return M3
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=m_2())
        # Возвращаемя к этапу M2
        return M2


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из монстров
def prov_mu3(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.m_q3[0]:
        ans_m[user]['Гуль'] += 1
    if update.message.text == Otveti.m_q3[1]:
        ans_m[user]['Шейпшифтер'] += 1
    if update.message.text == Otveti.m_q3[2]:
        ans_m[user]['Вампир'] += 1


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из монстров
def mu3(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.m_q3:
        # Вызов функции обрабатывающей ответ
        prov_mu3(update, context)
        # Отправка пользователю сообщения с 4 вопросом о монстрах
        update.message.reply_text('Ты следишь за собой?', reply_markup=m_4())
        # Переходим к этапу M4
        return M4
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=m_3())
        # Возвращаемя к этапу M3
        return M3


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из монстров
def prov_mu4(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.m_q4[0]:
        ans_m[user]['Гуль'] += 1
    if update.message.text == Otveti.m_q4[1]:
        ans_m[user]['Шейпшифтер'] += 1
    if update.message.text == Otveti.m_q4[2]:
        ans_m[user]['Вампир'] += 1


def mu4(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.m_q4:
        # Вызов функции обрабатывающей ответ
        prov_mu4(update, context)
        # Записываем в переменную результат работы функции для
        # отпределения к какому монстру относится пользователь
        t_m = res_m(update, context)
        # Отправка информации о монстре + картинка + ссылка
        # где можно прочесть больше
        # Информация и ссылка хранятся в отдельном файле class_answers.py
        update.message.reply_text(t_m[1], reply_markup=st_key())
        photo = open('Images/' + t_m[0] + '.jpg', 'rb')
        context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=photo)
        update.message.reply_text(Otveti.res_monster[t_m[0]][2])
        # Завершаем диалог
        return ConversationHandler.END
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=m_4())
        # Возвращаемя к M4
        return M4


# Функция определяющая какой из ключей набрал больше всего поинтов и
# возвращающая эток ключ и текст о монстре(списком), по которым в дальнейшем
# происходит отправка сообщений с нужным текстом и картинкой
def res_m(update, context):
    user = update.message.from_user.id
    max1_p = 0
    point1_n = []
    # Проверяем ключи в словаре пользователя и записываем тот, который набрал
    # большее количество поинтов.
    # Если два типа монстров набрало равное кол-во поинтов, то выдаём случайное
    # из них.
    for i in ans_m[user].keys():
        if ans_m[user][i] == max1_p:
            max1_p = ans_m[user][i]
            point1_n.append(i)
        if ans_m[user][i] > max1_p:
            max1_p = ans_m[user][i]
            point1_n.clear()
            point1_n.append(i)
    us_m = random.choice(point1_n)
    # Определяем имя пользователя и записываем текст о монстре в переменную.
    user = update.message.from_user.first_name
    text_M = Otveti.res_monster[us_m][0] + user + Otveti.res_monster[us_m][1]

    return [us_m, text_M]


# Функция записывающая в словарь с колдунами пользователя
def zap_v_ans_w(update, context):
    user = update.message.from_user.id
    if user not in ans_w:
        ans_w[user] = {
            'Джин': 0,
            'Ведьма': 0,
            'Демон': 0
        }
    else:
        ans_w[user] = {
            'Джин': 0,
            'Ведьма': 0,
            'Демон': 0
        }


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из колдунов
def prov_wu1(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.w_q1[0]:
        ans_w[user]['Демон'] += 1
    if update.message.text == Otveti.w_q1[1]:
        ans_w[user]['Джин'] += 1
    if update.message.text == Otveti.w_q1[2]:
        ans_w[user]['Ведьма'] += 1


def wu1(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.w_q1:
        # Вызов функции обрабатывающей ответ
        prov_wu1(update, context)
        # Отправка пользователю сообщения со 2 вопросом о кодунах
        update.message.reply_text('У тебя есть татуировки?', reply_markup=w_2())
        # Переходим к этапу W2
        return W2
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=w_1())
        # Возвращаемся к этапу W1
        return W1


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из колдунов
def prov_wu2(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.w_q2[0]:
        ans_w[user]['Джин'] += 1
    if update.message.text == Otveti.w_q2[1]:
        ans_w[user]['Ведьма'] += 1
    if update.message.text == Otveti.w_q2[2]:
        ans_w[user]['Демон'] += 1


def wu2(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.w_q2:
        # Вызов функции обрабатывающей ответ
        prov_wu2(update, context)
        # Отправка пользователю сообщения с 3 вопросом о кодунах
        update.message.reply_text('Эгоистичен/чна ли ты?', reply_markup=w_3())
        # Переходим к этапу W3
        return W3
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=w_2())
        # Возвращаемся к W2
        return W2


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из колдунов
def prov_wu3(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.w_q3[0]:
        ans_w[user]['Демон'] += 1
    if update.message.text == Otveti.w_q3[1]:
        ans_w[user]['Джин'] += 1
    if update.message.text == Otveti.w_q3[2]:
        ans_w[user]['Ведьма'] += 1


def wu3(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.w_q3:
        # Вызов функции обрабатывающей ответ
        prov_wu3(update, context)
        # Отправка пользователю сообщения с 4 вопросом о кодунах
        update.message.reply_text('У тебя есть кореша в Аду?',
                                  reply_markup=w_4())
        # Переходим к этапу W4
        return W4
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=w_3())
        # Возвращаемся к W3
        return W3


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из колдунов
def prov_wu4(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.w_q4[0]:
        ans_w[user]['Ведьма'] += 1
    if update.message.text == Otveti.w_q4[1]:
        ans_w[user]['Джин'] += 1
    if update.message.text == Otveti.w_q4[2]:
        ans_w[user]['Демон'] += 1


def wu4(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.w_q4:
        # Вызов функции обрабатывающей ответ
        prov_wu4(update, context)
        # Записываем в переменную результат работы функции для
        # отпределения к какому монстру относится пользователь
        t_w = res_w(update, context)
        # Отправка информации о колдуне + картинка + ссылка
        # где можно прочесть больше
        # Информация и ссылка хранятся в отдельном файле class_answers.py
        update.message.reply_text(t_w[1],
                                  reply_markup=st_key())
        photo1 = open('Images/' + t_w[0] + '.jpg', 'rb')
        context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=photo1)
        update.message.reply_text(Otveti.res_wiz[t_w[0]][2])
        # Завершаем диалог
        return ConversationHandler.END
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=w_4())
        # Возвращаемя к этапу W4
        return W4


# Функция определяющая какой из ключей набрал больше всего поинтов и
# возвращающая эток ключ и текст о колдуне(списком), по которым в дальнейшем
# происходит отправка сообщений с нужным текстом и картинкой
def res_w(update, context):
    user = update.message.from_user.id
    max2_p = 0
    point2_n = []
    # Проверяем ключи в словаре пользователя и записываем тот, который набрал
    # большее количество поинтов.
    # Если два типа колдунов набрало равное кол-во поинтов, то выдаём случайное
    # из них.
    for i in ans_w[user].keys():
        if ans_w[user][i] == max2_p:
            max2_p = ans_w[user][i]
            point2_n.append(i)
        if ans_w[user][i] > max2_p:
            max2_p = ans_w[user][i]
            point2_n.clear()
            point2_n.append(i)
    us_w = random.choice(point2_n)
    # Определяем имя пользователя и записываем текст о колдуне в переменную.
    user1 = update.message.from_user.first_name
    text_W = Otveti.res_wiz[us_w][0] + user1 + Otveti.res_wiz[us_w][1]

    return [us_w, text_W]


# Функция записывающая в словарь с потусторонними пользователя
def zap_v_ans_p(update, context):
    user = update.message.from_user.id
    if user not in ans_p:
        ans_p[user] = {
            'Призрак': 0,
            'Бурубуру': 0,
            'Полтергейст': 0
        }
    else:
        ans_p[user] = {
            'Призрак': 0,
            'Бурубуру': 0,
            'Полтергейст': 0
        }


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из потусторонних
def prov_pu1(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.p_q1[0]:
        ans_p[user]['Призрак'] += 1
    if update.message.text == Otveti.p_q1[1]:
        ans_p[user]['Бурубуру'] += 1
    if update.message.text == Otveti.p_q1[2]:
        ans_p[user]['Полтергейст'] += 1


def pu1(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.p_q1:
        # Вызов функции обрабатывающей ответ
        prov_pu1(update, context)
        # Отправка пользователю сообщения со 2 вопросом о потусторонних
        update.message.reply_text('Как часто, когда ты болеешь, ты кого-то '
                                  'заражаешь?', reply_markup=p_2())
        # Переходим к этапу P2
        return P2
    else:
        # Если ответ не корректек, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=p_1())
        # Возвращаемся к этапу P1
        return P1


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из потусторонних
def prov_pu2(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.p_q2[0]:
        ans_p[user]['Бурубуру'] += 1
    if update.message.text == Otveti.p_q2[1]:
        ans_p[user]['Полтергейст'] += 1
    if update.message.text == Otveti.p_q2[2]:
        ans_p[user]['Призрак'] += 1


def pu2(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.p_q2:
        # Вызов функции обрабатывающей ответ
        prov_pu2(update, context)
        # Отправка пользователю сообщения с 3 вопросом о потусторонних
        update.message.reply_text('Тебе нравится японская культура?',
                                  reply_markup=p_3())
        # Переходим к этапу P3
        return P3
    else:
        # Если ответ не корректен, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=p_2())
        # Возвращаемся к этапу P2
        return P2


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из потусторонних
def prov_pu3(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.p_q3[0]:
        ans_p[user]['Бурубуру'] += 1
    if update.message.text == Otveti.p_q3[1]:
        ans_p[user]['Призрак'] += 1
    if update.message.text == Otveti.p_q3[2]:
        ans_p[user]['Полтергейст'] += 1


def pu3(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.p_q3:
        # Вызов функции обрабатывающей ответ
        prov_pu3(update, context)
        # Отправка пользователю сообщения с 4 вопросом о потусторонних
        update.message.reply_text('Ты обычно незаметный/ая?',
                                  reply_markup=p_4())
        # Переходим к этапу P4
        return P4
    else:
        # Если ответ не корректен, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=p_3())
        # Возвращение P3
        return P3


# Функция обрабатывающая корректный ответ и добаляющая
# +1 к одному из потусторонних
def prov_pu4(update, context):
    user = update.message.from_user.id
    if update.message.text == Otveti.p_q4[0]:
        ans_p[user]['Полтергейст'] += 1
    if update.message.text == Otveti.p_q4[1]:
        ans_p[user]['Призрак'] += 1
    if update.message.text == Otveti.p_q4[2]:
        ans_p[user]['Бурубуру'] += 1


def pu4(update, context):
    # Проверка корретности ответа, если он содержится в данных вариантах то:
    if update.message.text in Otveti.p_q4:
        # Вызов функции обрабатывающей ответ
        prov_pu4(update, context)
        # Отправка информации о монстре + картинка + ссылка
        # где можно прочесть больше
        # Информация и ссылка хранятся в отдельном файле class_answers.py
        t_p = res_p(update, context)
        # Отправка информации о потустороннем + картинка + ссылка
        # где можно прочесть больше
        # Информация и ссылка хранятся в отдельном файле class_answers.py
        update.message.reply_text(t_p[1], reply_markup=st_key())
        photo2 = open('Images/' + t_p[0] + '.jpg', 'rb')
        context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=photo2)
        update.message.reply_text(Otveti.res_ostarl[t_p[0]][2])
        # Завершаем диалог
        return ConversationHandler.END
    else:
        # Если ответ не корректен, то сообщение об этом
        update.message.reply_text('Неверный ответ, выбери из предложенных',
                                  reply_markup=p_4())
        # Возвращаемся к этапу P4
        return P4


# Функция определяющая какой из ключей набрал больше всего поинтов и
# возвращающая эток ключ и текст о потустороннем(списком),
# по которым в дальнейшем происходит отправка сообщений с
# нужным текстом и картинкой
def res_p(update, context):
    user = update.message.from_user.id
    max3_p = 0
    point3_n = []
    # Проверяем ключи в словаре пользователя и записываем тот, который набрал
    # большее количество поинтов.
    # Если два типа потусторонних набрало равное кол-во поинтов, то
    # выдаём случайное из них.
    for i in ans_p[user].keys():
        if ans_p[user][i] == max3_p:
            max3_p = ans_p[user][i]
            point3_n.append(i)
        if ans_p[user][i] > max3_p:
            max3_p = ans_p[user][i]
            point3_n.clear()
            point3_n.append(i)
    us_p = random.choice(point3_n)
    # Определяем имя пользователя и записываем текст о
    # потустороннем в переменную.
    user2 = update.message.from_user.first_name
    text_P = Otveti.res_ostarl[us_p][0] + user2 + Otveti.res_ostarl[us_p][1]
    return [us_p, text_P]


# Функция описание бота
def help(update, context):
    # Оправляем сообщение пользователю
    update.message.reply_text(
        'Этот бот поможет понять, какой ты монстр из культового сериала '
        '“Сверхъестественное”. Призрак? Вампир? Ведьма? А может другое'
        ' могущественное создание?🙄\nПройди тест и узнай, кто ты!'
        '\n\n\n'
        'Список доступных коммнад бота можно узнать командой: /commands',
        reply_markup=st_key())

    return ConversationHandler.END


# Функция описание комманд бота
def commands(update, context):
    # Отправляем сообщение пользователю
    update.message.reply_text(
        'Команда /go - начать тест\n'
        'Команда /commands - посмотреть список доступных команд\n'
        'Команда /cancel - прекратить тест\n'
        'Команда /help - посмотреть описание бота\n''\n''\n'
        'Команды /help, /cancel и /commands можно написать во время '
        'теста, тогда он завершится и придётся начать его заново - /go',
        reply_markup=st_key())
    return ConversationHandler.END


# Функция принудительно завершающая тест
def cancel(update, context):
    # Отправляем сообщение пользователю
    update.message.reply_text(
        'Тест отменён.\n'
        'Напиши /go, если захочешь пройти тест.',
        reply_markup=st_key())
    return ConversationHandler.END


# Функция запускающая бота
def main():
    updater = Updater("5204373260:AAHPWpvimMwZYTrW21bdq9ZG74uiaY2GHIU")
    dispatcher = updater.dispatcher
    conv_handler = ch()
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


# Возвращающая conv_handler
def ch():
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('go', go),
                      CommandHandler('help', help),
                      CommandHandler('start', start),
                      CommandHandler('commands', commands)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            QU1: [MessageHandler(Filters.all & ~Filters.command, qu1)],
            QU2: [MessageHandler(Filters.all & ~Filters.command, qu2)],
            QU3: [MessageHandler(Filters.all & ~Filters.command, qu3)],
            QU4: [MessageHandler(Filters.all & ~Filters.command, qu4)],
            QU5: [MessageHandler(Filters.all & ~Filters.command, qu5)],
            QU6: [MessageHandler(Filters.all & ~Filters.command, qu6)],
            QU7: [MessageHandler(Filters.all & ~Filters.command, qu7)],
            QU8: [MessageHandler(Filters.all & ~Filters.command, qu8)],
            M1: [MessageHandler(Filters.all & ~Filters.command, mu1)],
            M2: [MessageHandler(Filters.all & ~Filters.command, mu2)],
            M3: [MessageHandler(Filters.all & ~Filters.command, mu3)],
            M4: [MessageHandler(Filters.all & ~Filters.command, mu4)],
            W1: [MessageHandler(Filters.all & ~Filters.command, wu1)],
            W2: [MessageHandler(Filters.all & ~Filters.command, wu2)],
            W3: [MessageHandler(Filters.all & ~Filters.command, wu3)],
            W4: [MessageHandler(Filters.all & ~Filters.command, wu4)],
            P1: [MessageHandler(Filters.all & ~Filters.command, pu1)],
            P2: [MessageHandler(Filters.all & ~Filters.command, pu2)],
            P3: [MessageHandler(Filters.all & ~Filters.command, pu3)],
            P4: [MessageHandler(Filters.all & ~Filters.command, pu4)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel),
                   CommandHandler('help', help),
                   CommandHandler('commands', commands)])
    return conv_handler


if __name__ == '__main__':
    # Создаём словари для хранения информации каждого пользователя
    ans_ob = {}
    ans_m = {}
    ans_w = {}
    ans_p = {}
    main()

