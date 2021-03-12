from matplotlib import pyplot as plt

xloc = [2**x for x in range (1,30)]
yloc = [10**x for x in range (1,12)]

plt.figure()
plt.suptitle('std::string objects')
plt.subplot(231)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. bytes in input (x 4)')
plt.ylabel('nanoseconds')
plt.title('random')
plt.plot([2**x for x in range(1, 28)],[21,54,104,168,388,478,1229,2082,4444,10293,20556,41323,89161,157358,315165,669060,1472086,3188930,6987520,14326762,35424902,76493840,159299389,340118278,723133771,1576535079,3469508812,],'bs',[2**x for x in range(1, 29)],[56,149,287,401,735,852,1358,2001,3053,4606,7431,11442,18394,28929,46813,72109,115888,162880,247767,367690,569535,848738,1484703,2142935,3302943,4830126,7719322,11601172,],'g^',[2**x for x in range(1, 29)],[3215,3399,3270,3424,3644,4115,5460,5885,7593,9176,12185,16782,24339,33672,48214,75775,114892,175590,308387,531141,1004328,1925194,3227989,5625023,10024158,18569341,34565048,63927415,],'rP',[2**x for x in range(1, 29)],[34,86,123,159,316,722,976,1481,2096,3294,5515,8461,14627,22647,35872,55000,90671,140073,248918,502811,1022981,1873729,3040316,5406363,9522554,17655169,33323712,62128892,],'mD',[2**x for x in range(1, 29)],[30,68,110,239,486,530,621,986,1619,2538,3955,6354,9589,14967,24017,40843,63576,103415,152708,246619,379574,562213,985090,1545210,2327195,3554009,5605352,9781177,],'co',)
plt.legend(['bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(232)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. bytes in input (x 4)')
plt.ylabel('nanoseconds')
plt.title('almost sorted')
plt.plot([2**x for x in range(1, 29)],[24,29,57,156,253,653,571,1121,3227,3880,13251,26802,50766,100016,201911,420788,837128,1838180,3857775,8767142,18930763,43949474,88311609,184017955,386656064,825811247,1993595420,5493087991,],'bs',[2**x for x in range(1, 29)],[61,160,286,450,707,866,1251,1980,3133,4402,6757,9653,14885,21699,32307,47005,68894,96683,137080,208573,326767,545549,944263,1326894,2086919,2875467,4465498,6521724,],'g^',[2**x for x in range(1, 29)],[3055,3357,3356,3829,4010,4196,5033,5497,6889,8796,11297,15038,20619,29527,43497,64343,101644,141506,247968,520436,1030239,1584508,2850530,5087738,9324340,16954088,32609509,69884094,],'rP',[2**x for x in range(1, 29)],[35,90,134,270,379,873,1619,2468,3709,8051,5513,23953,22677,37438,44345,82212,116542,202347,351610,861349,1313774,2632994,4011778,7311852,13360623,22870136,42543175,101710384,],'mD',[2**x for x in range(1, 29)],[34,59,91,156,212,282,460,580,1282,1995,3727,12297,9965,25464,19931,41902,73219,98301,113692,170538,295910,411640,764814,1480300,1756438,2578898,4134533,22626274,],'co',)
plt.legend(['bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(233)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. bytes in input (x 4)')
plt.ylabel('nanoseconds')
plt.title('almost sorted (decreasing)')
plt.plot([2**x for x in range(1, 29)],[23,52,129,242,599,799,1497,2875,5762,10799,21077,42109,84603,165981,333260,670581,1345009,2989145,5877128,13614517,29026868,68314639,134592070,279236298,564323043,1176264253,2467624994,6189301640,],'bs',[2**x for x in range(1, 29)],[64,180,308,510,753,932,1456,2101,3509,4902,7789,10750,15846,23826,35030,50661,74327,102482,149369,227432,339054,517143,991266,1471636,2150321,3059540,4756142,6967335,],'g^',[2**x for x in range(1, 29)],[3297,3536,3787,3817,4247,4534,5127,6631,8232,9288,13135,16234,22355,31127,47248,70413,100299,157426,248736,494341,886610,1850602,2815582,5103614,9070077,16902318,32503368,59363015,],'rP',[2**x for x in range(1, 29)],[37,96,178,217,615,810,1258,2260,4172,6010,8082,12140,31021,42786,51880,74688,133074,168382,333441,638154,1206257,2202198,3803894,6722367,12819121,22872626,42572634,83032847,],'mD',[2**x for x in range(1, 29)],[35,69,131,202,423,430,626,721,1843,2303,3584,6836,8178,12285,18776,29101,43741,97948,153168,174660,239832,392429,733017,1160256,1805014,2647235,4249163,6768069,],'co',)
plt.legend(['bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(234)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. bytes in input (x 4)')
plt.ylabel('nanoseconds')
plt.title('sorted')
plt.plot([2**x for x in range(1, 29)],[23,31,41,50,69,90,114,133,171,230,298,410,565,942,1274,2166,3074,4408,6134,21511,54667,86846,168367,239761,359069,492333,712263,921815,],'bs',[2**x for x in range(1, 29)],[64,173,302,438,734,884,1304,2087,3208,4602,7037,9952,14908,21832,32506,47243,69194,96778,143573,204592,303933,467555,933992,1279399,1994742,2781266,4314106,6365876,],'g^',[2**x for x in range(1, 29)],[3214,3587,3470,3911,4190,4790,5261,5762,7431,9231,11976,16237,21919,29994,46172,63047,105065,155347,258664,491624,979282,1757086,2797218,5072443,9138834,16596600,31211385,58161472,],'rP',[2**x for x in range(1, 28)],[38,99,187,306,623,1357,2294,4145,7811,15308,27172,53232,112685,216810,413225,873728,1751604,3528612,7715743,14647469,32800969,73262075,149258211,292302404,607700989,1251981054,2653932699,],'mD',[2**x for x in range(1, 29)],[34,63,88,129,186,200,447,524,1247,1661,2881,3942,7919,9314,16628,20858,34200,45825,70112,98393,176607,249127,572025,829383,1328444,1987163,3120972,5080843,],'co',)
plt.legend(['bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(235)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. bytes in input (x 4)')
plt.ylabel('nanoseconds')
plt.title('sorted (decreasing)')
plt.plot([2**x for x in range(1, 29)],[25,61,129,249,587,814,1479,2676,5492,10384,20351,42972,83571,163219,323016,680199,1370021,3189051,6253086,14061893,28620329,66888099,133153965,275271607,552940222,1145886813,2402169591,6021313401,],'bs',[2**x for x in range(1, 29)],[63,170,307,442,743,891,1348,2064,3229,4688,7401,10033,15971,22539,35237,48910,70949,97834,144519,227718,336765,496502,918426,1286640,1972274,2808643,4355640,6088805,],'g^',[2**x for x in range(1, 29)],[3171,3466,3987,3596,3961,4956,4987,5753,7254,9725,11666,17067,22124,30910,44455,66077,95639,151201,235083,530246,862810,1789010,2740764,4965198,9008870,16613755,31434339,58876423,],'rP',[2**x for x in range(1, 29)],[37,94,173,284,620,1232,2095,3662,6863,12363,23996,46394,95905,182346,356620,712465,1490662,3171711,6434828,14297864,28774566,65322106,131687963,270119350,542992873,1113761933,2379386838,6126056417,],'mD',[2**x for x in range(1, 29)],[36,75,129,203,415,361,550,642,1106,1454,2557,3507,5744,7741,12649,17376,27895,36403,58016,87531,167038,221086,531944,778758,1240425,1874566,2953177,4935088,],'co',)
plt.legend(['bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.subplot(236)
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.gca().set_xticks(xloc)
plt.gca().set_yticks(yloc)
plt.grid(True)
plt.xlabel('no. bytes in input (x 4)')
plt.ylabel('nanoseconds')
plt.title('filled with one element')
plt.plot([2**x for x in range(1, 29)],[24,34,46,54,82,117,153,210,280,380,709,1042,1491,2119,4750,9403,16436,39383,76380,230923,539496,1367591,2872856,5588500,9488604,18790547,37608798,74766345,],'bs',[2**x for x in range(1, 29)],[64,174,316,453,813,1010,1545,2345,3734,5422,9535,13471,19489,27468,52275,80543,134860,245830,429621,862132,2199421,5018689,8862079,19554504,43361315,92953406,203924517,428987103,],'g^',[2**x for x in range(1, 24)],[3190,3579,3846,3807,4676,5601,7030,10576,15080,24253,50898,104889,194239,370871,1114504,2803664,7356565,18051079,51638199,140504480,506837398,1942484126,6301662976,],'rP',[2**x for x in range(1, 24)],[38,100,198,325,697,1457,2584,4689,9524,17519,41029,82112,173192,358965,1008759,2481572,6673598,18270439,47032589,131820350,447037715,1733627325,5764244238,],'mD',[2**x for x in range(1, 29)],[36,68,101,142,212,255,490,630,1204,1578,3849,5673,9938,14115,35214,57596,122418,246001,514166,1186654,3373988,7588000,18391785,36019415,81102941,172771941,390226308,810329186,],'co',)
plt.legend(['bubble_sort', 'merge_sort', 'quick_sort_rand', 'quick_sort_last', 'std::sort', ])
plt.show()
