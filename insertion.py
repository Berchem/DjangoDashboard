import sqlite3

conn = sqlite3.connect("db.sqlite3")

cursor = conn.cursor()

cursor.execute("drop table if exists 'capital_futures_corp'")
cursor.execute("create table capital_futures_corp ("
               "'index' integer NOT NULL PRIMARY KEY AUTOINCREMENT,"
               "'bank' varchar(128) NOT NULL,"
               "'code' char(3) NOT NULL,"
               "'prefix' char(7) NOT NULL)")

data = [
    ("國泰世華銀行忠孝分行", "013", "9369"),
    ("華南銀行敦化分行", "008", "96800"),
    ("台灣中小企銀世貿分行", "050", "9900200"),
    ("安泰商銀台北101分行", "816", "99901"),
    ("渣打國際商業銀行內湖分行", "052", "7180"),
    ("第一商業銀行內科園區分行", "007", "7001581"),
    ("中國信託商銀敦南分行", "822", "98020"),
    ("彰化銀行敦化分行", "009", "5272996"),
    ("台新國際商銀建北分行", "812", "8631000"),
    ("上海商業儲蓄銀行仁愛分行", "011", "2493836"),
]

cursor.executemany("insert into capital_futures_corp (bank, code, prefix) values (?, ?, ?)", data)
conn.commit()
conn.close()
	
