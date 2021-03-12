from matplotlib import pyplot as plt

xloc = [2**x for x in range (1,30)]
yloc = [10**x for x in range (1,12)]

plt.figure()
plt.suptitle('unsigned values')
plt.subplot(231)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('random')
plt.plot([2**x for x in range(1, 28)],[59,66,78,98,141,226,367,683,1336,2671,6698,21620,56055,125687,269869,563137,1169563,2796932,6118936,11316448,31039316,77724763,171765344,362919284,748377738,1514858214,3055532159,],'bs',[2**x for x in range(1, 26)],[43,52,70,113,212,430,906,1878,10567,35300,90131,207931,441588,968504,2016315,4318402,9078465,19347733,38799105,81532041,168720340,363462212,725290362,1522276878,3163469666,],'g^',[2**x for x in range(1, 17)],[19,21,44,117,418,1664,8067,40353,157737,599462,2318769,11037921,58700019,273661956,1190484845,5028089534,],'rP',[2**x for x in range(1, 26)],[42,101,222,491,1088,2266,4718,10296,25387,67193,152117,330950,680962,1436238,3068181,6428472,13701501,28466068,59708979,123729865,258232998,542657038,1127823349,2373091398,4976608012,],'mD',[2**x for x in range(1, 26)],[3485,3285,3451,3891,4339,6064,9385,16737,31374,64651,135300,279882,585126,1241638,2544471,5433857,11071024,23304374,48121465,100976256,206815799,431262600,893012289,1872530269,3887753691,],'co',[2**x for x in range(1, 26)],[22,28,50,100,206,410,922,2067,6723,27370,71570,171508,382638,828200,1734746,3628839,7688128,16233626,33803150,71039544,148697169,307872926,638031173,1334366210,2813926444,],'yX',[2**x for x in range(1, 26)],[22,25,39,69,134,364,743,1747,3909,21445,69159,170785,385640,825258,1749131,3682420,7785758,16326373,34644231,71296470,148439891,310898576,643330971,1350136327,2825210316,],'kh',)
plt.legend(['count_sort', 'radix_sort', 'bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(232)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('almost sorted')
plt.plot([2**x for x in range(1, 29)],[65,70,78,104,147,227,385,703,1364,2824,6767,21406,54501,123039,257025,525614,1055964,2258839,4425672,9308276,19459420,40622756,80279984,158712450,316501121,641852761,1273077687,2659098947,],'bs',[2**x for x in range(1, 27)],[53,61,88,137,247,461,978,1901,4335,15113,43253,102369,216579,447633,964196,1926804,3804718,8031819,16741965,33982186,67080185,140992932,283011133,601078434,1178023619,2513624812,],'g^',[2**x for x in range(1, 18)],[18,20,42,111,386,1143,5828,21474,81313,319278,1251153,5016603,20051812,80176393,319089306,1348676180,5750890779,],'rP',[2**x for x in range(1, 27)],[44,110,241,518,1077,2266,4636,9568,19608,40209,82283,169710,351523,715047,1432984,2939787,5915814,12223663,26586084,55566974,113565857,237004203,484355087,997173514,2074626359,4347055921,],'mD',[2**x for x in range(1, 27)],[3312,3449,3611,3851,4532,5615,8461,14179,26004,50815,102197,203904,419241,855637,1725375,3600960,7412513,15459336,31155889,64950463,133140117,281994354,559721917,1135949116,2343260623,4834251043,],'co',[2**x for x in range(1, 26)],[22,35,55,109,280,950,1305,3788,9169,32375,61181,146542,356146,875150,1615958,3514961,9033512,18193807,36794690,86463416,171719091,385274593,734135200,1634796907,3291828049,],'yX',[2**x for x in range(1, 27)],[22,25,31,47,116,262,1128,3604,4010,9643,33460,86658,194634,428941,954743,2049532,3415329,14179959,16323792,32522805,70014640,178588961,313276445,609621661,1449066590,4030910413,],'kh',)
plt.legend(['count_sort', 'radix_sort', 'bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(233)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('almost sorted (decreasing)')
plt.plot([2**x for x in range(1, 29)],[65,69,79,105,151,238,434,748,1448,2793,7074,21844,55379,124405,257301,519714,1046789,2239851,4633573,9141095,19100336,39960671,80169852,158906319,318973573,636896526,1277161101,2678576993,],'bs',[2**x for x in range(1, 27)],[49,51,76,119,248,490,1021,2132,5080,16092,45865,105392,224555,490634,976464,1968249,4202886,8644084,18085685,36116323,74353376,157225884,320797185,682565117,1410802134,2913981617,],'g^',[2**x for x in range(1, 18)],[19,24,46,130,482,2241,8390,32539,124084,477336,1890587,7420089,30093036,121758335,485491354,2021638872,8238110192,],'rP',[2**x for x in range(1, 27)],[46,113,247,544,1123,2238,4695,9791,19716,40210,82580,170919,354967,726428,1471853,2983914,5963607,12544891,26531842,55867278,116085192,241744749,501677723,1031769966,2139371175,4488556791,],'mD',[2**x for x in range(1, 27)],[3370,3566,3672,4027,4657,6052,8895,15072,27626,54000,108455,221323,454772,922737,1891858,3817268,7924327,15827218,33245189,67922998,140383027,285963113,596864441,1209496557,2445032694,5205002845,],'co',[2**x for x in range(1, 27)],[23,36,61,98,261,781,2269,5100,9374,20404,44774,120288,271462,542064,1090436,2656024,5065654,11719499,24466540,49214044,103392977,225850906,451907361,921942749,1947031298,3952118190,],'yX',[2**x for x in range(1, 27)],[22,30,46,89,159,311,754,1635,4186,10667,48661,74797,190200,523775,804253,1788449,4210511,7493099,15207896,58877938,87281529,252056948,301258443,728802591,1436906117,2643295182,],'kh',)
plt.legend(['count_sort', 'radix_sort', 'bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(234)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('sorted')
plt.plot([2**x for x in range(1, 29)],[66,70,86,111,166,264,452,827,1579,3201,6360,12488,25242,49761,100766,211682,419037,1088827,2627261,5430036,10638517,21317878,34194634,65903106,131024745,265575317,529453202,1160866758,],'bs',[2**x for x in range(1, 28)],[50,62,88,142,257,517,1124,2376,5060,10688,22244,47033,96811,197153,417244,848963,1769705,3620928,7483123,15603581,34137841,69107100,143291726,292614325,607941772,1256665086,2569981318,],'g^',[2**x for x in range(1, 29)],[19,20,23,28,44,63,99,177,325,619,1210,2410,4787,9551,19065,37759,75352,171809,339404,684260,1359202,2645282,5144921,10278441,20748579,41291824,83651188,169144394,],'rP',[2**x for x in range(1, 27)],[45,113,245,521,1061,2185,4476,9058,18287,37386,76051,152004,309525,627251,1283777,2583729,5242753,10894853,23484230,49614154,99263503,208658191,425643970,874431303,1812771775,3772491705,],'mD',[2**x for x in range(1, 27)],[3447,3705,3735,3992,4625,5845,8163,13376,24387,46140,92801,189817,386024,791232,1628124,3318524,6716935,13871960,28326157,56693593,120233930,239446415,503434708,1014082595,2066276433,4253930710,],'co',[2**x for x in range(1, 16)],[24,36,72,191,667,2298,8305,31180,120986,475926,1894070,7530406,29817982,114932397,454447002,],'yX',[2**x for x in range(1, 28)],[22,26,29,37,92,236,601,1491,3474,7851,17367,37913,82149,173516,376198,817227,1814016,3889022,8020836,17231850,35007857,74238574,157090927,327661749,690414607,1446437114,3023255683,],'kh',)
plt.legend(['count_sort', 'radix_sort', 'bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(235)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('sorted (decreasing)')
plt.plot([2**x for x in range(1, 29)],[64,72,81,110,164,268,452,829,1571,3088,5773,11601,23311,46842,94515,185980,381334,966330,1705049,3683253,7980888,17353964,34354874,65350598,131729028,264432063,529604820,1159548393,],'bs',[2**x for x in range(1, 28)],[48,58,76,119,209,416,929,1974,4333,8731,18213,39640,84990,174504,373037,750665,1586506,3181102,6698247,14183730,30139270,65871509,138192036,288945086,613257659,1273229782,2646328935,],'g^',[2**x for x in range(1, 18)],[20,25,45,133,579,2175,8197,31150,121988,440590,1868769,7586168,30607833,121583025,484229032,1928156205,7393220097,],'rP',[2**x for x in range(1, 27)],[45,111,245,530,1097,2265,4629,9405,19168,35663,80029,163260,334990,675552,1371161,2802054,5654261,12226712,25370229,53022850,109526033,228121122,469247861,968438956,2011724345,4186115847,],'mD',[2**x for x in range(1, 27)],[3409,3542,3735,4046,4660,6164,8921,14817,26882,49214,103091,208848,423218,866651,1737593,3581415,7143554,15150858,30915117,62477250,129256297,258416446,532479646,1085817466,2216805232,4589054112,],'co',[2**x for x in range(1, 16)],[22,34,69,170,575,1926,6507,23808,90071,335818,1353463,5419379,21434748,83360867,329721964,],'yX',[2**x for x in range(1, 29)],[23,33,53,98,96,216,514,1214,2712,5894,13159,29095,61992,130916,273027,592895,1285811,2790290,5892644,12447061,26334969,53435605,112544005,236289257,493370219,1029223518,2145603705,4471852028,],'kh',)
plt.legend(['count_sort', 'radix_sort', 'bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(236)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. elements')
plt.ylabel('nanoseconds')
plt.title('filled with one element')
plt.plot([2**x for x in range(1, 29)],[64,72,78,96,129,222,399,761,1500,2899,5780,11454,23383,46143,93715,187788,390010,890467,1755861,3760055,8258164,16941109,35646525,68932147,134808514,271192811,541116033,1180426255,],'bs',[2**x for x in range(1, 28)],[55,59,73,98,213,366,696,1430,3011,6522,14087,30687,71118,150649,319402,683547,1444988,2993908,6531442,15195885,33237250,69691192,145868725,302459353,630668358,1309006001,2716253650,],'g^',[2**x for x in range(1, 29)],[19,21,23,28,44,63,100,177,329,629,1214,2408,4814,9582,18996,37852,75926,174620,342856,672060,1334533,2684236,5183752,10307915,20765511,41736005,84410296,169589268,],'rP',[2**x for x in range(1, 27)],[45,110,242,510,1067,2191,4490,9194,18521,38677,78746,161325,324178,664240,1374632,2798096,5707665,11785191,25401462,53145009,110196429,230512644,472341919,969744055,2026006606,4190193217,],'mD',[2**x for x in range(1, 16)],[3346,3498,3700,4023,4947,8107,17467,51293,177924,669064,2609940,10156665,40062136,158630796,635691525,],'co',[2**x for x in range(1, 16)],[23,36,72,190,675,2332,8446,32006,125545,483151,1877898,7438924,29128880,114043957,451919942,],'yX',[2**x for x in range(1, 29)],[22,25,29,37,74,190,404,902,2023,4478,9850,20845,45453,96900,210430,443278,993995,2179806,4583590,9564787,20172014,42460118,90068863,187574578,395953708,828098733,1744919033,3652527801,],'kh',)
plt.legend(['count_sort', 'radix_sort', 'bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.show()
