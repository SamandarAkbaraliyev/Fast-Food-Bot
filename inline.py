from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
            InlineKeyboardButton(text="🥩🌯 Mol go'shtli lavash 🥩🌯", callback_data="b1")
        ],
        [
            InlineKeyboardButton(text="🍗🌯 Tovuqli lavash 🍗🌯", callback_data="b2")
        ],
        [
            InlineKeyboardButton(text="🔽🥩🌯 Mini mol go'shtli lavash 🔽🥩🌯", callback_data="b3")
        ],
        [
            InlineKeyboardButton(text="🔽🍗🌯 Mini tovuqli lavash 🔽🍗🌯", callback_data="b4")
        ],
        [
            InlineKeyboardButton(text="🧀🥩🌯 Sirli mol go'shtli lavash 🧀🥩🌯", callback_data="b5")
        ],
        [
            InlineKeyboardButton(text="🧀🍗🌯 Sir qo'shilgan tovuqli lavash 🧀🍗🌯", callback_data="b6")
        ],
        [
            InlineKeyboardButton(text="🔽🧀🌯🥩 Mini sir qo'shilgan lavash 🔽🧀🌯🥩", callback_data="b7")
        ],
        [
            InlineKeyboardButton(text="🔽🧀🌯🍗 Mini sir qo'shilgan lavash 🔽🧀🌯🍗", callback_data="b8")
        ],
        [
            InlineKeyboardButton(text="🥩🌶🌯 Qalampirli lavash 🥩🌶🌯", callback_data="b9")
        ],
        [
            InlineKeyboardButton(text="🍗🌶🌯 Qalampirli lavash 🍗🌶🌯", callback_data="ba")
        ],
        [
            InlineKeyboardButton(text="🌯🥗 Fitter 🌯🥗", callback_data="bb")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
menuHot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌭 Hot-dog 🌭", callback_data="c1")
        ],
        [
            InlineKeyboardButton(text="🌭🌭 Double Hot-dog 🌭🌭", callback_data="c2")
        ],
        [
            InlineKeyboardButton(text="🔽🌭 Mini Hot-dog 🔽🌭", callback_data="c3")
        ],
        [
            InlineKeyboardButton(text="🍟 Kartoshka FRI 🍟", callback_data="c4")
        ],
        [
            InlineKeyboardButton(text="🍟🥔 Kartoshka po derevenski 🥔🍟", callback_data="c5")
        ],
        [
            InlineKeyboardButton(text="🔽🌭 Kichik yoshdagilar uchun Hot-dog 🌭🔽", callback_data="c6")
        ],
        [
            InlineKeyboardButton(text="🍗🥟 Tovuqli Sab 🥟🍗", callback_data="c7")
        ],
        [
            InlineKeyboardButton(text="🥩🥟 Mol go'shtli Sab 🥟🥩", callback_data="c8")
        ],
        [
            InlineKeyboardButton(text="🧀🍗🥟 Sir qo'shilgan Sab 🧀🍗🥟", callback_data="c9")
        ],
        [
            InlineKeyboardButton(text="🧀🥩🥟 Sir qo'shilgan Sab 🧀🥩🥟", callback_data="l2")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuShaur = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔽🍔🥩 Mini mol go'shtli Shaurma 🥩🍔🔽", callback_data="d1")
        ],
        [
            InlineKeyboardButton(text="🍔🥩 Mol go'shtli Shaurma 🥩🍔", callback_data="d2")
        ],
        [
            InlineKeyboardButton(text="🔽🍔🍗 Mini tovuqli Shaurma 🍗🍔🔽", callback_data="d3")
        ],
        [
            InlineKeyboardButton(text="🍔🍗 Tovuqli Shaurma 🍗🍔", callback_data="d4")
        ],
        [
            InlineKeyboardButton(text="🌶🍔🥩 Qalampirli Shaurma 🥩🍔🌶", callback_data="d5")
        ],
        [
            InlineKeyboardButton(text="🔽🌶🍔🥩 Mini Qalampirli Shaurma 🥩🍔🌶🔽", callback_data="d6")
        ],
        [
            InlineKeyboardButton(text="🌶🍔🍗 Qalampirli Shaurma 🍗🍔🌶", callback_data="d7")
        ],
        [
            InlineKeyboardButton(text="🔽🌶🍔🍗 Mini Qalampirli Shaurma 🍗🍔🌶🔽", callback_data="d8")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuGam = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍔 Gamburger 🍔", callback_data="e1")
        ],
        [
            InlineKeyboardButton(text="🍔🍔 Double Burger 🍔🍔", callback_data="e2")
        ],
        [
            InlineKeyboardButton(text="🧀🍔 Cheese burger 🍔🧀", callback_data="e3")
        ],
        [
            InlineKeyboardButton(text="🧀🍔🍔 Double cheese burger 🍔🍔🧀", callback_data="e4")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuAssorti = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥩 Mol go'shtli danar 🥩", callback_data="f1")
        ],
        [
            InlineKeyboardButton(text="🍗 Tovuqli danar 🍗", callback_data="f2")
        ],
        [
            InlineKeyboardButton(text="🍗🍗 Stripsi 🍗🍗", callback_data="f3")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuKombo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌭🍟 Kombo plyus 🍟🌭", callback_data="g1")
        ],
        [
            InlineKeyboardButton(text="🌭🍟 Detskoe Kombo 🍟🌭", callback_data="g2")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuDesert = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍯🍰 Medovik 🍰🍯", callback_data="h1")
        ],
        [
            InlineKeyboardButton(text="🧀🍰 Cheese Cake 🍰🧀", callback_data="h2")
        ],
        [
            InlineKeyboardButton(text="🍩🍓 Donat yagodniy misks 🍓🍩", callback_data="h3")
        ],
        [
            InlineKeyboardButton(text="🍩🍭 Donat caramel 🍭🍩", callback_data="h4")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuSous = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ketchup", callback_data="i1"),
            InlineKeyboardButton(text="Mayonez", callback_data="i2")
        ],
        [
            InlineKeyboardButton(text="Sir qo'shilgan sous", callback_data="i3"),
            InlineKeyboardButton(text="Chesnok qo'shilgan sous", callback_data="i4")
        ],
        [
            InlineKeyboardButton(text="Chili sous", callback_data="i5"),
            InlineKeyboardButton(text="Guruch", callback_data="i6")
        ],
        [
            InlineKeyboardButton(text="Salat", callback_data="i7"),
            InlineKeyboardButton(text="Non", callback_data="i8")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuSok = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sok Bliss. 1 litr", callback_data="j1")
        ],
        [
            InlineKeyboardButton(text="Pepsi 1.5 litr", callback_data="j2"),
            InlineKeyboardButton(text="Pepsi 0.5 litr", callback_data="j3")
        ],
        [
            InlineKeyboardButton(text="Gazsiz suv 0.5 litr", callback_data="j4"),
            InlineKeyboardButton(text="Pepsi razliv 0.4 litr", callback_data="j5")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

menuChoy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'k choy", callback_data="k1"),
            InlineKeyboardButton(text="Qora choy", callback_data="k2")
        ],
        [
            InlineKeyboardButton(text="Limonli ko'k choy", callback_data="k3"),
            InlineKeyboardButton(text="Limonli qora choy", callback_data="k4")
        ],
        [
            InlineKeyboardButton(text="Cappuccino", callback_data="k5"),
            InlineKeyboardButton(text="Americano", callback_data="k6")
        ],
        [
            InlineKeyboardButton(text="Latte", callback_data="k7"),
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
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="back")
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
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="ack")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

Hotdogmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l1")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)

Shaurmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l3")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Hamburgermenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l4")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Blyudamenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l5")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Combomenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l6")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Desertmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l7")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Sousmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l8")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Sokmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="l9")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
Choymenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧺 Savatchaga qo'shish 🧺", callback_data="basket")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga 🔙", callback_data="m1")
        ],
        [
            InlineKeyboardButton(text="🍽 Menu 🍽", callback_data="menu")
        ]
    ]
)
