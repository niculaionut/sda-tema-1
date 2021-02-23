from matplotlib import pyplot as plt

xloc = [2**x for x in range (1,30)]
yloc = [10**x for x in range (1,12)]

plt.figure()
plt.subplot(221)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('random')
plt.plot([2**x for x in range(1, 11)],[1448,325,257,2057,442,651,1111,1938,3879,8041,],'bs',[2**x for x in range(1, 11)],[127,112,199,687,1841,5391,18391,58937,189986,680881,],'g^',[2**x for x in range(1, 11)],[316,429,800,1276,2139,4345,8637,17499,36231,75901,],'r*',[2**x for x in range(1, 11)],[233,95,154,240,636,1555,3233,7302,17061,36888,],'mX',)
plt.legend(['count_sort', 'bubble_sort', 'merge_sort', 'std::sort', ])
plt.subplot(222)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('almost sorted')
plt.plot([2**x for x in range(1, 11)],[236,282,176,279,390,606,1071,2020,3840,8595,],'bs',[2**x for x in range(1, 11)],[61,63,80,35,266,1714,8083,29304,111264,474680,],'g^',[2**x for x in range(1, 11)],[198,239,631,1185,1622,2977,5548,23361,20515,39674,],'r*',[2**x for x in range(1, 11)],[125,180,85,69,351,962,1639,4049,23682,38197,],'mX',)
plt.legend(['count_sort', 'bubble_sort', 'merge_sort', 'std::sort', ])
plt.subplot(223)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('almost sorted (decreasing)')
plt.plot([2**x for x in range(1, 11)],[215,283,277,231,499,637,1015,1907,3802,7312,],'bs',[2**x for x in range(1, 11)],[173,91,148,312,881,2968,11056,53415,178994,630509,],'g^',[2**x for x in range(1, 11)],[188,279,606,821,1668,3172,6463,9781,18977,37219,],'r*',[2**x for x in range(1, 11)],[144,115,157,228,317,1010,1777,7124,9421,18470,],'mX',)
plt.legend(['count_sort', 'bubble_sort', 'merge_sort', 'std::sort', ])
plt.subplot(224)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('sorted')
plt.plot([2**x for x in range(1, 11)],[176,159,162,253,425,571,991,1974,3456,7218,],'bs',[2**x for x in range(1, 11)],[52,50,58,40,46,77,123,244,467,862,],'g^',[2**x for x in range(1, 11)],[170,372,525,861,1884,3359,5450,10611,19681,38842,],'r*',[2**x for x in range(1, 11)],[120,74,37,51,506,708,1606,2378,4729,9212,],'mX',)
plt.legend(['count_sort', 'bubble_sort', 'merge_sort', 'std::sort', ])
plt.show()
