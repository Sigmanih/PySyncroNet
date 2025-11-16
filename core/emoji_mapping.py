"""
Mapping delle emoji e caratteri speciali per la conversione PDF
"""

EMOJI_MAPPING = {
    # Emoji comuni con codici Unicode esatti
    '\u2728': '[SPARKLES]',      # ✨
    '\u2705': '[CHECK]',         # ✅
    '\u274c': '[CROSS]',         # ❌
    '\u26a0\ufe0f': '[WARNING]', # ⚠️
    '\u2139\ufe0f': '[INFO]',    # ℹ️
    '\u1f50d': '[SEARCH]',       # 🔍
    '\u1f4c1': '[FOLDER]',       # 📁
    '\u1f4c4': '[FILE]',         # 📄
    '\u2699\ufe0f': '[GEAR]',    # ⚙️
    '\u1f504': '[REFRESH]',      # 🔄
    '\u1f4ca': '[CHART]',        # 📊
    '\u1f512': '[LOCK]',         # 🔒
    '\u1f513': '[UNLOCK]',       # 🔓
    '\u1f4cb': '[CLIPBOARD]',    # 📋
    '\u1f3af': '[TARGET]',       # 🎯
    '\u1f680': '[ROCKET]',       # 🚀
    '\u1f4be': '[SAVE]',         # 💾
    '\u1f4e4': '[UPLOAD]',       # 📤
    '\u1f4e5': '[DOWNLOAD]',     # 📥
    '\u1f5d1\ufe0f': '[TRASH]',  # 🗑️
    '\u2b50': '[STAR]',          # ⭐
    '\u1f525': '[FIRE]',         # 🔥
    '\u1f4a1': '[BULB]',         # 💡
    '\u270f\ufe0f': '[PENCIL]',  # ✏️
    '\u1f514': '[BELL]',         # 🔔
    '\u1f3a8': '[ART]',          # 🎨
    '\u1f527': '[WRENCH]',       # 🔧
    '\u1f4c8': '[GRAPH_UP]',     # 📈
    '\u1f4c9': '[GRAPH_DOWN]',   # 📉
    '\u1f552': '[CLOCK]',        # 🕒
    '\u1f441\ufe0f': '[EYE]',    # 👁️
    '\u1f465': '[USERS]',        # 👥
    '\u1f4ac': '[SPEECH]',       # 💬
    '\u1f4cc': '[PIN]',          # 📌
    '\u1f4cd': '[ROUND_PIN]',    # 📍
    '\u1f6e0\ufe0f': '[TOOLS]',  # 🛠️
    '\u1f528': '[HAMMER]',       # 🔨
    '\u23f1\ufe0f': '[TIMER]',   # ⏱️
    '\u1f3ad': '[MASK]',         # 🎭
    '\u1f4da': '[BOOKS]',        # 📚
    '\u1f517': '[LINK]',         # 🔗
    
    # NUOVE EMOJI RICHIESTE
    '\u1f9f9': '[BROOM]',        # 🧹
    '\u1f524': '[SYMBOLS]',      # 🔤
    '\u1f31f': '[GLOWING_STAR]', # 🌟
    '\u1f464': '[SILHOUETTE]',   # 👤
    '\u1f4c5': '[CALENDAR]',     # 📅
    '\u1f41b': '[BUG]',          # 🐛
    
    # Frecce
    '\u2192': '[ARROW_RIGHT]',   # →
    '\u27a1\ufe0f': '[ARROW_RIGHT_FULL]', # ➡️
    '\u2b05\ufe0f': '[ARROW_LEFT]',      # ⬅️
    '\u2b06\ufe0f': '[ARROW_UP]',        # ⬆️
    '\u2b07\ufe0f': '[ARROW_DOWN]',      # ⬇️
    '\u21a9\ufe0f': '[ARROW_LEFT_HOOK]', # ↩️
    '\u21aa\ufe0f': '[ARROW_RIGHT_HOOK]',# ↪️
    
    # Controlli media
    '\u23ea': '[REWIND]',        # ⏪
    '\u23e9': '[FAST_FORWARD]',  # ⏩
    '\u23f8\ufe0f': '[PAUSE]',   # ⏸️
    '\u23f9\ufe0f': '[STOP]',    # ⏹️
    '\u23fa\ufe0f': '[RECORD]',  # ⏺️
    
    # Altri simboli
    '\u1f3b5': '[MUSIC]',        # 🎵
    '\u1f3b6': '[NOTES]',        # 🎶
    '\u1f3f7\ufe0f': '[LABEL]',  # 🏷️
    '\u1f4e7': '[EMAIL]',        # 📧
    '\u1f4f1': '[PHONE]',        # 📱
    '\u1f4bb': '[LAPTOP]',       # 💻
    '\u1f5a5\ufe0f': '[DESKTOP]',# 🖥️
    '\u1f5a8\ufe0f': '[PRINTER]',# 🖨️
    '\u1f4f8': '[CAMERA]',       # 📸
    '\u1f3a5': '[VIDEO_CAMERA]', # 🎥
    '\u1f4e1': '[SATELLITE]',    # 📡
    '\u1f526': '[FLASHLIGHT]',   # 🔦
    '\u1f4b0': '[MONEY_BAG]',    # 💰
    '\u1f4b3': '[CREDIT_CARD]',  # 💳
    '\u1f310': '[GLOBE]',        # 🌐
    '\u1f5fa\ufe0f': '[MAP]',    # 🗺️
    
    # EMOJI AGGIUNTIVE
    '\u1f4a3': '[BOMB]',         # 💣
    '\u1f4a4': '[ZZZ]',          # 💤
    '\u1f4a5': '[COLLISION]',    # 💥
    '\u1f4a6': '[SWEAT_DROPS]',  # 💦
    '\u1f4a7': '[DROPLET]',      # 💧
    '\u1f4a8': '[DASH]',         # 💨
    '\u1f4a9': '[POOP]',         # 💩
    '\u1f4aa': '[MUSCLE]',       # 💪
    '\u1f4ab': '[DIZZY]',        # 💫
    '\u1f4ac': '[SPEECH_BUBBLE]',# 💬
    '\u1f4ad': '[THOUGHT]',      # 💭
    '\u1f4ae': '[WHITE_FLOWER]', # 💮
    '\u1f4af': '[HUNDRED]',      # 💯
    '\u1f4b4': '[YEN]',          # 💴
    '\u1f4b5': '[DOLLAR]',       # 💵
    '\u1f4b6': '[EURO]',         # 💶
    '\u1f4b7': '[POUND]',        # 💷
    '\u1f4b8': '[MONEY_WINGS]',  # 💸
    '\u1f4b9': '[CHART]',        # 💹
    '\u1f4ba': '[SEAT]',         # 💺
    '\u1f4bc': '[BRIEFCASE]',    # 💼
    '\u1f4bd': '[DISC]',         # 💽
    '\u1f4bf': '[CD]',           # 💿
    '\u1f4c0': '[DVD]',          # 📀
    '\u1f4c2': '[OPEN_FOLDER]',  # 📂
    '\u1f4c3': '[PAGE]',         # 📃
    '\u1f4c6': '[TEAR_CALENDAR]',# 📆
    '\u1f4c7': '[CARD_INDEX]',   # 📇
    '\u1f4cc': '[PUSHPIN]',      # 📌
    '\u1f4ce': '[PAPERCLIP]',    # 📎
    '\u1f4cf': '[STRAIGHT_RULER]',# 📏
    '\u1f4d0': '[TRIANGLE_RULER]',# 📐
    '\u1f4d1': '[BOOKMARK_TABS]',# 📑
    '\u1f4d2': '[LEDGER]',       # 📒
    '\u1f4d3': '[NOTEBOOK]',     # 📓
    '\u1f4d4': '[NOTEBOOK_DECORATIVE]',# 📔
    '\u1f4d5': '[CLOSED_BOOK]',  # 📕
    '\u1f4d6': '[OPEN_BOOK]',    # 📖
    '\u1f4d7': '[GREEN_BOOK]',   # 📗
    '\u1f4d8': '[BLUE_BOOK]',    # 📘
    '\u1f4d9': '[ORANGE_BOOK]',  # 📙
    '\u1f4db': '[ORANGE_BOOK]',  # 📛
    '\u1f4dc': '[SCROLL]',       # 📜
    '\u1f4dd': '[MEMO]',         # 📝
    '\u1f4de': '[TELEPHONE]',    # 📞
    '\u1f4df': '[PAGER]',        # 📟
    '\u1f4e0': '[FAX]',          # 📠
    '\u1f4e1': '[SATELLITE_ANTENNA]',# 📡
    '\u1f4e2': '[LOUDSPEAKER]',  # 📢
    '\u1f4e3': '[MEGAPHONE]',    # 📣
    '\u1f4e6': '[PACKAGE]',      # 📦
    '\u1f4e8': '[INCOMING_ENVELOPE]',# 📨
    '\u1f4e9': '[ENVELOPE_ARROW]',# 📩
    '\u1f4ea': '[MAILBOX_CLOSED]',# 📪
    '\u1f4eb': '[MAILBOX]',      # 📫
    '\u1f4ec': '[MAILBOX_OPEN]', # 📬
    '\u1f4ed': '[MAILBOX_FLAG]', # 📭
    '\u1f4ee': '[POSTBOX]',      # 📮
    '\u1f4ef': '[POSTAL_HORN]',  # 📯
    '\u1f4f0': '[NEWSPAPER]',    # 📰
    '\u1f4f2': '[MOBILE_PHONE]', # 📲
    '\u1f4f7': '[CAMERA_FLASH]', # 📷
    '\u1f4f9': '[VIDEO_CASSETTE]',# 📹
    '\u1f4fa': '[TV]',           # 📺
    '\u1f4fb': '[RADIO]',        # 📻
    '\u1f4fc': '[VIDEOCASSETTE]',# 📼
    
    '\u1f468\u200d\u1f4bb': '[MAN_TECHNOLOGIST]',  # 👨‍💻
    '\u1f469\u200d\u1f4bb': '[WOMAN_TECHNOLOGIST]',  # 👩‍💻
    '\u1f9d1\u200d\u1f4bb': '[PERSON_TECHNOLOGIST]',  # 🧑‍💻    
    '\u1f468\u200d\u1f393': '[MAN_STUDENT]',         # 👨‍🎓
    '\u1f469\u200d\u1f393': '[WOMAN_STUDENT]',       # 👩‍🎓
    '\u1f468\u200d\u1f3a4': '[MAN_SINGER]',          # 👨‍🎤
    '\u1f469\u200d\u1f3a4': '[WOMAN_SINGER]',        # 👩‍🎤    

    # Emoji tecniche e computer
    '\u1f5a5': '[DESKTOP_COMPUTER]',# 🖥
    '\u1f5a8': '[PRINTER_2]',    # 🖨
    '\u1f5b1': '[THREE_BUTTON_MOUSE]',# 🖱
    '\u1f5b2': '[TRACKBALL]',    # 🖲
    '\u1f5bc': '[FRAME]',        # 🖼
    '\u1f5c2': '[CARD_BOX]',     # 🗂
    '\u1f5c3': '[FILE_CABINET]', # 🗃
    '\u1f5c4': '[WASTEBASKET]',  # 🗄
    '\u1f5d1': '[WASTEBASKET_2]',# 🗑
    '\u1f5d2': '[SPIRAL_NOTE]',  # 🗒
    '\u1f5d3': '[SPIRAL_CALENDAR]',# 🗓
    '\u1f5dc': '[COMPRESSION]',  # 🗜
    '\u1f5dd': '[OLD_KEY]',      # 🗝
    '\u1f5de': '[ROLLED_NEWSPAPER]',# 🗞
    
    # Simboli e segni
    '\u1f5e3': '[SPEAKING_HEAD]',# 🗣
    '\u1f5e8': '[LEFT_SPEECH]',  # 🗨
    '\u1f5ef': '[RIGHT_ANGER]',  # 🗯
    '\u1f5f3': '[BALLOT_BOX]',   # 🗳
    '\u1f5fa': '[WORLD_MAP]',    # 🗺
    
    # Caratteri problematici generici
    '\u003f': '[QUESTION]',      # ?
    '\ufffd': '[UNKNOWN]',       # �
    
    # Aggiungi anche le rappresentazioni stringa per compatibilità
    '✨': '[SPARKLES]',
    '✅': '[CHECK]',
    '❌': '[CROSS]',
    '⚠️': '[WARNING]',
    '📂': '[OPEN_FOLDER]',    
    'ℹ️': '[INFO]',
    '🔍': '[SEARCH]',
    '📁': '[FOLDER]',
    '📄': '[FILE]',
    '⚙️': '[GEAR]',
    '🔄': '[REFRESH]',
    '📊': '[CHART]',
    '🔒': '[LOCK]',
    '🔓': '[UNLOCK]',
    '📋': '[CLIPBOARD]',
    '🎯': '[TARGET]',
    '🚀': '[ROCKET]',
    '💾': '[SAVE]',
    '📤': '[UPLOAD]',
    '📥': '[DOWNLOAD]',
    '🗑️': '[TRASH]',
    '⭐': '[STAR]',
    '🔥': '[FIRE]',
    '💡': '[BULB]',
    '📝': '[PENCIL]',
    '🔔': '[BELL]',
    '🎨': '[ART]',
    '🔧': '[WRENCH]',
    '📈': '[GRAPH_UP]',
    '📉': '[GRAPH_DOWN]',
    '🕒': '[CLOCK]',
    '👁️': '[EYE]',
    '👥': '[USERS]',
    '💬': '[SPEECH]',
    '📌': '[PIN]',
    '📍': '[ROUND_PIN]',
    '🛠️': '[TOOLS]',
    '🔨': '[HAMMER]',
    '⏱️': '[TIMER]',
    '🎭': '[MASK]',
    '📚': '[BOOKS]',
    '🔗': '[LINK]',
    '→': '[ARROW_RIGHT]',
    '➡️': '[ARROW_RIGHT_FULL]',
    '⬅️': '[ARROW_LEFT]',
    '⬆️': '[ARROW_UP]',
    '⬇️': '[ARROW_DOWN]',
    '↩️': '[ARROW_LEFT_HOOK]',
    '↪️': '[ARROW_RIGHT_HOOK]',
    '⏪': '[REWIND]',
    '⏩': '[FAST_FORWARD]',
    '⏸️': '[PAUSE]',
    '⏹️': '[STOP]',
    '⏺️': '[RECORD]',
    '🎵': '[MUSIC]',
    '🎶': '[NOTES]',
    '🏷️': '[LABEL]',
    '📧': '[EMAIL]',
    '📱': '[PHONE]',
    '💻': '[LAPTOP]',
    '🖥️': '[DESKTOP]',
    '🖨️': '[PRINTER]',
    '📸': '[CAMERA]',
    '🎥': '[VIDEO_CAMERA]',
    '📡': '[SATELLITE]',
    '🔦': '[FLASHLIGHT]',
    '💰': '[MONEY_BAG]',
    '💳': '[CREDIT_CARD]',
    '🌐': '[GLOBE]',
    '🗺️': '[MAP]',
    '🧹': '[BROOM]',
    '🔤': '[SYMBOLS]',
    '🌟': '[GLOWING_STAR]',
    '👤': '[SILHOUETTE]',
    '📅': '[CALENDAR]',
    '🐛': '[BUG]',
    '👨‍💻': '[MAN_TECHNOLOGIST]',
    '👩‍💻': '[WOMAN_TECHNOLOGIST]',
    '🧑‍💻': '[PERSON_TECHNOLOGIST]',
    '👨‍🎓': '[MAN_STUDENT]',
    '👩‍🎓': '[WOMAN_STUDENT]',
    '👨‍🎤': '[MAN_SINGER]',
    '👩‍🎤': '[WOMAN_SINGER]'
}

# Mapping inverso per la decodifica
REVERSE_EMOJI_MAPPING = {v: k for k, v in EMOJI_MAPPING.items()}