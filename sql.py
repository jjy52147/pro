import pymysql
from flask import Flask
import string

#連線到資料庫檔案

"""app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')

@app.route('/gets/',methods=['POST'])"""





conn = pymysql.connect(
    host = '34.142.180.39',
    port = 13306,
    user = 'root',
    password = 'oh_my_ody!',
    db = 'data_center',
    charset = 'utf8'
)

cur = conn.cursor()

cur.execute("SELECT COUNT(channel_id) FROM channel WHERE channel_id IS NOT NULL")

    #r = cur.fetchone()
    #一筆資料

    #r = cur.fetchmany(size)

r = cur.fetchall()
    #全部資料

conn.commit()

print(r)

cur.close()
conn.close()


str_r = ''.join(str(r))

punctuation_string = string.punctuation

for i in punctuation_string:
    str_r = str_r.replace(i,'')

print(str_r)




app = Flask(__name__)
@app.route("/")


def search():
    return (str_r)
if __name__ == "__main__":
    app.run()