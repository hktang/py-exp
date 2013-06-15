py-exp
======

Some random experiments using Python. 

birthday_paradox.py
-------------------

Provides brute-force calculation for the probability of same-birthday 
occurrences in a group of arbitrary number of people. Inspired by the 
"birthday paradox" described by the weibo at 
http://www.weibo.com/2313291734/zvARF0tdX. More about birthday paradox at http://en.wikipedia.org/wiki/Birthday_problem

暴力验证生日概率问题：http://www.weibo.com/2313291734/zvARF0tdX

attitude-100.py
---------------

Finds all English words, the value of whose individual characters, if 
mapped to a numbered list (1, 2, 3 ... 26), add up to exactly 100.
Word list from SIL International Linguistics Department at 
http://www-01.sil.org/linguistics/wordlists/english/. 
Inspired by the (in)famous HR gag of 'ATTITUDE' = 100%. The list of words 
found are recorded in `/runs-output/attitude-100.txt`

设 a=1，b=2，... z=26，找出包括 "attitude" 在内的所有字母所代表数字之和为100的所有英文单词。