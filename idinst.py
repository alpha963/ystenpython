# coding=utf-8
__author__ = 'Aaron'

#烦请绑定如下ID模板
#三星JU6800   ID：010110003520001 ~010110003720000   共20万   panel：173   epg:56
# ID：010110003720001~010110003920000，共20万

sta,en,itv =10110003720001,10110003920000,50000
c=sta-itv
sli,sl2,sl3=[],[],[]
for i in range((en-sta+1)/itv):
	c=c+itv
	sli.append(c)
	sl2.append(sli[i]+itv-1)
	sl3.append(sli[i])
	sl3.append(sl2[i])
print (sl3)

for i in  range((en-sta+1)/itv):
	print(sli[i],sl2[i])
