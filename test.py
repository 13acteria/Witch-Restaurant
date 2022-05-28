s='中文'
print (type(s)) #檢視s的字元型別
print (s)  

s.decode('utf8') #解碼utf8，預設的編碼方式是unicode
s.decode('gbk', "ignore") #解碼utf8，忽略其中有異常的編碼，僅顯示有效的編碼
s.decode('gbk', 'replace')
print (type(s))
print (s)

s.encode('gb2312') ##編碼為utf8
print (type(s))
print (s)