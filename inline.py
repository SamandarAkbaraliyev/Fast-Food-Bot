from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQuery

mainMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌟 Хиты продаж 🌟", callback_data="🌟")
        ],
        [
            InlineKeyboardButton(text="🌯 Lavash 🌯", callback_data="🌯"),
            InlineKeyboardButton(text="🌭 Hot-dog 🌭", callback_data="🌭")
        ],
        [
            InlineKeyboardButton(text="🌮 Shaurma 🌮", callback_data="🌮"),
            InlineKeyboardButton(text="🍔 Gamburger 🍔", callback_data="🍔")
        ],
        [
            InlineKeyboardButton(text="🥙 Assorti 🥙", callback_data="🥙"),
            InlineKeyboardButton(text="🍟 Combo 🍟", callback_data="🍟")
        ],
        [
            InlineKeyboardButton(text="🍰 Desert 🍰", callback_data="🍰"),
            InlineKeyboardButton(text="🥗 Sous va salatlar 🥗", callback_data="🥗")
        ],
        [
            InlineKeyboardButton(text="🍹 Sok va ichimliklar 🍹", callback_data="🍹"),
            InlineKeyboardButton(text="☕ Choy va Kofelar ☕", callback_data="☕")
        ]
    ]
)
menuXiti = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍗🍔 Tovuqli shaurma 🍗🍔", callback_data="1a"),
        ],
        [
            InlineKeyboardButton(text="🥩 Mol go'shtli danar 🥩", callback_data="2a")
        ],
        [
            InlineKeyboardButton(text="🍗🍔🌶 Achchiq tovuqli shaurma 🍗🍔🌶", callback_data="3a"),
        ],
        [
            InlineKeyboardButton(text="🥩🥟 Mol go'shtli sab 🥩🥟", callback_data="4a")
        ],
        [
            InlineKeyboardButton(text="🍗🥟 Tovuqli sab 🍗🥟", callback_data="5a"),
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuLav = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥩🌯 Mol go'shtli lavash 🥩🌯", callback_data="mlavash")
        ],
        [
            InlineKeyboardButton(text="🍗🌯 Tovuqli lavash 🍗🌯", callback_data="tovuq lavash")
        ],
        [
            InlineKeyboardButton(text="🔽🥩🌯 Mini mol go'shtli lavash 🔽🥩🌯", callback_data="mini mol lavash")
        ],
        [
            InlineKeyboardButton(text="🔽🍗🌯 Mini tovuqli lavash 🔽🍗🌯", callback_data="mini tovuq lavash")
        ],
        [
            InlineKeyboardButton(text="🧀🥩🌯 Sirli mol go'shtli lavash 🧀🥩🌯", callback_data="cheese mol lavash")
        ],
        [
            InlineKeyboardButton(text="🧀🍗🌯 Sir qo'shilgan tovuqli lavash 🧀🍗🌯", callback_data="cheese tovuq lavash")
        ],
        [
            InlineKeyboardButton(text="🔽🧀🌯🥩 Mini sir qo'shilgan lavash 🔽🧀🌯🥩", callback_data="mini cheese mol lavash")
        ],
        [
            InlineKeyboardButton(text="🔽🧀🌯🍗 Mini sir qo'shilgan lavash 🔽🧀🌯🍗", callback_data="mini tovuq lavash")
        ],
        [
            InlineKeyboardButton(text="🥩🌶🌯 Qalampirli lavash 🥩🌶🌯", callback_data="qalampir mol lavash")
        ],
        [
            InlineKeyboardButton(text="🍗🌶🌯 Qalampirli lavash 🍗🌶🌯", callback_data="qalampir tovuq lavash")
        ],
        [
            InlineKeyboardButton(text="🌯🥗 Fitter 🌯🥗", callback_data="fitter")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
menuHot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌭 Hot-dog 🌭", callback_data="hotdog")
        ],
        [
            InlineKeyboardButton(text="🌭🌭 Double Hot-dog 🌭🌭", callback_data="double hotdog")
        ],
        [
            InlineKeyboardButton(text="🔽🌭 Mini Hot-dog 🔽🌭", callback_data="mini hotdog")
        ],
        [
            InlineKeyboardButton(text="🍟 Kartoshka FRI 🍟", callback_data="free")
        ],
        [
            InlineKeyboardButton(text="🍟🥔 Kartoshka po derevenski 🥔🍟", callback_data="kartoshka")
        ],
        [
            InlineKeyboardButton(text="🔽🌭 Kichik yoshdagilar uchun Hot-dog 🌭🔽", callback_data="mmini hotdog")
        ],
        [
            InlineKeyboardButton(text="🍗🥟 Tovuqli Sab 🥟🍗", callback_data="tovuq sab")
        ],
        [
            InlineKeyboardButton(text="🥩🥟 Mol go'shtli Sab 🥟🥩", callback_data="mol sab")
        ],
        [
            InlineKeyboardButton(text="🧀🍗🥟 Sir qo'shilgan Sab 🧀🍗🥟", callback_data="sir tovuq sab")
        ],
        [
            InlineKeyboardButton(text="🧀🥩🥟 Sir qo'shilgan Sab 🧀🥩🥟", callback_data="sir mol sab")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuShaur = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔽🍔🥩 Mini mol go'shtli Shaurma 🥩🍔🔽", callback_data="mini mol shaur")
        ],
        [
            InlineKeyboardButton(text="🍔🥩 Mol go'shtli Shaurma 🥩🍔", callback_data="mol shaur")
        ],
        [
            InlineKeyboardButton(text="🔽🍔🍗 Mini tovuqli Shaurma 🍗🍔🔽", callback_data="mini tovuq shaur")
        ],
        [
            InlineKeyboardButton(text="🍔🍗 Tovuqli Shaurma 🍗🍔", callback_data="tovuq shaur")
        ],
        [
            InlineKeyboardButton(text="🌶🍔🥩 Qalampirli Shaurma 🥩🍔🌶", callback_data="qalampir mol shaur")
        ],
        [
            InlineKeyboardButton(text="🔽🌶🍔🥩 Mini Qalampirli Shaurma 🥩🍔🌶🔽", callback_data="mini qalampir mol shaur")
        ],
        [
            InlineKeyboardButton(text="🌶🍔🍗 Qalampirli Shaurma 🍗🍔🌶", callback_data="qalampir tovuq shaur")
        ],
        [
            InlineKeyboardButton(text="🔽🌶🍔🍗 Mini Qalampirli Shaurma 🍗🍔🌶🔽", callback_data="mini qalampir tovuq shaur")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuGam = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍔 Gamburger 🍔", callback_data="gamburger")
        ],
        [
            InlineKeyboardButton(text="🍔🍔 Double Burger 🍔🍔", callback_data="double burger")
        ],
        [
            InlineKeyboardButton(text="🧀🍔 Cheese burger 🍔🧀", callback_data="cheese burger")
        ],
        [
            InlineKeyboardButton(text="🧀🍔🍔 Double cheese burger 🍔🍔🧀", callback_data="double cheese burger")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuAssorti = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥩 Mol go'shtli danar 🥩", callback_data="mol danar")
        ],
        [
            InlineKeyboardButton(text="🍗 Tovuqli danar 🍗", callback_data="tovuq danar")
        ],
        [
            InlineKeyboardButton(text="🍗🍗 Stripsi 🍗🍗", callback_data="strips")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuKombo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌭🍟 Kombo plyus 🍟🌭", callback_data="kombo plyus")
        ],
        [
            InlineKeyboardButton(text="🌭🍟 Detskoe Kombo 🍟🌭", callback_data="kombo yosh")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuDesert = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍯🍰 Medovik 🍰🍯", callback_data="medovik")
        ],
        [
            InlineKeyboardButton(text="🧀🍰 Cheese Cake 🍰🧀", callback_data="cheese cake")
        ],
        [
            InlineKeyboardButton(text="🍩🍓 Donat yagodniy misks 🍓🍩", callback_data="donat yagoda")
        ],
        [
            InlineKeyboardButton(text="🍩🍭 Donat caramel 🍭🍩", callback_data="donat caramel")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuSous = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ketchup", callback_data="ketchup"),
            InlineKeyboardButton(text="Mayonez", callback_data="mayonez")
        ],
        [
            InlineKeyboardButton(text="Sir qo'shilgan sous", callback_data="sir sous"),
            InlineKeyboardButton(text="Chesnok qo'shilgan sous", callback_data="chesnok sous")
        ],
        [
            InlineKeyboardButton(text="Chili sous", callback_data="chili sous"),
            InlineKeyboardButton(text="Guruch", callback_data="guruch")
        ],
        [
            InlineKeyboardButton(text="Salat", callback_data="salat"),
            InlineKeyboardButton(text="Non", callback_data="non")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuSok = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sok Bliss. 1 litr", callback_data="bliss")
        ],
        [
            InlineKeyboardButton(text="Pepsi 1.5 litr", callback_data="pepsi 1.5"),
            InlineKeyboardButton(text="Pepsi 0.5 litr", callback_data="pepsi 0.5")
        ],
        [
            InlineKeyboardButton(text="Gazsiz suv 0.5 litr", callback_data="gazsiz suv"),
            InlineKeyboardButton(text="Pepsi razliv 0.4 litr", callback_data="pepsi 0.4 litr")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuChoy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'k choy", callback_data="ko'k choy"),
            InlineKeyboardButton(text="Qora choy", callback_data="qora choy")
        ],
        [
            InlineKeyboardButton(text="Limonli ko'k choy", callback_data="limon ko'k choy"),
            InlineKeyboardButton(text="Limonli qora choy", callback_data="limon qora choy")
        ],
        [
            InlineKeyboardButton(text="Cappuccino", callback_data="cappuccino"),
            InlineKeyboardButton(text="Americano", callback_data="americano")
        ],
        [
            InlineKeyboardButton(text="Latte", callback_data="latte"),
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

shaurmamenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga 🔙", callback_data="back")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Lavashmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga 🔙", callback_data="ack")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
