import keralabot

import logging

from config import *

@bot.message_handler(commands=['ban'])
def ban(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    members = bot.get_chat_member(chat_id, user_id)
    
    if message.chat.type == "private":
        bot.reply_to(message, "This command is meant to be used in Groups")
        return
    if message.reply_to_message == None and members.status == "administrator" or members.status == "creator":
        ban_user = message.text[5:]
        if ban_user == None:
            bot.reply_to(message, "Reply to a message or send me the ID of the user")
        else:
            bot.send_sticker(message.chat.id, "CAADBAADJQEAAu0egAUl-J3zbwtTgBYE")
            bot.kick_chat_member(message.chat.id, ban_user)
            bot.reply_to(message, "{} banned {}".format(message.from_user.first_name, members.first_name))
            bot.delete_message(message.chat.id, message.from_user.message_id)      #Added delete some command for misuse of that
    if message.reply_to_message != None and members.status == "administrator" or members.status == "creator":
        bot.send_sticker(message.chat.id, "CAADBAADJQEAAu0egAUl-J3zbwtTgBYE")
        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.reply_to(message, "{} banned {}".format(message.from_user.first_name, message.reply_to_message.from_user.first_name))
        bot.delete_message(message.chat.id, message.message_id)      #Added delete some command for misuse of that
        return

@bot.message_handler(commands=['unban'])
def unban(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    members = bot.get_chat_member(chat_id, user_id)
    if message.chat.type == "private":
        bot.reply_to(message, "This command is meant to be used in Groups")
        return
    
    if message.reply_to_message == None and members.status == "administrator" or members.status == "creator":
        unban_user = message.text[7:]
        if unban_user == None:
            bot.reply_to(message, "Reply to a message or send me the ID of the user")
        else:
            bot.unban_chat_member(message.chat.id, unban_user)
            bot.reply_to(message, "Now that user can join this chat")
            bot.delete_message(message.chat.id, message.message_id)      #Added delete some command for misuse of that
    if message.reply_to_message != None and members.status == "administrator" or members.status == "creator":
        bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.reply_to(message, "Now that user can join this chat")
        bot.delete_message(message.chat.id, message.message_id)      #Added delete some command for misuse of that
        return
