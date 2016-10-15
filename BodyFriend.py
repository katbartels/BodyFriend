#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
ThumbUp   = u"\U0001F44D" # Thumb up
ThumbDown = u"\U0001F44E" # Thumb Down

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		#bot.sendMessage(chat_id, msg['from']['first_name'])
		#print(msg['text'])
		input = str(msg['text']).lower()
		if input == 'hallo' or input == 'hi':
			# # give a descriptive hint
		   bot.sendMessage(chat_id,'Hallo '+ msg['from']['first_name']+'!\nWelcome back!')
		   bot.sendMessage(chat_id, 'What's up?',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='Have a question'), KeyboardButton(text='Wanna track symptoms')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'have a question':
			bot.sendMessage(chat_id,'Just tell me!')
		elif 'period' in input:
			#time.sleep(0.9)
			bot.sendMessage(chat_id,'OK. Let’s stay cool for a minute ok? I will check some data.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Ok, I got something.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Your average cycle is 28 days. Today you are on day 30. \nDelays of <b>2-4 days are very usual and normal</b>.',parse_mode='HTML')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'In Berlin alone, 67% of women your age. \nhave periods delayed by 3 days at least 5 times a year.')
			bot.sendMessage(chat_id, 'What now?',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='Cool, that’s enough.'), KeyboardButton(text='Anything else?')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'anything else?':
			time.sleep(1.5)
			bot.sendMessage(chat_id,'OK, let me check more data.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'From your temperature and fluids, looks like you ovulated on 3rd Sept. \nThat’s 2 later than your previous cycles.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Your fitbit says you only slept 4 hours for the last night.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'It also says that you have not done any exercise for 10 days.')
			bot.sendMessage(chat_id, 'Is it right?',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='Yes, it\'s right'), KeyboardButton(text='No, it\'s not right')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'yes, it\'s right':
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Lack of sleep and exercise affect your period. \nYou need to rest more girl!')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Your resting heartbeat has been higher than usual.')
			time.sleep(1.5)
			bot.sendMessage(chat_id, 'Do you feel more stressed than normal?',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='Yes, a little'), KeyboardButton(text='No, I\'m not stressed')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'yes, a little':
			bot.sendMessage(chat_id,'Ok, let’s make a plan. \nWe need to bring your stress level down.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'How about a film tonight and sleeping early?')
			bot.sendMessage(chat_id, 'New season of Narcos is out on Netflix.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='Tell me more'), KeyboardButton(text='Don\'t want to stay at home')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'no, i\'m not stressed':
			bot.sendMessage(chat_id,'********************')
		elif input == 'no, it\'s not right':
			bot.sendMessage(chat_id,'********************')		
		elif input == 'tell me more':
			bot.sendMessage(chat_id,'********************')
		elif input == 'don\'t want to stay at home':
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Ok, then exercise would be a good idea. \nFresh air and being outdoors.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'You love running.')
			bot.sendMessage(chat_id, 'Here are some 5K routes around you from Mapmyrun.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='Cool, that’s enough.'), KeyboardButton(text='Anything else I should do?')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'anything else i should do?':
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Am happy you asked!\nYes, you need to sleep more.')
			time.sleep(1.5)
			bot.sendMessage(chat_id, 'Have you tried these teas? \nThey will help you relax and can help with period abnormalities.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='That’s cool'), KeyboardButton(text='I don’t like tea')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'that\'s cool':
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Cool, so plan is: \nRun, drink tea and sleep loads.')
			time.sleep(1.5)
			bot.sendMessage(chat_id, 'We wait one day and see what happens OK?',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text='Sounds like a plan'), KeyboardButton(text='I am still worried')]
                                ], 
								resize_keyboard=True,
								one_time_keyboard=True
                            ))
		elif input == 'sounds like a plan':
			bot.sendMessage(chat_id, 'Great. I will remind you to exercise and sleep early OK?',
								reply_markup=ReplyKeyboardMarkup(
									keyboard=[
										[KeyboardButton(text=ThumbUp), KeyboardButton(text=ThumbDown)]
									], 
									resize_keyboard=True,
									one_time_keyboard=True
								))
		elif input == 'i am still worried':
			bot.sendMessage(chat_id,'********************')
		elif input == ThumbUp:
			bot.sendMessage(chat_id,'********************')
		elif input == ThumbDown:
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Ok, I won’t disturb you. \nGive your body some rest and exercise.')
			time.sleep(1.5)
			bot.sendMessage(chat_id,'Let’s see what happens. I am here if you need to talk.')
		elif input == 'i don\'t like tea':
			bot.sendMessage(chat_id,'********************')
		elif input == 'wanna track symptoms':
			bot.sendMessage(chat_id,'test2')
		elif input == 'cool, that\'s enough.':
			bot.sendMessage(chat_id,'I\'m glad it helped!')
		else:
			bot.sendMessage(chat_id,'Sorry, I can\'t understand')

TOKEN = '288580874:AAEr0kSYI6WeRmOiKzBOrOWr595cG-ZVqMk' #sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)