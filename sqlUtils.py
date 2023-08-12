import csv, sqlite3

conn = sqlite3.connect('data/collective.db')
cur = conn.cursor()
#cur.execute("CREATE TABLE aiModels (model, requestPerMin, tokenPerMin);")


with open('models.csv', 'r') as fin:
    dr = csv.DictReader(fin, delimiter=';')
    toDB = [(i['model'], i['rmp'], i['tpm']) for i in dr]

cur.executemany("INSERT INTO aiModels (model, requestPerMin, tokenPerMin) VALUES (?,?,?);", toDB)
conn.commit()
conn.close()
