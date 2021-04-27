#!/usr/bin/env python
# coding: utf-8

import random
import json
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import nltk


# ПОДГОТОВКА ВВОДА ПОЛЬЗОВАТЕЛЯ
def cleaner(text):
    cleaned_text = ''
    for ch in text.lower():
        if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
            cleaned_text += ch
    return cleaned_text


# РАБОТА С ОПЕЧАТКАМИ
def match(text, example):
    return nltk.edit_distance(text, example) / len(example) < 0.25


#  ПОЛУЧИТЬ ИНТЕНТ
def get_intent(text):
    for intent in BOT_CONFIG['intents']:
        for example in BOT_CONFIG['intents'][intent]['examples']:
            if match(cleaner(text), cleaner(example)):
                return intent


# ПРЕДСКАЗАТЬ ИНТЕНТ
def get_intent_by_model(text):
    return lg.predict(vectorizer.transform([text]))[0]


# ВЫДАТЬ РЕЗУЛЬТАТ
def bot(text):
    intent = get_intent(text)
    if intent is None:
        intent = get_intent_by_model(text)
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])


# ВЫБОРКА
BOT_CONFIG = {'intents': {
    'Общие симптомы': {
        'examples': ['Температура', 'Озноб', 'Жар', 'Морозит', 'Холодно', 'Болит Голова', 'Головная боль',
                     'Боль в голове', 'Боли в голове'],
        'responses': ['Вам стоит обратиться к терапевту']},
    'Болезни нервной системы': {
        'examples': ['Плохой сон', 'Бессоница', 'Не могу уснуть', 'Проблемы со сном', 'Обморок', 'Упал в обморок',
                     'Головокружение', 'Нарушение слуха', 'Стал плохо слышать', 'Кружится голова', 'Голова кружится',
                     'Проблемы со слухом', 'Нарушения чувствительности', 'Плохо чувстую пальцами',
                     'Упала чувствительность',
                     'Нарушения координации', 'Проблема с координацией', 'Эпилепсия', 'Эпилептический припадок',
                     ],
        'responses': ['Полагаю, что вам нужно обратиться к неврологу', 'Попробуйте обратиться к неврологу',
                      'Я считаю вам нужен невролог']},
    'Инфекционные болезни': {
        'examples': ['Температура', 'Высокая температура', 'Жар', 'Слабость', 'Озноб', 'Морозит',
                     'Холодно', 'Нет аппетита', 'Снижение аппетита', 'Плохой аппетит',
                     'Плохой сон', 'Нарушение сна', 'Ломит', 'Тошнота', 'Рвота',
                     'Потоотделение', 'Головокружение', 'Кружится голова', 'Голова кружится',
                     'Сильная головная боль', 'Болит голова', 'Сильно болит голова', 'Апатия',
                     'Боли в голове', 'Ломота в суставах'],
        'responses': ['Вам нужен врач инфекционист']},
    'Болезни органов дыхания': {
        'examples': ['Отдышка', 'Появилась отдышка', 'Сильная отдышка', 'Тяжело дышать',
                     'Проблемы с дыханием', 'Кашель', 'Появился кашель', 'Влажный кашель',
                     'Сухой кашель', 'Кашляю', 'Сильный кашель', 'Кровохарканье', 'Харкаю кровью',
                     'Отхаркивается кровь', 'Боль в груди', 'Боль в горле', 'Болит грудь',
                     'Болит горло', 'Сложно дышать', 'Больно дышать', 'Боли при дыхании'],
        'responses': ['Похоже у вас заболевание органов дыхания, обратитесь к врачу-пульмонологу']},
    'Болезни ЖКТ': {
        'examples': ['Изжога', 'Жжение в желудке', 'Метеоризм', 'Стеноз кишечника', 'Вздутие',
                     'Скопление газов', 'Отрыжка', 'Тошнота', 'Рвота', 'Тошнит',
                     'Проблемы со стулом', 'Запор', 'Диарея', 'Понос', 'Налет на языке',
                     'Запах изо рта', 'Непритяный запах изо рта', 'Нарушения глотания',
                     'Дисфагия', 'Отек языка', 'Горечь во рту'],
        'responses': ['Похоже у вас заболевание ЖКТ, вам нужен гастроэнтеролог']},
    'Болезни кожи': {
        'examples': ['Зуд', 'Чесотка', 'Чешется', 'Чешется тело', 'Жжение тела', 'Жгет', 'Жгёт', 'Жжение',
                     'Покраснения', 'Покраснения на коже', 'Красная кожа', 'Сыпь', 'Сыпь на теле',
                     'Сыпь на коже', 'Кожные высыпания', 'Волдыри', 'Пятна', 'Пятна на теле',
                     'Пузырьки', 'Пузырьки на теле', 'Бугорки', 'Бугорки на теле'],
        'responses': ['Вам нужен дерматолог']},
    'Болезни костно-мышечной системы': {
        'examples': ['Боли в спине', 'Боли в ногах', 'Боли в пояснице', 'Боли в шее',
                     'Боль в спине', ',Боль в шее', 'Боль в ногах', 'Боль в пояснице',
                     'Болит спина', 'Болит шея', 'Болит нога', 'Болят ноги', 'Болит поясница',
                     'Скованность в движениях', 'Боли в мышцах', 'Боль в мышцах', 'Бледность кожи',
                     'Снижение температурной чувствительности', 'Температурная чувствительность',
                     'Отеки', 'Покраснения', 'Мурашки', 'Краснота', 'Анемение', 'Перелом', 'Сломал'],
        'responses': ['Вам нужен травмотолог или ортопед, так же может подойти физиотерапевт']},
    'Болезни крови': {
        'examples': ['Бледность', 'Бледный', 'Бледное тело', 'Озноб', 'Морозит', 'Чувство холода',
                     'Чешется', 'Сыпь на теле', 'Лихорадка', 'Пятна',
                     'Пятна на теле', 'Слабость', 'Отсутсвие сил', 'Температура', 'Жар',
                     'Высокая температура', 'Кровотечения', 'Увеличение лимфоузлов', 'Боль в суставах',
                     'Боли в суставах', 'Плохая свертываемость крови', 'Суставная боль'],
        'responses': ['Гематолог']},
    'Болезни уха': {
        'examples': ['Температура', 'Насморк', 'Сопли', 'Заложен нос', 'Отеки', 'Отечность',
                     'Боль в горле', 'Больно глотать', 'Жжение в горле', 'Осиплость в голосе',
                     'Пропал голос', 'Нет голоса', 'Озноб', 'Морозит',
                     'Тяжело дышать', 'Кашель', 'Сухой кашель', 'Влажный кашель', 'Уши', 'Ухо', 'Запахи',
                     'Не чувствую запах', 'Нос'],
        'responses': ['Вам нужен отоларинголог(ЛОР)']},
    'Болезни эндокринной системы': {
        'examples': ['Усталость', 'Слабость', 'Изменение веса', 'Похоудел', 'Потолстел',
                     'Боли в сердце', 'Высокий пульс', 'Потливость', 'Потооделение', 'Потею',
                     'Температура', 'Жар', 'Сонливость', 'Мочеиспускание', 'Часто хожу в туалет',
                     'Жажда', 'Высокое давление', 'Головные боли', 'Боли в голове',
                     'Болит голова'], 'responses': ['Врач - эндокринолог']},
    'Кардио Болезни': {
        'examples': ['Боли в сердце', 'Болит сердце', 'Сердечнве боли', 'Высокий пульс',
                     'Низкий пульс', 'Отечность ног', 'Отечность', 'Отдышка', 'Появилась отдышка',
                     'Сильная отдышка', 'Артериальное давление', 'Появление артериального давления',
                     'Головокружение', 'Кружится голова', 'Голова кружится'],
        'responses': ['Вам нужен врач - кардиолог']},
    'Болезни глаз': {
        'examples': ['Стал хуже видеть', 'Нарущилось зрение', 'Ухудшилось зрение', 'Стал плохо видеть',
                     'Боли в галазах', 'Болят глаза', 'Боль в галазах', 'Покраснение глаз',
                     'Красные глаза', 'Слёзы', 'Слезоточение', 'Чувствительность к свету',
                     'Сильный зуд в глазах', 'Зуд в глазах', 'Глаз', 'Глаза', 'Проблемы с глазами',
                     'Не поднимаются веки', 'Веки', 'Веко'],
        'responses': ['Вам нужен офтальмолог(окулист)']},
    'Болезни зубов': {
        'examples': ['Зуб', 'Зубы', 'Болит зуб', 'Боли в зубах', 'Пломба', 'Боль на еду',
                     'Больно жевать', 'Боль на холодное', 'Боль на горячее', 'Больно кусать',
                     'Коронка', 'Реакция на сладкое', 'Реакция на горячее', 'Болит от сладкого',
                     'Десна', 'Дёсны', 'Запах изо рта', 'Прикус', 'Челюсть', 'Кариес', 'Зубная боль'],
        'responses': ['Вам нужен стоматолог']},
    'Приветствия': {
        'examples': ['Привет', 'Йоу', 'Прив', 'Добрый день', 'Здравстуй', 'Здравстуйте', 'Бонжур', 'Салам',
                     'Можно уточнить', 'Помоги', 'Нужна помощь', 'Здарова', 'Хай', 'Хеллоу'],
        'responses': ['Здравстуйте, чем я могу вам помочь?', 'Здравстуйте, опишите ваши сиптомы']},
    'Прощания': {
        'examples': ['Спасибо', 'Пока', 'До свидания', 'Прощай', 'Хорошего дня', 'Большое спасибо'],
        'responses': ['До свидания, надеюсь я вам помог', 'До свидания, не болейте']}
},
    'failure_phrases': ['Я вас не понял']}

# with open('BOT_CONFIG.json', 'r') as f:
#    BOT_CONFIG = json.load(f)
X = []
y = []

for intent, intent_data in BOT_CONFIG['intents'].items():
    for example in intent_data['examples']:
        X.append(example)
        y.append(intent)
print(len(X), len(y))

# ВЕКТОРИЗАЦИЯ

vectorizer = CountVectorizer(preprocessor=cleaner, ngram_range=(1, 5),
                             stop_words=['у', 'меня', 'и', 'но', 'еще', 'сильно'])
X_vect = vectorizer.fit_transform(X)
len(vectorizer.get_feature_names())
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.33)

# -----ТЕСТЫ-----

# ЛИНЕЙНАЯ
clf = LinearSVC()
clf.fit(X_vect, y)
print(clf.score(X_test, y_test))
print(clf.score(X_vect, y))
print()
# КЛАССИФИКАЦИЯ
sgd = SGDClassifier()
sgd.fit(X_vect, y)
print(sgd.score(X_test, y_test))
print(sgd.score(X_vect, y))
print()
# ЛОГИСТИЧЕСКАЯ РЕГРЕССИЯ
lg = LogisticRegression()
lg.fit(X_vect, y)
print(lg.score(X_test, y_test))
print(lg.score(X_vect, y))
print()

# ПРОВЕРКА В КОНСОЛИ

# q = ''
# while True:
#    q = input()
#    print(bot(q))

# БОТ

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Здравстуй, {user.mention_markdown_v2()}\!\nЯ медицинский бот \nЯ помогу вам определиться с тем к каому врачу вам стоит обратиться Все, что вам нужно  это написать что вас беспокоит, а я вам скажу к кому вам стоит обратиться\nЕсли есть вопросы напишите /help',

    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Все что от вас требуется - это написать свои сиптомы.\nНапример:\nУ меня температура, болит голова, слаботь')


def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""

    update.message.reply_text(bot(update.message.text))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1791781535:AAEq427xiLkZ_ldz3qkcpd8Wrp1z3-2ITQ4")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


main()
