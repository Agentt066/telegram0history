import telebot
import os
from flask import Flask, request

# import os os.system("C:\Users\User\AppData\Roaming\Spotify")
TOKEN = '5097559487:AAGdiYe2xfoDwYwpFcAlowRY50Ux56237xk'
APP_URL = f'https://telegramhistory.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Привет,я могу тебе помочь с историй чтобы ты сдал историю на 5. Напиши /help.")
    elif message.text == "Как дела":
        bot.send_message(message.from_user.id, "Нормально")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id, "Пока")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "860 рф":
        bot.send_message(message.from_user.id, "поход Руси на Константинополь")
    elif message.text == "862 рф":
        bot.send_message(message.from_user.id, "призвание» Рюрика")
    elif message.text == "882 рф":
        bot.send_message(message.from_user.id, "захват Олегом Киева")
    elif message.text == "907 рф":
        bot.send_message(message.from_user.id, "поход Олега на Константинополь")
    elif message.text == "911 рф":
        bot.send_message(message.from_user.id, "договор Руси с Византией")
    elif message.text == "941 рф":
        bot.send_message(message.from_user.id, "походы Игоря на Константинополь, договоры Руси с Византией")
    elif message.text == "944 рф":
        bot.send_message(message.from_user.id, "походы Игоря на Константинополь, договоры Руси с Византией")
    elif message.text == "964-972 рф":
        bot.send_message(message.from_user.id, "походы Святослава")
    elif message.text == "978-1015 рф":
        bot.send_message(message.from_user.id, "княжение Владимира Святославича в Киеве")
    elif message.text == "988 рф":
        bot.send_message(message.from_user.id, "крещение Руси")
    elif message.text == "1016-1018 рф":
        bot.send_message(message.from_user.id, "первый период княжение Ярослава Мудрого")
    elif message.text == "1019-1054 рф":
        bot.send_message(message.from_user.id, "второй период княжение Ярослава Мудрого")
    elif message.text == "1016-1054 рф":
        bot.send_message(message.from_user.id, "поход Олега на Константинополь")
    elif message.text == "1097 рф":
        bot.send_message(message.from_user.id, "Любечский съезд")
    elif message.text == "1113-1125 рф":
        bot.send_message(message.from_user.id, "княжение в Киеве Владимира Мономаха")
    elif message.text == "1125-1132 рф":
        bot.send_message(message.from_user.id, "княжение в Киеве Мстислава Великого")
    elif message.text == "1147 рф":
        bot.send_message(message.from_user.id, "первое упоминание Москвы в летописях")
    elif message.text == "1185 рф":
        bot.send_message(message.from_user.id, "поход Игоря Святославича на половцев")
    elif message.text == "1223 рф":
        bot.send_message(message.from_user.id, "битва на р. Калке")
    elif message.text == "1237-1241 рф":
        bot.send_message(message.from_user.id, "завоевание Руси ханом Батыем")
    elif message.text == "1240 15 июля рф":
        bot.send_message(message.from_user.id, "Невская битва")
    elif message.text == "1242 5 апреля рф":
        bot.send_message(message.from_user.id, "Ледовое побоище")
    elif message.text == "1242-1243 рф":
        bot.send_message(message.from_user.id, "образование Улуса Джучи (Золотой орды)")
    elif message.text == "1325-1340 рф":
        bot.send_message(message.from_user.id, "княжение Ивана Калиты")
    elif message.text == "1327 рф":
        bot.send_message(message.from_user.id, "антиордынское восстание в Твери")
    elif message.text == "1359-1389 рф":
        bot.send_message(message.from_user.id, "княжение Дмитрия Донского")
    elif message.text == "1378 11 августа рф":
        bot.send_message(message.from_user.id, "битва на р. Воже")
    elif message.text == "1380 8 сентября рф":
        bot.send_message(message.from_user.id, "Куликовская битва")
    elif message.text == "1382 рф":
        bot.send_message(message.from_user.id, "разорение Москвы Тохтамышем")
    elif message.text == "1389-1425 рф":
        bot.send_message(message.from_user.id, "княжение Василия I")
    elif message.text == "1395 рф":
        bot.send_message(message.from_user.id, "разгром Золотой орды Тимуром")
    elif message.text == "1410 15 июля рф":
        bot.send_message(message.from_user.id, "Грюнвальдская битва")
    elif message.text == "1425-1453 рф":
        bot.send_message(message.from_user.id, "междоусобная война в Московском княжестве")
    elif message.text == "1425-1462 рф":
        bot.send_message(message.from_user.id, "княжение Василия II")
    elif message.text == "1448 рф":
        bot.send_message(message.from_user.id, "установление автокефалии Русской церкви")
    elif message.text == "1462-1505 рф":
        bot.send_message(message.from_user.id, "княжение Ивана III")
    elif message.text == "1478 рф":
        bot.send_message(message.from_user.id, "присоединение Новгородской земли к Москве")
    elif message.text == "1480 рф":
        bot.send_message(message.from_user.id, "«стояние» на р. Угре. Падение Ордынского владычества.")
    elif message.text == "1485 рф":
        bot.send_message(message.from_user.id, "присоединение Тверского великого княжества к Москве")
    elif message.text == "1497 рф":
        bot.send_message(message.from_user.id, "принятие общерусского Судебника")
    elif message.text == "1505-1533 рф":
        bot.send_message(message.from_user.id, "княжение Василия III")
    elif message.text == "1510 рф":
        bot.send_message(message.from_user.id, "присоединение Псковской земли")
    elif message.text == "1514 рф":
        bot.send_message(message.from_user.id, "включение в состав Русского государства Смоленской земли")
    elif message.text == "1521 рф":
        bot.send_message(message.from_user.id, "присоединение Рязанского княжества")
    elif message.text == "1533-1584 рф":
        bot.send_message(message.from_user.id, "княжение (царствование) Ивана IV Васильевича Грозного.")
    elif message.text == "1533-1538 рф":
        bot.send_message(message.from_user.id, "регентство Елены Глинской")
    elif message.text == "1538-1547 рф":
        bot.send_message(message.from_user.id, "период боярского правления")
    elif message.text == "1547 рф":
        bot.send_message(message.from_user.id, "принятие Иваном Грозным царского титула")
    elif message.text == "1549 рф":
        bot.send_message(message.from_user.id, "первый Земский собор")
    elif message.text == "1550 рф":
        bot.send_message(message.from_user.id, "принятие Судебника Ивана IV")
    elif message.text == "1552 рф":
        bot.send_message(message.from_user.id, "взятие русскими войсками Казани")
    elif message.text == "1556 рф":
        bot.send_message(message.from_user.id, "присоединение к России Астраханского ханства."
                                               " и отмена кормлений")
    elif message.text == "1558-1583 рф":
        bot.send_message(message.from_user.id, "Ливонская война")
    elif message.text == "1564 рф":
        bot.send_message(message.from_user.id, "издание первой датированной российской печатной книги")
    elif message.text == "1565-1572 рф":
        bot.send_message(message.from_user.id, "опричнина")
    elif message.text == "1581-1585 рф":
        bot.send_message(message.from_user.id, "покорение Сибирского ханства Ермаком")
    elif message.text == "1584-1598 рф":
        bot.send_message(message.from_user.id, "царствование Федора Ивановича")
    elif message.text == "1589 рф":
        bot.send_message(message.from_user.id, "учреждение в России патриаршества")
    elif message.text == "1598-1605":
        bot.send_message(message.from_user.id, "царствование Бориса Годунова")
    elif message.text == "1604-1618 рф":
        bot.send_message(message.from_user.id, "Смута в России")
    elif message.text == "1605-1606 рф":
        bot.send_message(message.from_user.id, "правление Лжедмитрия I")
    elif message.text == "1606-1610 рф":
        bot.send_message(message.from_user.id, "царствование Василия Шуйского.")
    elif message.text == "1606-1607 рф":
        bot.send_message(message.from_user.id, "восстание Ивана Болотникова.")
    elif message.text == "1607-1610 рф":
        bot.send_message(message.from_user.id, "движение Лжедмитрия II")
    elif message.text == "1611-1612 рф":
        bot.send_message(message.from_user.id, "I и II Ополчения. Освобождение Москвы.")
    elif message.text == "1613-1645 рф":
        bot.send_message(message.from_user.id, "царствование Михаила Федоровича.")
    elif message.text == "1617 рф":
        bot.send_message(message.from_user.id, "Столбовский мир со Швецией")
    elif message.text == "1618 рф":
        bot.send_message(message.from_user.id, "Деулинское перемирие с Речью Посполитой.")
    elif message.text == "1632-1634 рф":
        bot.send_message(message.from_user.id, "Смоленская война")
    elif message.text == "1645-1676 рф":
        bot.send_message(message.from_user.id, "царствование Алексея Михайловича")
    elif message.text == "1648 рф":
        bot.send_message(message.from_user.id, "Соляной бунт в Москве"
                                               "поход Семена Дежнева")
    elif message.text == "1649 рф":
        bot.send_message(message.from_user.id,
                         "принятие Соборного Уложения. Оформление крепостного права в центральных регионах страны")
    elif message.text == "1649-1653 рф":
        bot.send_message(message.from_user.id, "походы Ерофея Хабарова")
    elif message.text == "1653 рф":
        bot.send_message(message.from_user.id, "реформы патриарха Никона"
                                               " и начало старообрядческого раскола в Русской Церкви")
    elif message.text == "1654 рф":
        bot.send_message(message.from_user.id, "Переяславская Рада. Переход под власть России Левобережной Украины")
    elif message.text == "1654-1667 рф":
        bot.send_message(message.from_user.id, "война с Речью Посполитой")
    elif message.text == "1656-1658 рф":
        bot.send_message(message.from_user.id, "война со Швецией")
    elif message.text == "1662 рф":
        bot.send_message(message.from_user.id, "Медный бунт")
    elif message.text == "1667 рф":
        bot.send_message(message.from_user.id, "Андрусовское перемирие")
    elif message.text == "1670-1671 рф":
        bot.send_message(message.from_user.id, "восстание Степана Разина")
    elif message.text == "1676-1682 рф":
        bot.send_message(message.from_user.id, "царствование Федора Алексеевича")
    elif message.text == "1682-1725 рф":
        bot.send_message(message.from_user.id, "царствование Петра I (до 1696 г. совместно с Иваном V)")
    elif message.text == "1682-1689 рф":
        bot.send_message(message.from_user.id, "правление царевны Софьи")
    elif message.text == "1682 рф":
        bot.send_message(message.from_user.id, "восстания стрельцов")
    elif message.text == "1689 рф":
        bot.send_message(message.from_user.id, "восстания стрельцов")
    elif message.text == "1698 рф":
        bot.send_message(message.from_user.id, "восстания стрельцов")
    elif message.text == "1686 рф":
        bot.send_message(message.from_user.id, "Вечный мир с Речью Посполитой")
    elif message.text == "1686-1700 рф":
        bot.send_message(message.from_user.id, "война с Османской империей")
    elif message.text == "1687 рф":
        bot.send_message(message.from_user.id, "основание Славяно-греко-латинской академии в Москв"
                                               " и Крымские походы")
    elif message.text == "1689 рф":
        bot.send_message(message.from_user.id, "Нерчинский договор с Китаем")
    elif message.text == "1695 рф":
        bot.send_message(message.from_user.id, "Азовские походы")
    elif message.text == "1696 рф":
        bot.send_message(message.from_user.id, "Азовские походы")
    elif message.text == "1697-1698 рф":
        bot.send_message(message.from_user.id, "Великое посольство")
    elif message.text == "1700-1721 рф":
        bot.send_message(message.from_user.id, "Северная война")
    elif message.text == "1700 рф":
        bot.send_message(message.from_user.id, "поражение под Нарвой")
    elif message.text == "1703 16 мая рф":
        bot.send_message(message.from_user.id, "основание С.-Петербурга")
    elif message.text == "1705-1706 рф":
        bot.send_message(message.from_user.id, "восстание в Астрахани")
    elif message.text == "1707-1708 рф":
        bot.send_message(message.from_user.id, "восстание Кондратия Булавина")
    elif message.text == "1708-1710 рф":
        bot.send_message(message.from_user.id, "учреждение губерний")
    elif message.text == "1708 сентябрь рф":
        bot.send_message(message.from_user.id, "битва при д.Лесной")
    elif message.text == "1709 27 июня рф":
        bot.send_message(message.from_user.id, "Полтавская битва")
    elif message.text == "1711 рф":
        bot.send_message(message.from_user.id, "учреждение Сената; Прутский поход")
    elif message.text == "1714 рф":
        bot.send_message(message.from_user.id, "указ о единонаследии")
    elif message.text == "1714 27 июля рф":
        bot.send_message(message.from_user.id, "Гангутское сражение")
    elif message.text == "1718-1721 рф":
        bot.send_message(message.from_user.id, "учреждение коллегий")
    elif message.text == "1718-1724 рф":
        bot.send_message(message.from_user.id, "проведение подушной переписи и первой ревизии")
    elif message.text == "1720 рф":
        bot.send_message(message.from_user.id, "сражение у о. Гренгам")
    elif message.text == "1721 рф":
        bot.send_message(message.from_user.id, "Ништадтский мир"
                                               " и провозглашение России империей")
    elif message.text == "1722 рф":
        bot.send_message(message.from_user.id, "введение Табели о рангах")
    elif message.text == "1722-1723 рф":
        bot.send_message(message.from_user.id, "Каспийский (Персидский) поход")
    elif message.text == "1725 рф":
        bot.send_message(message.from_user.id, "учреждение Академии наук в Петербурге")
    elif message.text == "1725-1727 рф":
        bot.send_message(message.from_user.id, "правление Екатерины I")
    elif message.text == "1727-1730 рф":
        bot.send_message(message.from_user.id, "правление Петра II")
    elif message.text == "1730-1740 рф":
        bot.send_message(message.from_user.id, "правление Анны Иоанновны")
    elif message.text == "1733-1735 рф":
        bot.send_message(message.from_user.id, "война за Польское наследство")
    elif message.text == "1736-1739 рф":
        bot.send_message(message.from_user.id, "Русско-турецкая война")
    elif message.text == "1741-1743 рф":
        bot.send_message(message.from_user.id, "Русско-шведская война")
    elif message.text == "1740-1741 рф":
        bot.send_message(message.from_user.id, "правление Иоанна Антоновича")
    elif message.text == "1741-1761 рф":
        bot.send_message(message.from_user.id, "правление Елизаветы Петровны")
    elif message.text == "1755 рф":
        bot.send_message(message.from_user.id, "основание Московского университета")
    elif message.text == "1756-1763 рф":
        bot.send_message(message.from_user.id, "Семилетняя война")
    elif message.text == "1761-1762 рф":
        bot.send_message(message.from_user.id, "правление Петра III")
    elif message.text == "1762 рф":
        bot.send_message(message.from_user.id, "Манифест о вольности дворянской")
    elif message.text == "1762-1796 рф":
        bot.send_message(message.from_user.id, "правление Екатерины II")
    elif message.text == "1769-1774 рф":
        bot.send_message(message.from_user.id, "Русско-турецкая война")
    elif message.text == "1770 26 июня рф":
        bot.send_message(message.from_user.id, "Чесменское сражение")
    elif message.text == "1770 21 июля рф":
        bot.send_message(message.from_user.id, "сражение при Кагуле")
    elif message.text == "1773-1775 рф":
        bot.send_message(message.from_user.id, "восстание Емельяна Пугачёва")
    elif message.text == "1774 рф":
        bot.send_message(message.from_user.id, "Кючук-Кайнарджийский мир с Османской империей")
    elif message.text == "1775 рф":
        bot.send_message(message.from_user.id, "начало губернской реформы")
    elif message.text == "1783 рф":
        bot.send_message(message.from_user.id, "присоединение Крыма к России")
    elif message.text == "1785 рф":
        bot.send_message(message.from_user.id, "Жалованные грамоты дворянству и городам")
    elif message.text == "1787-1791 рф":
        bot.send_message(message.from_user.id, "Русско-турецкая война")
    elif message.text == "1788 рф":
        bot.send_message(message.from_user.id, "Указ об учреждении «Духовного собрания магометанского закона»")
    elif message.text == "1788-1790 рф":
        bot.send_message(message.from_user.id, "Русско-шведская война")
    elif message.text == "1790 11 декабря рф":
        bot.send_message(message.from_user.id, "взятие Измаила")
    elif message.text == "1791 рф":
        bot.send_message(message.from_user.id, "Ясский мир с Османской империей")
    elif message.text == "1772 рф":
        bot.send_message(message.from_user.id, "Разделы Речи Посполитой")
    elif message.text == "1793 рф":
        bot.send_message(message.from_user.id, "Разделы Речи Посполитой")
    elif message.text == "1795 рф":
        bot.send_message(message.from_user.id, "Разделы Речи Посполитой")
    elif message.text == "1796-1801 рф":
        bot.send_message(message.from_user.id, "правление Павла I")
    elif message.text == "1799 рф":
        bot.send_message(message.from_user.id, 'Итальянский и Швейцарский походы русской армии')
    elif message.text == "1801-1825 рф":
        bot.send_message(message.from_user.id, "годы правления Александра I")
    elif message.text == "1805 20 ноября рф":
        bot.send_message(message.from_user.id, "битва при Аустерлице")
    elif message.text == "1807 25 июня рф":
        bot.send_message(message.from_user.id, "Тильзитский мир")
    elif message.text == "1810 1 января рф":
        bot.send_message(message.from_user.id, "учреждение Государственного Совета")
    elif message.text == "1811 рф":
        bot.send_message(message.from_user.id, "учреждение Царскосельского лицея")
    elif message.text == "1812 рф":
        bot.send_message(message.from_user.id, "Бухарестский мир с Османской империей")
    elif message.text == "1812 12 июня-14 декабря рф":
        bot.send_message(message.from_user.id, "Отечественная война 1812 г.")
    elif message.text == "1812 26 августа рф":
        bot.send_message(message.from_user.id, "Бородинская битва")
    elif message.text == "1813-1814 рф":
        bot.send_message(message.from_user.id, "Заграничные походы русской армии")
    elif message.text == "1813 4-7 октября рф":
        bot.send_message(message.from_user.id, "битва при Лейпциге")
    elif message.text == "1815 рф":
        bot.send_message(message.from_user.id, "Венский конгресс")
    elif message.text == "1817-1864 рф":
        bot.send_message(message.from_user.id, "война на Северном Кавказе")
    elif message.text == "1821 рф":
        bot.send_message(message.from_user.id, "образование Северного и Южного обществ")
    elif message.text == "1824 рф":
        bot.send_message(message.from_user.id, "открытие Малого театра в Москве")
    elif message.text == "1825 рф":
        bot.send_message(message.from_user.id, "открытие Большого театра в Москве")
    elif message.text == "1825 14 декабря рф":
        bot.send_message(message.from_user.id, "восстание декабристов на Сенатской площади")
    elif message.text == "1825-1855 рф":
        bot.send_message(message.from_user.id, "годы правления Николая I")
    elif message.text == "1826 рф":
        bot.send_message(message.from_user.id, "открытие неевклидовой геометрии Н.И. Лобачевским")
    elif message.text == "1828 рф":
        bot.send_message(message.from_user.id, "Туркманчайский мир с Персией")
    elif message.text == "1829 рф":
        bot.send_message(message.from_user.id, "Адрианопольский мир с Османской империей")
    elif message.text == "1837-1841 рф":
        bot.send_message(message.from_user.id, "реформа управления государственными крестьянами П.Д. Киселева")
    elif message.text == "1853-1856 рф":
        bot.send_message(message.from_user.id, "Крымская война")
    elif message.text == "1856 рф":
        bot.send_message(message.from_user.id, "Парижский трактат")
    elif message.text == "1855-1881 рф":
        bot.send_message(message.from_user.id, "годы правления Александра II")
    elif message.text == "1858-1861 рф":
        bot.send_message(message.from_user.id, "присоединение к России Приамурья и Дальнего Востока")
    elif message.text == "1861 19 февраля рф":
        bot.send_message(message.from_user.id,
                         "издание Манифеста об освобождении крестьян и «Положения о крестьянах, вышедших из крепостной зависимости»")
    elif message.text == "1862 рф":
        bot.send_message(message.from_user.id, "учреждение Санкт-Петербургской консерватории")
    elif message.text == "1863-1864 рф":
        bot.send_message(message.from_user.id, "восстание в Польше")
    elif message.text == "1864 рф":
        bot.send_message(message.from_user.id, "судебная реформа"
                                               " и земская реформа")
    elif message.text == "1866 рф":
        bot.send_message(message.from_user.id, "учреждение Московской консерватории")
    elif message.text == "1867 рф":
        bot.send_message(message.from_user.id, "продажа Аляски Соединенным штатам Америки")
    elif message.text == "1869 рф":
        bot.send_message(message.from_user.id, "открытие периодического закона химических элементов Д.И. Менделеевым")
    elif message.text == "1870 рф":
        bot.send_message(message.from_user.id, "возникновение «Товарищества передвижных художественных выставок»"
                                               " и реформа городского самоуправления")
    elif message.text == "1874 рф":
        bot.send_message(message.from_user.id, "военная реформа")
    elif message.text == "1877-1878 рф":
        bot.send_message(message.from_user.id, "Русско-турецкая война")
    elif message.text == "1878 рф":
        bot.send_message(message.from_user.id, "Берлинский конгресс")
    elif message.text == "1881 1 марта рф":
        bot.send_message(message.from_user.id, "убийство императора Александра II")
    elif message.text == "1881-1894 рф":
        bot.send_message(message.from_user.id, "годы правления Александра III")
    elif message.text == "1881 рф":
        bot.send_message(message.from_user.id,
                         "издание «Положения о мерах к охранению государственного порядка и общественного спокойствия»")
    elif message.text == "1884 рф":
        bot.send_message(message.from_user.id, "издание нового Университетского устава")
    elif message.text == "1890 рф":
        bot.send_message(message.from_user.id, "издание нового Земского положения")
    elif message.text == "1891-1892 рф":
        bot.send_message(message.from_user.id, "голод в России")
    elif message.text == "1892 рф":
        bot.send_message(message.from_user.id, "создание Третьяковской галереи")
    elif message.text == "1894 рф":
        bot.send_message(message.from_user.id, "заключение союза с Францией")
    elif message.text == "1894-1917 рф":
        bot.send_message(message.from_user.id, "годы правления Николая II")
    elif message.text == "1897 рф":
        bot.send_message(message.from_user.id, "введение золотого рубля")
    elif message.text == "1898 рф":
        bot.send_message(message.from_user.id, "образование Московского художественного театра (МХТ)")
    elif message.text == "1904-1905 рф":
        bot.send_message(message.from_user.id, "Русско-японская война")
    elif message.text == "1905-1907 рф":
        bot.send_message(message.from_user.id, "Первая российская революция")
    elif message.text == "1905 9 января рф":
        bot.send_message(message.from_user.id, "«Кровавое воскресенье»")
    elif message.text == "1905 17 апреля рф":
        bot.send_message(message.from_user.id, "Указ Об Укреплении Начал Веротерпимости")
    elif message.text == "1905 14-15 мая рф":
        bot.send_message(message.from_user.id, "поражение русского флота в Цусимском сражении")
    elif message.text == "1905 6 августа рф":
        bot.send_message(message.from_user.id, "Манифест об учреждении законосовещательной Государственной думы")
    elif message.text == "1905 5 сентября рф":
        bot.send_message(message.from_user.id, "заключение Портсмутского мира")
    elif message.text == "1905 7-25 октября рф":
        bot.send_message(message.from_user.id, "Всероссийская политическая забастовка")
    elif message.text == "1905 17 октября рф":
        bot.send_message(message.from_user.id,
                         "Высочайший Манифест о даровании свобод и учреждении Государственной думы")
    elif message.text == "1905 9-19 декабря рф":
        bot.send_message(message.from_user.id, "вооруженное восстание в Москве")
    elif message.text == "1905 11 декабря рф":
        bot.send_message(message.from_user.id, "закон о выборах в Государственную думу")
    elif message.text == "1906 23 апреля рф":
        bot.send_message(message.from_user.id, "издание Основных государственных законов")
    elif message.text == "1906 27 апреля-8 июля рф":
        bot.send_message(message.from_user.id, "деятельность I Государственной думы")
    elif message.text == "1906 9 ноября рф":
        bot.send_message(message.from_user.id, "начало аграрной реформы П.А. Столыпина")
    elif message.text == "1907 20 февраля-3 июня рф":
        bot.send_message(message.from_user.id,
                         "деятельность II Государственной думы и издание избирательного закона 3 июня")
    elif message.text == "1907 рф":
        bot.send_message(message.from_user.id, "окончательное оформление Антанты")
    elif message.text == "1907-1912 рф":
        bot.send_message(message.from_user.id, "работа III Государственной думы")
    elif message.text == "1912-1917 рф":
        bot.send_message(message.from_user.id, "работа IV Государственной думы")
    elif message.text == "1914-1918 28 июля-11 ноября рф":
        bot.send_message(message.from_user.id, "Первая мировая война")
    elif message.text == "1914 1 августа рф":
        bot.send_message(message.from_user.id, "объявление Германией войны России")
    elif message.text == "1915 рф":
        bot.send_message(message.from_user.id, "образование Прогрессивного блока")
    elif message.text == "1916 май рф":
        bot.send_message(message.from_user.id, "«Брусиловский прорыв»")
    elif message.text == "1917 февраль-ноябрь рф":
        bot.send_message(message.from_user.id, "Великая российская революция")
    elif message.text == "1917 февраль-март рф":
        bot.send_message(message.from_user.id, "Февральский переворот и падение монархии")
    elif message.text == "1917 26 февраля рф":
        bot.send_message(message.from_user.id,
                         "расстрел демонстрации на Знаменской площади Петрограда, переход части воинских частей на сторону восставших")
    elif message.text == "1917 27 февраля рф":
        bot.send_message(message.from_user.id, "формирование Временного Комитета Государственной думы")
    elif message.text == "1917 2 марта рф":
        bot.send_message(message.from_user.id, "отречение Николая II")
    elif message.text == "1917 1 сентября рф":
        bot.send_message(message.from_user.id, "провозглашение России республикой")
    elif message.text == "1917 25-26 октября рф":
        bot.send_message(message.from_user.id, "свержение Временного правительства, взятие власти большевиками")
    elif message.text == "1917 26 октября рф":
        bot.send_message(message.from_user.id, "создание Совета народных комиссаров (советского правительства)")
    elif message.text == "1917-1921 ноябрь рф":
        bot.send_message(message.from_user.id, "период Гражданской войны")
    elif message.text == "1917 ноябрь рф":
        bot.send_message(message.from_user.id, "принятие Декларации прав народов России")
    elif message.text == "1917 декабрь рф":
        bot.send_message(message.from_user.id, "создание Всероссийской чрезвычайной комиссии (ВЧК)"
                                               "создание Высшего совета народного хозяйства (ВСНХ)")
    elif message.text == "1918 5-6 января рф":
        bot.send_message(message.from_user.id, "Учредительное собрание")
    elif message.text == "1918 январь рф":
        bot.send_message(message.from_user.id, "создание регулярной Красной Армии (РККА)")
    elif message.text == "1918 3 марта рф":
        bot.send_message(message.from_user.id,
                         "подписание советским правительством Брестского мира с Германией и выход России из Первой мировой войны")
    elif message.text == "1918 рф":
        bot.send_message(message.from_user.id, "признание советским правительством независимости Финляндии")
    elif message.text == "1918 Май рф":
        bot.send_message(message.from_user.id,
                         "восстание чехословацкого корпуса, начало широкомасштабной Гражданской войны в России")
    elif message.text == "1918 июль рф":
        bot.send_message(message.from_user.id, "выступление левых эсеров против большевиков"
                                               "принятие первой советской Конституции России")
    elif message.text == "1918 5 сентября рф":
        bot.send_message(message.from_user.id, "объявление большевиками «красного террора»")
    elif message.text == "1918 18 ноября рф":
        bot.send_message(message.from_user.id, "свержение Директории и установление диктатуры А.В.Колчака")
    elif message.text == "1919 май-октябрь рф":
        bot.send_message(message.from_user.id, "наступление Белой армии под командованием А.И.Деникина")
    elif message.text == "1919-1920 октябрь-январь рф":
        bot.send_message(message.from_user.id, "общее наступление Красной Армии")
    elif message.text == "1920-1921 рф":
        bot.send_message(message.from_user.id, "Занятие Красной Армией Азербайджана, Армении, Хивы и Бухары, Грузии"
                                               "Тамбовское антибольшевистское восстание")
    elif message.text == "1920 рф":
        bot.send_message(message.from_user.id,
                         "заключение Советской Россией мирных договоров с Литвой, Латвией и Эстонией."
                         "принятие плана ГОЭЛРО")
    elif message.text == "1920 апрель-октябрь рф":
        bot.send_message(message.from_user.id, "боевые действия в ходе советско-польской войны")
    elif message.text == "1920 ноябрь рф":
        bot.send_message(message.from_user.id, "разгром армии П.Н. Врангеля в Крыму")
    elif message.text == "1921 рф":
        bot.send_message(message.from_user.id, "Рижский мир с Польшей")
    elif message.text == "1917-1924 рф":
        bot.send_message(message.from_user.id, "В.И.Ленин во главе страны")
    elif message.text == "1921 март рф":
        bot.send_message(message.from_user.id, "восстание в Кронштадте")
    elif message.text == "1920-1921 рф":
        bot.send_message(message.from_user.id, "Тамбовское восстание")
    elif message.text == "1921 14 марта рф":
        bot.send_message(message.from_user.id, "переход к нэпу")
    elif message.text == "1921—1922 рф":
        bot.send_message(message.from_user.id, "Голод в советской России")
    elif message.text == "1922 16 апреля рф":
        bot.send_message(message.from_user.id, "Договор в Рапалло")
    elif message.text == "1922 рф":
        bot.send_message(message.from_user.id, "завершение гражданской войны на Дальнем Востоке.")
    elif message.text == "1922 30 декабря рф":
        bot.send_message(message.from_user.id, "создание СССР")
    elif message.text == "1922-1924 рф":
        bot.send_message(message.from_user.id, "финансовая реформа")
    elif message.text == "1923 рф":
        bot.send_message(message.from_user.id, "создание Госплана")
    elif message.text == "1924 рф":
        bot.send_message(message.from_user.id, "принятие Конституции СССР"
                                               "«Полоса признания СССР»")
    elif message.text == "1924-1953 рф":
        bot.send_message(message.from_user.id, "И.В. Сталин во главе СССР")
    elif message.text == "1925 рф":
        bot.send_message(message.from_user.id, "начало разработки ежегодных народнохозяйственных планов")
    elif message.text == "1927 рф":
        bot.send_message(message.from_user.id, "учреждение звания «Герой Труда»")
    elif message.text == "1928-1929 рф":
        bot.send_message(message.from_user.id, "свёртывание нэпа")
    elif message.text == "1928 рф":
        bot.send_message(message.from_user.id, "Шахтинский процесс")
    elif message.text == "1928-1932 рф":
        bot.send_message(message.from_user.id, "первая пятилетка")
    elif message.text == "1929 рф":
        bot.send_message(message.from_user.id, "принятие первого пятилетнего планас"
                                               "переход к сплошной коллективизации сельского хозяйства (год «великого перелома»)")
    elif message.text == "1930 рф":
        bot.send_message(message.from_user.id, "ликвидация массовой безработицы, закрытие бирж труда")
    elif message.text == "1930-1935 рф":
        bot.send_message(message.from_user.id, "карточная система снабжения населения")
    elif message.text == "1932 рф":
        bot.send_message(message.from_user.id, "введение паспортной системы")
    elif message.text == "1932-1933 рф":
        bot.send_message(message.from_user.id, "голод в СССР")
    elif message.text == "1933-1937 рф":
        bot.send_message(message.from_user.id, "вторая пятилетка")
    elif message.text == "1934 рф":
        bot.send_message(message.from_user.id, "учреждение звания Герой Советского Союза")
    elif message.text == "1936 рф":
        bot.send_message(message.from_user.id, "принятие новой Конституции СССР")
    elif message.text == "1937-1938 рф":
        bot.send_message(message.from_user.id, "пик массовых политических репрессий")
    elif message.text == "1938 рф":
        bot.send_message(message.from_user.id, "учреждение звания «Герой Социалистического Труда»")
    elif message.text == "1938 24 июля-11 августа рф":
        bot.send_message(message.from_user.id, "военный конфликт с Японией на оз. Хасан")
    elif message.text == "1939 11 мая-16 сентября рф":
        bot.send_message(message.from_user.id, "военный конфликт с Японией на р. Халхин-Гол")
    elif message.text == "1939 23 августа рф":
        bot.send_message(message.from_user.id, "советско-германский договор о ненападении")
    elif message.text == "1939 1 сентября рф":
        bot.send_message(message.from_user.id, "начало Второй мировой войны")
    elif message.text == "1939-1940 рф":
        bot.send_message(message.from_user.id, "советско-финская («зимняя») война")
    elif message.text == "1940 рф":
        bot.send_message(message.from_user.id, "вхождение прибалтийских государств в СССР")
    elif message.text == "1939-1945 рф":
        bot.send_message(message.from_user.id, "Вторая мировая война")
    elif message.text == "1941-1945 рф":
        bot.send_message(message.from_user.id, "Великая Отечественная война")
    elif message.text == "1941 24 июня рф":
        bot.send_message(message.from_user.id, "создание Совета по эвакуации")
    elif message.text == "1941 10 июля-10 сентября рф":
        bot.send_message(message.from_user.id, "Смоленское сражение")
    elif message.text == "1941 8 сентября рф":
        bot.send_message(message.from_user.id, "начало блокады Ленинграда")
    elif message.text == "1941 30 сентября рф":
        bot.send_message(message.from_user.id, "начало битвы под Москвой")
    elif message.text == "1941 7 ноября рф":
        bot.send_message(message.from_user.id,
                         "парад войск московского гарнизона и московской зоны обороны на Красной площади")
    elif message.text == "1941 7 ноября рф":
        bot.send_message(message.from_user.id, "официальное решение США о распространении ленд-лиза на СССР")
    elif message.text == "1941 5-6 декабря рф":
        bot.send_message(message.from_user.id, "переход советских войск в контрнаступление под Москвой")
    elif message.text == "1942 17 июля-2 февраля рф":
        bot.send_message(message.from_user.id, "Сталинградская битва")
    elif message.text == "1942 25 июля рф":
        bot.send_message(message.from_user.id, "начало Битвы за Кавказ")
    elif message.text == "1942 28 июля рф":
        bot.send_message(message.from_user.id, "приказ № 227 («Ни шагу назад!»)")
    elif message.text == "1942 19 ноября рф":
        bot.send_message(message.from_user.id, "переход советских войск в контрнаступление под Сталинградом")
    elif message.text == "1943 12-18 января рф":
        bot.send_message(message.from_user.id, "прорыв блокады Ленинграда")
    elif message.text == "1943 5 июля-23 августа рф":
        bot.send_message(message.from_user.id, "Курская битва")
    elif message.text == "1943 5 августа рф":
        bot.send_message(message.from_user.id, "освобождение Орла и Белгорода, первый салют в Москве")
    elif message.text == "1943 3 августа-15 сентября рф":
        bot.send_message(message.from_user.id, "партизанская операция «Рельсовая война»")
    elif message.text == "1943 6 ноября рф":
        bot.send_message(message.from_user.id, "освобождение Киева")
    elif message.text == "1943 28 ноября-1 декабря рф":
        bot.send_message(message.from_user.id, "Тегеранская конференция")
    elif message.text == "1944 27 января рф":
        bot.send_message(message.from_user.id, "полное освобождение Ленинграда от вражеской блокады")
    elif message.text == "1944 26 марта рф":
        bot.send_message(message.from_user.id,
                         "выход советских войск на румынскую границу, начало освобождения Красной Армией стран Европы (1944-1945)")
    elif message.text == "1944 6 июня рф":
        bot.send_message(message.from_user.id, "высадка союзников во Франции, открытие второго фронта")
    elif message.text == "1944 23 июня-29 августа рф":
        bot.send_message(message.from_user.id, "Белорусская наступательная операция советских войск")
    elif message.text == "1943-1944 рф":
        bot.send_message(message.from_user.id, "депортация «репрессированных народов» СССР")
    elif message.text == "1945 27 января рф":
        bot.send_message(message.from_user.id, "освобождение Освенцима")
    elif message.text == "1945 4-11 февраля рф":
        bot.send_message(message.from_user.id, "Ялтинская конференция")
    elif message.text == "1945 16 апреля-2 мая рф":
        bot.send_message(message.from_user.id, "поход Олега на Константинополь")
    elif message.text == "1945 25 апреля-26 июня рф":
        bot.send_message(message.from_user.id, "Конференция Объединенных наций в Сан-Франциско. Принятие Устава ООН")
    elif message.text == "1945 9 мая рф":
        bot.send_message(message.from_user.id,
                         "безоговорочная капитуляция Германии, окончание Великой Отечественной войны")
    elif message.text == "1945 17 июля-2 августа рф":
        bot.send_message(message.from_user.id, "Потсдамская конференция")
    elif message.text == "1945 9 августа-2 сентября рф":
        bot.send_message(message.from_user.id, "советско-японская война")
    elif message.text == "1945 2 сентября рф":
        bot.send_message(message.from_user.id, "капитуляция Японии и окончание Второй мировой войны")
    elif message.text == "1946 Март рф":
        bot.send_message(message.from_user.id, "Фултонская речь У. Черчилля")
    elif message.text == "1946-1991 рф":
        bot.send_message(message.from_user.id, "период «холодной войны»")
    elif message.text == "1947 рф":
        bot.send_message(message.from_user.id, "выдвижение Плана Маршалла"
                                               " и отмена карточек на продукты и денежная реформа")
    elif message.text == "1946-1947 рф":
        bot.send_message(message.from_user.id, "голод в СССР")
    elif message.text == "1946 рф":
        bot.send_message(message.from_user.id, "постановление ЦК ВКП (б) «О журналах «Звезда» и «Ленинград»».")
    elif message.text == "1947-1956 рф":
        bot.send_message(message.from_user.id, "деятельность Коминформбюро")
    elif message.text == "1948 рф":
        bot.send_message(message.from_user.id, "дело Еврейского антифашистского комитета")
    elif message.text == "1949 рф":
        bot.send_message(message.from_user.id, "создание Совета экономической взаимопомощи (СЭВ)"
                                               ", организация Североатлантического договора (НАТО)"
                                               " и первое успешное испытание советской атомной бомбы")
    elif message.text == "1948-1949 рф":
        bot.send_message(message.from_user.id, "1-й Берлинский кризис")
    elif message.text == "1949-1950 рф":
        bot.send_message(message.from_user.id, "«Ленинградское дело»")
    elif message.text == "1950-1953 рф":
        bot.send_message(message.from_user.id, "война в Корее")
    elif message.text == "1952 рф":
        bot.send_message(message.from_user.id, "XIX съезд ВКП (б). Переименование ВКП (б) в КПСС")
    elif message.text == "1953 5 марта рф":
        bot.send_message(message.from_user.id, "смерть И.В. Сталина")
    elif message.text == "1953-1964 рф":
        bot.send_message(message.from_user.id, "Н.С.Хрущев – первый секретарь ЦК КПСС")
    elif message.text == "1954 рф":
        bot.send_message(message.from_user.id, "начало освоения целинных земель")
    elif message.text == "1955 рф":
        bot.send_message(message.from_user.id, "создание Организации Варшавского договора (ОВД)")
    elif message.text == "1956 рф":
        bot.send_message(message.from_user.id, "XX съезд КПСС, разоблачение культа личности Сталина"
                                               "Суэцкий кризис, политический кризис в Венгрии и реакция СССР")
    elif message.text == "1957 рф":
        bot.send_message(message.from_user.id, "Всемирный фестиваль молодежи и студентов в Москве"
                                               " и запуск СССР первого в мире искусственного спутника Земли")
    elif message.text == "1961 12 апреля рф":
        bot.send_message(message.from_user.id, "полет в космос первого в мире космонавта Ю.А. Гагарина")
    elif message.text == "1961 рф":
        bot.send_message(message.from_user.id, "второй Берлинский кризис. Сооружение Берлинской стены"
                                               " и XXII съезд КПСС. Принятие Программы построения коммунизма")
    elif message.text == "1961 рф":
        bot.send_message(message.from_user.id, "XXII съезд КПСС. Принятие Программы построения коммунизма")
    elif message.text == "1962 рф":
        bot.send_message(message.from_user.id, "события в г. Новочеркасске"
                                               " и Карибский кризис")
    elif message.text == "1963 рф":
        bot.send_message(message.from_user.id, "космический полет первой в мире женщины-космонавта В.В.Терешковой")
    elif message.text == "1964 рф":
        bot.send_message(message.from_user.id, "смещение Н.С. Хрущева с поста первого секретаря ЦК КПСС.")
    elif message.text == "1964-1982 рф":
        bot.send_message(message.from_user.id, "первый (с 1966 г. – Генеральный) секретарь ЦК КПСС Л.И.Брежнев")
    elif message.text == "1965 рф":
        bot.send_message(message.from_user.id, "начало реформы А.Н. Косыгина")
    elif message.text == "1968 рф":
        bot.send_message(message.from_user.id,
                         "Пражская весна». Ввод войск стран ОВД в Чехословакию по инициативе СССР")
    elif message.text == "1969 рф":
        bot.send_message(message.from_user.id, "пограничный советско-китайский конфликт")
    elif message.text == "1972 рф":
        bot.send_message(message.from_user.id,
                         "Советско-американский договор об ограничении систем противоракетной обороны (ПРО) и Договор об ограничении стратегических вооружений (ОСВ-1)")
    elif message.text == "1975 рф":
        bot.send_message(message.from_user.id,
                         "завершающий этап Совещания по безопасности и сотрудничеству в Европе (СБСЕ) в Хельсинки. Подписание Заключительного акта.")
    elif message.text == "1977 рф":
        bot.send_message(message.from_user.id, "принятие последней Конституции СССР")
    elif message.text == "1979 рф":
        bot.send_message(message.from_user.id,
                         "Договор между СССР и США об ограничении стратегических вооружений-2 (ОСВ-2)"
                         " и ввод советских войск в Афганистан")
    elif message.text == "1980 рф":
        bot.send_message(message.from_user.id, "летние Олимпийские игры в Москве")
    elif message.text == "1982 рф":
        bot.send_message(message.from_user.id, "смерть Л.И. Брежнева")
    elif message.text == "1982-1984 рф":
        bot.send_message(message.from_user.id, "Ю.В. Андропов - Генеральный секретарь ЦК КПСС")
    elif message.text == "1984-1985 рф":
        bot.send_message(message.from_user.id, "К.У. Черненко - Генеральный секретарь ЦК КПСС")
    elif message.text == "1985 март рф":
        bot.send_message(message.from_user.id, "избрание М.С. Горбачева Генеральным секретарем ЦК КПСС")
    elif message.text == "1985 апрель рф":
        bot.send_message(message.from_user.id,
                         "(Пленум ЦК КПСС) - провозглашение М.С.Горбачевым курса на ускорение экономического развития страны")
    elif message.text == "1986 февраль  рф":
        bot.send_message(message.from_user.id,
                         "провозглашение основных направлений политики «перестройки» на XXVII съезде КПСС")
    elif message.text == "1986 26 апреля рф":
        bot.send_message(message.from_user.id, "авария на Чернобыльской АЭС")
    elif message.text == "1987 январь рф":
        bot.send_message(message.from_user.id, "провозглашение политики гласности")
    elif message.text == "1988 июнь-июль рф":
        bot.send_message(message.from_user.id, "ХIХ конференция КПСС")
    elif message.text == "1989 февраль рф":
        bot.send_message(message.from_user.id, "вывод советских войск из Афганистана")
    elif message.text == "1989 май-июнь рф":
        bot.send_message(message.from_user.id, "I Съезд народных депутатов СССР")
    elif message.text == "1990 февраль-май рф":
        bot.send_message(message.from_user.id,
                         "начало процесса объявления государственной независимости союзными республиками СССР")
    elif message.text == "1990 15 марта рф":
        bot.send_message(message.from_user.id,
                         "избрание М.С.Горбачева Президентом СССР на III Съезде народных депутатов СССР")
    elif message.text == "1990 апрель рф":
        bot.send_message(message.from_user.id,
                         "план «автономизации» М.С.Горбачева и законы о разграничении полномочий между Союзом ССР и субъектами федерации (повышение статуса автономий до уровня союзных республик)")
    elif message.text == "1990 май-июнь рф":
        bot.send_message(message.from_user.id,
                         "I Съезд народных депутатов РСФСР. 1990 г., 12 июня - Принятие Декларации о государственном суверенитете РСФСР")
    elif message.text == "1990 май рф":
        bot.send_message(message.from_user.id, "создание Коммунистической партии РСФСР")
    elif message.text == "1990 июнь-октябрь рф":
        bot.send_message(message.from_user.id, "борьба экономических программ перехода СССР к рынку")
    elif message.text == "1990 июль рф":
        bot.send_message(message.from_user.id,
                         "совместное поручение М.С.Горбачева и Б.Н.Ельцина о подготовке согласованной программы перехода СССР и РСФСР к рыночной экономике")
    elif message.text == "1991 17 марта рф":
        bot.send_message(message.from_user.id, "референдум о сохранении СССР и о введении поста Президента РСФСР")
    elif message.text == "1991 июнь рф":
        bot.send_message(message.from_user.id, "избрание Б.Н.Ельцина Президентом РСФСР.")
    elif message.text == "1991 19-21 августа рф":
        bot.send_message(message.from_user.id, "ГКЧП и оборона Белого дома")
    elif message.text == "1991 август рф":
        bot.send_message(message.from_user.id, "сложение М.С.Горбачевым полномочий Генерального секретаря ЦК КПСС")
    elif message.text == "1991 22 августа рф":
        bot.send_message(message.from_user.id,
                         "Указ Президента РСФСР Б.Н.Ельцина о приостановлении деятельности Коммунистической партии РСФСР")
    elif message.text == "1991 22 августа-2 октября рф":
        bot.send_message(message.from_user.id, "запрет деятельности коммунистических партий в союзных республиках")
    elif message.text == "1991 29 августа рф":
        bot.send_message(message.from_user.id,
                         "Решение Верховного Совета СССР от 29 августа 1991 года о приостановке деятельности КПСС на всей территории СССР")
    elif message.text == "1991 август-октябрь рф":
        bot.send_message(message.from_user.id,
                         "объявление государственной независимости союзными республиками, за исключением России и Казахстана")
    elif message.text == "1991 6 ноября рф":
        bot.send_message(message.from_user.id,
                         "Указ Президента РСФСР Б.Н.Ельцина о прекращении деятельности КПСС и роспуске её структур на территории РСФСР")
    elif message.text == "1991 1 декабря рф":
        bot.send_message(message.from_user.id, "референдум о независимости Украины")
    elif message.text == "1991 декабрь рф":
        bot.send_message(message.from_user.id,
                         "юридическое оформление распада СССР и создание Содружества Независимых Государств («Беловежское соглашение», Алма-Атинские документы)")
    elif message.text == "1992 2 января рф":
        bot.send_message(message.from_user.id, "начало экономической реформы")
    elif message.text == "1992 рф":
        bot.send_message(message.from_user.id,
                         "указ Президента РФ о введении в действие системы приватизационных чеков (ваучеров), начало приватизации госимущества")
    elif message.text == "1992 март рф":
        bot.send_message(message.from_user.id,
                         "подписание субъектами РФ Федеративного договора (кроме Татарстана и Чечни)")
    elif message.text == "1993 январь рф":
        bot.send_message(message.from_user.id, "подписание Договора СНВ-2 между Россией и США")
    elif message.text == "1993 25 апреля рф":
        bot.send_message(message.from_user.id, "референдум о доверии Президенту Б.Н.Ельцину и Верховному совету")
    elif message.text == "1993 21 сентября рф":
        bot.send_message(message.from_user.id,
                         "Указ Президента РФ №1400 «О поэтапной конституци-онной реформе», объявление о роспуске съезда народных депутатов и Верховного Совета и о проведении 12 декабря 1993 г. референдума по новой Конституции")
    elif message.text == "1993 1-3 октября рф":
        bot.send_message(message.from_user.id,
                         "безрезультатные переговоры о мирном разрешении политического кризиса в Свято-Даниловом монастыре")
    elif message.text == "1993 октябрь рф":
        bot.send_message(message.from_user.id, "трагические события в Москве, обстрел Белого дома")
    elif message.text == "1993 12 декабря рф":
        bot.send_message(message.from_user.id, "принятие Конституции РФ и выборы в Федеральное Собрание РФ")
    elif message.text == "1994 февраль рф":
        bot.send_message(message.from_user.id,
                         "объявление Государственной Думой РФ амнистии участникам событий октября 1993 г.")
    elif message.text == "1994 февраль рф":
        bot.send_message(message.from_user.id, "подписание договора Российской Федерации с Татарстаном")
    elif message.text == "1994 август рф":
        bot.send_message(message.from_user.id, "завершение вывода советских / российских войск из Германии")
    elif message.text == "1994 декабрь рф":
        bot.send_message(message.from_user.id, "начало военно-политического кризиса в Чеченской Республике")
    elif message.text == "1995 июнь рф":
        bot.send_message(message.from_user.id, "нападение боевиков на г. Буденновск")
    elif message.text == "1996 рф":
        bot.send_message(message.from_user.id, "выборы Президента РФ"
                                               ", Хасавюртовские соглашения"
                                               " и вступление России в Совет Европы")
    elif message.text == "1998 август рф":
        bot.send_message(message.from_user.id, "дефолт, финансовый кризис")
    elif message.text == "1999 рф":
        bot.send_message(message.from_user.id, "возобновление военного конфликта на Северном Кавказе"
                                               "и добровольная отставка (сложение полномочий) Б.Н.Ельцина ")
    elif message.text == "2000 рф":
        bot.send_message(message.from_user.id, "выборы и вступление в должность Президента РФ В.В.Путина"
                                               ", создание института Полномочных представителей Президента РФ в федеральных округах, создание Государственного Совета РФ"
                                               " и утверждение новой концепции внешней политики РФ")
    elif message.text == "2003 рф":
        bot.send_message(message.from_user.id, "выборы в Государственную Думу")
    elif message.text == "2004 рф":
        bot.send_message(message.from_user.id, "избрание В.В. Путина Президентом РФ на второй срок")
    elif message.text == "2008 август рф":
        bot.send_message(message.from_user.id, "операция по принуждению Грузии к миру")
    elif message.text == "2008 рф":
        bot.send_message(message.from_user.id,
                         "вступление России в мировой финансовый кризис. Корректировка тактики социально-экономического развития в условиях финансово-экономического кризиса в РФ (2008г.)"
                         ", принятие закона об увеличении срока полномочий Государственной Думы до 5 лет и Президента РФ до 6 лет"
                         " и избрание Д.А. Медведева Президентом РФ")
    elif message.text == "2012 рф":
        bot.send_message(message.from_user.id, "избрание В.В. Путина Президентом РФ")
    elif message.text == "2014 рф":
        bot.send_message(message.from_user.id, "Зимняя Олимпиада в Сочи"
                                               " и договор о принятии Республики Крым и г.Севастополя в состав России")
    ########################################################всеобщей истории
    ########################################################всеобщей истории
    ########################################################всеобщей истории
    elif message.text == "1700-1721":
        bot.send_message(message.from_user.id, "Великая Северная войня")
    elif message.text == "1701":
        bot.send_message(message.from_user.id, "Провозглашение королевства Пруссия")
    elif message.text == "1701-1714":
        bot.send_message(message.from_user.id, "Война за испанское наследство")
    elif message.text == "1707":
        bot.send_message(message.from_user.id, "Акт единения между Англией и Шотландией. Создания Великобритании")
    elif message.text == "1709":
        bot.send_message(message.from_user.id, "Полтавская битва")
    elif message.text == "1710-1774":
        bot.send_message(message.from_user.id, "Годы жизни Людовика XVI, короля Франции (1774-1792)")
    elif message.text == "1721":
        bot.send_message(message.from_user.id, "Провозглашение Российской Империи")
    elif message.text == "1736-1795":
        bot.send_message(message.from_user.id, "Правление Цяньлуна в цинском Китае")
    elif message.text == "1739":
        bot.send_message(message.from_user.id, "Нашествие на империю Великих Моголов иранского правителя Надир-шаха")
    elif message.text == "1740-1780":
        bot.send_message(message.from_user.id, "Правление Марии Терезии в монархии Габсбургов")
    elif message.text == "1740-1786":
        bot.send_message(message.from_user.id, "Правление Фридриха II в Пруссии ")
    elif message.text == "1754-1793":
        bot.send_message(message.from_user.id, "Годы жизни Людовика XVI, короля Франции (1774-1792)")
    elif message.text == "1756-1763":
        bot.send_message(message.from_user.id, "Семелетняя война")
    elif message.text == "1757":
        bot.send_message(message.from_user.id, "Битва при Плесси. Начало британского господства в Индии")
    elif message.text == "1760":
        bot.send_message(message.from_user.id, "Начало промышленной революции в Англии")
    elif message.text == "1762-1796":
        bot.send_message(message.from_user.id, "Правление Екатерине II в России")
    elif message.text == "1765":
        bot.send_message(message.from_user.id, "Создание Дж. Харгривсом механической прялки"
                                               " и акт о гербовом сборе")
    elif message.text == "1772":
        bot.send_message(message.from_user.id, "Первый раздел Польши")
    elif message.text == "1773":
        bot.send_message(message.from_user.id, "Бостонское чаепитие")
    elif message.text == "1774":
        bot.send_message(message.from_user.id, "Кючук-Кайнарджийский мирный договор")
    elif message.text == "1775-1783":
        bot.send_message(message.from_user.id, "Война за независимость североамериканских колоний Англии")
    elif message.text == "1776 4 июля":
        bot.send_message(message.from_user.id, "Принятие Декларации независимости США ")
    elif message.text == "1780-1790":
        bot.send_message(message.from_user.id, "Правление в монархии Габсбургов Иосифа II")
    elif message.text == "1783":
        bot.send_message(message.from_user.id, "Включение Крыма в состав Российской империи")
    elif message.text == "1784":
        bot.send_message(message.from_user.id, "Создание Дж.Уаттом паровой машины")
    elif message.text == "1787":
        bot.send_message(message.from_user.id, "Принятие Конституции США")
    elif message.text == "1789 5 мая":
        bot.send_message(message.from_user.id, "начало работы Генеральных штатов во Франции")
    elif message.text == "1789 17 июня":
        bot.send_message(message.from_user.id, "Депутаты Генеральных штатов от третьего сословия объявили себя ")
    elif message.text == "1789 9 июля":
        bot.send_message(message.from_user.id, "Начало работы Учредительного собрания во Франции")
    elif message.text == "1789 14 июля":
        bot.send_message(message.from_user.id, "Взятие Бастилии в Париже ")
    elif message.text == "1789 26 августа":
        bot.send_message(message.from_user.id,
                         "Принятие Учредительным собранием во  франции Декларации прав человека и гражданина")
    elif message.text == "1789-1808":
        bot.send_message(message.from_user.id, "Правление османского султана Селима III")
    elif message.text == "1791":
        bot.send_message(message.from_user.id, "Приняятие первой в истории Франции Конституции")
    elif message.text == "1791 1 октября":
        bot.send_message(message.from_user.id, "Начало работы Законодательного собрания во Франции")
    elif message.text == "1792":
        bot.send_message(message.from_user.id, "Начало революционных войн во Франции")
    elif message.text == "1792 9-10 августа":
        bot.send_message(message.from_user.id, "Восстание и крушение монархии во Франции")
    elif message.text == "1793 2 июня":
        bot.send_message(message.from_user.id, "Приход к власти якобинцев")
    elif message.text == "1793":
        bot.send_message(message.from_user.id, "Второй раздел Польши")
    elif message.text == "1794 27 июля":
        bot.send_message(message.from_user.id, "Переворот 9 термидора")
    elif message.text == "1795":
        bot.send_message(message.from_user.id, "Учреждение Директории и принятие республиканской Конституции")
    elif message.text == "1796-1797":
        bot.send_message(message.from_user.id, "Итальянский поход Наполеона Бонапарта")
    elif message.text == "1798-1799":
        bot.send_message(message.from_user.id, "Египетский поход Наполеона Бонапарта")
    elif message.text == "1799 9-10 ноября":
        bot.send_message(message.from_user.id,
                         "Государственный переворот Напалеона Бонапарта 18-19 брюмера. Завершение революции во Франции")
    elif message.text == "1799":
        bot.send_message(message.from_user.id, "Итальянский и Швейцарский походы А. В. Суворова")
    elif message.text == "1799-1804":
        bot.send_message(message.from_user.id, "Период консульства во франции")
    elif message.text == "1802":
        bot.send_message(message.from_user.id, "Наполеон Бонапарт становится пожизненным консулом")
    elif message.text == "1803":
        bot.send_message(message.from_user.id, "пущен первый паровой автомобиль")
    elif message.text == "1804 18 мая":
        bot.send_message(message.from_user.id, "Наполеон Банопарт становится (императором французов)")
    elif message.text == "1804":
        bot.send_message(message.from_user.id, "издани Гражданского кодекса Наполеона")
    elif message.text == "1804-1814":
        bot.send_message(message.from_user.id, "Первая империя во Франции")
    elif message.text == "1805 декабрь":
        bot.send_message(message.from_user.id, "сражение при Аустрелице")
    elif message.text == "1806 21 ноября":
        bot.send_message(message.from_user.id, "декрет Наполеона I о континентальной блокаде")
    elif message.text == "1807":
        bot.send_message(message.from_user.id, "первый рейс парохода Фултона"
                                               "заключение Тильзитского мира между Францией и Россией")
    elif message.text == "1810-1826":
        bot.send_message(message.from_user.id, "войны за независимость Испанских колоний в Латинской Америке")
    elif message.text == "1812 июнь":
        bot.send_message(message.from_user.id, "вторжение армии Наполеона I в Россию")
    elif message.text == "1813 16-19 декабря":
        bot.send_message(message.from_user.id, "Битва народов (под Лейпцигом)")
    elif message.text == "1814":
        bot.send_message(message.from_user.id,
                         "Реставрация Бурбонов, отречение Наполеона I. его ссылка на остров Эльба")
    elif message.text == "1814-1815":
        bot.send_message(message.from_user.id, "Венский конгресс")
    elif message.text == "1815 март-июнь":
        bot.send_message(message.from_user.id, " (Сто дней) Наполеона Бонапарта (Полёт орла) ")
    elif message.text == "1815 18 июня":
        bot.send_message(message.from_user.id, "Битва при Ватерлоо")
    elif message.text == "1815":
        bot.send_message(message.from_user.id, "Договор о создании Священного союза"
                                               "Создание Германского союза")
    elif message.text == "1823":
        bot.send_message(message.from_user.id, "Принятие доктрины Монро в США")
    elif message.text == "1825":
        bot.send_message(message.from_user.id, "Начало функционировать первая железная дорога в Великобритании")
    elif message.text == "1830":
        bot.send_message(message.from_user.id, "Июльская револиция во Франции.")
    elif message.text == "1830-1848":
        bot.send_message(message.from_user.id, "Июльская монархия во Франции.")
    elif message.text == "1831":
        bot.send_message(message.from_user.id, "Восстания рабочих в Лионе")
    elif message.text == "1832":
        bot.send_message(message.from_user.id, "Первая избирательная реформа во Великобритании")
    elif message.text == "1834":
        bot.send_message(message.from_user.id, "Договор о Таможенном союзе в Германии")
    elif message.text == "1837-1901":
        bot.send_message(message.from_user.id, "Правление королевы Виктории во Великобритании")
    elif message.text == "1836-1848":
        bot.send_message(message.from_user.id, "Чартистское движение во Великобритании")
    elif message.text == "1840-1842":
        bot.send_message(message.from_user.id, "Первая (опиумная война)")
    elif message.text == "1844":
        bot.send_message(message.from_user.id,
                         "Впервые установлена телеграфная связь между городами с помощью аппарата Морзе.")
    elif message.text == "1846-1848":
        bot.send_message(message.from_user.id, "Американо-мексиканская война")
    elif message.text == "1848-1849":
        bot.send_message(message.from_user.id, "Революции в странах Западной Европы (весна народов)")
    elif message.text == "1848":
        bot.send_message(message.from_user.id, "Установление Второй республики во Франции")
    elif message.text == "1850":
        bot.send_message(message.from_user.id,
                         "Впервые по дну пролива Ла-Манш между Кале и Дувром проложили подводный телеграфный кабель")
    elif message.text == "1850-1864":
        bot.send_message(message.from_user.id, "Восстание тайпинов в Китае")
    elif message.text == "1851":
        bot.send_message(message.from_user.id, "Первая Всемирная промышленная выставка в Лондоне")
    elif message.text == "1852":
        bot.send_message(message.from_user.id, "на воду спущено первое паровое судно с винто вым двигателем.")
    elif message.text == "1852-1870":
        bot.send_message(message.from_user.id, "Вторая империя во Франции.")
    elif message.text == "1853-1856":
        bot.send_message(message.from_user.id, "Крымская война")
    elif message.text == "1854":
        bot.send_message(message.from_user.id, "Насильственное <открытие> Японии.")
    elif message.text == "1856-1860 ":
        bot.send_message(message.from_user.id, "Вторая опиумная война")
    elif message.text == "1857-1859 ":
        bot.send_message(message.from_user.id, "восстание сипаев в Индии.")
    elif message.text == "1859":
        bot.send_message(message.from_user.id, "Австро-итало-француская война"
                                               "Восттание аболиционистов под руководством Джона Брауна в США.")
    elif message.text == "1859-1869":
        bot.send_message(message.from_user.id, "Строительство суэцкого канала.")
    elif message.text == "1860":
        bot.send_message(message.from_user.id, "Экспедиция тысячи Дж. Гарибальди в Сицилию.")
    elif message.text == "1861 17 марта":
        bot.send_message(message.from_user.id, "Образование Итальянского королевства.")
    elif message.text == "1861-1865":
        bot.send_message(message.from_user.id, "Гражданская война в США")
    elif message.text == "1862":
        bot.send_message(message.from_user.id, "Закон о гомстедах в США")
    elif message.text == "1863":
        bot.send_message(message.from_user.id, "первая подземная железная дорога в Лондоне.")
    elif message.text == "1863 1 января":
        bot.send_message(message.from_user.id, "Отмена рабства в южных штатаз США")
    elif message.text == "1864":
        bot.send_message(message.from_user.id, "Создание Международного товарищества рабочих (I Интернационал)."
                                               "война Пруссии и Австрии против Дании.")
    elif message.text == "1866":
        bot.send_message(message.from_user.id, "Австро-прусская война."
                                               "Образование Северогерманского союза во главе с Пруссией.")
    elif message.text == "1867":
        bot.send_message(message.from_user.id, "Преобразование Австрийской империи в двуединую монархию Австро-Венгрию."
                                               "Вторая парламентская реформа в Великобритании.")
    elif message.text == "1868":
        bot.send_message(message.from_user.id, "<революция Мэйдзи> в Японии."
                                               "Создание Британского  конгресса тред-юнионов.")
    elif message.text == "1870-1871":
        bot.send_message(message.from_user.id, "Франко-прусская война.")
    elif message.text == "1870 2-4 сентября":
        bot.send_message(message.from_user.id, "падение Второй империи и создание Третьей республики во Франции.")
    elif message.text == "1871":
        bot.send_message(message.from_user.id, "Парижская коммуна."
                                               "Образование Германской империи.")
    elif message.text == "1876":
        bot.send_message(message.from_user.id, "Изобретение телефона")
    elif message.text == "1877-1878":
        bot.send_message(message.from_user.id, "Русско-турецкая война.")
    elif message.text == "1882":
        bot.send_message(message.from_user.id, "Создание Тройственного союза Германии, Австро-Венгрии и Италии.")
    elif message.text == "1884-1885":
        bot.send_message(message.from_user.id, "Третья парламетская избирательная рефома в Великобритании.")
    elif message.text == "1885":
        bot.send_message(message.from_user.id, "Основание Индийского  национального конгресса.")
    elif message.text == "1889":
        bot.send_message(message.from_user.id,
                         "проведение Международного социалистического конгресса в Париже и создание II Интернационала.")
    elif message.text == "1892":
        bot.send_message(message.from_user.id, "Подписание русско-французкой военной конвенции.")
    elif message.text == "1894-1895":
        bot.send_message(message.from_user.id, "Японо-Китайская война, захват Японией острова Тайвань")
    elif message.text == "1896":
        bot.send_message(message.from_user.id, "Впервые в мире в Петербурге проведён сеанс радиосвязи.")
    elif message.text == "1898":
        bot.send_message(message.from_user.id, "Испано-американская война."
                                               "Фашодский конфликт между Великобританией и Францией")
    elif message.text == "1899":
        bot.send_message(message.from_user.id,
                         "Гаагская конференция по вопросам ограничения вооружения и предотвращения военных конфликтов.")
    elif message.text == "1899-1902":
        bot.send_message(message.from_user.id, "Англо-бурская война")
    elif message.text == "1899-1901":
        bot.send_message(message.from_user.id, "<Боксёрской восстание> в Китае")
    elif message.text == "Создание Антанты - военного союза Великобритании, Франции и России.":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    elif message.text == "":
        bot.send_message(message.from_user.id, "")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))