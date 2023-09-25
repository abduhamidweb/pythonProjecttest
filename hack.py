# from twilio.rest import Client
#
# account_sid = 'AC54c3279399e88ec4243861f8f66457ee'
# auth_token = '9f891449f40990ecbdf72c2c3375b5c4'
# client = Client(account_sid, auth_token)
#
# to_phone_number = '+998881745858'  # Qabul qiluvchining raqami
# from_phone_number = '+12517328046'   # Sizning Twilio raqamingiz
# message_body = 'Salom, bu Twilio orqali yuborilgan xabar.'
#
# # 20 ta SMS yuborish
# for _ in range(2):
#     message = client.messages.create(
#         body=message_body,
#         from_=from_phone_number,
#         to=to_phone_number
#     )
#     print(f"Yuborilgan SMS ID: {message.sid}")

# from twilio.rest import Client
#
# # Twilio account SID va auth token
# account_sid = 'ACf3bdb9e0536d0b9e659d3d3c103393e9'
# auth_token = '1642c7264d92784446eab18fb4769b49'
#
# # Twilio xizmatiga ulanish
# client = Client(account_sid, auth_token)
#
# # Xabar ma'lumotlari
# to_phone_number = '+998937322405'  # Qabul qiluvchining raqami
# from_phone_number = '+12512990385'   # Sizning Twilio raqamingiz
# message_body = 'Salom, bu Twilio orqali yuborilgan xabar.'
#
# for _ in range(1):
#     message = client.messages.create(
#         body=message_body,
#         from_=from_phone_number,
#         to=to_phone_number
#     )
#     print(f"Yuborilgan SMS ID: {message.sid}")
# import pyautogui
# import time
#
# a="Hamiddan attacka tg: abduhamidbotirov"
# b = 5
# print("Boshlandi")
# while b!=0:
#     time.sleep(1)
#     print(b,"s qoldi")
#     b-= 1
#     print("Start")
#     i=0
# ## while True:
# for i in range(1,10):
#     pyautogui.typewrite(a+"\n")
#     print(i,"jo'natildi")
#     i+=1
