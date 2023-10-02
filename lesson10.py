# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
#
# result = {}
# for d in [dic1, dic2, dic3]:
#     result.update(d)
#
# print(result)


# n = 15
# result = {i: i**2 for i in range(1, n + 1)}
# print(result)


# my_dict = {1: 10, 2: 20, 3: 30}
# total = sum(my_dict.values())
# print(total)

# my_dict = {'a': 10, 'b': 30, 'c': 20}
# max_value = max(my_dict.values())
# print(max_value)

# my_dict = {'a': 10, 'b': 5, 'c': 20}
# min_value = min(my_dict.values())
# print(min_value)




# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# result = {}
# for key in set(d1) | set(d2):
#     result[key] = d1.get(key, 0) + d2.get(key, 0)
# print(result)

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# unique_values = {item['V'] for item in data if 'V' in item}
# print(unique_values)
# soooz = str(input("Soz kiriting: "))
# soz = soooz.lower()
# d={i: soz.count(i) for i in soz if i != ' '
#    }
# print(d)
a=int(input("hafta kunini kiriting: "));
h="D" if a==1  else\
   "S" if a==2 else\
      "CH" if a==3 else\
         "P" if a==4 else\
            "J" if a==5 else\
               "SH" if a==6 else\
                  "Y" if a==7 else\
                     "Bunday xafta kuni mavjud emas"
print(h)