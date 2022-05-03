import os
import pymysql

#target_dir = '/home/'

con = pymysql.connect(host='127.0.0.1', user='user', password='user', db='ttl_db', charset='utf8')
cur = con.cursor()

# sql_type = "select distinct title_id from homepage_contents where talker_identifier not in ('n', 'f1', 'm1', 'm2')"
# cur.execute(sql_type)

# rows_type = cur.fetchall()
too_many_character_tale_list = []
# for row in rows_type:
#     too_many_character_tale_list.append(row[0])

too_many_character_tale_list.append(17)
print(str(too_many_character_tale_list) + ' will not present')

sql = 'select *  from homepage_contents'
cur.execute(sql)
f = open('/home/workspace/folktale_full_data', 'w')
voice_map = {}
voice_map['n'] = 10
voice_map['m1'] = 0
voice_map['m2'] = 1
voice_map['m3'] = 2
voice_map['m4'] = 3
voice_map['m5'] = 4
voice_map['m6'] = 5
voice_map['f1'] = 6
voice_map['f2'] = 7
voice_map['f3'] = 8
voice_map['f4'] = 9
voice_map['f5'] = 10

rows = cur.fetchall()
for row in rows : # row[2] : contents / row[3] : talker_identifier / row[4] : title_id / row[1] : line_index
    if row[4] not in too_many_character_tale_list :
        f.write(str(row[2]) + '\t' + str(voice_map[row[3]]) + '\t' + str(row[4]) + '\t' + str(row[1]) + '\n')

con.close()
