district_coords = {
    # 'aceh selatan': (2.8543, 97.6994),
    # 'aceh tenggara': (3.107, 97.9674),
    # 'aceh timur': (4.5523, 97.7031),
    # 'aceh tengah': (4.7437, 96.5192),
    # 'aceh barat': (4.3787, 96.1826),
    # 'aceh besar': (5.5203, 95.4671),
    # 'pidie': (5.2141, 95.9017),
    # 'aceh utara': (5.1159, 97.0116),
    # 'simeulue': (2.6154, 95.9241),
    # 'aceh singkil': (3.1187, 97.3112),
    # 'bireuen': (5.224, 96.8509),
    # 'aceh barat daya': (3.6103, 96.9562),
    # 'gayo lues': (4.1003, 97.2116),
    # 'aceh jaya': (4.7151, 95.9574),
    # 'nagan raya': (4.4538, 96.523),
    # 'aceh tamiang': (4.335, 97.8096),
    # 'bener meriah': (4.8193, 96.7416),
    # 'pidie jaya': (5.241, 96.2078),
    # 'banda aceh': (5.5556, 95.3561),
    # 'sabang': (5.8375, 95.3715),
    # 'lhokseumawe': (5.2038, 97.0423),
    # 'langsa': (4.4585, 97.9057),
    # 'subulussalam': (2.589, 97.8954),
    # 'tapanuli tengah': (1.7528, 98.8562),
    # 'tapanuli utara': (2.3404, 98.9366),
    # 'tapanuli selatan': (1.2939, 99.0177),
    # 'nias': (1.0742, 97.6879),
    # 'langkat': (4.1675, 98.1184),
    # 'karo': (3.1626, 98.3422),
    # 'deli serdang': (3.6078, 98.8614),
    # 'simalungun': (2.9066, 98.5696),
    # 'asahan': (2.5852, 99.6049),
    # 'labuhanbatu': (2.5138, 100.0916),
    # 'dairi': (2.7325, 98.3555),
    # 'toba samosir': (2.4642, 99.1607),
    # 'mandailing natal': (0.9152, 99.475),
    # 'nias selatan': (0.921, 97.8229),
    # 'pakpak bharat': (2.5596, 98.3668),
    # 'humbang hasundutan': (2.2467, 98.5057),
    # 'samosir': (2.4679, 98.7171),
    # 'serdang bedagai': (3.2993, 98.9379),
    # 'batu bara': (3.0829, 99.5809),
    # 'padang lawas utara': (1.5911, 100.201),
    # 'padang lawas': (1.3406, 99.6644),
    # 'labuhanbatu selatan': (1.9527, 99.993),
    # 'labuhanbatu utara': (2.525, 99.8381),
    # 'nias utara': (1.314, 97.3671),
    # 'nias barat': (1.0392, 97.5798),
    # 'medan': (3.5386, 98.6337),
    # 'pematangsiantar': (2.9346, 99.0628),
    # 'sibolga': (1.7314, 98.7895),
    # 'tanjung balai': (2.9463, 99.8238),
    # 'binjai': (3.6004, 98.4926),
    # 'tebing tinggi': (3.3296, 99.1647),
    # 'padang sidimpuan': (1.4587, 99.2543),
    # 'gunungsitoli': (1.2078, 97.5875),
    # 'pesisir selatan': (-2.4489, 101.026),
    # 'solok': (-0.757, 100.6693),
    # 'sijunjung': (-0.7241, 100.8295),
    # 'tanah datar': (-0.6338, 100.4368),
    # 'padang pariaman': (-0.6339, 100.2252),
    # 'agam': (-0.432, 100.2428),
    # 'lima puluh kota': (-0.2427, 100.5624),
    # 'pasaman': (0.4835, 100.0595),
    # 'kepulauan mentawai': (3.1187, 97.3112),
    # 'dharmasraya': (-1.2614, 101.7016),
    # 'solok selatan': (-1.3623, 101.4771),
    # 'pasaman barat': (0.0309, 99.6775),
    # 'padang': (3.1187, 97.3112),
    # 'sawahlunto': (-0.6371, 100.7812),
    # 'padang panjang': (-0.4655, 100.4029),
    # 'bukittinggi': (-0.3092, 100.3962),
    # 'payakumbuh': (-0.1925, 100.642),
    # 'pariaman': (-0.6057, 100.1622),
    # 'kampar': (0.2635, 100.6204),
    # 'indragiri hulu': (-0.5291, 101.9287),
    # 'bengkalis': (1.4109, 101.4036),
    # 'indragiri hilir': (-0.6268, 103.1732),
    # 'pelalawan': (0.1674, 102.1372),
    # 'rokan hulu': (0.4853, 100.5017),
    # 'rokan hilir': (2.1753, 100.6718),
    # 'siak': (1.045, 102.1067),
    # 'kuantan singingi': (-0.8418, 101.7094),
    # 'kepulauan meranti': (1.1463, 102.7997),
    # 'pekanbaru': (0.5649, 101.4403),
    # 'dumai': (1.648, 101.4396),
    # 'kerinci': (-1.9823, 101.3489),
    # 'merangin': (-2.3497, 102.2624),
    # 'sarolangun': (-2.3387, 102.4387),
    # 'batanghari': (-1.649, 103.1533),
    # 'muaro jambi': (-1.3723, 103.8463),
    # 'tanjung jabung barat': (-0.8089, 103.1171),
    # 'tanjung jabung timur': (-1.2297, 104.1426),
    # 'bungo': (-1.3716, 101.9011),
    # 'tebo': (-1.6621, 102.5488),
    # 'jambi': (-1.6405, 103.6347),
    # 'sungai penuh': (-2.068, 101.3903),
    # 'ogan komering ulu': (-3.8068, 104.5351),
    # 'ogan komering ilir': (-3.5862, 105.2764),
    # 'muara enim': (-3.8712, 103.9729),
    # 'lahat': (-3.9496, 103.2312),
    # 'musi rawas': (-3.1834, 103.2131),
    # 'musi banyuasin': (-2.8653, 104.1322),
    # 'banyuasin': (-2.9757, 104.9681),
    # 'ogan komering ulu timur': (-4.1775, 104.5018),
    # 'ogan komering ulu selatan': (-4.5997, 104.033),
    # 'ogan ilir': (-3.4012, 104.5629),
    # 'empat lawang': (-3.7863, 102.9062),
    # 'penukal abab lematang ilir': (-3.327, 104.0506),
    # 'musi rawas utara': (-2.8475, 102.4355),
    # 'palembang': (-2.9642, 104.7741),
    # 'pagar alam': (-4.1508, 103.2243),
    # 'lubuklinggau': (-3.2802, 102.86),
    # 'prabumulih': (-3.5163, 104.2086),
    # 'bengkulu selatan': (-4.4643, 102.9227),
    # 'rejang lebong': (-3.3552, 102.4418),
    # 'bengkulu utara': (-3.1781, 101.6527),
    # 'kaur': (-4.3848, 103.35),
    # 'seluma': (-4.1915, 102.6008),
    # 'mukomuko': (-2.8728, 101.4439),
    # 'lebong': (-2.7634, 101.9919),
    # 'kepahiang': (-3.5623, 102.7752),
    # 'bengkulu tengah': (-3.596, 102.3422),
    # 'bengkulu': (-3.8209, 102.3036),
    # 'lampung selatan': (-5.5671, 105.5919),
    # 'lampung tengah': (-4.8259, 105.635),
    # 'lampung utara': (-4.6774, 104.6655),
    # 'lampung barat': (-5.2557, 104.3109),
    # 'tulang bawang': (-4.3688, 105.3092),
    # 'tanggamus': (-5.6304, 104.9866),
    # 'lampung timur': (-5.3345, 105.6055),
    # 'way kanan': (-4.3251, 104.5581),
    # 'pesawaran': (3.1187, 97.3112),
    # 'pringsewu': (3.1187, 97.3112),
    # 'mesuji': (-3.9304, 105.3531),
    # 'tulang bawang barat': (-4.4189, 105.1616),
    # 'pesisir barat': (-5.5983, 104.3451),
    # 'bandar lampung': (-5.449, 105.2693),
    # 'metro': (-5.1529, 105.3037),
    # 'bangka': (-1.9851, 105.9818),
    # 'belitung': (-2.8594, 107.8227),
    # 'bangka selatan': (-2.8732, 107.0154),
    # 'bangka tengah': (-2.6073, 106.7018),
    # 'bangka barat': (-1.562, 105.5764),
    # 'belitung timur': (-3.2, 107.9764),
    # 'pangkalpinang': (-2.1386, 106.1246),
    # 'bintan': (3.1187, 97.3112),
    # 'karimun': (0.8281, 103.4785),
    # 'natuna': (2.9871, 107.7925),
    # 'lingga': (-0.3804, 104.2204),
    # 'kepulauan anambas': (3.2719, 106.2636),
    # 'batam': (1.0516, 103.9602),
    # 'tanjungpinang': (0.9217, 104.4617),
    # 'kepulauan seribu': (3.1187, 97.3112),
    # 'jakarta pusat': (-6.1798, 106.8494),
    # 'jakarta utara': (-6.1553, 106.8966),
    # 'jakarta barat': (-6.1845, 106.7375),
    # 'jakarta selatan': (-6.2354, 106.7634),
    # 'jakarta timur': (-6.3087, 106.8952),
    # 'bogor': (-6.5469, 106.7753),
    # 'sukabumi': (-6.9476, 106.9399),
    # 'cianjur': (-7.2243, 107.2142),
    # 'bandung': (-6.9008, 107.6845),
    # 'garut': (-7.2236, 107.9941),
    # 'tasikmalaya': (-7.339, 108.2903),
    # 'ciamis': (-7.4906, 108.4954),
    # 'kuningan': (-6.8976, 108.5073),
    # 'cirebon': (-6.7405, 108.5329),
    # 'majalengka': (-7.0525, 108.2209),
    # 'sumedang': (-6.8836, 108.1859),
    # 'indramayu': (-6.3164, 108.0207),
    # 'subang': (-6.3223, 107.9237),
    # 'purwakarta': (-6.6603, 107.5535),
    # 'karawang': (-6.1582, 107.4338),
    # 'bekasi': (-6.3269, 106.9311),
    # 'bandung barat': (-6.8995, 107.3729),
    # 'pangandaran': (-7.5809, 108.5844),
    # 'depok': (-6.4306, 106.7443),
    # 'cimahi': (-6.854, 107.54),
    # 'banjar': (-3.4028, 114.6223),
    # 'cilacap': (-7.7037, 108.8565),
    # 'banyumas': (-7.4043, 109.2225),
    # 'purbalingga': (-7.3341, 109.4312),
    # 'banjarnegara': (-7.4277, 109.6561),
    # 'kebumen': (-7.5189, 109.6743),
    # 'purworejo': (-7.5382, 110.0382),
    # 'wonosobo': (-7.4817, 109.9078),
    # 'magelang': (-7.4767, 110.2255),
    # 'boyolali': (-7.2146, 110.8374),
    # 'klaten': (-7.7133, 110.5773),
    # 'sukoharjo': (-7.5481, 110.7219),
    # 'wonogiri': (-7.7553, 111.2363),
    # 'karanganyar': (-8.2501, 115.5242),
    # 'sragen': (-7.2656, 111.1227),
    # 'grobogan': (-7.0881, 110.5687),
    # 'blora': (-6.8767, 111.2577),
    # 'rembang': (-6.6531, 111.4737),
    # 'pati': (-6.6594, 111.1091),
    # 'kudus': (-6.6625, 110.901),
    # 'jepara': (-6.4746, 110.9463),
    # 'demak': (-6.9851, 110.7135),
    # 'semarang': (-6.9555, 110.3107),
    # 'temanggung': (-7.23, 110.1444),
    # 'kendal': (3.1187, 97.3112),
    # 'batang': (-6.991, 109.9468),
    # 'pekalongan': (-6.9215, 109.6874),
    # 'pemalang': (-7.0637, 109.2707),
    # 'tegal': (-6.8648, 109.1114),
    # 'brebes': (-6.9862, 108.8051),
    # 'surakarta': (-7.5385, 110.8052),
    # 'salatiga': (-7.3329, 110.5025),
    # 'kulon progo': (-7.6576, 110.2436),
    # 'bantul': (-7.8098, 110.2796),
    # 'gunungkidul': (-7.9924, 110.3792),
    # 'sleman': (-7.6177, 110.4374),
    # 'yogyakarta': (-7.829, 110.4028),
    # 'pacitan': (-8.2645, 111.3893),
    # 'ponorogo': (-7.8486, 111.7469),
    # 'trenggalek': (-8.1282, 111.6462),
    # 'tulungagung': (-8.1727, 111.8969),
    # 'blitar': (-6.9107, 115.2472),
    # 'kediri': (-6.9067, 113.7964),
    # 'malang': (-7.1759, 113.5505),
    # 'lumajang': (3.1187, 97.3112),
    # 'jember': (-8.0892, 113.9607),
    # 'banyuwangi': (-8.279, 114.3586),
    # 'bondowoso': (-8.0211, 113.8716),
    # 'situbondo': (-7.7072, 113.8381),
    # 'probolinggo': (-6.9011, 112.9433),
    # 'pasuruan': (-7.6353, 112.9227),
    # 'sidoarjo': (-7.3484, 112.7187),
    # 'mojokerto': (-7.4653, 112.4357),
    # 'jombang': (3.1187, 97.3112),
    # 'nganjuk': (-7.5116, 112.135),
    # 'madiun': (-7.4815, 112.4102),
    # 'magetan': (-7.6464, 111.2873),
    # 'ngawi': (-7.3769, 111.506),
    # 'bojonegoro': (-7.1388, 111.703),
    # 'tuban': (-7.0256, 112.0511),
    # 'lamongan': (-7.7859, 111.9988),
    # 'gresik': (-7.4541, 112.4529),
    # 'bangkalan': (-6.9918, 112.5631),
    # 'sampang': (-7.0284, 112.8331),
    # 'pamekasan': (-6.9045, 113.721),
    # 'sumenep': (-7.0834, 112.808),
    # 'surabaya': (-7.1386, 114.5239),
    # 'batu': (-7.0585, 113.0973),
    # 'pandeglang': (-6.5593, 105.8007),
    # 'lebak': (-6.7001, 106.2389),
    # 'tangerang': (-6.2406, 106.7432),
    # 'serang': (-6.0833, 106.1267),
    # 'cilegon': (-6.0164, 106.035),
    # 'tangerang selatan': (-6.3527, 106.7116),
    # 'jembrana': (-8.3482, 114.66),
    # 'tabanan': (-8.331, 115.0019),
    # 'badung': (-8.6167, 115.1706),
    # 'gianyar': (-8.4281, 115.2692),
    # 'klungkung': (-8.5104, 115.4577),
    # 'bangli': (-8.2037, 115.4106),
    # 'buleleng': (-8.1712, 115.4353),
    # 'denpasar': (-8.6111, 115.2256),
    # 'lombok barat': (-8.7179, 116.1681),
    # 'lombok tengah': (-8.5115, 116.3195),
    # 'lombok timur': (3.1187, 97.3112),
    # 'sumbawa': (-8.7535, 117.4687),
    # 'dompu': (-8.611, 118.4784),
    # 'bima': (-8.4485, 118.7578),
    # 'sumbawa barat': (-8.921, 116.7512),
    # 'lombok utara': (-8.4348, 116.0517),
    # 'mataram': (-8.5991, 116.1541),
    # 'kupang': (-10.1573, 123.6014),
    # 'timor tengah selatan': (-9.641, 124.0788),
    # 'timor tengah utara': (-9.2512, 124.7519),
    # 'belu': (-9.2945, 124.9942),
    # 'alor': (-8.4229, 123.9803),
    # 'flores timur': (-8.4716, 123.0434),
    # 'sikka': (-8.6908, 122.4468),
    # 'ende': (-8.6485, 121.8934),
    # 'ngada': (-8.9096, 120.9748),
    # 'manggarai': (-8.7728, 120.2933),
    # 'sumba timur': (-10.1473, 120.5012),
    # 'sumba barat': (-9.7417, 119.3142),
    # 'lembata': (-8.2562, 123.5101),
    # 'rote ndao': (3.1187, 97.3112),
    # 'manggarai barat': (-8.624, 120.0284),
    # 'nagekeo': (-8.6501, 121.2458),
    # 'sumba tengah': (-9.6777, 119.6483),
    # 'sumba barat daya': (-9.6991, 119.0814),
    # 'manggarai timur': (-8.6439, 120.8213),
    # 'sabu raijua': (-10.6096, 121.5717),
    # 'malaka': (-9.4947, 124.887),
    # 'sambas': (1.0084, 109.1742),
    # 'mempawah': (0.3182, 108.9763),
    # 'sanggau': (1.1161, 110.1587),
    # 'ketapang': (-1.8995, 110.3762),
    # 'sintang': (0.1525, 111.4882),
    # 'kapuas hulu': (0.946, 111.5681),
    # 'bengkayang': (1.0268, 109.833),
    # 'landak': (0.4488, 109.4993),
    # 'sekadau': (0.1997, 111.2151),
    # 'melawi': (-0.8937, 111.3005),
    # 'kayong utara': (3.1187, 97.3112),
    # 'kubu raya': (-0.2066, 109.2079),
    # 'pontianak': (-0.0792, 109.3498),
    # 'singkawang': (0.8182, 108.9748),
    # 'kotawaringin barat': (-2.3614, 111.8771),
    # 'kotawaringin timur': (-1.6653, 112.6309),
    # 'kapuas': (-3.049, 114.3381),
    # 'barito selatan': (-1.69, 114.7802),
    # 'barito utara': (-0.7659, 114.8017),
    # 'katingan': (-1.0615, 112.1727),
    # 'seruyan': (-1.4279, 111.7625),
    # 'sukamara': (-2.2187, 111.1418),
    # 'lamandau': (-1.472, 111.164),
    # 'gunung mas': (-1.0593, 113.479),
    # 'pulang pisau': (-3.366, 113.6969),
    # 'murung raya': (0.0758, 114.1976),
    # 'barito timur': (-1.992, 115.1367),
    # 'palangkaraya': (-1.6869, 113.6119),
    # 'tanah laut': (-3.5467, 114.5985),
    # 'kotabaru': (-3.9756, 116.119),
    # 'barito kuala': (-3.2144, 114.7705),
    # 'tapin': (-3.1695, 115.2138),
    # 'hulu sungai selatan': (-2.7256, 115.0051),
    # 'hulu sungai tengah': (-2.5133, 115.5024),
    # 'hulu sungai utara': (-2.4542, 115.16),
    # 'tabalong': (-1.7613, 115.3476),
    # 'tanah bumbu': (-3.5501, 115.7278),
    # 'balangan': (-2.4916, 115.7453),
    # 'banjarmasin': (-3.3297, 114.5975),
    # 'banjarbaru': (-3.4703, 114.7234),
    # 'paser': (-2.3266, 115.8788),
    # 'kutai kartanegara': (-0.2333, 116.3257),
    # 'berau': (1.4412, 117.9066),
    # 'kutai barat': (-0.2798, 115.7416),
    # 'kutai timur': (0.4909, 116.7294),
    # 'penajam paser utara': (-1.0718, 116.6958),
    # 'mahakam ulu': (0.7427, 114.5165),
    # 'balikpapan': (-1.2578, 116.8613),
    # 'samarinda': (-0.5283, 117.1421),
    # 'bontang': (0.1364, 117.4529),
    # 'bulungan': (3.1187, 97.3112),
    # 'malinau': (2.9966, 116.0483),
    # 'nunukan': (4.1297, 115.8429),
    # 'tana tidung': (3.6466, 116.8365),
    # 'tarakan': (3.3727, 117.5618),
    # 'bolaang mongondow': (0.5465, 124.0604),
    # 'minahasa': (1.1514, 124.7885),
    # 'kepulauan sangihe': (3.1187, 97.3112),
    # 'kepulauan talaud': (4.4209, 126.7099),
    # 'minahasa selatan': (1.2549, 124.6649),
    # 'minahasa utara': (1.6618, 124.9939),
    # 'minahasa tenggara': (1.0804, 124.8629),
    # 'bolaang mongondow utara': (0.8801, 123.1932),
    # 'kep. siau tagulandang biaro': (2.3373, 125.4562),
    # 'bolaang mongondow timur': (0.7955, 124.5347),
    # 'bolaang mongondow selatan': (0.3663, 123.7032),
    # 'manado': (1.4876, 124.8569),
    # 'bitung': (1.4636, 125.2458),
    # 'tomohon': (1.3529, 124.8813),
    # 'kotamobagu': (0.7367, 124.2845),
    # 'banggai': (-1.0588, 122.6783),
    # 'poso': (-1.6867, 120.7077),
    # 'donggala': (3.1187, 97.3112),
    # 'tolitoli': (1.3133, 120.84),
    # 'buol': (3.1187, 97.3112),
    # 'morowali': (-2.6401, 121.958),
    # 'banggai kepulauan': (-1.31, 123.4517),
    # 'parigi moutong': (0.3052, 120.2178),
    # 'tojo una-una': (3.1187, 97.3112),
    # 'sigi': (-0.9206, 119.7356),
    # 'banggai laut': (-1.6582, 123.4896),
    # 'morowali utara': (-2.0349, 121.2941),
    # 'palu': (-0.8872, 119.8876),
    # 'kepulauan selayar': (-5.9771, 120.5364),
    # 'bulukumba': (-5.4508, 120.2025),
    # 'bantaeng': (-5.4886, 119.9484),
    # 'jeneponto': (-5.566, 119.8895),
    # 'takalar': (-5.3492, 119.3984),
    # 'gowa': (-5.3034, 119.3973),
    # 'sinjai': (3.1187, 97.3112),
    # 'bone': (-4.8584, 120.1266),
    # 'maros': (-5.0259, 119.5726),
    # 'pangkajene dan kepulauan': (3.1187, 97.3112),
    # 'barru': (-4.3495, 119.6611),
    # 'soppeng': (-4.3918, 120.0125),
    # 'wajo': (-3.8004, 120.3407),
    # 'sidenreng rappang': (-3.6062, 120.1479),
    # 'pinrang': (-3.6261, 119.7075),
    # 'enrekang': (-3.2609, 119.8219),
    # 'luwu': (-3.1536, 120.0191),
    # 'tana toraja': (-2.9607, 119.7455),
    # 'luwu utara': (-2.6336, 120.5486),
    # 'luwu timur': (-2.7539, 121.3139),
    # 'toraja utara': (-2.9049, 119.7245),
    # 'makassar': (-5.1435, 119.4975),
    # 'pare pare': (-4.0311, 119.6393),
    # 'palopo': (-2.9335, 120.1778),
    # 'kolaka': (-3.7181, 121.2649),
    'konawe': (-4.0757, 122.0293),
    'muna': (-4.5975, 122.7198),
    'buton': (-5.5627, 122.8961),
    'konawe selatan': (-4.0109, 122.3605),
    'bombana': (-4.6462, 121.8653),
    'wakatobi': (-5.9689, 124.0119),
    'kolaka utara': (-2.8635, 121.1851),
    'konawe utara': (-3.2563, 122.1969),
    'buton utara': (-4.5029, 122.9634),
    'kolaka timur': (-4.214, 121.9936),
    'konawe kepulauan': (-4.123, 122.973),
    'muna barat': (-4.6761, 122.6214),
    'buton tengah': (-5.3645, 122.6194),
    'buton selatan': (3.1187, 97.3112),
    'kendari': (-3.9998, 122.5187),
    'bau bau': (-5.4592, 122.6031),
    'gorontalo': (0.5296, 123.0552),
    'boalemo': (0.4964, 122.6266),
    'bone bolango': (0.5103, 123.4256),
    'pahuwato': (0.6374, 121.2705),
    'gorontalo utara': (3.1187, 97.3112),
    'mamuju utara': (-1.4322, 119.3026),
    'mamuju': (3.1187, 97.3112),
    'mamasa': (-3.0977, 119.085),
    'polewali mandar': (-3.2571, 119.1537),
    'majene': (-3.4884, 118.9427),
    'mamuju tengah': (-1.7899, 119.515),
    'maluku tengah': (-3.5075, 128.7191),
    'maluku tenggara': (-5.9092, 132.7664),
    'maluku tenggara barat': (-6.8906, 131.4841),
    'buru': (-3.1545, 126.921),
    'seram bagian timur': (-3.3163, 130.7858),
    'seram bagian barat': (3.1187, 97.3112),
    'kepulauan aru': (3.1187, 97.3112),
    'maluku barat daya': (-7.9627, 127.1888),
    'buru selatan': (-3.4763, 126.5299),
    'ambon': (-3.711, 128.2606),
    'tual': (3.1187, 97.3112),
    'halmahera barat': (1.2444, 127.5205),
    'halmahera tengah': (0.3381, 128.6819),
    'halmahera utara': (1.114, 127.6268),
    'halmahera selatan': (3.1187, 97.3112),
    'kepulauan sula': (-2.0414, 125.8748),
    'halmahera timur': (0.6993, 128.2257),
    'pulau morotai': (2.2594, 128.506),
    'pulau taliabu': (-1.891, 124.8507),
    'ternate': (0.8843, 127.3192),
    'tidore kepulauan': (0.6961, 127.4133),
    'merauke': (-7.3924, 139.2215),
    'jayawijaya': (-4.0975, 138.961),
    'jayapura': (-2.6173, 140.6319),
    'nabire': (-3.4737, 135.8154),
    'kepulauan yapen': (-1.8731, 136.2893),
    'biak numfor': (-0.7552, 135.8228),
    'puncak jaya': (-3.17, 137.9851),
    'paniai': (-3.8365, 136.4822),
    'mimika': (-4.184, 137.9507),
    'sarmi': (-2.384, 139.8811),
    'keerom': (-3.7517, 140.6807),
    'pegunungan bintang': (-4.1339, 139.9898),
    'yahukimo': (-4.7006, 139.3285),
    'tolikara': (-3.5959, 138.5404),
    'waropen': (-2.3929, 136.6434),
    'boven digoel': (-5.509, 140.4075),
    'mappi': (-5.5412, 139.3178),
    'asmat': (-5.9153, 138.3396),
    'supiori': (3.1187, 97.3112),
    'mamberamo raya': (-1.8234, 137.5353),
    'mamberamo tengah': (-3.8465, 138.9865),
    'yalimo': (-3.9672, 139.5012),
    'lanny jaya': (-3.8566, 138.1046),
    'nduga': (-4.646, 138.6737),
    'puncak': (-3.4873, 137.3688),
    'dogiyai': (-3.9333, 136.0298),
    'intan jaya': (-3.6788, 137.1052),
    'deiyai': (-4.242, 136.244),
    'sorong': (-0.825, 131.2346),
    'manokwari': (-0.7946, 133.5733),
    'fakfak': (-2.8641, 133.0118),
    'sorong selatan': (-1.8033, 132.3196),
    'raja ampat': (-0.8701, 130.7545),
    'teluk bintuni': (-1.3712, 132.8961),
    'teluk wondama': (-1.8687, 134.1011),
    'kaimana': (-4.1676, 134.8913),
    'tambrauw': (-0.7372, 131.8192),
    'maybrat': (-1.1305, 132.3501),
    'manokwari selatan': (-1.7203, 133.9694),
    'pegunungan arfak': (-1.2122, 134.0098)
}


duri_kepa_coords={
  "kebon jeruk": (106.7671, -6.1921),
  "sukabumi utara": (106.7800, -6.1950),
  "sukabumi selatan": (106.7800, -6.2100),
  "kelapa dua": (106.7950, -6.1850),
  "duri kepa": (106.7749, -6.1692),
  "kedoya utara": (106.7550, -6.1750),
  "kedoya selatan": (106.7550, -6.1900)
}


# Get All Kelurahan
expected_output = {
  "kelurahan": [
      {
        "id": 4195,
        "province": "kebon jeruk",
        "infrastructure": "Placeholder",
        "renewable_energy": "Placeholder",
        "poverty_index": 7.08,
        "ndvi": 0.23,
        "precipitation": 8.1,
        "sentinel": -1.473,
        "no2": 126.88,
        "co": 33.397,
        "so2": 132.154,
        "o3": 0.117,
        "pm25": 52.2,
        "ai_investment_score": 0.0,
        "period": "2025-05-31",
        "level": "kelurahan",
        "aqi": 96,
        "riskLevel": "high",

        # GEN AI RESPONSE
        "diseaseData": [
            {
                "name": "DBD",
                "percentage": 0.5, 
                "riskLevel": "high",
                "explanationWhyItsFeasible": "DBD is a disease that is caused by a virus.",
                "prevention": "Avoid mosquito bites, use mosquito repellent, and get vaccinated against dengue fever."
            },
            {
                "name": "ISPA",
                "percentage": 0.3,
                "riskLevel": "medium",
                "explanation": "ISPA is a disease that is caused by a virus."
            }
        ]
    }
  ]
}

# Get Detail Kelurahan
expected_output2 = {
  "kelurahan": [
    {
        "name": "Duri Kepa",
        "eviData": 0.5,
        "ndviData": 0.3,
        "nightLightData": 0.2,
        "dayLightData": 0.1,
        "precipitationData": 0.4,
        "soilMoistureData": 0.3,
        "temperatureData": 0.2,
        "riskLevel": "high", 
        # GEN AI RESPONSE
        "diseaseData": [
            {
                "name": "DBD",
                "percentage": 0.5, 
                "riskLevel": "high",
                "explanationWhyItsFeasible": "DBD is a disease that is caused by a virus.",
                "prevention": "Avoid mosquito bites, use mosquito repellent, and get vaccinated against dengue fever."
            },
            {
                "name": "ISPA",
                "percentage": 0.3,
                "riskLevel": "medium",
                "explanation": "ISPA is a disease that is caused by a virus."
            }
        ]
    }
  ]
}
