#coding = utf - 8

import re

'''
(?P<name>exp):匹配exp表达式并捕获成命名组，该组的名字为name。后面可通过(?P=name)
来引用前面捕获的组。通过此处介绍不难看出，(exp)和(?P<name>exp)的功能大致相似，只是
exp捕获的组没有显示指定组名，因此后面使用\1、\2等方式来引用这种组所匹配的子串；而(?P<name>exp)
捕获的组指定了名称，因此后面可通过<?P=name>这种方式来引用命名组所匹配的子串。

（?P=name):引用name命名组所匹配的子串。
测试代码如下:
'''
print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>','<h3>xx</h3>'))
#输出:<_sre.SRE_Match object; span=(0, 11), match='<h3>xx</h3>'>



'''
上面的正则表达式为r'<(?P<tag>\w+)>\w+</(?P=tag)>',表达式开始是"<"符号，它直接匹配
该符号;接下来定义了一个命名组:(?P<tag>\w+),该组名为tag,该组能匹配1~N个任意字符;表达式
又定义了一个">"符号，用于匹配一个HTML或XML标签。接下来的"\w+"用于匹配标签中的内容;正则
表达式又定义了"</",它直接匹配这两个字符;之后的(?P=tag)就引用前面的tag标签组所匹配的子串
也就是说，该正则表达式要求内容必须在合理关闭的HTML或XML标签内。因此上面的<h3>xxx</h3>可以
匹配。
测试代码如下:
'''
#print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>','<h3>xx</h2>'))
#None

'''
上面的表达式尝试匹配的字符串虽然在HTML标签内，但由于前后两个标签不同，因此不能匹配
================================================================================================
'''
