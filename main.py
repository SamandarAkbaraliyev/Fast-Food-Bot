from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp
from main_button import menuStart
from inline import mainMenu, menuXiti, menuLav, menuHot, menuShaur, menuGam, menuAssorti, menuKombo, menuDesert
from inline import menuSous, menuSok, menuChoy, shaurmamenu, Lavashmenu


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


@dp.message_handler(text_contains="4a")
async def shaur(call: CallbackQuery):
    txt = f"Саб с говядиной\n" \
          f"Сочная говядина гриль, кольца свежего красного лука, соус 'барбекю' с дымком в " \
          f"удлиненной пышной булочке\n\n" \
          f"Narhi: 17000 so'm"
    await call.message.answer_photo(open("Images /sub_s_govyadinoy_evos.png", "rb"), caption=txt,
                                    reply_markup=shaurmamenu)


@dp.message_handler(text_contains="5a")
async def shaur(call: CallbackQuery):
    txt = f"Саб с курицей\n" \
          f"Куриное мясо гриль, кольца свежего красного лука, соус " \
          f"'барбекю' с дымком в удлиненной и пышной булочке\n\n" \
          f"Narhi: 15000 so'm"
    await call.message.answer_photo(open("Images /sub_s_kurochkoy_evos.png", "rb"), caption=txt,
                                    reply_markup=shaurmamenu)


@dp.message_handler(text_contains="mlavash")
async def lavash(call: CallbackQuery):
    txt = f"Лаваш с говядиной\n" \
          f"Сочные кусочки говядины гриль и спелых помидоров, золотистые картофельные чипсы, томатный восточный соус " \
          f"со" \
          f"свежим луком и зеленью в свежайшем классическом лаваше.\n\n" \
          f"Narhi: 25000 so'm"
    await call.message.answer_photo(open("Images /lavash_s_govyadinoy_evos.png", "rb"), caption=txt,
                                    reply_markup=Lavashmenu)


@dp.callback_query_handler(text_contains="ack")
async def xit(call: CallbackQuery):
    await call.message.answer_photo(open("Images /Lavash_menu.png", "rb"), "Mahsulotni Tanlang: ", reply_markup=menuLav)


if __name__ == '__main__':
    executor.start_polling(dp)
