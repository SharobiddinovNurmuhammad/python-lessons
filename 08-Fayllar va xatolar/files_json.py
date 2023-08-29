import json

# dumps 
# x = 10 
# x_json = json.dumps(x)

# ism = 'Nurmuhammad'
# ism_json = json.dumps(ism)

# sonlar = ['1', '3', '5', '7']
# sonlar_json = json.dumps(sonlar)

# bemor = {
#   "ism": "Nurmuhammad Sharobiddinov",
#   "yosh": 20,
#   "oila": True,
#   "farzandlar": None,
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# bemor_json = json.dumps(bemor, indent=4)

# with open('bemor.json', 'w') as f:
#     json.dump(bemor, f)

# bemor = json.loads(bemor_json)
# print(type(bemor))

# with open('bemor.json') as f:
#     kasal = json.load(f)

# print(type(kasal))


#-------------------------------------------------------

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json = json.dumps(data)

# print(data_json)

#--------------------------------------------------------

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
ism = talaba['ism']
familya = talaba['familiya']

#----------------------------------------------------------

with open('ism.json', 'w') as f:
    json.dump(ism, f)

with open('familiya.json', 'w') as f:
    json.dump(familya, f)

#--------------------------------------------------------

with open('students.json') as f:
    students = json.load(f)

for item in data['student']:
    print(f"{item['name']} {item['lastname']} {item['year']}-kurs, {item['faculty']} talabasi")

#---------------------------------------------------------

with open('api-result.json') as f:
    result = json.load(f)

title = result['query']['pages']['13801']['title']
extract = result['query']['pages']['13801']['extract'].replace('\n', '')
print(title)
print(extract)

#--------------------------------------------------------------