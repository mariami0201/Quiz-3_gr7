import requests
import json
import sqlite3

conn = sqlite3.connect('pets.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS pets (facts TEXT,breed TEXT, cntr TEXT); ''')

url1 = "https://catfact.ninja/breeds?limit=1"
url = "https://catfact.ninja/fact?max_length=140"
num = int(input("random fact-1 ,breeds-2: "))
if num == 1:
    r = requests.get(url)
    fact = r.json()["fact"]
    cur.execute('INSERT INTO pets (facts) VALUES (?)', (fact,))
    conn.commit() #1 - ის შემთხვევაში pets ცხრილში შეგვაქვს მხოლოდ fact.
elif num == 2:
    r = requests.get(url1)
    for i in range(15):
        breed = r.json()["data"][i]["breed"]
        country = r.json()["data"][i]["country"]
        cur.execute('INSERT INTO pets (breed,cntr) VALUES (?,?)', (breed, country))
        conn.commit() #2-ის შემთხვევაში კი ცხრილში მხოლოდ ჯიში და ქვეყანა შეგვაქვს.

print(r)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json())
res = json.loads(r.text)
print(type(res))
print(json.dumps(res, indent=4))
with open('pets.json', 'w') as f:
    json.dump(res, f, indent=4)

    