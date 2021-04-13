import shapely.geometry
import shapely.affinity
import matplotlib.pyplot as plt


class RotatedRect:
    def __init__(self, cx, cy, p1, p2,p3,p4,p5, angle):
        self.cx = cx
        self.cy = cy
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.angle = angle

    def get_contour(self):
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        p4 = self.p4
        p5 = self.p5
        #h = self.h
        c = shapely.geometry.Polygon([p1, p2, p3,p4,p5])
        #c = shapely.geometry.Polygon([(d11, d12), (d21, d22), (d31, d32),(d41,d42),(d51,d52)])
        rc = shapely.affinity.rotate(c, self.angle)
        return shapely.affinity.translate(rc, self.cx, self.cy)

    def intersection(self, other):
        return self.get_contour().intersection(other.get_contour())

OSD1 = 0.142
OSD2 = 0.106
OSD3 = 0.11
OSD4 = 0.157
OSD5 = 0.274
OSX = -0.163
OSY = 0.589

TSD1 = 0.187
TSD2 = 0.14
TSD3 = 0.134
TSD4 = 0.19
TSD5 = 0.333
TSX = -0.478
TSY = 0.272



#---------------------- Domain 1 ------------------------
p11 = (-OSD2, -OSD3)
p12 = (OSD1, -OSD3)
p13 = (OSD1, OSD4)
p14 = (0, OSD5)
p15 = (-OSD2, OSD4)
a1 = -353
#---------------------- Domain 2 ------------------------
p21 = (-TSD2, -TSD3)
p22 = (TSD1, -TSD3)
p23 = (TSD1, TSD4)
p24 = (0, TSD5)
p25 = (-TSD2, TSD4)
a2 = -246
r1 = RotatedRect(OSX, OSY, p11,p12,p13,p14,p15, a1)
r2 = RotatedRect(TSX, TSY, p21,p22,p23,p24,p25, a2)
#r3 = RotatedRect(16, 17, 20, 10, 0)

from matplotlib import pyplot
from descartes import PolygonPatch

fig = pyplot.figure(1, figsize=(10, 4))
ax = fig.add_subplot(121)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

ax.add_patch(PolygonPatch(r1.get_contour(), fc='#990000', alpha=0.7,label='OWN SHIP'))
ax.add_patch(PolygonPatch(r2.get_contour(), fc='#000099', alpha=0.7,label='TS 1'))
#ax.add_patch(PolygonPatch(r3.get_contour(), fc='#000099', alpha=0.7))
if r1.intersection(r2):

    ax.add_patch(PolygonPatch(r1.intersection(r2), fc='#009900', alpha=1,label='Intersection'))
else:
    pass


inter_area = r1.intersection(r2)
a = inter_area.area

print('The Intersection area : ',a)
plt.ylabel('Longitudinal Distance NM')
plt.xlabel('Latitudinal Distance NM')
plt.legend(bbox_to_anchor=(1.1, 1.05))
pyplot.show()