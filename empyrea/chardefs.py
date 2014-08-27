# Soft-numbered character locations for use with f. DoChar

rboulder1 = [26,32,255]
rboulder2 = [27,32,255]
rboulder3 = [26,33,255]
rboulder4 = [27,33,255]
rboulderchars = [rboulder1, rboulder2, rboulder3, rboulder4]

rweeds1 = [26,34,255]
rweeds2 = [27,34,255]
rweeds3 = [26,35,255]
rweeds4 = [27,35,255]
rweedschars = [rweeds1, rweeds2, rweeds3, rweeds4]

bankweed1 = [26,36,255]
bankweed2 = [27,36,255]
bankweed3 = [26,37,255]
bankweed4 = [27,37,255]
bankweedchars = [bankweed1, bankweed2, bankweed3, bankweed4]

thickgrass1 = [26,38,255]
thickgrass2 = [27,38,255]
thickgrass3 = [26,39,255]
thickgrass4 = [27,39,255]
thickgrass5 = [26,40,255]
thickgrass6 = [27,40,255]
thickgrass7 = [26,41,255]
thickgrass8 = [27,41,255]
thickgrasschars = [thickgrass1, thickgrass2, thickgrass3, thickgrass4, \
            thickgrass5, thickgrass6, thickgrass7, thickgrass8]

count = 0
tallgrasschars = []
for x in range(28,32):
    for y in range(36,40):
        count += 1
        globals()['tallgrass%s' % count] = [x,y,255]

tallgrasschars = [tallgrass1, tallgrass2, tallgrass3, tallgrass4, \
            tallgrass5, tallgrass6, tallgrass7, tallgrass8, \
            tallgrass9, tallgrass10, tallgrass11, tallgrass12, \
            tallgrass13, tallgrass14, tallgrass15, tallgrass16]

count = 0
midgrasschars = []
for x in range(28,32):
    for y in range(40,44):
        count += 1
        globals()['midgrass%s' % count] = [x,y,255]

midgrasschars = [midgrass1, midgrass2, midgrass3, midgrass4, \
          midgrass5, midgrass6, midgrass7, midgrass8, \
          midgrass9, midgrass10, midgrass11, midgrass12, \
          midgrass13, midgrass14, midgrass15, midgrass16]

leafchar1 = [19,6,255]
leafchar2 = [20,6,255]
leafchar3 = [19,7,255]
leafchar4 = [20,7,255]
leafchars = [leafchar1, leafchar2, leafchar3, leafchar4]

lshrubul = [0,7,255]
lshrubur = [1,7,255]
lshrubll = [2,7,255]
lshrublr = [3,7,255]

aconu = [19,5,161]
acond = [20,5,163]
aconl = [21,5,162]
aconr = [22,5,164]
dconu = [19,6,161]
dcond = [20,6,163]
dconl = [19,7,162]
dconr = [20,7,164]

bordercorner = [28,2,255]

border3waye = [26,4,255]

bordercapn = [26,3,255]
bordercape = [27,3,255]
bordercaps = [28,3,255]
bordercapw = [29,3,255]

borderhchar1 = [25,2,255]
borderhchar2 = [26,2,255]
borderhchar3 = [27,2,255]
borderhchars = [borderhchar1, borderhchar2, borderhchar3]

bordervchar1 = [29,2,255]
bordervchar2 = [30,2,255]
bordervchar3 = [31,2,255]
bordervchars = [bordervchar1, bordervchar2, bordervchar3]

twdownborder = [20,2,255]
twupborder = [18,2,255]

vnborder = [14,1,255]
hnborder = [15,1,255]
fwnborder = [16,1,255]

unchecked = [10,2,255]
checked = [11,2,255]

uschar = [4,2,255]
dschar = [5,2,255]
lschar = [6,2,255]
rschar = [7,2,255]

cavechar = [7,5,255]

swampchar1 = [23,5,255]
swampchar2 = [24,5,255]
swampchar3 = [25,5,255]
swampchar4 = [26,5,255]

mountain1 = [11,6,255]
mountain2 = [12,6,255]
mountain3 = [11,7,255]
mountain4 = [12,7,255]
mountain5 = [13,6,255]
mountain6 = [14,6,255]
mountain7 = [13,7,255]
mountain8 = [14,7,255]

water1 = [24,6,255]
water2 = [25,6,255]
water3 = [24,7,255]
water4 = [25,7,255]

beach1 = [28,4,255]
beach2 = [29,4,255]
beach3 = [28,5,255]
beach4 = [29,5 ,255]
beachchars = [beach1, beach2, beach3, beach4]

shore1 = [30,4,255]
shore2 = [31,4,255]
shore3 = [30,5,255]
shore4 = [31,5,255]
shorechars = [shore1, shore2, shore3, shore4]

snow1 = [26,6,255]
snow2 = [27,6,255]
snow3 = [26,7,255]
snow4 = [27,7,255]

glacier1 = [28,6,255]
glacier2 = [29,6,255]
glacier3 = [28,7,255]
glacier4 = [29,7,255]

desert1 = [15,6,255]
desert2 = [16,6,255]
desert3 = [15,7,255]
desert4 = [16,7,255]

dirt1 = [21,6,255]
dirt2 = [22,6,255]
dirt3 = [21,7,255]
dirt4 = [22,7,255]

dirtleaf1 = [30,6,255]
dirtleaf2 = [31,6,255]
dirtleaf3 = [30,7,255]
dirtleaf4 = [31,7,255]
dirtleafchars = [dirtleaf1, dirtleaf2, dirtleaf3, dirtleaf4]

blankchar = [5,7,255]

rivsources1 = [27,9,255]
rivsourcew1 = [28,9,255]
rivsourcen1 = [29,9,255]
rivsourcee1 = [30,9,255]
rivsources2 = [27,10,255]
rivsourcew2 = [28,10,255]
rivsourcen2 = [29,10,255]
rivsourcee2 = [30,10,255]

lrivsources1 = [27,11,255]
lrivsourcew1 = [28,11,255]
lrivsourcen1 = [29,11,255]
lrivsourcee1 = [30,11,255]

scrollul = [21,9,255]
scrollum = [22,9,255]
scrollur = [23,9,255]
scrolll = [21,10,255]
scrollr = [23,10,255]
scrollbl = [21,11,255]
scrollbm = [22,11,255]
scrollbr = [23,11,255]

scroll2ul = [24,9,255]
scroll2um = [25,9,255]
scroll2ur = [26,9,255]
scroll2l = [24,10,255]
scroll2r = [26,10,255]
scroll2bl = [24,11,255]
scroll2bm = [25,11,255]
scroll2br = [26,11,255]

citychar = [12,5,255]
villagechar = [11,5,255]
castlechar = [10,5,255]
humanchar = chr(145)

grasschar1 = [17,6,254]
grasschar2 = [18,6,254]
grasschar3 = [17,7,254]
grasschar4 = [18,7,254]

leafground1 = [19,6,254]
leafground2 = [20,6,254]
leafground3 = [19,7,254]
leafground4 = [20,7,254]

trunkchar1 = [17,122,255]
trunkchar2 = [18,122,255]
trunkchar3 = [17,123,255]
trunkchar4 = [18,123,255]
trunkchars = [trunkchar1, trunkchar2, trunkchar3, trunkchar4]

rootcharng = [19,122,255]
rootcharwg = [20,122,255]
rootchareg = [19,123,255]
rootcharsg = [20,123,255]
rootcharnl = [21,122,255]
rootcharwl = [22,122,255]
rootcharel = [21,123,255]
rootcharsl = [22,123,255]
rootcharntg = [23,122,255]
rootcharwtg = [24,122,255]
rootcharetg = [23,123,255]
rootcharstg = [24,123,255]
rootcharnd = [25,122,255]
rootcharwd = [26,122,255]
rootchared = [25,123,255]
rootcharsd = [26,123,255]

ballchar = [23,6,255]

waterchars = [water1,water2,water3,water4]
grasschars = [grasschar1, grasschar2, grasschar3, grasschar2, grasschar3, \
            grasschar2, grasschar3, grasschar2, grasschar3, grasschar4]
leafgroundchars = [leafground1, leafground2, leafground3, leafground4]
swampchars = [swampchar1, swampchar2, swampchar3, swampchar4]
desertchars = [desert1, desert2, desert3, desert4]
dirtchars = [desert1, desert2, desert3, desert4, dirt1, dirt2, dirt3, dirt4]
mountaincharshigh = [mountain1, mountain2, mountain3, mountain4]
mountaincharslow = [mountain5, mountain6, mountain7, mountain8]
snowchars = [snow1, snow2, snow3, snow4]
glacierchars = [glacier1, glacier2, glacier3, glacier4]

vectorchar1 = [21,16,255]
vectorchar2 = [21,17,255]
vectorchar3 = [21,18,255]
vectorchar4 = [21,19,255]
vectorchar5 = [21,20,255]
vectorchar6 = [21,21,255]
vectorchar7 = [21,22,255]
vectorchar8 = [21,23,255]
vectorchar9 = [21,24,255]
vectorchar10 = [21,25,255]
vectorchar11 = [21,26,255]
vectorchar12 = [22,16,255]
vectorchars = [vectorchar1, vectorchar2, vectorchar3, vectorchar4, vectorchar5, \
            vectorchar6, vectorchar7, vectorchar8, vectorchar9, vectorchar10, \
            vectorchar11, vectorchar12]
