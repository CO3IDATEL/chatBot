import json
import copy
BOT_CONFIG = {'intents': {'Болезни нервной системы': {
    'examples': ['Проблемы со сном', 'Обморок',
                 'Головокружение', 'Нарушение слуха',
                 'Нарушения чувствительности',
                 'Нарушения координации', 'Эпилепсия',
                 'Депрессия'],
    'responses': ['Полагаю, что вам нужно обратиться к неврологу', 'Попробуйте обратиться к неврологу',
                  'Я считаю вам нужен невролог']},
                          'Инфекционные болезни': {
                              'examples': ['Температура', 'Жар', 'Слабость', 'Озноб',
                                           'Снижение аппетита',
                                           'Проблемы со сном', 'Боли в мышцах', 'Тошнота', 'Рвота',
                                           'Потоотделение', 'Головокружение', 'Кружится голова',
                                           'Апатия',
                                           'Головная боль', 'Ломота в суставах'],
                              'responses': ['Вам нужен врач инфекционист']},
                          'Болезни органов дыхания': {
                              'examples': ['Отдышка', 'Кашель', 'Кровохарканье',
                                           'Боль в груди', 'Боль в горле','Боли при дыхании'],
                              'responses': [
                                  'Похоже у вас заболевание органов дыхания, обратитесь к врачу-пульмонологу']},
                          'Болезни ЖКТ': {
                              'examples': ['Изжога', 'Вздутие',
                                           'Тошнота', 'Рвота',
                                           'Запор', 'Диарея', 'Налет на языке',
                                           'Запах изо рта', 'Нарушения глотания',
                                           'Отек языка', 'Горечь во рту', 'Зуд'],
                              'responses': ['Похоже у вас заболевание ЖКТ, вам нужен гастроэнтеролог']},
                          'Болезни кожи': {
                              'examples': ['Зуд', 'Жжение тела', 'Покраснения на коже', 'Сыпь', 'Волдыри', 'Пятна',
                                           'Пузырьки'],
                              'responses': ['Вам нужен дерматолог']},
                          'Болезни костно-мышечной системы': {
                              'examples': ['Боли в спине', 'Боли в ногах', 'Боли в пояснице', 'Боли в шее',
                                           'Скованность в движениях', 'Боли в мышцах', 'Бледность кожи',
                                           'Снижение температурной чувствительности',
                                           'Отеки', 'Покраснения на коже', 'Онемение', 'Перелом'],
                              'responses': ['Вам нужен травмотолог или отропед, так же может подойти физиотерапевт']},
                          'Болезни крови': {
                              'examples': ['Бледность кожи', 'Озноб',
                                           'Сыпь', 'Зуд', 'Пятна',
                                           'Слабость', 'Температура', 'Жар',
                                           'Кровотечения', 'Увеличение лимфоузлов',
                                           'Суставаная боль', 'Плохая свертываемость крови'],
                              'responses': ['Гематолог']},
                          'Болезни уха': {
                              'examples': ['Температура', 'Насморк', 'Отеки',
                                           'Боль в горле', 'Жжение в горле',
                                           'Головная боль',
                                           'Озноб', 'Суставаная боль',
                                           'Отдышка', 'Кашель'],
                              'responses': ['Вам нужен отоларинголог(ЛОР)']},
                          'Болезни эндокринной системы': {
                              'examples': ['Слабость', 'Изменение веса',
                                           'Боли в сердце', 'Высокий пульс', 'Потливость',
                                           'Температура', 'Жар', 'Сонливость', 'Мочеиспускание',
                                           'Жажда', 'Высокое давление', 'Головные боли', 'Головная боль'
                                           ], 'responses': ['Врач - эндокринолог']}
                          },
              'failure_phrases': ['Я вас не понял']}
bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни нервной системы']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни нервной системы']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни нервной системы']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни нервной системы']['examples'].append(add3)


bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни органов дыхания']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни органов дыхания']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни органов дыхания']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни органов дыхания']['examples'].append(add3)


bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни ЖКТ']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни ЖКТ']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни ЖКТ']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни ЖКТ']['examples'].append(add3)

bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни кожи']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни кожи']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни кожи']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни кожи']['examples'].append(add3)

bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни костно-мышечной системы']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни костно-мышечной системы']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни костно-мышечной системы']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни костно-мышечной системы']['examples'].append(add3)

bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни крови']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни крови']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни крови']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни крови']['examples'].append(add3)

bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни уха']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни уха']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни уха']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни уха']['examples'].append(add3)

bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Инфекционные болезни']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Инфекционные болезни']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Инфекционные болезни']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Инфекционные болезни']['examples'].append(add3)

bot_to_write = copy.deepcopy(BOT_CONFIG['intents']['Болезни эндокринной системы']['examples'])
for i in bot_to_write:
    for j1 in range(len(bot_to_write)):
        if bot_to_write[j1] not in i:
            add1 = i + ' ' + bot_to_write[j1]
            BOT_CONFIG['intents']['Болезни эндокринной системы']['examples'].append(add1)
            for j2 in range(len(bot_to_write)):
                if bot_to_write[j2] not in add1:
                    add2 = add1 + ' ' + bot_to_write[j2]
                    BOT_CONFIG['intents']['Болезни эндокринной системы']['examples'].append(add2)
                    for j3 in range(len(bot_to_write)):
                        if bot_to_write[j3] not in add2:
                            add3 = add2 + ' ' + bot_to_write[j3]
                            BOT_CONFIG['intents']['Болезни эндокринной системы']['examples'].append(add3)

with open('BOT_CONFIG.json', 'w') as f:
    json.dump(BOT_CONFIG, f)

#with open('BOT_CONFIG.json', 'r') as f:
#    BOT_CONFIG = json.load(f)
#print(BOT_CONFIG)