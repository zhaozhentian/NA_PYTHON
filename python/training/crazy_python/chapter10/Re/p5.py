#coding = utf - 8

import re

'''
在某些情况下，所执行的替换要基于被替换的内容进行改变。比如下面程序需要将字符串中的每个英文单词都变成
一本图书的名字。
'''

#在匹配的字符串前后添加内容
def fun(matched):
	#matched就是匹配对象，通过该对象的group()方法可获取匹配的字符串
	value = "《疯狂" + (matched.group('lang')) + "讲义》"
	return value


s = 'Python很好，Kotlin也很好'

#对s里面的英文单词(用re.A旗标控制)进行替换
#使用fun函数指定替换内容
print(re.sub((r'(?P<lang>\w+)'),fun,s,flags=re.A))

'''
上面程序使用sub函数执行替换时，指定使用fun()函数作为替换内容，
而fun()函数则负责在pattern匹配的字符串之前添加
"《疯狂" + 在pattern匹配的字符串之后添加 + "讲义》"


上面代码使用了一个稍微复杂的正则表达式:r'(?P<lang>\w+)'
这个正则表达式用圆括号表达式创建了一个组，并使用"?P"选项为该组起名为
lang——所起的组名要放在尖括号内。剩下的"\w+"才是正则表示的内容，其中
"\w"代表任意字符；'+'用于限定前面的"\w"可出现一次到多次，因此"\w"
代表一个或多个任意字符。又由于程序执行了sub()函数时指定了re.A选项，
这样"\w+"就只能代表ASCII字符，不能代表汉字。

当使用sub()函数执行替换时，正则表达式'\w+'所匹配的内容可以通过
组名"lang"来获取，这样fun()函数就调用了matched.group('lang')
来获取"\w+"
'''