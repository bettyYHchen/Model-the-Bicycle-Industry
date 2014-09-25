from Bike_business import *
import random
import copy
bike_list=[]
for j in xrange(6):
	j=j+1
	name='bike%s'%j
	cost=150.00+float(random.choice(range(400)))
	weight=50.00+float(random.choice(range(10)))
	b=Bicycle(name,weight,cost)
	bike_list.append(b)

bike_list[0].cost=101.0

inventory={}
for b in bike_list:
	inventory[b.name]=random.choice(range(30))

margin={}
for b in bike_list:
	margin[b.name]=0.2*b.cost

my_bshop=BikeShops("red_and_blue",inventory,margin)

c1=Customers('bob',200,'True')
c2=Customers('dave',500,'True')
c3=Customers('jesse',1000,'True')
b1={}
b2={}
b3={}
for b in bike_list:
	if b.cost <= 1000:
		b3[b.name]=b.cost
		if b.cost <= 500:
			b2[b.name]=b.cost
			if b.cost <= 200:
				b1[b.name]=b.cost
print c1.name+" can afford"+str(b1)
print c2.name+" can afford"+str(b2)
print c3.name+" can afford"+str(b3)

print "The initial inventory is"+str(my_bshop.inventory)
profit=0
p1=random.choice(list(b1.keys()))
c1.fund=c1.fund-b1[p1]
my_bshop.inventory[p1]=my_bshop.inventory[p1]-1
profit=profit+my_bshop.margin[p1]
print c1.name+" purchases "+p1+".\n"+c1.name+" now have "+str(c1.fund)+" dollars left."

p2=random.choice(list(b2.keys()))
c2.fund=c2.fund-b2[p2]
my_bshop.inventory[p2]=my_bshop.inventory[p2]-1
profit=profit+my_bshop.margin[p2]
print c2.name+" purchases "+p2+".\n"+c2.name+" now have "+str(c2.fund)+" dollars left."

p3=random.choice(list(b3.keys()))
c3.fund=c3.fund-b3[p3]
my_bshop.inventory[p3]=my_bshop.inventory[p3]-1
profit=profit+my_bshop.margin[p3]
print c3.name+" purchases "+p3+".\n"+c3.name+" now have "+str(c3.fund)+" dollars left."


print "Remaining inventory is"+str(my_bshop.inventory)
print "We made "+str(profit)+" dollars profit"




		




	

	
