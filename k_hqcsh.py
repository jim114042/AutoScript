# -*- coding: utf-8 -*-
"""
先运行脚本，有问题再到群里问
默认不推送通知，如需推送，下载仓库的sendNotify.py到脚本所在文件夹并设置好相关参数
"""
import sys
version = sys.version.split(" ")
ver = version[0].split(".")
if int(ver[1]) != 10:
    print(f"\n【python版本为{version[0]},请使用py3.10运行此脚本】\n")
    exit()
q1 = {'id': '647894196522340352', 'jf': 188, 'money': 1.08}  # 188积分 1.08元
q2 = {'id': '622187839353806848', 'jf': 288, 'money': 1.88}  # 288积分 1.88元
q3 = {'id': '622187928306601984', 'jf': 588, 'money': 3.88}  # 588积分 3.88元
q4 = {'id': '622188100122075136', 'jf': 888, 'money': 5.88}  # 888积分 5.88元
"""抢红包设置"""
q = q1
""""""
"""通知开关"""
notify = 1
"""1为开，0为关，打开后需复制青龙的notify.py到同级文件夹"""
try:import marshal, lzma, gzip, bz2, binascii, zlib;exec(marshal.loads(gzip.decompress(marshal.loads(bz2.decompress(marshal.loads(lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x10O\xf3K\x10\x00\x00BZh91AY&SY\xc4\xf3~\xfe\x00\x06\xd8\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\t_g\xd7o\x1f{\xeb\x0e\xe9[\xe7I\x0e\xbb\xef\xb7t\xf7\xdfh\xf7\xca\xee\x9f7\xd7\xde\xf3\xef|\x85=\x92z\xa6\xc6\xa9\xb2\x9bI\xbd\'\xaayO#\xd2\x9e\x9e\x934OMH\xfdO!\xaax@\x13\xcc\xa3\xd0\x86\x93h\xc9\xeaz\xa7\x80\xd4\xd3\xd5\x1e\xa6\xd3\x14\xf12i?Jz\'\xe8L\x8fM54\x9e4\xd4\xc2\x1a\x98O\x11\x8afCj\x9f\xaaz\x9b\xd0\x9e\xa4\xf6\x13L\x15<i=2dj=OLS\xd4:\x9abf\xa7\xa9\x88\xcd#L&#\xd0@\xd3\xd4\xd3\x19OHi\x83D\xc44\xd3#\xd4z\x8d\x1a\r\xa0\x8cj\x18\x99=OBh\xc8h\xf56\xa1\x8cHh\xf53S&\xc4\xd1\r\xa113\xd2M\x94\xf14jc\xd5\x1e\xa6G\xa1\xa9\x90\xf5\r4\xd3M\x92\x18\x88G\xa9\xe9\xa9\xa3OI\xb2\x9a0\x9a=\'\xa10\x9eA\x18\xd0\x11\xead\xd3e\x0c\x86\x11\xa6\x9ah\xd1\x83 F\x134\x86\x9e\x9a\x9bF\x994\xd1\x84\x04\xda\x013P\xc3S\x02\x1ah\xc1=\r\x13\t\xa34\x9a4\xc24\x1ah\xf56\x88\xf4h\x84&\xd2a=F\x83L\x83M\x1adf\xa6\xd2=M\x94\xf5214\xf4\x99=\'\x8a`i\x1e\x9ad\xd3!\xa9\xb4&\xd0h\x06\x99\x08\xf4\x9e\x82i\x91\xa3M4\xcdFL\x08\xf5\x1e\x81=A\xe84\x9bI\xea4\x1acQ\xb4\x98\x8d\x1ai\xa6\x04\xd1\x846\x86\xa1\xd1\xa3FBmL\xd4\xf4L#A\xa3Ce=OMOG\xa9\xea\x01=\x1a\x9e\xa6j\x19\xa4\xd0\xc9\xa1\x89\xa1\xe9=\x13\x13\xd2y5\x1e\xa6\x06\x93\xd4d\r\x01\x810\x13\'\x90\x83L\x04\xd0\xd0\xf56\x83SM\x1a6\x844\xf6\xa9\xa3\xd3Hbh4`\x12za4G\x94\xf4i4\xf56S\xc2\x9e\x81\x92mOQ\xa6\x9az\x99\x19\x0c\xd44\x18\xd2=M4mM\r\x1e\x90z\x8f$\xc4\xd3F\xc8\x80\xd3Fj\x1a<D\xda\x86F\x86\x86\xd1\xa8\xf2\x9bH\x1e\xa6@zOQ\xeaz\x9e\x9a\x9azM=\t\x89\xb4 \xf5\x18\x8fDf\xa0|\xe8\xb0"\x15\xc1\x81-\xcf\x11\\\x9a\rk\x8d\xb0\xce\xb9K70w\xe3J\xcb\xe7\x84\xd5~\x06\xdc"\x0f**wA<\xaf \xf6\xca\xb3\x01\x99\x83\xe2\xccE\xc5\x04\x89{(\xec\xfaJ\xd3\x96+\x1f^\x950\xdc\x96\x1ez\xfe\xba\xa9t\x07\xeeN[\xddw\xaa\x86h\rD\xa5]\x85{\x9bT\x17\xf84\xf7\x80"c\x16\xc1\xb6q\x04w\xb5h\x8a\x7f)\xfb{\xc0j\xe3P\xe7Q\xeev\x97\xb0\xf2S\x8c\x14\xceb\xb5\xec\xf8\x10\xb1\xe3m.\xa7\x01\xca]\x82q\x11\xb5\x90\x97\x0f\xba\xb1\xe5\x87&\xc2i\x14\xa5\x1e\xea?6f\xcd\xf08\x85.\x8a\x86l\x1f}\xb2_/\xbe\xa0(\x84\x1f\xe3)\x006\xb3V\xeeV\x85\x089\xc3\x01N!\xd2$\xeb\xa0A.\xeb\t\xe0\x848l\xbdd\xbb\xe5\xef\xc4\n\\\xae\x91\xe5z\xcfO\xed\xaf\xbe\xab\xcc\xb5\x92\x98\xfe(\x96\xb2t]\xadJy\xb7\x98\x86\x7f\x80\x94\xb5\xc9\x81z\xa3R\xa6\n\xfek\x06f;\xa80t\xa8\xc6.a\xb8\x1cXe^|\x97k.\xea\x17\x8b\xbf!\xb1.\xa2A\x18\x9bm\xda\\\x1e\xf1B\x8a\xaeV\xa4\x9e\x99\xf9\x83\x80\x9b\xbb\xcdu\xdaR\n\x1eQ\xfc\xf9\x92\x01\xb4E\xd8\xe5\xd4mZp\xd3\x80\x1b)Ml\xac\xc2\xf0\xfc\x88e\x93L5/\xc6\x80H\xe3\xc1_z\x11\x03\xf9+o\xb1\x9f\xc5\xc1\x04Zs\x15\xc7\x99\xd9R\xc9!\x96\xf4\xcf\x81\x00Y\xb1.\x8bfSUx\x15Q\xd3\xf3\x8eb\xec\'\xa0O0mL\xde\x1a~\x11\x0b\xe4f-\xa2m\xd2\xf9\x82<(\xa7\x89\x03.Cd\xa1+=\x08i\x03\x94\x8c7\xb7X\xc9\xcd\xcd\xef\xb6\x8f\\\xdb\x04\x89\xe7\x9dW\xf3\xd7L\xd7\x8a\xf7\x83.I\x00\xb8E\x9d\x92\xadk\xeeZ\x10Za\x7f\x8c\xa5[\xa7\x83\xee\xcd\xbf\xdaP`\xadTa\x89yF\n,\x84n\x7fEw\x08i\xa9@\xd6\xee\\\x1dF\xba\xcf\xf0\xad\x06\xcd4p`\xb1\xcb\xe7\x19LW\x87\x19\x81PC\x17\x0eN:\xea.C\x10"\x94O\xeb\x82\xb9DV\xeah\x1f\xda-\x0c\xe3\xa2\xac\xc8I{2\xae\xe1\xfc!\r\xf6d[*\x96\x95\xc5\x14i<T\xf4i\x18\r\xdd\xe1\x02\xb2\x02e\xad\x08\xf0H\xa0\x02.A46\xdcC+\'Y8\xfaU\x7f\x82RbA\xbf\x12\x98\x1eV"J\xaf\xd8\xdb\x04\x86%\x18\x85.\xc4h^C\x88G\xdbh\x03(\x98\xf0\x9e(f\x12c\x16%\x8a\xa7\x87T\x95\xde&\xc1\xb9]\tu\x97O\xdb\x17e\xda\xd9\xfc\xc9\xb0\xd0\xfaS\x97V[\x85+c\x8c\xe4\xfdtT\x8f"\xf3$\xb0=\x08`\x11\xf983\xb0\x87\x1a\xabB\xe9\x1b\x7f="\xc6f|\x1b\xd5\xcb\xc3t\xf5\xd1\x07\xe3\xc9g9.\xdf\xcd\x92\xbc\x9b\xe0]\xc5\x80\x01\x94\xf6\xc6\xd2\x8a1\xe0d\x95\xcb**\x88\xf0\xc7lp\xf3e\xbb%\x13\xd1\x9daV\xa1\x1e\xcd^\x06\xba\xe5\xb8\x1e\xc5x\xa2\xc1:\x00\xef^\xec\x08!#\xebT\xc79\xf4p\x94\xe0\xec\xb4\x01\x07\xf4\xc1\x1b}\xa3\xc9\xb3Z\x0be9on\xd7\x16\xadr4J\xd0\xa6\xa4o\x17\xf0\xdb2\xbdr\xec\x83\x90\xde\x86\xdb\x9fo\xb6n5\xe7a\xa8\xdf\xeaGV\xb4\x17\x00:\x8b\xd5\x8a\x1an\x02\xb2:\xfe\xc08\x87\x17\xe9\xa6=c\x94\xfb\xd08\x14\x1aS\xf1\xbb\xed\\\x1dZ8\x13\r\x97~\xbaI\x07U\x99\xf9*S\x1e^\x13k\xb6{\xd6$|\xebU\xb2I\xc3\xed#\x85\xa6#\x98F\x97\xcb\x80z\r\x9b\x81\x0c\x9b\x92\xdd\x950\x19\xd6\xc9!\xec\x886\x81\x8d\xaa\x05\xe2\x13\x1fl$\xfe\xa1\x1e\x981\xa9\x90\xee\x94\xd1)\xae\xa4\xbc\xde\xc0\xf2\xc1\xd5-\xb3\xffxN\xce\\}\xd1:\xc0 _Y\xb8\xec\xae\xce\x00x]\x1e\xe8\xf2\x84+\xef\xba\xe4\x19\xb4\x02\xfep\x86\xa9P\x99\xbe\x86\x0f\n\xf6\xf5\x04\\\xce\xf7!\x04\x84\xe4Y\xae\xb4<\x9e\xaf\xecpC\x0b\xc9\tu\xf4\n\xb9T\xa2q\x97\xa6\x8a\xd9Q\xb7\xc5\xf2\x04\x90<-\n\xa2\xfe|\x13\x15\xc1-6I\x1f\x84N~\x8a\xa6>7\xa6[z\x0ef\x94M\xdd\xfb\xfa\x91AK6`B24\xda\x9c\x8e\xd6\x8a)\xfa\x9b\xb6\xc7a\xbfaF%\x85\xcdv\x92n\xa2\x82}\x18n\x82-1s\xd1\xd5\xc5\xd5<\x88\xbb>\x14!"\xcb\xda\x92\xa4\x15V)\xabD[\xaac\xd5.\xa9V\x04\x1a\xd1%\xa0>\x8dD\xcb\xe0e\xbaK\x147 \xad\xf8\xb6k\n\xcf\xc2\x0e\xe1\xb9\xf0m\xf7\x1a\x86\x1c,?\xd9\xe4\xe8\xfaM\xe3\xee#@\x1dE\xe1\xce3\xa5\xb7\x9a\x80\xd8^\x93\x9c\x06\xd2>\xaf(\xd5_DhG\xa0\xe5@#8\xa2\x88\xd4\xc1\xa7y\xc6XK\xab)\xeaZ\xfdm d\xa9\xb2b/\x8b\xb5}\x91\\\x93\x02]\xd5r\xaeUc2\x10\xae\xe4`\xb8\x98\xa3\xc2\xe05\xb7g\x03\xb0\xb7Y\x96&#\xc1\xf3\'\x8e5\xf6>\x80aK\xbdU6u\xc1\xdb\x016\xe0\xf0q\xf8\xf1\xb3a0\x01\xa7e<},we${\xad(\xf9K\x1e\x1c\x84gy\xea\xd6\x8e\xa2i\xe3G\xfb\x11k\x0b9\xbfd\xebZ\x97\xf7o\xc90wYe%N\xe2\x8d\'!G\t2U\xe4\xb7^\xb2\xef\xd9?\x1f\x95|x \x8bGf3T\x13\xa8\xd2^:g\xdcv\xf1\x87\x1a\xdb\xa7\xf1\xe0\x81!\xa3\x0c\xc6\xb5\x99>\x03\xc5\xc2\x0c8\xa7\x0b)\xaa;\xb0\xaf\xe9\xc6O\xb6\x9e\x9f\xa58v\x8b\x10l&\xcfs\xd1|\xf6\x899\xae=t\x8aO\x1e\xe1~&\xdd\xcdS;l\xf6w\xc1>\x9e\x96\xd2OM\x95\x98x\xba\xae\xac\xc7PN\x0c\xf3h\xfc\xe9\xf6jj\xa0\xb8\x9d\x10\x8bh\xd4K?\xffW\xb9ff9\xf8}\xbe\x08.Bp+\x12Bu\xa3Q@\x0f\'o\xae)\x94\x9a\xc5X\xeb\x87\xcd\xb8\xdf*\x19Zi9bz"\x00/\xa0XM\x8d\xab!\x1b[%\xdez+ \xf0S\x19\xb0\xf7\xf7Q/\x91\x8b#\x92\xafO\x80\x82U\x83\xb5\xb5\t\x87\xa7\xf0\x18P.VR\xf0\xf6\xa7\x0f\x1c\xc3\x9f\xaa1\x8e\xfd\xabj\xb8\x83\x9d\xa0\xd3\x1f.\xc3\xac \x13@\xa7ij,;\xf5\xeb\xc9\x11G\xd5\x82\xb557\x18e\xf7\x04cy\x04o\xdb\xe8T\xdf\x7f\xb2\xed\x91\xa9?1|y!g \tn\xad\xdb\xdfu\x81b\x85\x0b\xd5\x81\x89\xbc>\xb8[`k\xa4\x7f\xf2\xd95\xe8\xe3\xf5\x02\xec4\xa7\x7f\nN\xe2\t\xe9j\x12\xe9\x9a\xeb\xdad\x84;\xd3d\xb9\xc4P7}\xd8\x99\xfeS\xa4\xd4\x1e\xc9\x07u\xc9i\x11\x06\xfcilHxZVb\xe3E*\xc3\x8bN\xd1\x8c/\x1b(\xe7\xd6[%\xcd\xc3Kkz\xa7\x8eP\x11\xe0\x1e\x11n\x0eUj\xe9\xab\xd8\n\xd0\xb4w\xect\xb2\x03\x7f\x18\x99e\xf3D\n\xdbvo\xeaf\xcb\xd2t\xe4m\'\xb3\x9bz\xe89\xd7:dXF\x83\x1b]4s\x9c\xaf=\n\xfe`n^\xee\x1a\xa1\xe5\xefD\x95\x88$M\xef\xcc\x0ct\x18\xe1\\kg\x1b\x07\x10\xe2t\xed\x0ccY\xfdW\xe3\xa1\xd0`C\xea\x88\xa3o\x97\xcc3\xe1\x08\xa1t\xf8\xeb\x98\x86x\x13V\xe9=\xec\xb5\xf3}\xcdL\xb5R\xfc\x9e\xb1y\x8dg\xfd\x98\x1f\xd1\x8d\xde\xa8_\x03\x99*gp\xd4\xff2eY2\x19w\xa78\x93\xa8K<.oXf\xb9\x08\xd5\x04\x8dPL\xa2\x880\xec8\xfd\x94\x0e\xa8\xdd<\xa1\x8f\xa1H~\x9d\xbe\xd3\xeb\x02\x9dT\xa89v{\xe3u8K\xfdI\xd1Rv\x87\xb5\xee\xc8r\xaf\xf5\xd9m\xa19\x7fq\xf3\xd0f\xa6\xd3g\xa61a\x92c\xd6\xdf\xb7\xe2\xc0\x10\x86\x91\xe5\x7fF\xcc\x03\x99\xc7l{_;<lk\x96\xb0\x8f!oIc\xfc"\x1c\'\xd1iD\x1fv@N\xe6m^m.\xbb\xa3\t\x17\x83\xbb\xf3\xa5P\x06\x18\xc5\xf6\xc0\xe2,\xce\x884^\\G\xeak\xa3\x08\x0c(\xb1\xc7k=\xb54-9|&j\x94\xb1\xb0e\xba\xf2h\xe5\xa4\x17\xc0\x9a\xb7V\xa2\x12%QhlfAi\xee=\x0f\x18\x08E\x18 P\x1fo\xf4L\xd5+\xde~O\x8e+bL\x0b\x81\x8f\x81\x11&mKJ\xffE\x94\x82\x07\x91(\xa7\xdfp\xc5]]\xf7\x05\xbb\xecU\xbez\xc6|\xf6\xe3kG\xaf\xa6\xe8C$\xa7\x90\xc2\x8e\x19\xee\xce\x1b\x7fPTA\x11\xd9\xba4\xe1pl\x01\xd9\x8e\xaa\x03\xf2\'w\xe5\x9c\xd9\x0e\x84T\x8b9\xda\x81b}\x8d\xa5\xaf|e\xf2\x898\xaaD\xaa\xfa\xb2\xa8n\xb8\xd2\\%\xd1\xe9.\x873`\x18\xc2&$\xf8X\xb2\xf2\x97\x8b$V\x0e\x99\x7f\xa26\xe3\xa1\x00Z\x06-\xdd\xfb\xf6\xa6\x17\xe6U\xbc\x8f\xf6\xa4y@\x88\x13\xa2\xb4\xf0\xe4\xfb\x00\xbc\x01\xa0\xf5\xfbc\x0c\xe2j\xfd\xda\t\x8aP\xf1\xedy,.|tiqg,\xd0Y\xfb\'7\xc4.\x83q\x98\xe6>\xa8O\x82>D\xa9\x16\xbb\xd3F\xe1\xfc\xefd\xf06\x8a\x9b\xa93\xdc~\xf1x\x96^\x94\x1d\x92\x95\xc3\\\xeeP\xedwFT\xc2\xfd\x8d\xd8\xce\xd5\xbfI\xa2!px\x88\x0f\x1d\x9c\t6\x99XF7\xd1\xd3\x075\xec\xea|\x8a\xda~\xc5\xf0\xa7m\xe6&\x01\xb8\x08i\x854\xf3\x9c\x19\x96\xc2a\x7fT\x82#\xfda\xd1\x04\x8d4Hs\xb9\xbc&-\xc7\x93\x7f\xfe+:\x90\x8av\n\x1f\xb2c\xa5\x99.\xe2\xb1)T\x00\xdd\xa8]jv\xf7\xf9<\x13\xa1\x87\x8e\xf8\x9f\xee\xd4\x11\x89\xfb(#\xd5y\x07\xb6d)\xe6^\x81\xc2G[]\xed\xf3\xa2\xbb\xb4\x1e\xcc\x93\xd8\xfe\xecu\xad/9M2j\xde\xb3y\x0bt\xeb\xb6\xaf\xa6\xf8\x98Z\xdf=\x0e|*\x8a\xab,{\xbdLw\xa2\x84\xe8Y*\x05\x10\xb7\xb0\x0e\xce\xd7\xe1\xa6\xae\xaa,L?\xae\x1bPY\x08\x0b\xbb`\xffG\xf8\xfb\xf3\xe5n\xf3\xf9\x01\xc6\xe2\xe3q\x81\xb2\x83\x15\x18\x90\xab\x81\xf65W\xd4\x89\x17\xb3X\x84\x13Q\xd8\xb9<l\xfd\xad\x06|/\xafKy\xee\xcc\x8b\x18!\x99\xd4\x85\xe7fnT\x9a\x05\x83\x9b\x8aCH\xebe\x06D\x1dhs\xbc\x1f\x874j\xba\xe4\xb2,F\n\xc0\xb5\x16\x14\x10P\xc2\xcc\x13\xd0\xbcUS\x90Ic<@\x8d\x8b\xaa\xb5\xf2\xf1\xdb\x0f9N\xa1\xa4"\xb6\x16\x07\x92\xe8(\xbe\x83\xcb\x8b\xc4w?\xbf\x08\x16X\xfa\'N\x9e\x11\xc8\xb5\xb2\xed\xf3.!\xb1/C\x1a\xed\xe2\x9e\xe92ce\x12h(]O\xe0\xadQ#s\xf2\xd3\xa5\x81D\xd6v\x0b\xaf\x90\xe6Ebz\x0c[\x11n\xcf\xc7\xde\xa5}_\x01\xc0\xe49<\x985\xf2\x10\xf8\xe9pmP\x14\x0b\x007\x8a\xaf\xe1d\x10\xc0\x15\x9b\r\xee@\xf5I\xc7I\x89\xf3o\x90\x95K\xf7\x0b,I\xc6=\xe5\xbfI\x81\x96n\xe9<\xcd\x17\xd5s\x18\xfbR\'\xd7y\x16\xce\\\x9a\xab\xd0\xd1\xa1F$\x04l\xb6>n\xc3vCH]\x03\xef\xc9\xfc\x96\x99lf{\x0b\x15\x0c\xd1\xd5,\xe7\xa7\x1b\xb0\x11\xe3\xb3\xba\xbdX\'y\xf8c\xa6<4J\xd4\x88Qt\xa1\xc7\x13\xe2!\xd6\x94-\x9b\xe0\xf4u\xb9\xea\xaa\x01\x18q\xe5\xfd\xa8\xc3J\xdb\x140\xd7rF\xac\xce\xa9\xc6\x8d<\xc9\xa3dM\xd2\xe2\x15+\x9f\x92^\x81\x98\xba\xf3\x02\x06\xb3\xd2\x823P\x838\x11b`\xf9\xf6\x8cY\x9f\xe4\x8cQN\xac\xedq\x83\x92\x88\x90N\xcf\xef\xc6\xaau\x1a\xf6r\x8c\xa5\xe6\xfeL\r1\\L\x96\xc1\xfb\xc4\xf8\xa4\x00\x9e\xd1\xca\xf3\x10\xfe.q\x15\xdf\xeef\x99^\x86\x8b\xbeY\x1c\xf8Jv\xd7\xe7\xca\x88\xa3\x81I\'Z\xb4\x85\xcbrV\x00\xe3:&|\xa3\x1f/e\x1b\xe3\x14\xcc\xd7\xb4s\xadm\xday\x07\xca\xc5f&\xb8\x8a8\xf1\x19eP\xeb\xef \xe0\xe5H\x7f\xebT\xf3\x94\x95\xf5]\xf2\xf4M\xa2\xf9h$\xa2\xc0\xd3\x13\x15Dv\x8a\x8d"\xd8\x84\x97\xdb\xed\xcd\xa1\xbf \nY\x1b\x02\xf6C!\xab\xb7a^\xc4S\xb1\xc1\x02\xee\xc3\xbc+h&\xe75\xa3\xabT\x97N\x86#\xf7\xee\xabw\xc3\xdd\xdb\rJ5\t\xae\x1e\x03\xe62\xf5\xe0I\x02\x84\x8f\x9bA?\x95\x8d;I\x06\x9f\xf4`\xaf\xd0\\nl\xad\x80\x9d"\xaf\x1a\xb4\xa2\xb21m\x80$\xe0zo\xb8P\xe4\xb2\x89\x08\x1dh\xbc\xae\xa2f\x84J\x80\xb4\xc2\xc2\xad\x16h\xb4f\xc9\x9c\xbf_\xbe\x8a\xb1\xab\x18\x8d\xa9\xe7\xa5\xa0:\xf7\xb0t$56\x07\xd0J\x81l(\xd0\xd46\xa5\xb4\xcaQ_\xe7\x14\xdf\xde\x01\x90\xf7\xcd\xccZAY\xee\xf6\xc4\x1f\xafN9\xb9*dB\x08\xd2\xd0\xb6k\x89\xbb\xca#T\xcc\xb5\xe8\x8f\x10GY\xb9+\x95\xc6\r\xf2+-\xecP\xcc\xd4\x83\xf4\x90\x07*\xdb\xfb\x99\xab\xd7\xc9\x04\x86B\xddJWP(q?\xc9$\x8f3\x8b\xd2\x1e\x98\xd8\xf0\xe3\xb7wQ<H\x85\x91zS\x00J)>\xa0\x81a-\xe1\xc6\xab\xcf6\xaa\xbf\x08E\tA\xc9\xd2\xb3~22\xde\x9e\xc7hOsP\x06\xb8\xb7\xae\xf1\xcba\xdd|\xdc\x91[#u\x16K\x11j\xf4\x03\xd1\xd1\x920\x13\x12\xa2@\x87bpH\xd4\xd9\x85\xb9A\xe7\xab\x84\x1c\x11q\x7f^\xc0\xa5=\xca\x07r\x92\x89\xafe\xce@#\xeay1\x9080F#r\xc9\x96?\xe2P@\x97Mb\xb8\x05\x11\xc6\x86\xd31\xc2x\xf9\x85\x06\x06N\x96w\x07\xfc\x9d\xc8\x1b\x9c9",C\x05@<\xbcw\xbe\x80\x08\xaa\xefy@B\x9a\xcd\xf6\xb7U1\x0c1\x13-s.\x0e)\xcb5;#\x9b\x97\xbf\xe7\xbf\x04\x8d\xcc\\e\xb41\xaa\xfd\x03=\xbdn\xf3\xd2\xf3\xa6\xcf:\xa8\x0f\x0f\xc5%\x19;r\xd6\x81_imI\x93\xc1\xaa\xc0\xf9\x1aXL+J\x8b\xd5\x8e\x97\xe5\x94\xe2\xdd;\x1d\xa9E\x05\t\x0bH\xcdI?\xc4\n\xd4\xef\xa40\xe9\xad\xf5C\xc2~|\xbdZ3o\x9f\xab\xd2\xee\x83\xc9\x91f.\x92\xe8\xe8\xa7@\xc2 \x13\xe1\x05\\\x9f\x18\xc5\xe5\x1d\xf1\xe4U\x1cR\x1aQ\x0cj\x16\xf9\xf7J.\x99\x08G\xdf5\xf4\x9cH\xc3T\xc7S\xaa\xcb\x91\xb4\x13\x1c\xf9\xe2Vn\xae@A_\xec\xfeS\xb3\x1d3H,7$\nx\x8dp\xc1)1\xbe\x1c\xf6\xda\x81\xf5\xc1\xb1x\x1cu\x99\xb5\xa91\x9a\x98`i\xe3\x84\x8b\xbc\xac}a)\x95gEcA\x1bR$\xad\x12fYy\x1e\xd0\xa8\xe0)C\x1cX\xd9E\xd9\xa67\xae\x0bqI\x9d\x08\x17\xfe.\xe4\x8ap\xa1!\x89\xe6\xfd\xfc\x00\x7f5\x1dB<gz\x0e\x00\x01\xe8 \xd0 \x00\x00O\x9d\x9a\xe6\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))))))
except KeyboardInterrupt:exit()