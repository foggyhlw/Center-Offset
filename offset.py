from math import sin, tan, cos, pi
# b 挂点处塔身宽度
# d 横担宽度
# L1 长横担长度，从塔身中央算起
# L2 短横担长度，从塔身中央算起
#theta 线路转角
b = 1198
d = 1000
L1 = 4200
L2 = 3500
theta = 34.78/180*pi
# theta = 73.47/180*pi
#PointA = ((L1-L2)/2+b/2)*cos(theta/2)-b/2*sin(theta/2)
PointA = b/2*(1-tan(theta/2))*cos(theta/2)
#PointB = (L1+L2)/2*cos(theta/2)-d/2*sin(theta/2)
PointB = L2*cos(theta/2)-d/2*sin(theta/2)
#PointC = -(L1+L2)/2*cos(theta/2)-d/2*sin(theta/2)
PointC = -L1*cos(theta/2)-d/2*sin(theta/2)


Pa = 0 
Pb = 3500
Pc = -3500

S = 1000
print(PointA, PointB, PointC)

def cal_leastsq(sq1, sq2):
	sum_square=0
	for i,j in zip(sq1, sq2):
		sum_square+=(i-j)**2
	return sum_square

def tower_offset(sq, s, theta):
	sq=[i+s*cos(theta/2) for i in sq]
	return sq

tower1=[PointA, PointB, PointC]
tower2=[Pa, Pb, Pc]
print(cal_leastsq(tower1, tower2))
# tower1=tower_offset(tower1, 61, theta)
# print(cal_leastsq(tower1, tower2))

sum_sq=100000000
offset_dist=0
for i in range(-1000,1000, 1):
	t=tower1.copy()
	t=tower_offset(t, i, theta)
	temp_sq=cal_leastsq(t,tower2)
	if (sum_sq > temp_sq):
		sum_sq = temp_sq
		offset_dist = i

print(offset_dist, sum_sq)