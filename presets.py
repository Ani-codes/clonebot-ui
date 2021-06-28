# ----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
class Presets(object):
    START_TEXT = """
Hello... {}
𝐼 𝑐𝑎𝑛 𝑐𝑙𝑜𝑛𝑒 𝑚𝑒𝑑𝑖𝑎 𝑓𝑟𝑜𝑚 𝑎𝑛𝑦 𝑐ℎ𝑎𝑡 𝑡𝑜 𝑦𝑜𝑢𝑟 𝑝𝑒𝑟𝑠𝑜𝑛𝑎𝑙 𝑐ℎ𝑎𝑡 ! 𝐶𝑙𝑖𝑐𝑘 𝑠𝑒𝑡𝑡𝑖𝑛𝑔𝑠 𝑡𝑜 𝑐𝑜𝑛𝑓𝑖𝑔𝑢𝑟𝑒 𝑚𝑒...𝑇ℎ𝑎𝑛𝑘𝑠
    """
    WELCOME_TEXT = "⭑⭑HELP for more info:⭑⭑"
    MESSAGE_COUNT = """
Live: <code>{}\n{}\n{}</code>\n
Starting Id: <b>{}</b>
Now: <b>{}</b>
Ending Id: <b>{}</b>
____________________________________
𝐂𝐥𝐨𝐧𝐞 𝐃𝐞𝐥𝐚𝐲: {}
𝐃𝐞𝐟𝐚𝐮𝐥𝐭 𝐂𝐚𝐩𝐭𝐢𝐨𝐧: {}
𝐅𝐢𝐥𝐞 𝐧𝐚𝐦𝐞 𝐚𝐬 𝐂𝐚𝐩𝐭𝐢𝐨𝐧: {}

Total Copied: <b>{}</b>
Total Completed: <b>{} %</b> 󠀥

× Documents: <b>{}</b>
× Videos: <b>{}</b>
× Audios: <b>{}</b>
× Photos: <b>{}</b>
× Voice: <b>{}</b>

✖️ 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧: <b>{}</b>
✖️ 𝐁𝐨𝐭 𝐔𝐩𝐭𝐢𝐦𝐞: <b>{}</b>

➠ 𝐂𝐥𝐨𝐧𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐭: <b>{}</b>
➠ 𝐋𝐚𝐬𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐝 𝐎𝐧: <b>{}</b>
    """
    INFO_CHAT_TYPES = """
You can enter following type:-

Id: 12345678 (-𝟏𝟎𝟎 𝐧𝐨𝐭 𝐫𝐞𝐪.)
Invite links : 𝐡𝐭𝐭𝐩𝐬://𝐭.𝐦𝐞/𝐣𝐨𝐢𝐧𝐜𝐡𝐚𝐭/
Public links : 𝐡𝐭𝐭𝐩𝐬://𝐭.𝐦𝐞/𝐩𝐲𝐭𝐡𝐨𝐧
Username: @telegram
    """
    SELECTED_TYPE = """
𝙔𝙤𝙪 𝙝𝙖𝙫𝙚 𝙨𝙚𝙡𝙚𝙘𝙩𝙚𝙙:
------------------------------
𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭 : {}
𝐀𝐮𝐝𝐢𝐨: {}
𝐕𝐢𝐝𝐞𝐨: {}
𝐏𝐡𝐨𝐭𝐨: {}
𝐕𝐨𝐢𝐜𝐞: {}
    """
    VIEW_CONF = """
Source id : {}
Target id : {}
From msg id: {} | To msg id : {}
Delayed : {} | Caption : {} | FN Caption: {}
Types: 📚:{} | 🎞:{} | 🔊:{} | 📸:{} | 🗣:{}
    """
    FILE_TYPES = ["document", "video", "audio", "voice", "photo"]
    COPIED_MESSAGES = "<b><a href='https://github.com/m4mallu/clonebot'>Medias Copied</a></b>"
    IN_CORRECT_PERMISSIONS_MESSAGE_DEST_POSTING = "𝘱𝘰𝘴𝘵𝘪𝘯𝘨 𝘱𝘳𝘪𝘷𝘪𝘭𝘢𝘨𝘦𝘴 𝘪𝘯 𝘵𝘩𝘦 𝘨𝘪𝘷𝘦𝘯 𝘤𝘩𝘢𝘵"
                         
    USER_ABSENT_MSG = "𝙎𝙚𝙨𝙨𝙞𝙤𝙣 𝙪𝙨𝙚𝙧 𝙞𝙨 𝙣𝙤𝙩 𝙞𝙣 𝙩𝙝𝙚 𝙩𝙖𝙧𝙜𝙚𝙩 𝙘𝙝𝙖𝙩 𝙜𝙞𝙫𝙚𝙣"
    CANCEL_CLONE = "𝙎𝙩𝙤𝙥𝙥𝙞𝙣𝙜 𝙩𝙝𝙚 𝙥𝙧𝙤𝙘𝙚𝙨𝙨... 𝙋𝙡𝙯 𝙬𝙖𝙞𝙩"
    CANCELLED_MSG = "𝙐𝙨𝙚𝙧 𝙘𝙖𝙣𝙘𝙚𝙡𝙡𝙚𝙙 𝙘𝙡𝙤𝙣𝙞𝙣𝙜"
    INITIAL_MESSAGE_TEXT = "𝙇𝙤𝙤𝙠𝙞𝙣𝙜 𝙛𝙤𝙧 𝙢𝙚𝙙𝙞𝙖 "
    WAIT_MSG = "𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩..𝙖 𝙨𝙚𝙘𝙤𝙣𝙙"
    SOURCE_CONFIRM = """
𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞: {}
𝐂𝐡𝐚𝐭 𝐈𝐝: <code> {}</code>
𝐂𝐡𝐚𝐭 𝐓𝐲𝐩𝐞: {}
𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {}
𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {}
𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {}
                                                              \xad
Chat Saved  ✔️
                     """
    DEST_CNF = """
𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞: {}
𝐂𝐡𝐚𝐭 𝐈𝐝: <code> {}</code>
𝐂𝐡𝐚𝐭 𝐓𝐲𝐩𝐞: {}
𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {}
𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {}
𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {}
\xad                                                              \xad
 Chat Saved  ✔️
               """
    SESSION_START_INFO = """
𝐔𝐬𝐞𝐫 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐬𝐭𝐚𝐫𝐭𝐞𝐝:

𝐃𝐚𝐭𝐞:  {}
𝐓𝐢𝐦𝐞:  {}

A user session started by some id.
If u are not aware of this then
terminate that session

    """
    NOT_CONFIGURED = "𝙎𝙤𝙪𝙧𝙘𝙚 & 𝙏𝙖𝙧𝙜𝙚𝙩 𝙘𝙝𝙖𝙩𝙨 𝙣𝙤𝙩 𝙘𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚𝙙 ⚠"
    NOT_AUTH_TEXT = "𝙔𝙤𝙪 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙  ⚠ "
    BOT_BLOCKED_MSG = "Bot is blocked by the  session user !"
    NOT_CONFIGURED_CLONE = "𝙉𝙤 𝙘𝙝𝙖𝙩 𝙘𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙛𝙤𝙪𝙣𝙙 ⚠\n\n𝘾𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚 𝙩𝙝𝙚 𝙎𝙤𝙪𝙧𝙘𝙚 & 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩𝙨 𝙗𝙚𝙛𝙤𝙧𝙚 𝙮𝙤𝙪 𝙘𝙡𝙤𝙣𝙚 🤷"
    FINISHED_TEXT = "𝘾𝙡𝙤𝙣𝙚  𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮  ✔️"
    TERMINATED_MSG = "🚫 𝘽𝙤𝙩 𝙏𝙚𝙧𝙢𝙞𝙣𝙖𝙩𝙚𝙙 🚫"
    COPY_ERROR = "𝙎𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜 𝙬𝙚𝙣𝙩 𝙬𝙧𝙤𝙣𝙜 !"
    INVALID_CHAT_ID = "<u>𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙘𝙝𝙖𝙩 𝙥𝙖𝙧𝙖𝙢𝙚𝙩𝙚𝙧 𝙛𝙤𝙪𝙣𝙙</u>\n\n𝐂𝐚𝐮𝐬𝐞𝐬:\n1. 𝘚𝘦𝘴𝘴𝘪𝘰𝘯 𝘶𝘴𝘦𝘳 𝘯𝘰𝘵 𝘪𝘯 𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘤𝘩𝘢𝘵\n" \
                      "2. 𝘍𝘰𝘳 𝘱𝘶𝘣𝘭𝘪𝘤 𝘤𝘩𝘢𝘵𝘴, 𝘶𝘴𝘦 '@𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦'\n𝘰𝘳 𝘭𝘪𝘯𝘬 𝘪𝘯𝘴𝘵𝘦𝘢𝘥 𝘰𝘧 '𝘪𝘥'"
    ASK_SOURCE = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙨𝙤𝙪𝙧𝙘𝙚 𝙘𝙝𝙖𝙩 𝙞𝙣𝙛𝙤:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    ASK_DESTINATION = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩 𝙞𝙣𝙛𝙤:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    ASK_START_MSG_ID = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙨𝙩𝙖𝙧𝙩𝙞𝙣𝙜 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝙙:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    ASK_END_MSG_ID = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙚𝙣𝙙 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝙙\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."
    CHAT_DUPLICATED_MSG = "𝙎𝙤𝙪𝙧𝙘𝙚 & 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩 𝙄𝙙𝙨 𝙘𝙖𝙣'𝙩 𝙗𝙚 𝙨𝙖𝙢𝙚 "
    FROM_MSG_ID_CNF = "𝐒𝐭𝐚𝐫𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐈𝐝: <code>{}</code> 𝐒𝐚𝐯𝐞𝐝  ✔️"
    END_MSG_ID_CNF = "𝐄𝐧𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐈𝐝: <code>{}</code> 𝐒𝐚𝐯𝐞𝐝  ✔️"
    INVALID_MSG_ID = "𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙞𝙙 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙖𝙣 𝙄𝙣𝙩𝙚𝙜𝙚𝙧 ❗️"
    INVALID_REPLY_MSG = "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙧𝙚𝙥𝙡𝙖𝙮 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 ❗️"
    CNF_SOURCE_FIRST = "𝘾𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚 𝙩𝙝𝙚 𝙨𝙤𝙪𝙧𝙘𝙚 𝙘𝙝𝙖𝙩 𝙛𝙞𝙧𝙨𝙩  ❗️"
    DELAY_OFF = "𝘿𝙚𝙡𝙖𝙮𝙚𝙙 𝙘𝙡𝙤𝙣𝙚 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"
    DELAY_ON = "𝘿𝙚𝙡𝙖𝙮𝙚𝙙 𝙘𝙡𝙤𝙣𝙚 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✔️"
    ADD_DOC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩 𝙖𝙙𝙙𝙚𝙙"
    RM_DOC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_VID = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝙑𝙞𝙙𝙚𝙤 𝙖𝙙𝙙𝙚𝙙"
    RM_VID = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝙑𝙞𝙙𝙚𝙤 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_AUD = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝘼𝙪𝙙𝙞𝙤 𝙖𝙙𝙙𝙚𝙙"
    RM_AUD = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝘼𝙪𝙙𝙞𝙤 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_PIC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝙋𝙝𝙤𝙩𝙤 𝙖𝙙𝙙𝙚𝙙"
    RM_PIC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝙋𝙝𝙤𝙩𝙤 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    ADD_VOI = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝙑𝙤𝙞𝙘𝙚 𝙖𝙙𝙙𝙚𝙙"
    RM_VOI = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 𝙑𝙤𝙞𝙘𝙚 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "
    BLANK = "_______________________"
    BLOCK = "ᴘʀᴏɢʀᴇꜱꜱ ꜰᴀɪʟᴇᴅ ᴛᴏ ᴅɪꜱᴘʟᴀʏ : ʜᴇʟᴘ"
    CAPTION_ON = "𝘾𝙖𝙥𝙩𝙞𝙤𝙣 𝙤𝙣 𝙛𝙞𝙡𝙚𝙨 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✔️"
    CAPTION_OFF = "𝘾𝙖𝙥𝙩𝙞𝙤𝙣 𝙤𝙣 𝙛𝙞𝙡𝙚𝙨 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"
    FN_AS_CAPT_ON = "𝙁𝙞𝙡𝙚 𝙣𝙖𝙢𝙚 𝙖𝙨 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✔️"
    FN_AS_CAPT_OFF = "𝙁𝙞𝙡𝙚 𝙣𝙖𝙢𝙚 𝙖𝙨 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"
    NOT_REQUIRED = "𝙏𝙝𝙞𝙨 𝙛𝙞𝙚𝙡𝙙 𝙞𝙨 𝙣𝙤𝙩 𝙈𝙖𝙙𝙖𝙩𝙤𝙧𝙮  ⚠"
    RST_MSG = "𝙍𝙚𝙨𝙚𝙩 𝙩𝙤 𝘽𝙤𝙩 𝙙𝙚𝙛𝙖𝙪𝙡𝙩𝙨 .. 𝘾𝙤𝙣𝙛𝙞𝙧𝙢𝙚𝙙 ✔️"
    OVER_FLOW = "𝙈𝙖𝙭𝙞𝙢𝙪𝙢 𝙡𝙞𝙢𝙞𝙩 𝙞𝙨 𝙚𝙭𝙘𝙚𝙚𝙙𝙚𝙙 !\n𝘾𝙝𝙚𝙘𝙠 𝙩𝙝𝙚 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙡𝙞𝙢𝙞𝙩, 𝙏𝙧𝙮 𝙖𝙜𝙖𝙞𝙣 !"
    SELECT_TYPE = " 𝙎𝙚𝙡𝙚𝙘𝙩𝙞𝙤𝙣 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙩𝙤𝙜𝙜𝙡𝙚𝙙 𝙤𝙣 𝙩𝙖𝙥\n𝘈𝘭𝘭 𝘢𝘳𝘦 𝘴𝘦𝘭𝘦𝘤𝘵𝘦𝘥 𝘣𝘺 𝘥𝘦𝘧𝘢𝘶𝘭𝘵 !"
