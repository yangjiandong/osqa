#-*- coding: utf-8 -*-#

#用下面的python脚本将oracle导出到txt，在pgsql中，\copy 表名 from 'lx'  with DELIMITER ';'120万数据，导出20分钟，导入1小时。
#import cx_Oracle
#db = cx_Oracle.connect(username/passwd@host:port/sevicename)
#db.commit()
#db.close()

import os
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.US7ASCII'
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#gb2312
import cx_Oracle
conn = cx_Oracle.Connection('aa/admin@aa')
cursor = conn.cursor()
cursor.execute('select * from sb_yzcwsbqc')
#cursor.execute('select * from cs2')
lx = file('lx', 'a')
i = 0
while 1:
        rows = cursor.fetchmany(1000)
        if not rows:
                break
        for b in rows:
                #bb = ';'
                cc = []
                for a in b:
                   if a:
                      cc.append(str(a))      
                   else:
                      cc.append('\N')      
                bb = ';'.join(cc)
                lx.write(bb)    

                
                lx.write('\n')
        lx.flush()
        i = i + 1000
        if i % 10000 == 0:
          print i
lx.close()
conn.close()
#如果有汉字，需要注意了，需要转码成utf8。如果有\等,也需要特殊处理转码。
