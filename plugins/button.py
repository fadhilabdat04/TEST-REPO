# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de


from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_1, FORCE_SUB_GROUP_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2  

from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and FORCE_SUB_GROUP_1 and FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and FORCE_SUB_GROUP_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="♻️ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink5),
                InlineKeyboardButton(text="♻️ 𝐆𝐑𝐎𝐔𝐏", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons

def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and not FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and FORCE_SUB_GROUP_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
             pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and FORCE_SUB_GROUP_1 and FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_1 and FORCE_SUB_GROUP_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink5),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink6),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
