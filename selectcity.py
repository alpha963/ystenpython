#coding=utf-8
import datetime
import  mysql.connector

def openinfo(filenam):
	infoip= open(filenam)  
	try:
		text = infoip.read( )  
	finally:
		infoip.close( ) 
	str1=text.split('\n')
	oip=[]
	for i in range(len(str1)):
		x=str1[i].find('=')
		oip.append(str1[i][x+2:-1])
	return oip

y=openinfo("d:\python\python\info.ini")
news = (datetime.datetime.now()).strftime("%Y%m%d")
print "It's :",news,"\n"

#mac=raw_input("Please input your MCA: ")
city='Kabul'
sqlts="SELECT  * FROM city WHERE name ="+'\''+city+'\''
print sqlts

try:
    conn = mysql.connector.connect(host=y[0], port=y[1], user=y[2], password=y[3], database=y[4]);
    cursor = conn.cursor();
    cursor.execute(sqlts);
    
	# 取回的是列表，列表中包含元组
    lists = cursor.fetchall();
    
	#print list;

    for record in lists:
		for i in range(len(record)):
			print record[i];
		print ""

except mysql.connector.Error as e:
    print ('Error : {}'.format(e));
finally:
    cursor.close;
    conn.close;
    print 'Connection closed in finally';