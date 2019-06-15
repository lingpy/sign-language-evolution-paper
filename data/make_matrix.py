from lexibase.lexibase import LexiBase
from lingpy import *
from lingpy.convert.strings import write_nexus
from unidecode import unidecode

data = """American_SL	ASL
British_SL	BSL
Czech_SL	CzSL
German_SL	DGS
Estonian_SL	EVK
Indian_SL	IndSL
French_SL	LSF
Latvian_SL	LSL
Spanish_SL	LSE
Lithuanian_SL	LGK
Portuguese_SL	LGP
Polish_SL	PJM
Swedish_SL	STS
Turkish_SL	TİD
Austrian_SL	ÖGS
Greek_SL	ΕΝΓ
Bulgarian_SL	BŽE
Russian_SL	РЖЯ
Croatian_SL	HZJ
Icelandic_SL	ÍTM
Italian_SL	LIS
Brazilian_SL	LSB
Mexican_SL	LSM
Pakistan_SL	PSL
Ukrainian_SL	УЖМ
Australian_SL	Auslan
Danish_SL	DTS
Norwegian_SL	NTS
Finnish_SL	FinSL
Flemish_SL	VGT
French-Belgian_SL	LSFB
Dutch_SL	NGT
Irish_SL	IrSL
International_MA	IS
Catalan_SL	LSC
NewZealand_SL	NZSL
Albanian_SL	AlbSL
Quebec_SL	LSQ
Afghan_SL	ZEA
Jordanian_SL	LIU
Yebra_1593	Y_1593
Bonet_1620	B_1620
American_1821	ASL_1821
American_1886	ASL_1886
American_1918	ASL_1918
Austrian_1786	ÖGS_1786
Austrian_1823	ÖGS_1823
Austrian_1839	ÖGS_1839
Brazilian_1875	Libras_1875
Danish_1808	DTS_1808
Danish_1871	DTS_1871
Danish_1907	DTS_1907
Danish_1926	DTS_1926
Danish_1967	DTS_1967
Dutch_1790	NGT_1790
Dutch_1820	NGT_1820
Estonian_1988	EVK_1988
French_1800	LSF_1800
French_1803	LSF_1803
French_1815	LSF_1815
French_1856	LSF_1856
German_1820	DGS_1820
German_1909	DGS_1909
German_1916	DGS_1916
Hungary_1827	MJ_1827
Icelandic_1857	ÍTM_1857
Italian_1897	LIS_1897
Norwegian_1893	NTS_1893
Norwegian_1900	NTS_1900
Norwegian_1955	NTS_1955
Polish_1879	PJM_1879
Spanish_1818	LSE_1818
Spanish_1845	LSE_1845
Spanish_1859	LSE_1859
Swedish_1866	STS_1866"""

converter = dict([line.split('\t') for line in data.split('\n')])

lex = LexiBase.from_dbase(
        'signalphabets', 
        dbase='signalphabets.sqlite3',
        # url='signalphabets.sqlite3'
        )

abbrs = csv2list('signlgs.txt', sep=", ")

count = 0

N = {0: lex.columns}

for idx, concept, tokens in lex.iter_rows('concept',
        'tokens'):
    tokens = basictypes.lists(tokens)
    N[idx] = lex[idx]
    N[idx][lex.header['doculect']] = unidecode(converter.get(
            lex[idx, 'doculect'], 
            lex[idx, 'doculect']))

lex = Wordlist(N)

write_nexus(lex, mode='splitstree', ref='cogid', filename='signs-cogid.nex')
