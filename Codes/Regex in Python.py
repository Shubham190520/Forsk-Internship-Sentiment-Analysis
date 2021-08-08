import re

s = "aaa@xxx.com bbb@xxx.com ccc@zzz.com"

print (re.sub('[a-z]*@', 'ABC@', s))



str1 = '123abc123xyz456_0'

re.findall('\d\d\d', str1)
             or
re.findall([^1-3] {3}, str1 )       
     


str1 = 'hello123abc123xyz456_0'

re.findall('\d$', str1)
 


str1 = 'foo123bar'

result = re.search('\d\d\d' , str1)

 result.start()
 result.end()
 
 if re.search('^\d\d\d', str1):
     print("found a match")
 else:
     print("no match")
     
     
  
 str2 = "Forsk forskcoding school"

re.search('forsk' , str2)
re.match('forsk' , str2)

re.search('Forsk' , str2)
re.match('Forsk' , str2)    


""""""""""""""""""

str1 = "yogendrasingh@zdrv.com 123 yogendra@mango.com Jaipur ysingh@qualcomm.com yogendra@forsk.in covid 19"

pattern = re.compile('\w+@\w+\.\w+')
pattern.findall(str1)
              OR
re.findall(r'\w+@\w+\.\w+' , str1)
