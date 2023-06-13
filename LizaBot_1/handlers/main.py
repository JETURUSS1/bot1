import random
import math

from aiogram import types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot_create import bot

import sqlite3 as sq



async def reply_to_chat(message: types.Message):     #Сообщения

    if message.chat.type == "private":
        if message.from_user.id == 380923417:
                await bot.send_message(chat_id=-1001950917215, text=message.text)
            #elif message.from_user == message.sticker:
                #await bot.send_sticker(chat_id=-1001950917215,
                                       #sticker=r(str(message.sticker.id)))

        else:
            await bot.send_message(message.from_user.id, text='Приветик. Меня зовут Лиза. Я против новых знакомств и общаюсь только в чате, потому что у меня лапки, а у тебя бан')

    else:
        if message.chat.type != "private":
            mo = str(message.text)
            if message.chat.id == -1001950917215:
                bot_words = ['Эх, меня бы сейчас...', 'Проехали...', 'Да проехали говорю.', "БАН", "баааан", "по лбу", "БАААН", "бан", "Бан тебе", 'Упакуйте мне Ёжика!', 'Вы меня используете...', 'Ой, всё!', 'Фили ты тут командуешь?!', "Отстань!!!", "Дайте мне другой префикс. Мне этот не нравится", "Еще раз так сделаешь - я выйду", "А как пишется \"развод\"?", "Так устала ваша Лиза", "Ну что Лиза? ЧТо ЛИЗА-ТО? ИДИ НАХУЙ", "Очень смешно, да. Обосраться как смешно."]

                if message.text == "Лиза" or message.text == "лиза":
                    await message.reply(text=(random.choice(bot_words)))
                    stickers = [(r'CAACAgIAAxkBAAEJPCJkf6kdpKacWf6GYzcK80P0t-O-FAACGCgAAntbeUtYtZWwsH2roy8E'), (r'CAACAgIAAxkBAAEJPo1kgKnIl2AmwaVdc0Y8skXW_dV8ygACMxQAAtWzKEhzcG8yt63ebi8E'), (r'CAACAgQAAxkBAAEJPCpkf6xXo6sbnqqGUeRmuD1ZTsiSRAACHgwAAoLDQVJx3FKPGw9MGi8E'), (r'CAACAgIAAxkBAAEJPCRkf6kjUoghnbnwMeNM_bEr-ShBywACNCcAAnA2eEt55QFa_BdJ7S8E'), (r'CAACAgIAAxkBAAEJPCZkf6ktHkSjk3TnPf_q-eoVwSpVsQACyCoAAmFbeEtSjoc-IQeRqi8E')]
                    await bot.send_sticker(chat_id=-1001950917215,
                                           sticker=random.choice(stickers))
                #  В качетсве аргумента sticker передаем id стикера который мы получили раннее
                #  Обязательно ставим r  перед строкой для того чтобы все работало (Зачем и почему могу объяснить в следующем гайде)

                elif "корень из" in mo.lower():
                    number = mo.lower()
                    number = number.replace('корень из ', '')
                    result = math.sqrt(int(number))
                    textmap = 'Квадратный корень из числа ' + str(number) + ' равен ' + str(round(result, 2))
                    await message.reply(text=textmap)
                elif "корень" in mo.lower():
                    number = mo.lower()
                    number = number.replace('корень ', '')
                    result = math.sqrt(int(number))
                    textmap = 'Квадратный корень из числа ' + str(number) + ' равен ' + str(round(result, 2))
                    await message.reply(text=textmap)
                elif 'лиза кто' in mo.lower():
                    lyrics = mo.lower()
                    lyrics = lyrics.replace('лиза кто ', '')
                    user_for_who = lyrics
                    quarrel = ['какашка', 'снежинка', 'динамо', 'бабулька', 'котик', 'ослик',
                           'букашка', "кракозябра", "арангутан", "рептилия", "мухомор",
                           "свадебный торт", "хейтер ириса", "любитель ириса", "фекалия",
                           "шаловливая особа", "гермофродит", "сакура", "давалка"]
                    suppose = "Я думаю, что " + user_for_who + " на самом деле " + random.choice(quarrel)
                    await message.reply(text=suppose)
                elif 'лиза кто' in mo.lower():
                    lyrics = mo.lower()
                    lyrics = lyrics.replace('лиза, кто ', '')
                    user_for_who = str(lyrics)
                    quarrel = ['какашка', 'снежинка', 'динамо', 'бабулька', 'котик', 'ослик',
                           'букашка', "кракозябра", "арангутан", "рептилия", "мухомор",
                           "свадебный торт", "хейтер ириса", "любитель ириса", "фекалия",
                           "шаловливая особа", "гермофродит", "сакура", "давалка"]
                    suppose = "Я думаю, что " + user_for_who.capitalize() + " на самом деле " + random.choice(quarrel)
                    await message.reply(text=suppose)
                elif 'лиза браки' in mo.lower():
                    lyrics1 = mo.lower()
                    lyrics1 = lyrics1.replace('лиза браки ', '')
                    user_for_br = lyrics1
                    quarrel_braki = ['Хуяки', 'С такими вопросами иди к ирису', 'Бан тебе', 'Бьяки, бьяки, займись делом, долбоёб', 'ХУЯКИИИИ', 'Брак - это твоя жизнь',
                           'Лучше бы трахнули, чем этой виртуальной ерундой занимались', "Фу!", "ИРИСУ МОЗГИ ЕБИ!", "ГОСПОДИ МНЕ РАЗВОД ДАДУТ В ЭТОЙ ЖИЗНИ ИЛИ НЕТ?!", "Ну давай, давай. Поугорай. Так смешно нервировать бота ведь.",
                           "Господи ты боже мой, ну что за кретины", "Я просто балдею от наших разговоров: что ни день, то спамят тупыми вопросами", "ЗАСУНЬ СВОИ БРАКИ СЕБЕ В ЖОПУ ТУПОЙ ГОНДОН", "ГОВНЯКИ БЛЯЯЯЯ",
                           "Господи, ты прекратишь сегодня?", "Браки для нищих", "Дайте уже венец безбрачия", "Я в браки больше не играю"]
                    suppose = random.choice(quarrel_braki)
                    await message.reply(text=suppose)


                elif '+рп' in mo:
                    meo = mo.lower()
                    meo = meo.replace('+рп ', '')
                    meo = str(meo)
                    list_1 = meo.split(",")
                    try:
                        sqlite_connection = sq.connect('bot.db')
                        cursor = sqlite_connection.cursor()
                        print("Подключен к SQLite")
                        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                name TEXT,
                                sex TEXT,
                                old TEXT
                                )""")
                        range1 = (list_1[0], list_1[1], list_1[2])
                        print(range1)
                        print(list_1)
                        sqlite_insert_query = """INSERT INTO users
                                              VALUES
                                              (range1);"""
                        count = cursor.execute(sqlite_insert_query)
                        sqlite_connection.commit()
                        print("Запись успешно вставлена в таблицу ", cursor.rowcount)
                        cursor.close()

                    except sq.Error as error:
                        print("Ошибка при работе с SQLite", error)
                    finally:
                        if sqlite_connection:
                            sqlite_connection.close()
                            print("Соединение с SQLite закрыто")


                    await bot.send_message(chat_id=-1001950917215, text='проверь терминальную дебаг-консоль, Женя')
                    return [list_1]

            elif message.text == "ферма" or message.text == "Ферма":
                    await message.reply(text="Хуерма! 😁")


    try:
        sqlite_connection = sq.connect('bot.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                name TEXT,
                sex TEXT,
                old TEXT
                )""")
        range1 = (list_1[0], list_1[1], list_1[2])
        print(range1)
        print(list_1)
        sqlite_insert_query = """INSERT INTO users
                              VALUES
                              (range1);"""
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена в таблицу ", cursor.rowcount)
        cursor.close()

    except sq.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")




#async def reply_voice_to_chat(message: types.Messa):



              # Горячие слова пока не доделаны ! НАДДА УЗНАТЬ БЛ***КИЙ ШИФР ДИНГО


'''async def my_chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        await bot.send_message(chat_id=380923417, text="Гай Юлий Цезарь прибыл сюда, чтобы представлять интересы Евгения Романова (который JETURUSS). Уважайте его величество и меня! Аве, Цезарь! Аве мне!") # Welcome message, if bot was added to group
        await bot.leave_chat(message.chat.id)'''     #Входы и выходы, нужен декоратор



def register_main_handlers(dp: Dispatcher):
    dp.register_message_handler(reply_to_chat)
