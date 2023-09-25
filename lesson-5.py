# a, b =map(int, input().split())
# for i in range(0, b):
#     print(a)
# a = int(input("son kiriting: "))
# sumr =0;
# for i in range(0)
# step = 0.2
# start = 1
# end = 2.2
#
# for i in range(int(start / step), int(end / step)):
#     weight = i * step
#     price = weight * a
#     print(f"{weight:.1f} kg narxi {price} bo'ladi")
# sum =0
# for i in range(0, a):
    #     print(f"{i} tub son")
    # else:print(f"{i} tub emas")

# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))
#
# while a>b:
#     a-=b
# print(a)

# Butun sonni olish
# n = int(input("Istalgan butun sonni kiriting: "))
# a=1
# s=0
# while a<n:
#     a*=2
#     s+=1
# print(s)

# while a<n:
#     a*=3
# if a==n:
#     print(True)
# else:
#     print(False)
# 3 ning darajasi bo'lsa
# is_three_power = False
# current_power = 1
# while current_power <= n:
#     if current_power == n:
#         is_three_power = True
#     current_power *= 3
#
# if is_three_power:
#     print(f"{n} 3 - ning darajasi")
# else:
#     print(f"{n} 3 - ning darajasi emas")





# SMS yuborish natijasi


# from twilio.rest import Client
# account_sid = 'AC54c3279399e88ec4243861f8f66457ee'
# auth_token = '9f891449f40990ecbdf72c2c3375b5c4'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#   from_='+12517328046',
#   body='cdcc',
#   to='+998937322405'
# )
#
# print(message.sid)


# week =[1,2,3,4,6,5];
# print(len(week))
# newList = list(("nok", "behi"))
# print(newList)
# week[0]=0;
# week[1:3]=["bom"];
# week.append("oke");
# week.insert(2,"Juma")
# week.extend(["bobo"])
# week.remove(2)
# week.pop(2)
# del week
# week.clear()
# week.sort()
# week.reverse()
# week.count(2)
# week.index(2)
# print(week.index(2))





from twilio.rest import Client

# Twilio to'g'ridan-to'g'ri kodlarini qo'yib olishingiz kerak
account_sid = 'AC54c3279399e88ec4243861f8f66457ee'
auth_token = '9f891449f40990ecbdf72c2c3375b5c4'
# #
# # Twilio xizmatiga ulanish
client = Client(account_sid, auth_token)

# Xabar ma'lumotlari
to_phone_number = '+998881745858'  # Qabul qiluvchining raqami
from_phone_number = '+12517328046'   # Sizning Twilio raqamingiz
message_body = 'Salom, bu Twilio orqali yuborilgan xabar.'

# 20 ta SMS yuborish
for _ in range(2):
    message = client.messages.create(
        body=message_body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print(f"Yuborilgan SMS ID: {message.sid}")