import discord
import time
client = discord.Client()
order = ""
l_author = []
l_nick = []
l_mention = []
l_author_m = []
lst_reid = []
reid = []
last_reid = []
last_index_reid = []
wins = []
sum_reid = []
indexl = []
composit = ['','','','','','','','','','']
teen = []
sostaw = []
zapas = []
ltime = ["сегодня"]
messag = 0
zapisano = 0
dezap = 0
ykaz = 0
autir = 0
def d_raid(data, l_reid, ind):
    d = data.split(':')
    l = l_reid.split(':')
    if l[0] == 'none':
        return True
    elif d[1] == l[1] and d[2] == l[2]:
        return False
    elif (int(d[1]) - 1) == int(l[1]) and d[2] == l[2] and d[0] > l[0]:
        return False
    else:
        return True
def index_all(lst: tuple, val: str):
  return [i for i, v in enumerate(lst) if v == val]
def composition():
  global teen, zapas, composit
  composit = ['', '', '', '', '', '', '', '', '', '']
  teen.clear()
  indexl.clear()                      # |
  zapas = list(reid.copy())           # |
  if len(reid)<=10:                   # |
    teen = list(reid.copy())
    zapas.clear()                     # |
  else:                                # \
    for i in range(10):                  # > Создание списка первых 10 записавшихся и списка запасных
      teen.append(reid[i])             # /
      try:                            # |
        del zapas[0]                  # |
      except:                         # |
        pass                          # |
  for i in range(len(teen)):                      # |
    indexl.append(l_author.index(teen[i]))        # | Создание списка индексов записавшихся
#   --------------------------------------------------------------------------------------------------------------------
  for i in range(len(teen)):
      try:
        if len(index_all(indexl, indexl[i])) > 1:
          pass
        else:
          data = time.strftime("%d:%m:%Y")
          if d_raid(data, last_reid[i], i) == True:
            pass
          else:
            if composit[i] == '':
                composit[int(last_index_reid[i])-1] = i
      except:
          pass
  for i in range(10):
    if composit[i] == '':
      pass
    else:
      d = indexl.index(composit[i])
      del indexl[d]
  for i in range(4):
    if composit[i] == '':
      v_pl = -1
      in_pl = "none"
      for a in range(len(indexl)):
        if len(index_all(indexl, indexl[a])) == 1:
          if int(v_pl) < int(wins[indexl[a]]):
            v_pl = wins[indexl[a]]
            in_pl = indexl[a]
          elif int(v_pl) == int(wins[indexl[a]]):
            if int(sum_reid[int(in_pl)]) < int(sum_reid[indexl[a]]):
              v_pl = wins[indexl[a]]
              in_pl = indexl[a]
        if in_pl == 'none':
            if int(v_pl) < int(wins[indexl[a]]):
                v_pl = wins[indexl[a]]
                in_pl = indexl[a]
            elif int(v_pl) == int(wins[indexl[a]]):
                if int(sum_reid[int(in_pl)]) < int(sum_reid[indexl[a]]):
                    v_pl = wins[indexl[a]]
                    in_pl = indexl[a]
      composit[i] = in_pl
      del indexl[indexl.index(in_pl)]
  tt = 0
  i = 0
  if not len(indexl) == 0:
      while not (len(indexl) - tt) <= -1:
        i = (len(indexl) - tt-1)
        tt +=1
        if len(index_all(indexl, indexl[i])) > 1:
          if composit[4] == '' and composit[9] == '':
            f = index_all(indexl, indexl[i])
            f = f[::-1]
            composit[4] = indexl[f[0]]
            composit[9] = indexl[f[1]]
            del indexl[f[0]]
            del indexl[f[1]]
          elif composit[5] == '' and composit[8] == '':
            f = index_all(indexl, indexl[i])
            f = f[::-1]
            composit[5] = indexl[f[0]]
            composit[8] = indexl[f[1]]
            del indexl[f[0]]
            del indexl[f[1]]
          elif composit[6] == '' and composit[7] == '':
            f = index_all(indexl, indexl[i])
            f = f[::-1]
            composit[6] = indexl[f[0]]
            composit[7] = indexl[f[1]]
            del indexl[f[0]]
            del indexl[f[1]]
  for _ in range(len(indexl)):
    for i in range(10):
      if composit[i] == '':
        composit[i] = indexl[0]
        del indexl[0]
        break
def a_a():
    a = list(sostaw)
    a = ' '.join(a)
    a = a.split("(")
    a = ' '.join(a)
    a = a.split(")")
    a = ' '.join(a)
    a = a.split(" ")
    b = index_all(a, "")
    b = b[::-1]
    for i in range(len(b)):
        del a[b[0]]
        del b[0]
    b = index_all(a, "*****")
    b = b[::-1]
    for i in range(len(b)):
        del a[b[0]]
        del b[0]
    return a
@client.event
async def on_message(message):
    global order, messag, zapisano, dezap, ykaz, autir
    msg = message.content.lower()
    ctx = message
    msg_list = msg.split()

    if len(msg_list) > 1 and msg_list[0] == "орден":
      channel = client.get_channel(int(733230754817114166))
      await ctx.channel.purge(limit=1)
      del msg_list[0]
      order = " ".join(msg_list).title()
      retStr = str(f"""```css\n> Орден для рейдов был обновлён игроком {message.author} на \"{order}\" ```""")
      await ctx.channel.send(retStr)
    elif len(msg_list) >= 2 and str(msg_list[0]+" " +msg_list[1]) == "запись открыта":
        await ctx.channel.purge(limit=1)
        lst_reid.clear()
        reid.clear()
        if not zapisano == 0:
            await client.http.unpin_message(zapisano.channel.id, zapisano.id)
        if (ltime[0] in msg_list) == True:
            data = time.strftime("%d:%m:%Y")
            await message.channel.send(f"""Запись на рейд {data} ОТКРЫТА!
РЕЙД 21.30 по МСК  
Наличие дискорда обязательное, ну прям ооочень нужно, возможны исключения лишь при согласовании с Максом
Рейд на основе ордена \" {order} \"
Перекличка 21:00-21:15 по МСК
Быть в дискорде в 21:25 (в противном случае замена)
Старт рейда 21:30 (без исключений) по МСК
+ Ниже для записи""")
        else:
          d = time.strftime("%d")
          d1 = int(d)+1
          data = time.strftime(":%m:%Y")
          await message.channel.send(f"""Запись на рейд {d1}{data} ОТКРЫТА!
РЕЙД 21.30 по МСК  
Наличие дискорда обязательное, ну прям ооочень нужно, возможны исключения лишь при согласовании с Максом
Рейд на основе ордена \" {order} \"
Перекличка 21:00-21:15 по МСК
Быть в дискорде в 21:25 (в противном случае замена)
Старт рейда 21:30 (без исключений) по МСК
+ Ниже для записи""")
        await message.channel.send(f"Игроков записано {len(reid)}")
    elif len(msg_list) >= 1 and msg_list[0] == "+":
        await ctx.channel.purge(limit=1)
        if len(msg_list) == 3 and msg_list[1] == "пустышка":
            n = l_author.index(message.author.name)
            reid.append(l_author[n])
            lst_reid.append(f'{l_author[n]}({msg_list[2]})')
            retStr = str(f"""```css\n\"{l_author[n]}\" был записан на рейд!```""")
            await ctx.channel.send(retStr)
            new = f"Игроков записано {str(len(reid))}"
            try:
                await zapisano.edit(content=new)
            except:
                pass
        elif len(msg_list) == 3 and msg_list[1] == "автор":
            try:
                if (l_author[l_nick.index(msg_list[2])] in reid) == True:
                    await ctx.channel.send(f"Игрок {l_author[l_nick.index(msg_list[2])]} уже записан !")
                    time.sleep(5)
                    await client.http.delete_message(autir.channel.id, autir.id)
                elif (msg_list[2] in l_nick) == True:
                    n = l_nick.index(msg_list[2])
                    reid.append(l_author[n])
                    lst_reid.append(f'{l_author[n]}({l_nick[n]})')
                    retStr = str(f"""```css\n\"{l_author[n]}\" был записан на рейд!```""")
                    await ctx.channel.send(retStr)
                    new = f"Игроков записано {str(len(reid))}"
                    try:
                        await zapisano.edit(content=new)
                    except:
                        pass
                else:
                    await ctx.channel.send("Введите корректный ник Игрока для его записи!")
            except:
                await ctx.channel.send("Введите корректный ник Игрока для его записи!")
        else:
            if not (message.author.name in l_author) == True:
                if len(msg_list) == 2:
                    l_author.append(message.author.name)
                    l_mention.append(message.author.mention)
                    l_nick.append(msg_list[1])
                    l_author_m.append(message.author)
                    last_reid.append("none")
                    last_index_reid.append("none")
                    wins.append(0)
                    sum_reid.append(0)
                    n = l_author.index(message.author.name)
                    reid.append(l_author[n])
                    lst_reid.append(f'{l_author[n]}({l_nick[n]})')
                    retStr = str(f"""```css\n\"{l_author[n]}\" был записан на рейд!```""")
                    await ctx.channel.send(retStr)
                    new = f"Игроков записано {str(len(reid))}"
                    try:
                        await zapisano.edit(content=new)
                    except:
                        pass
                else:
                    await message.channel.send("Укажите \"+\", а после ник вашего игрового персонажа используя вместо пробела в нике нижнее подчёркивание.")
                    time.sleep(7)
                    await client.http.delete_message(ykaz.channel.id, ykaz.id)
            elif (f'{l_author[l_author.index(message.author.name)]}({l_nick[l_author.index(message.author.name)]})' in lst_reid) == True:
                await ctx.channel.send(f"Вы уже записаны {message.author.name}!")
                time.sleep(5)
                await client.http.delete_message(dezap.channel, dezap.id)
            else:
                n = l_author.index(message.author.name)
                reid.append(l_author[n])
                lst_reid.append(f'{l_author[n]}({l_nick[n]})')
                retStr = str(f"""```css\n\"{l_author[n]}\" был записан на рейд!```""")
                await ctx.channel.send(retStr)
                new = f"Игроков записано {str(len(reid))}"
                try:
                    await zapisano.edit(content=new)
                except:
                    pass
    elif msg == "состав":
        await ctx.channel.purge(limit=1)
        if len(reid) >= 5:
            sostaw.clear()
            composition()
            for i in range(10):
                try:
                    sostaw.append(lst_reid[reid.index(l_author[int(composit[i])])])
                except:
                    sostaw.append("*****")
            a = a_a()
            v = 0
            m = 0
            ln = len(a_a())
            while not ln - m == 0:
                m += 1
                v += 1
                if not v % 2 == 0:
                    del a[ln - m]
            for i in range(len(index_all(sostaw, "*****"))):
                v = index_all(sostaw, "*****")
                a.insert(v[i], "*****")
            for i in range(len(a)):
                if len(index_all(a, a[i])) > 1:
                    if a[i] == "*****":
                        pass
                    else:
                        bhh = index_all(reid, a[i])
                        nbt= index_all(a, a[i])
                        for i in range(len(nbt)):
                            sostaw[nbt[i]] = lst_reid[bhh[i]]
            zap = "Никого нет!"
            for i in range(len(zapas)):
                zap = ", ".join(zapas)
            ret = str(f"""```css\nКоманда 4 ({sostaw[6]}, {sostaw[7]})
Команда 6 ({sostaw[5]}, {sostaw[8]})
Команда 8 ({sostaw[4]}, {sostaw[9]})
Гопник 1 ({sostaw[3]})
Гопник 5 ({sostaw[2]})
Гопник 7 ({sostaw[1]})
Пахан ({sostaw[0]})
На замене: {zap}```""")
            await ctx.channel.send(ret)
        else:
            await ctx.channel.send("Недостаточно игроков для генерации состава!")
    elif msg == "команды":
         await message.channel.send("""Список команд бота:
\"Орден *Название ордена*\" - Эта команда изменяет орден в котором будут проводиться рейды(Отображается во время записи)
\"Запись открыта\" - Эта команда открывает запись на рейд(Публикация новой записи удаляет всех кто записался под старой записью). Прибавив в предложение слово "Сегодня", откроет рейд на этот же день.
\"Состав\" - Публикует состав(если записавшихся менее 5 запись не будет создана)
\"Рейд победа\" или \"Рейд поражение\" - изменяе статистику участвующих в зависимости от результата рейда
\"+\" - записывает автора сообщения на рейд
\"+ пустышка *Ник*\" - позволяет записать себя повторно на рейд под другим ником
\"+ автор *Ник*\" - позволяет записать другого участника на рейд
\"Замена *\'номер текущей роли\'* *\'Ник на кого заменяется\'* - замена игрока 
\"Очистить *\'количество сообщений которые следует удалить\'*\" - удалить n-ое количество сообщений
\"Список всех игроков\" - выводит список всех игроков и их ников
\"Статистика *Ник*\" - выводит статистику отдельного игрока
\"Вызвать всех\" - упоминает абсолютно всех участников 
\"Созвать всех на рейд\" - упоминает только тех кто не записался на рейд
\"Задолбать всех в ЛС\" - присылает личное сообщение абсолютно всем участникам
\"Подмена "*Номер игрока в составе*" "*Номер игрока в составе*"\" - меняет местами игроков в составе
\"Команды\" - выводит список всех команд бота""")
    elif len(msg_list) >= 2 and msg_list[0] == "очистить":
        await ctx.channel.purge(limit=int(msg_list[1])+1)
    elif len(msg_list) == 3 and msg_list[0] == "замена" and int(msg_list[1]) <= 10:
        if (msg_list[2] in l_nick) == True:
            sostaw.clear()
            composit[int(msg_list[1])-1] = l_nick.index(msg_list[2])
            for i in range(10):
                try:
                    sostaw.append(lst_reid[reid.index(l_author[int(composit[i])])])
                except:
                    sostaw.append("*****")
            channel = client.get_channel(int(733230754817114166))
            new_text = str(f"""```css\nКоманда 4 ({sostaw[6]}, {sostaw[7]})
Команда 6 ({sostaw[5]}, {sostaw[8]})
Команда 8 ({sostaw[4]}, {sostaw[9]})
Гопник 1 ({sostaw[3]})
Гопник 5 ({sostaw[2]})
Гопник 7 ({sostaw[1]})
Пахан ({sostaw[0]})```""")
            await messag.edit(content = new_text)
            await message.channel.send("Была произведена замена ")
        else:
            await ctx.channel.send("Введите корректный ник Игрока для замены!")
    elif len(msg_list) == 3 and msg_list[0] == "подмена":
        if int(msg_list[1]) <= 10 and int(msg_list[2]) <= 10:
            lv = int(msg_list[2]) - 1
            lw = int(msg_list[1]) - 1
            w = sostaw[lv]
            v = sostaw[lw]
            sostaw[lw] = w
            sostaw[lv] = v
            new_text = str(f"""```css\nКоманда 4 ({sostaw[6]}, {sostaw[7]})
Команда 6 ({sostaw[5]}, {sostaw[8]})
Команда 8 ({sostaw[4]}, {sostaw[9]})
Гопник 1 ({sostaw[3]})
Гопник 5 ({sostaw[2]})
Гопник 7 ({sostaw[1]})
Пахан ({sostaw[0]})```""")
            await messag.edit(content=new_text)
            await message.channel.send("Была произведена подмена")
        else:
            await ctx.channel.send("Введите корректные значения для замены!")
    elif msg == "список всех игроков":
        ls = []
        for i in range(len(l_author)):
            ls.append(" ")
            ls[i] = str(l_author[i] +" - " +l_nick[i] +",")
        a = "\n".join(ls)
        await message.channel.send(a)
    elif len(msg_list) == 2 and msg_list[0] == "статистика":
        if (msg_list[1] in l_nick) == True:
            a = l_nick.index(msg_list[1])
            b = str(f"""```css\nИгрок: {l_author[a]},
Ник: {l_nick[a]},
ID Игрока: {l_mention[a]},
Количество рейдов: {sum_reid[a]},
Количество побед: {wins[a]},
Дата последнего рейда: {last_reid[a]},
Роль на последнем рейде: {last_index_reid[a]}.```""")
            await message.channel.send(b)
        else:
            await message.channel.send("Введите корректный ник Игрока для того чтоб увидеть его статистику!")
    elif len(msg_list) == 2 and msg_list[0] == "рейд" and msg_list[1] == "победа" or len(msg_list) == 2 and msg_list[0] == "рейд" and msg_list[1] =="поражение":
        a = a_a()
        v = 0
        m = 0
        ln = len(a_a())
        while not ln-m == 0:
            m+=1
            v+=1
            if not v %2 ==0:
                del a[ln-m]
        kyl = list(a)
        a = list(set(a))
        if msg_list[1] == "победа":
            for i in range(len(a)):
                tnd = l_author.index(a[i])
                sum_reid[tnd] = int(sum_reid[tnd]+1)
                wins[tnd] = int(wins[tnd]+1)
                last_reid[tnd] = time.strftime("%d:%m:%Y")
                last_index_reid[tnd] = int(kyl.index(a[i]))+1
            await message.channel.send("Поздравляю!")
            reid.clear()
            lst_reid.clear()
            sostaw.clear()
        else:
            for i in range(len(a)):
                tnd = l_author.index(a[i])
                sum_reid[tnd] = int(sum_reid[tnd]+1)
                last_reid[tnd] = time.strftime("%d:%m:%Y")
                last_index_reid[tnd] = int(kyl.index(a[i]))+1
            reid.clear()
            lst_reid.clear()
            sostaw.clear()
            await message.channel.send("Сочувствую...")
            reid.clear()
            lst_reid.clear()
            sostaw.clear()
    elif msg == "вызвать всех":
        rt = []
        for i in range(len(l_author)):
            if l_author[i] == message.author.name:
                pass
            else:
                rt.append(l_mention[i])
                rt = ", ".join(l_mention)
        await message.channel.send(f"Вас призывает {message.author.name}! Придити же! {rt}.")
    elif msg == "созвать всех на рейд":
        rt = []
        for i in range(len(l_author)):
            if (l_author[i] in reid) == True or not l_author[i] == message.author.name:
                pass
            else:
                rt.append(l_mention[i])
                rt = ", ".join(l_mention)
        if len(rt) == 0:
            await message.channel.send(f"Все уже записаны!")
        else:
            await message.channel.send(f"Вас призывает {message.author.name} для участия в рейде! Придити же и запишитесь! {rt}.")
    elif msg == "задолбать всех в лс":
        for i in range(len(l_author)):
            if l_author[i] == message.author.name:
                pass
            else:
                member = l_author_m[i]
                await member.send(f"Срочно явиться в дискорд! Вас призывает {message.author.name}")
        await message.channel.send("Задача\"Задолбать всех в ЛС\" выполнена успешно!")
    elif len(msg_list)==5 and msg_list[0] =="удалить" and msg_list[1] == "игрока" and msg_list[3] =="из" and msg_list[4] == "состава":
        if int(msg_list[2]) <= 10 and int(msg_list[2])>0:
            sostaw[int(msg_list[2])-1] = "*****"
            new_text = str(f"""```css\nКоманда 4 ({sostaw[6]}, {sostaw[7]})
Команда 6 ({sostaw[5]}, {sostaw[8]})
Команда 8 ({sostaw[4]}, {sostaw[9]})
Гопник 1 ({sostaw[3]})
Гопник 5 ({sostaw[2]})
Гопник 7 ({sostaw[1]})
Пахан ({sostaw[0]})```""")
            await messag.edit(content=new_text)
            await message.channel.send("Игрок был удалён с состава")
        else:
            await ctx.channel.send("Введите корректные значения для удаления игрока с состава!")
    elif len(msg_list) >= 4 and msg_list[0] == "redact":
        await ctx.channel.purge(limit=1)
        try:
            if msg_list[1] == "nick":
                if (msg_list[2] in l_nick) == True:
                    l_nick[l_nick.index(msg_list[2])] = msg_list[3]
                    await message.channel.send("Pass context: l_nick changed successfully")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
                else:
                    await message.channel.send("Pass context: index not found")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
            elif msg_list[1] == "wins":
                if (msg_list[2] in l_nick) == True:
                    wins[l_nick.index(msg_list[2])] = int(msg_list[3])
                    await message.channel.send("Pass context: wins changed successfully")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
                else:
                    await message.channel.send("Pass context: index not found")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
            elif msg_list[1] == "sum_reid":
                if (msg_list[2] in l_nick) == True:
                    sum_reid[l_nick.index(msg_list[2])] = int(msg_list[3])
                    await message.channel.send("Pass context: sum_reid changed successfully")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
                else:
                    await message.channel.send("Pass context: index not found")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
            elif msg_list[1] == "last_index_reid":
                if (msg_list[2] in l_nick) == True:
                    last_index_reid[l_nick.index(msg_list[2])] = int(msg_list[3])
                    await message.channel.send("Pass context: wins changed successfully")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
                else:
                    await message.channel.send("Pass context: index not found")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
            elif msg_list[1] == "last_reid":
                if (msg_list[2] in l_nick) == True:
                    last_reid[l_nick.index(msg_list[2])] = msg_list[3]
                    await message.channel.send("Pass context: wins changed successfully")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
                else:
                    await message.channel.send("Pass context: index not found")
                    time.sleep(2)
                    await ctx.channel.purge(limit=1)
        except:
            await message.channel.send("Error index!")
            time.sleep(2)
            await ctx.channel.purge(limit=1)
    elif msg == "скрытые команды":
        await message.channel.send("~~ <1<1;<<<1;>1;>3>1;>1;>>>1;>1; >>2;<1;<3;<1<2; \">1>2;<2;<1;>1;<<2;<1<2;\" <<<1;>1; >1;<<<1;>4;>>>1;>>2;<<1;<1<1;<<2;<<<2;>>>2; >1^3;>>1;>4>1;<<2;<2;, >1>1;<<<2;<1<1;>>>1;<2; <<<1;>1;>>1;>3;>1;<<<1;>>2;<2; <1<1;>1>1;>>2;<1<1;<<2;>1; <<2;<<<2;<1<2;<<<2;>1>2;>4>1;<<1; <1<1;>>>1;<2;<1;>2>1;<2;<1<2; >>2;>>1;>>>2;<2;<<<1;>>2;<1<2;>4>2;, >1>1;<<<2;<1<1;>>>1;<2; <1<1;>1>1;>>2;<1<1;<<2;>1; >>2;<1;<3;<1<2; <<<1;>>2;<<2; >>2;>4;>1>2;<<<2;<<2;>1; >2>1; <<2;<<<2;<1<2;<<<2;>1>2;<<<2;>4;<<<2; >1>1;>1>2;<<<2;>>2;>>1;>3;<<<2;<1;>>2;<1<2;<1<1;>1^3; >1>2;<2;<1;>1;<<2;<1<2;>>2;>1>2;<<<2;>3;>1;<<<1;>>2;<2; >>2; >>>1;>>2;>3>2;>4>2; >1>1;<<<2;<1<1;>>>1;<2; >>1;<<<1;>1;>3>1;<2;<<<1;>>2;<2; <<<1;>1; <<2;<<<2;<1<2;<<<2;>1>2;<<<2;<2; >1>1;>1>2;<<<2;>>2;>>1;>3;<<<2;<1;>>2;<1<2;<1<1;>1^3; >>1;>1;>>>2;<2;<<<1;>1;")
    elif len(msg_list)==2 and msg_list[0] == "*!^7849&45128$1632/+11":
        try:
            if (msg_list[1] in l_nick) == True:
                n = l_nick.index(msg_list[1])
                if (l_author[n] in reid) == True:
                    del reid[reid.index(l_author[n])]
                del l_nick[n]
                del l_author[n]
                del l_mention[n]
                del last_reid[n]
                del last_index_reid[n]
                del l_author_m[n]
                await message.channel.send("Задача выполнена успешно!")
                time.sleep(2)
                await ctx.channel.purge(limit=2)
            else:
                await message.channel.send("Игрок не найден!")
                time.sleep(2)
                await ctx.channel.purge(limit=2)
        except:
            pass
    if len(msg_list) > 5 and msg_list[0] == "```css" and msg_list[1] =="команда" and msg_list[2] =="4":
        messag = message
    if len(msg_list) > 2 and msg_list[0] == 'игроков' and msg_list[1] =="записано":
        time.sleep(5)
        zapisano = message
        await message.pin()
    if len(msg_list) > 4 and msg_list[0] == "укажите" and msg_list[1] == "\"+\"," and msg_list[2] == "а" and msg_list[3] == "после":
        ykaz = message
    if len(msg_list) == 2  and msg_list[0] == "вы" and msg_list[1] == " уже" and msg_list[2] =="записаны!":
        dezap = message
    if len(msg_list) > 4 and msg_list[0] == "игрок" and msg_list[2] == "уже" and msg_list[3] == "записан":
        autir = messag

@client.event
async def on_ready():
    channel = client.get_channel(int(733230754817114166))
    await channel.send('К серверу присоеденился {0}!'.format(client.user.name))
tokin = os.environ.get('bot_token')
client.run(str(tokin))
