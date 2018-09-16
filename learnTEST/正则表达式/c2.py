import re

a = 'axc,aec,afc,bfc,ahc,acc'

# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# r = re.findall("a[fc]c", a)
r = re.findall("\w[fc]\w", a)
print(r)
