from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp
from main_button import menuStart
from inline import mainMenu, menuXiti, menuLav, menuHot, menuShaur, menuGam, menuAssorti, menuKombo, menuDesert
from inline import menuSous, menuSok, menuChoy, shaurmamenu, Lavashmenu, Hotdogmenu, Shaurmenu, Hamburgermenu
from inline import Blyudamenu, Combomenu, Desertmenu, Sousmenu, Sokmenu, Choymenu


@dp.message_handler(commands="start")
async def start(msg: Message):
    await msg.answer_photo(open("Images /evos-01.png", "rb"), f"Assalomu alaykum {msg.from_user.full_name}."
                                                              f"\nEVOS Dostavka botiga xush kelibsiz!"
                                                              f"", reply_markup=menuStart)


@dp.message_handler(commands="help")
async def help1(msg: Message):
    await msg.answer_photo(open("Images /help.jpg", "rb"), f"Yordam uchun https://t.me/Hello_this_isAbdurrohman "
                                                           f"profiliga murojaat qiling!")


@dp.message_handler(text="🍽 MENU 🍽")
async def menu(msg: Message):
    await msg.answer_photo(open("Images /menu.png", "rb"), "Mahsulot turini tanlang: ", reply_markup=mainMenu)


@dp.callback_query_handler(text_contains="menu")
async def menu(call: CallbackQuery):
    await call.message.answer_photo(open("Images /menu.png", "rb"), "Mahsulot turini tanlang: ", reply_markup=mainMenu)


@dp.callback_query_handler(text_contains="back")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Star.jpg", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuXiti)


@dp.callback_query_handler(text_contains="🌟")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Star.jpg", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuXiti)


@dp.callback_query_handler(text_contains="🌯")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Lavash_menu.png", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuLav)


@dp.callback_query_handler(text_contains="🌭")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Xot_dog_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuHot)


@dp.callback_query_handler(text_contains="🌮")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Shaurma_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuShaur)


@dp.callback_query_handler(text_contains="🍔")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /gamburger_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuGam)


@dp.callback_query_handler(text_contains="🥙")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /asss_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuAssorti)


@dp.callback_query_handler(text_contains="🍟")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /kombo.png", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuKombo)


@dp.callback_query_handler(text_contains="🍰")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Desert_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuDesert)


@dp.callback_query_handler(text_contains="🥗")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /sous.png", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuSous)


@dp.callback_query_handler(text_contains="🍹")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Sok_menu.png", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuSok)


@dp.callback_query_handler(text_contains="☕")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Coffee.jpg", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuChoy)


@dp.callback_query_handler(text_contains="1a")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма с курицей\n" \
          f"Румяное куриное мясо гриль, кусочки свежего огрурца и сочного помидора, хрустящие чипсы, " \
          f"томатный восточный соус со свежим луком и зеленью в ароматной полукруглой булочке с кунжутными " \
          f"семечками.\n\n" \
          f"Narhi: 22000 so'm"
    await call.message.answer_photo(open("Images /shaurma_s_kurochkoy_biq_evos.png", "rb"), caption=txt,
                                    reply_markup=shaurmamenu)


@dp.callback_query_handler(text_contains="2a")
async def danar(call: CallbackQuery):
    txt = f"Донар с говядиной\n"\
          f"Кусочки сочной говядины гриль, золотистая картошка 'фри', рис, натуральный фирменный " \
          f"салат, специальный соус и ароматная лепешка на комбинированном блюде\n\n" \
          f"Narhi: 40000 so'm."
    await call.message.answer_photo(open("Images /donar_s_govyadinoy_evos.png", "rb"), caption=txt,
                                    reply_markup=shaurmamenu)


@dp.callback_query_handler(text_contains="3a")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма острая с курицей\n" \
          f"Румяное куриное мясо гриль, ломтики свежего огрурца и сочного помидора, хрустящие чипсы, томатный острый " \
          f"соус Калампир с кусочками лука в ароматной булочке с кунжутными семечками.\n\n" \
          f"Narhi: 22000 so'm"
    await call.message.answer_photo(open("Images /shaurma_ostraya_s_kurochkoy_big_evos.png", "rb"), caption=txt,
                                    reply_markup=shaurmamenu)


@dp.callback_query_handler(text_contains="4a")
async def shaur(call: CallbackQuery):
    txt = f"Саб с говядиной\n" \
          f"Сочная говядина гриль, кольца свежего красного лука, соус 'барбекю' с дымком в " \
          f"удлиненной пышной булочке\n\n" \
          f"Narhi: 17000 so'm"
    await call.message.answer_photo(open("Images /sub_s_govyadinoy_evos.png", "rb"), caption=txt,
                                    reply_markup=shaurmamenu)


@dp.callback_query_handler(text_contains="5a")
async def shaur(call: CallbackQuery):
    txt = f"Саб с курицей\n" \
          f"Куриное мясо гриль, кольца свежего красного лука, соус " \
          f"'барбекю' с дымком в удлиненной и пышной булочке\n\n" \
          f"Narhi: 15000 so'm"
    await call.message.answer_photo(open("Images /sub_s_kurochkoy_evos.png", "rb"), caption=txt,
                                    reply_markup=shaurmamenu)


@dp.callback_query_handler(text_contains="b1")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с говядиной\n" \
          f"Сочные кусочки говядины гриль и спелых помидоров, золотистые картофельные чипсы, томатный восточный соус " \
          f"со" \
          f"свежим луком и зеленью в свежайшем классическом лаваше.\n\n" \
          f"Narhi: 25000 so'm"
    await call.message.answer_photo(open("Images /lavash_s_govyadinoy_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b2")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с курицей\n" \
          f"куриное мясо гриль, маринованное по фирменному рецепту с восточными специями, кусочки свежего спелого" \
          f" помидора, натуральные картофельные чипсы, томатный восточный соус со свежим луком и зеленью в" \
          f" свежайшем классическом лаваше.\n\nNarhi: 23000 so'm"
    await call.message.answer_photo(open("Images /lavash_kur.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b3")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с говядиной Мини\n" \
          f"Сочные кусочки говядины гриль и спелых помидоров, золотистые картофельные чипсы, " \
          f"томатный восточный соус со" \
          f" свежим луком и зеленью в свежайшем классическом лаваше. Мини-версия - идеально в качестве" \
          f" легкого перекуса!\n\nNarhi: 21000 so'm"
    await call.message.answer_photo(open("Images /lavash_s_govyadinoy_mini_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b4")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с курицей Мини\n" \
          f"куриное мясо гриль, маринованное по фирменному рецепту с восточными специями" \
          f", кусочки свежего спелого помидора, натуральные картофельные чипсы, томатный восточный" \
          f" соус с кусочками лука и пряными травами в свежайшем классическом лаваше. Мини-версия - идеально" \
          f" в качестве легкого перекуса!\n\nNarhi: 19000 so'm"
    await call.message.answer_photo(open("Images /lavash_kur_mini_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b5")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с говядиной и сыром\n" \
          f"Сочные кусочки говядины гриль и спелых помидоров, золотистые картофельные чипсы" \
          f", сыр 'Чеддер' и томатный восточный соус со свежим луком и зеленью в свежайшем классическом лаваше\n\n" \
          f"Narhi: 28000 so'm"
    await call.message.answer_photo(open("Images /lavash_s_govyadinoy_s_sirom_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b6")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с курицей и сыром\n" \
          f"куриное мясо гриль, маринованное по фирменному рецепту с восточными специями," \
          f" кусочки свежего спелого помидора, натуральные картофельные чипсы, ломтик сыра 'Чеддер'," \
          f" томатный восточный соус со свежим луком и зеленью в свежайшем сырном лаваше.\n\n" \
          f"Narhi: 26000 so'm"
    await call.message.answer_photo(open("Images /lavash_s_kurochkoy_s_sirom_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b7")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с говядиной и сыром Мини\n" \
          f"Сочные кусочки говядины гриль и спелых помидоров, золотистые картофельные чипсы, сыр 'Чеддер' " \
          f"и томатный восточный соус со свежим луком и зеленью в свежайшем сырном лаваше. Мини-версия -" \
          f" идеально в качестве легкого перекуса!\n\nNarhi: 24000 so'm"
    await call.message.answer_photo(open("Images /lavash_s_govyadinoy_s_sirom_mini_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b8")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с курицей и сыром Мини\n" \
          f"куриное мясо гриль, маринованное по фирменному рецепту с восточными специями, кусочки свежего " \
          f"спелого помидора, натуральные картофельные чипсы, ломтик сыра 'Чеддер', томатный восточный соус" \
          f" со свежим луком и зеленью в свежайшем сырном лаваше. Мини-версия - идеально в качестве легкого" \
          f" перекуса!\n\nNarhi: 22000 so'm"
    await call.message.answer_photo(open("Images /lavash_s_kurochkoy_s_sirom_mini_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="b9")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш острый с говядиной\n" \
          f"Сочные кусочки говядины гриль и спелых помидоров, золотистые чипсы, томатный острый " \
          f"соус Калампир со свежим луком в румяном ред-лаваше.\n\nNarhi: 25000 so'm"
    await call.message.answer_photo(open("Images /lavash_ostriy_s_govyadinoy_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="ba")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш острый с курицей\n" \
          f"Пикантное куриное мясо гриль, кусочки спелых помидоров, золотистые чипсы, ломтик сыра 'Чеддер'" \
          f", томатный острый соус Калампир со свежим луком в румяном ред-лаваше.\n\nNarhi: 23000 so'm"
    await call.message.answer_photo(open("Images /lavash_ostriy_s_kurochkoy_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="bb")
async def lavash(call: CallbackQuery):
    txt = f"Фиттер\n" \
          f'Нежное куриное мясо гриль, салат "Айсберг", кусочки спелого помидора и свежего огурца, мягкий сыр ' \
          f'"Фетакса" легкий сливочный соус Эко в нежно-салатовом лаваше Фиттер\n\nNarhi: 21000 so"m'
    await call.message.answer_photo(open("Images /fitter_lavash_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="c1")
async def hot(call: CallbackQuery):
    txt = f"Хот-дог\n" \
          f"Аппетитная сосиска, кусочки свежего помидора и хрустящего маринованного огурца, листья " \
          f"салата Айсберг под специальным сливочным соусом в нежном кунжутном багете\n\nNarhi: 12000 so'm"
    await call.message.answer_photo(open("Images /hot_dog_Baguette_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c2")
async def hot(call: CallbackQuery):
    txt = f"Даблхот-дог\n" \
          f"Две аппетитных сосиски, кусочки свежего помидора и хрустящего маринованного огурца, листья салата " \
          f"Айсберг, кусочки свежего помидора и ломтик сыра 'Чеддер' под специальным сливочным соусом в н" \
          f"ежном кунжутном багете\n\nNarhi: 18000 so'm"
    await call.message.answer_photo(open("Images /dabl_hot_dog_Baguette_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c3")
async def hot(call: CallbackQuery):
    txt = f"Хот-дог Мини\n" \
          f"Кандские сосиски из индейки, хрустящая луковая стружка-фри и томатно-горчичный " \
          f"соус в классической длинной булочке\n\nNarhi: 8000 so'm"
    await call.message.answer_photo(open("Images /classic_hot_dog_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c4")
async def hot(call: CallbackQuery):
    txt = f"Картофель Фри\n" \
          f"Вкусные, обжаренные в растительном фритюре и слегка посоленные палочки картофеля. Идеально - " \
          f"в паре с любимым вкусом соуса.\n\nNarhi: 13000 so'm"
    await call.message.answer_photo(open("Images /kartofel_fri_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c5")
async def hot(call: CallbackQuery):
    txt = f"Картофель по-деревенски\n" \
          f"Аппетитные и вкусные крупные ломтики картошки, обжаренные в растительном фритюре с" \
          f" ароматными специями. Попробуйте с любимым соусом!\n\nNarhi: 14000 so'm"
    await call.message.answer_photo(open("Images /kartofel_po_derevenski_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c6")
async def hot(call: CallbackQuery):
    txt = f"Хот-дог детский\n" \
          f"Кандские сосиски из индейки, хрустящая луковая стружка-фри, сырный соус в мягкой булочке\n\n" \
          f"Narhi: 8000 so'm"
    await call.message.answer_photo(open("Images /hot_dog_kids.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c7")
async def hot(call: CallbackQuery):
    txt = f"Саб с курицей\n" \
          f"Куриное мясо гриль, кольца свежего красного лука, соус " \
          f"'барбекю' с дымком в удлиненной и пышной булочке\n\nNarhi: 15000 so'm"
    await call.message.answer_photo(open("Images /sub_s_kurochkoy_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c8")
async def hot(call: CallbackQuery):
    txt = f"Саб с говядиной" \
          f"Сочная говядина гриль, кольца свежего красного лука, соус 'барбекю' " \
          f"с дымком в удлиненной пышной булочке\n\nNarhi: 17000 so'm"
    await call.message.answer_photo(open("Images /sub_s_govyadinoy_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="c9")
async def hot(call: CallbackQuery):
    txt = f"Саб с курицей и сыром\n" \
          f"куриное мясо гриль, кольца свежего красного лука, соус 'барбекю' с дымком, ломтик ароматного сыра " \
          f"'Чеддер' в удлиненной и пышной булочке\n\nNarhi: 17000 so'm"
    await call.message.answer_photo(open("Images /sub_s_kurochkoy_s_sirom_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="l2")
async def hot(call: CallbackQuery):
    txt = f"Саб с говядиной и сыром\n" \
          f"Сочная говядина гриль, кольца свежего красного лука, ломтик ароматного сыра 'Чеддер' и соус 'барбекю' " \
          f"с дымком в удлиненной пышной булочке\n\nNarhi: 19000 so'm"
    await call.message.answer_photo(open("Images /sub_s_govyadinoy_s_sirom_evos.png", "rb"), caption=txt,
                                    reply_markup=Hotdogmenu)


@dp.callback_query_handler(text_contains="d2")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма с говядиной\n" \
          f"Сочные кусочки говядины гриль, свежего огрурца и сочного помидора, хрустящие картофельные чипсы, " \
          f"томатный восточный соус со свежим луком и зеленью в ароматной полукруглой булочке с кунжутными " \
          f"семечками.\n\nNarhi: 24000 so'm"
    await call.message.answer_photo(open("Images /shaurma_s_govyadinoy_big_evos.png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="d4")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма с курицей\n" \
          f"Румяное куриное мясо гриль, кусочки свежего огрурца и сочного помидора, хрустящие чипсы, томатный" \
          f" восточный соус со свежим луком и зеленью в ароматной полукруглой булочке с кунжутными семечками.\n\n" \
          f"Narhi: 22000 so'm"
    await call.message.answer_photo(open("Images /shaurma_s_kurochkoy_biq_evos (1).png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="d1")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма с говядиной Мини\n" \
          f"Сочные кусочки говядины гриль, свежего огрурца и сочного помидора, хрустящие картофельные" \
          f" чипсы, томатный восточный соус со свежим луком и зеленью в ароматной полукруглой булочке " \
          f"с кунжутными семечками. Мини-версия - идеально для легкого перекуса!\n\nNarhi: 20000 so'm"
    await call.message.answer_photo(open("Images /shaurma_s_govyadinoy_sredniy_evos.png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="d3")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма с курицей Мини\n" \
          f"Румяное куриное мясо гриль, ломтики свежего огрурца и сочного помидора, хрустящие чипсы, " \
          f"томатный восточный соус со свежим луком и зеленью в ароматной полукруглой булочке с кунжутными" \
          f" семечками. Мини-версия - идеально в качестве легкого перекуса!\n\nNarhi: 19000 so'm"
    await call.message.answer_photo(open("Images /shaurma_s_kurochkoy_sredniyi_evos.png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="d5")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма острая с говядиной\n" \
          f"Нежнейшая пикантная говядина гриль, кусочки свежего огрурца и сочного помидора, хрустящие " \
          f"картофельные чипсы, острый томатный соус со свежим луком и зеленью в ароматной полукруглой " \
          f"булочке с кунжутными семечками.\n\nNarhi: 24000 so'm"
    await call.message.answer_photo(open("Images /shaurma_ostraya_s_govyadinoy_big_evos.png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="d7")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма острая с курицей\n" \
          f"Румяное куриное мясо гриль, ломтики свежего огрурца и сочного помидора, хрустящие чипсы" \
          f", томатный острый соус Калампир с кусочками лука в ароматной булочке с кунжутными семечками.\n\n" \
          f"Narhi: 22000 so'm"
    await call.message.answer_photo(open("Images /shaurma_ostraya_s_kurochkoy_big_evos.png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="d8")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма острая с курицей Мини\n" \
          f"Румяное куриное мясо гриль, ломтики свежего огрурца и сочного помидора, хрустящие чипсы," \
          f" томатный острый соус Калампир с кусочками лука в ароматной булочке с кунжутными семечками. Мини" \
          f"-версия - идеально в качестве легкого перекуса!\n\nNarhi: 19000 so'm"
    await call.message.answer_photo(open("Images /shaurma_ostraya_s_kurochkoy_mini_evos.png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="d6")
async def shaur(call: CallbackQuery):
    txt = f"Шаурма острая с говядиной Мини\n" \
          f"Нежнейшая пикантная говядина гриль, кусочки свежего огрурца и сочного помидора, хрустящие" \
          f" картофельные чипсы, острый томатный соус со свежим луком и зеленью в ароматной полукруглой булочке" \
          f" с кунжутными семечками. Мини-версия - идеально для легкого перекуса!\n\nNarhi: 20000 so'm"
    await call.message.answer_photo(open("Images /shaurma_ostraya_s_govyadinoy_mini_evos.png", "rb"), caption=txt,
                                    reply_markup=Shaurmenu)


@dp.callback_query_handler(text_contains="l1")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Xot_dog_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuHot)


@dp.callback_query_handler(text_contains="l3")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Shaurma_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuShaur)


@dp.callback_query_handler(text_contains="l4")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /gamburger_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuGam)


@dp.callback_query_handler(text_contains="l5")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /asss_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuAssorti)


@dp.callback_query_handler(text_contains="l6")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /kombo.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuKombo)


@dp.callback_query_handler(text_contains="l7")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Desert_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuDesert)


@dp.callback_query_handler(text_contains="l8")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /sous.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuSous)


@dp.callback_query_handler(text_contains="l9")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Sok_menu.png", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuSok)


@dp.callback_query_handler(text_contains="m1")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Coffee.jpg", "rb"), "Mahsulotni Tanlang: ",
                                    reply_markup=menuChoy)


@dp.callback_query_handler(text_contains="ack")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Lavash_menu.png", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuLav)


@dp.callback_query_handler(text_contains="e1")
async def gam(call: CallbackQuery):
    txt = f"Гамбургер\n" \
          f"Сочная котлета из натуральной говядины, круглые кусочки спелого свежего помидора " \
          f"и маринованного огурца, салат 'Айсберг', кольца красного сладкого лука под сливочно" \
          f"-томатным соусом в мягкой круглой булочке\n\nNarhi: 20000 so'm"
    await call.message.answer_photo(open("Images /gamburger_evos.png", "rb"), caption=txt,
                                    reply_markup=Hamburgermenu)


@dp.callback_query_handler(text_contains="e4")
async def gam(call: CallbackQuery):
    txt = f"Чизбургер\n" \
          f"Сочная котлета из натуральной говядины, круглые кусочки спелого свежего помидора и маринованного " \
          f"огурца, салат Айсберг, ломтик сыра 'Чеддер' под сливочно-томатным соусом в мягкой круглой " \
          f"булочке\n\nNarhi: 22000 so'm"
    await call.message.answer_photo(open("Images /chizburger_evos.png", "rb"), caption=txt,
                                    reply_markup=Hamburgermenu)


@dp.callback_query_handler(text_contains="e2")
async def gam(call: CallbackQuery):
    txt = f"Даблбургер\n" \
          f"Две сочные котлеты из натуральной говядины, круглые кусочки спелого свежего помидора и " \
          f"маринованного огурца, салат 'Айсберг', кольца красного сладкого лука под" \
          f" сливочно-томатным соусом в мягкой булочке\n\nNarhi: 29000 so'm"
    await call.message.answer_photo(open("Images /15.jpg", "rb"), caption=txt,
                                    reply_markup=Hamburgermenu)


@dp.callback_query_handler(text_contains="e3")
async def gam(call: CallbackQuery):
    txt = f"Даблчизбургер\n" \
          f"Две сочных котлеты из натуральной говядины, круглые кусочки спелого свежего помидора и маринованного " \
          f"огурца, салат Айсберг, два ломтика сыра 'Чеддер' под сливочно-томатным соусом в мягкой круглой " \
          f"булочке\n\nNarhi: 33000 so'm"
    await call.message.answer_photo(open("Images /Double_Cheeseburger_evos.png", "rb"), caption=txt,
                                    reply_markup=Hamburgermenu)


@dp.callback_query_handler(text_contains="f1")
async def asp(call: CallbackQuery):
    txt = f"Донар с говядиной\n" \
          f"Кусочки сочной говядины гриль, золотистая картошка 'фри', рис, натуральный фирменный салат, специальный " \
          f"соус и ароматная лепешка на комбинированном блюде\n\nNarhi: 40000 so'm"
    await call.message.answer_photo(open("Images /asss_menu.png", "rb"), caption=txt,
                                    reply_markup=Blyudamenu)


@dp.callback_query_handler(text_contains="f2")
async def asp(call: CallbackQuery):
    txt = f"Донар с курицей\n" \
          f"Кусочки куриного мяса гриль, золотистая картошка 'фри', рис, натуральный фирменный" \
          f" салат, специальный соус и ароматной лепешкой на комбинированном блюде\n\nNarhi: 38000 so'm"
    await call.message.answer_photo(open("Images /donar_s_kurochkoy_evos.png", "rb"), caption=txt,
                                    reply_markup=Blyudamenu)


@dp.callback_query_handler(text_contains="f3")
async def asp(call: CallbackQuery):
    txt = f"Стрипсы\n" \
          f"Сочная, нежная курица в хрустящей панировке\n\nNarhi: 17000 so'm"
    await call.message.answer_photo(open("Images /strips_iz_kurochki_evos.png", "rb"), caption=txt,
                                    reply_markup=Blyudamenu)


@dp.callback_query_handler(text_contains="g1")
async def kom(call: CallbackQuery):
    txt = f"Комбо плюс\n" \
          f"Порция золотистой картошки фри и стакан 'Pepsi'\n\nNarhi: 16000 so'm"
    await call.message.answer_photo(open("Images /kombo_plus_evos.png", "rb"), caption=txt,
                                    reply_markup=Combomenu)


@dp.callback_query_handler(text_contains="g2")
async def kom(call: CallbackQuery):
    txt = f"Детское комбо\n" \
          f"Вкуснейший Хот Дог 'Детский', натуральный детский сок 'Bliss Smile' (200мл) и порция" \
          f" золотистой картошки фри\n\nNarhi: 16000 so'm"
    await call.message.answer_photo(open("Images /kids_detskoe_kombo_evos.png", "rb"), caption=txt,
                                    reply_markup=Combomenu)


@dp.callback_query_handler(text_contains="h1")
async def des(call: CallbackQuery):
    txt = f"Медовик\n" \
          f"Медовый мягкий бисквит со сметанным кремом\n\nNarhi: 14000 so'm"
    await call.message.answer_photo(open("Images /asalim_medovik_evos.png", "rb"), caption=txt,
                                    reply_markup=Desertmenu)


@dp.callback_query_handler(text_contains="h2")
async def des(call: CallbackQuery):
    txt = f"Чизкейк\n" \
          f"Ванильный бисквит с сырно-сливочным кремом\n\nNarhi: 14000 so'm"
    await call.message.answer_photo(open("Images /Cheesecake_evos.png", "rb"), caption=txt,
                                    reply_markup=Desertmenu)


@dp.callback_query_handler(text_contains="h3")
async def des(call: CallbackQuery):
    txt = f"Донат Ягодный микс\n" \
          f"Мягкий нежный донат в клубнично-йогуртовой глазури\n\nNarhi: 14000 so'm"
    await call.message.answer_photo(open("Images /donat_klubnichniy_evos.png", "rb"), caption=txt,
                                    reply_markup=Desertmenu)


@dp.callback_query_handler(text_contains="h4")
async def des(call: CallbackQuery):
    txt = f"Донат Карамельный\n" \
          f"Мягкий нежный донат в карамельной глазури\n\nNarhi: 14000 so'm"
    await call.message.answer_photo(open("Images /donat_shokoladniy_evos.png", "rb"), caption=txt,
                                    reply_markup=Desertmenu)


@dp.callback_query_handler(text_contains="i1")
async def may(call: CallbackQuery):
    txt = f"Кетчуп\n" \
          f"Порция кетчупа из натуральных свежих томатов со специями\n\nNarhi: 1000 so'm"
    await call.message.answer_photo(open("Images /25.png", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="i2")
async def may(call: CallbackQuery):
    txt = f"Майонез\n" \
          f"Порция классического майонеза\n\nNarhi: 1000 so'm"
    await call.message.answer_photo(open("Images /33.png", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="i3")
async def may(call: CallbackQuery):
    txt = f"Сырный соус\n" \
          f"Порция густого и аппетитного сырного соуса\n\nNarhi: 1000 so'm"
    await call.message.answer_photo(open("Images /44.webp", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="i4")
async def may(call: CallbackQuery):
    txt = f"Чесночный соус\n" \
          f"Порция ароматного чесночного соуса\n\nNarhi: 1000 so'm"
    await call.message.answer_photo(open("Images /49.png", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="i5")
async def may(call: CallbackQuery):
    txt = f"Чили соус\n" \
          f"Порция пикантно-острого соуса 'чили'\n\nNarhi: 1000 so'm"
    await call.message.answer_photo(open("Images /52.png", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="i6")
async def may(call: CallbackQuery):
    txt = f"Рис\n" \
          f"Вкусный и полезный гарнир из белого риса и арпы\n\nNarhi: 6000 so'm"
    await call.message.answer_photo(open("Images /ris_evos.png", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="i7")
async def may(call: CallbackQuery):
    txt = f"Салат\n" \
          f"Свежие огурцы и красная капуста с добавлением зелени 'кашнич''," \
          f" приправленные лимонным соком и восточными специям\n\nNarhi: 6000 so'mи"
    await call.message.answer_photo(open("Images /salat_evos.png", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="i8")
async def may(call: CallbackQuery):
    txt = f"Лепешка\n" \
          f"Ароматный свежий хлеб\n\nNarhi: 3000 so'm"
    await call.message.answer_photo(open("Images /non_evos.png", "rb"), caption=txt,
                                    reply_markup=Sousmenu)


@dp.callback_query_handler(text_contains="j1")
async def may(call: CallbackQuery):
    txt = f"Сок Блисс, 1 литр\n\n" \
          f"Narhi: 15000 so'm"
    await call.message.answer_photo(open("Images /Sok_menu.png", "rb"), caption=txt,
                                    reply_markup=Sokmenu)


@dp.callback_query_handler(text_contains="j4")
async def may(call: CallbackQuery):
    txt = f"Вода без газа 0,5л\n" \
          f"Очищенная питьевая вода «Montella Daily»\n\n" \
          f"Narhi: 2000 so'm"
    await call.message.answer_photo(open("Images /voda_05l_evos.png", "rb"), caption=txt,
                                    reply_markup=Sokmenu)


@dp.callback_query_handler(text_contains="j2")
async def may(call: CallbackQuery):
    txt = f"Пепси, 1,5л\n" \
          f"Pepsi в ПЭТ-бутылке 1,5 литра\n\nNarhi: 15000 so'm"
    await call.message.answer_photo(open("Images /Pepsi_1.5l_evos.png", "rb"), caption=txt,
                                    reply_markup=Sokmenu)


@dp.callback_query_handler(text_contains="j5")
async def may(call: CallbackQuery):
    txt = f"Пепси, разлив 0,4л\n" \
          f"Разливной Pepsi в фирменном бумажном стакане\n\nNarhi: 7000 so'm"
    await call.message.answer_photo(open("Images /pepsi_v_stakane_evos.png", "rb"), caption=txt,
                                    reply_markup=Sokmenu)


@dp.callback_query_handler(text_contains="j3")
async def may(call: CallbackQuery):
    txt = f"Пепси, 0,5л\n" \
          f"Pepsi в ПЭТ-бутылке 0,5 литра\n\nNarhi: 9000 so'm"
    await call.message.answer_photo(open("Images /Pepsi_0.5l_evos.png", "rb"), caption=txt,
                                    reply_markup=Sokmenu)


@dp.callback_query_handler(text_contains="k1")
async def chpy(call: CallbackQuery):
    txt = f"Чай зеленый\n" \
          f"Зеленый цейлонский крупнолистовой чай\n\n" \
          f"Narhi: 3000 so'm"
    await call.message.answer_photo(open("Images /26.png", "rb"), caption=txt,
                                    reply_markup=Choymenu)


@dp.callback_query_handler(text_contains="k2")
async def chpy(call: CallbackQuery):
    txt = f"Чай черный\n" \
          f"Черный цейлонский крупнолистовой чай\n\nNarhi: 3000 so'm"
    await call.message.answer_photo(open("Images /26.png", "rb"), caption=txt,
                                    reply_markup=Choymenu)


@dp.callback_query_handler(text_contains="k3")
async def chpy(call: CallbackQuery):
    txt = f"Чай зелёный с лимоном\n" \
          f"Зеленый цейлонский крупнолистовой чай со свежим лимоном\n\nNarhi:5000 so'm"
    await call.message.answer_photo(open("Images /26.png", "rb"), caption=txt,
                                    reply_markup=Choymenu)


@dp.callback_query_handler(text_contains="k4")
async def chpy(call: CallbackQuery):
    txt = f"Чай чёрный с лимоном\n" \
          f"Черный цейлонский крупнолистовой чай со свежим лимоном\n\nNarhi: 5000 so'm"
    await call.message.answer_photo(open("Images /26.png", "rb"), caption=txt,
                                    reply_markup=Choymenu)


@dp.callback_query_handler(text_contains="k5")
async def chpy(call: CallbackQuery):
    txt = f"Капучино\n" \
          f"Натуральный зерновой кофе со взбитым молоком на основе эспрессо. В нём сохраняется баланс" \
          f": чувствуется вкус эспрессо, но он не преобладает над вкусом молока\n\nNarhi: 11000 so'm"
    await call.message.answer_photo(open("Images /Caffe_Latte.jpg", "rb"), caption=txt,
                                    reply_markup=Choymenu)


@dp.callback_query_handler(text_contains="k6")
async def chpy(call: CallbackQuery):
    txt = f"Американо\n" \
          f"Классический зерновой кофе на основе Эспрессо с добавлением воды\n\nNarhi: 10000 so'm"
    await call.message.answer_photo(open("Images /Caffe_Latte.jpg", "rb"), caption=txt,
                                    reply_markup=Choymenu)


@dp.callback_query_handler(text_contains="k7")
async def chpy(call: CallbackQuery):
    txt = f"Латте\n" \
          f"Натуральный зерновой кофе на основе кофе эспрессо." \
          f" Готовится при помощи вспененного молока и состоит из трех слоев: молока, кофе и молочной пенки" \
          f"\n\nNarhi: 12000 so'm"
    await call.message.answer_photo(open("Images /Caffe_Latte.jpg", "rb"), caption=txt,
                                    reply_markup=Choymenu)


if __name__ == '__main__':
    executor.start_polling(dp)
