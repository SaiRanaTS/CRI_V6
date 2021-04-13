import shapely.geometry
import shapely.affinity
import matplotlib.pyplot as plt

from matplotlib import pyplot
from descartes import PolygonPatch


def intersec(OSD1x, OSD2x, OSD3x, OSD4x, OSD5x, TSD1x, TSD2x, TSD3x, TSD4x, TSD5x, OSA, TSA,OSXx,OSYx,TSXx,TSYx):
    OSD1 = OSD1x
    OSD2 = OSD2x
    OSD3 = OSD3x
    OSD4 = OSD4x
    OSD5 = OSD5x

    TSD1 = TSD1x
    TSD2 = TSD2x
    TSD3 = TSD3x
    TSD4 = TSD4x
    TSD5 = TSD5x

    OSX = OSXx * 0.000539957
    OSY = OSYx * 0.000539957

    TSX = TSXx * 0.000539957
    TSY = TSYx * 0.000539957


    class RotatedRect:
        def __init__(self, cx, cy, p1, p2, p3, p4, p5, angle):
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
            # h = self.h
            c = shapely.geometry.Polygon([p1, p2, p3, p4, p5])
            # c = shapely.geometry.Polygon([(d11, d12), (d21, d22), (d31, d32),(d41,d42),(d51,d52)])
            rc = shapely.affinity.rotate(c, self.angle)
            return shapely.affinity.translate(rc, self.cx, self.cy)

        def intersection(self, other):
            return self.get_contour().intersection(other.get_contour())

    # ---------------------- Own Ship Domain 1 ------------------------
    p11 = (-OSD2, -OSD3)
    p12 = (OSD1, -OSD3)
    p13 = (OSD1, OSD4)
    p14 = (0, OSD5)
    p15 = (-OSD2, OSD4)
    a1 = -OSA
    # ---------------------- Domain 2 ------------------------
    p21 = (-TSD2, -TSD3)
    p22 = (TSD1, -TSD3)
    p23 = (TSD1, TSD4)
    p24 = (0, TSD5)
    p25 = (-TSD2, TSD4)
    a2 = -TSA
    r1 = RotatedRect(OSX, OSY, p11, p12, p13, p14, p15, a1)
    r2 = RotatedRect(TSX, TSY, p21, p22, p23, p24, p25, a2)
    # r3 = RotatedRect(16, 17, 20, 10, 0)


    # print('OSD1 :',OSD1)
    # print('OSD2 :', OSD2)
    # print('OSD3 :', OSD3)
    # print('OSD4 :', OSD4)
    # print('OSD5 :', OSD5)
    # print('OS X : ',OSX)
    # print('OS Y : ', OSY)
    # print('OS ange :', OSA)
    # print('--------------------------------')
    # print('TS1D1 :',TSD1)
    # print('TS1D2 :', TSD2)
    # print('TS1D3 :', TSD3)
    # print('TS1D4 :', TSD4)
    # print('TS1D5 :', TSD5)
    # print('TS X : ', TSX)
    # print('TS Y : ', TSY)
    # print('TS ange :',TSA)




    # fig = pyplot.figure(1, figsize=(10, 4))
    # ax = fig.add_subplot(121)
    # ax.set_xlim(0, 5)
    # ax.set_ylim(0, 5)

    # ax.add_patch(PolygonPatch(r1.get_contour(), fc='#990000', alpha=0.7, label='Ship Domain 1'))
    # ax.add_patch(PolygonPatch(r2.get_contour(), fc='#000099', alpha=0.7, label='Ship Domain 2'))
    #ax.add_patch(PolygonPatch(r3.get_contour(), fc='#000099', alpha=0.7))
    inter_dec = 0
    # if r1.intersection(r2):
    #     #print('Inter section of domian')
    #     #ax.add_patch(PolygonPatch(r1.intersection(r2), fc='#009900', alpha=1, label='Intersection'))
    # else:
    #     #print('No intersection')
    #     pass

    inter_area = r1.intersection(r2)
    a = round(inter_area.area,2)

    if a > 1.0:
        a= 0
    else:
        pass

    if a:
        inter_dec = 1
    else:
        inter_dec = 0

    #print('The Intersection area : ', a)
    # plt.ylabel('Longitudinal Distance NM')
    # plt.xlabel('Latitudinal Distance NM')
    #plt.legend(bbox_to_anchor=(1.1, 1.05))
    # pyplot.show()
    result = (inter_dec,a)
    return (result)