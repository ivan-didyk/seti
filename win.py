"""

"""

__chars = " ".join("""NUL 	SOH 	STX 	ETX 	EOT 	ENQ 	ACK 	BEL 	BS 	HT 	LF 	VT 	FF 	CR 	SO 	SI
DLE 	DC1 	DC2 	DC3 	DC4 	NAK 	SYN 	ETB 	CAN 	EM 	SUB 	ESC 	FS 	GS 	RS 	US
SP 	! 	" 	# 	$ 	% 	& 	' 	( 	) 	* 	+ 	, 	- 	. 	/
0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	: 	; 	< 	= 	> 	?
@ 	A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O
P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	[ 	\ 	] 	^ 	_
` 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o
p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z 	{ 	| 	} 	~ 	DEL
Ђ 	Ѓ 	‚ 	ѓ 	„ 	… 	† 	‡ 	€ 	‰ 	Љ 	‹ 	Њ 	Ќ 	Ћ 	Џ
ђ 	‘ 	’ 	“ 	” 	• 	– 	— 	? 	™ 	љ 	› 	њ 	ќ 	ћ 	џ
NBSP 	Ў 	ў 	Ј 	¤ 	Ґ 	¦ 	§ 	Ё 	© 	Є 	« 	¬ 	SHY 	® 	Ї
° 	± 	І 	і 	ґ 	µ 	¶ 	· 	ё 	№ 	є 	» 	ј 	Ѕ 	ѕ 	ї
А 	Б 	В 	Г 	Д 	Е 	Ж 	З 	И 	Й 	К 	Л 	М 	Н 	О 	П
Р 	С 	Т 	У 	Ф 	Х 	Ц 	Ч 	Ш 	Щ 	Ъ 	Ы 	Ь 	Э 	Ю 	Я
а 	б 	в 	г 	д 	е 	ж 	з 	и 	й 	к 	л 	м 	н 	о 	п
р 	с 	т 	у 	ф 	х 	ц 	ч 	ш 	щ 	ъ 	ы 	ь 	э 	ю 	я""".split()).split(" ")

def win1251(ch):
  """
  Получить символ из кодировки Windows-1251
  
  :param ch: Код символа
  :type ch: int
  :return: Символ
  :rtype: chr
  """
  if ch == 32:
    return ' '
  else:
    return __chars[ch]
