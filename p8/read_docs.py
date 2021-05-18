'''
1.不存在可变的字符串类型，但是 str.join() 或 io.StringIO 可以被被用来根据多个片段高效率地构建字符串。

2.str.capitalize()
返回原字符串的副本，其首个字符大写，其余为小写。

3.str.casefold()
返回原字符串消除大小写的副本。 消除大小写的字符串可用于忽略大小写的匹配。
消除大小写类似于转为小写，但是更加彻底一些，因为它会移除字符串中的所有大小写变化形式。 

4.str.center(width[, fillchar])
返回长度为 width 的字符串，原字符串在其正中。

5.str.count(sub[, start[, end]])
返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。 可选参数 start 与 end 会被解读为切片表示法。

6.str.endswith(suffix[, start[, end]])
如果字符串以指定的 suffix 结束返回 True，否则返回 False。 suffix 也可以为由多个供查找的后缀构成的元组。

7.str.find(sub[, start[, end]])
返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。 可选参数 start 与 end 会被解读为切片表示法。 如果 sub 未被找到则返回 -1。

8.str.format(*args, **kwargs)
执行字符串格式化操作。 调用此方法的字符串可以包含字符串字面值或者以花括号 {} 括起来的替换域。 每个替换域可以包含一个位置参数的数字索引，
或者一个关键字参数的名称。 返回的字符串副本中每个替换域都会被替换为对应参数的字符串值。
https://blog.csdn.net/jpch89/article/details/84099277

9.str.strip([chars])
返回原字符串的副本，移除其中的前导和末尾字符。 chars 参数为指定要移除字符的字符串。
 如果省略或为 None，则 chars 参数默认移除空白符。 
 
10.str.replace(old, new[, count])
返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。 
如果给出了可选参数 count，则只替换前 count 次出现。
差不多了，太多了
'''

a="hello_world"
b="HELLO_WORLD!!!"
print(a.capitalize())
print(a.casefold())
print(a.center(50,'-'))
print(a.endswith('d'))
print("i am {crying}".format(crying='pretenting crying'))
c=(a.center(50,'-'))
print(c.strip('-'))
d='i love you,you don`t know me,you hurt me.'
print(d.replace('you','she',2))
def is_palindrome(string):
    print(string[0:len(string)-1:-1])
#print(string[0:len(string)-1:-1])为什么不行
is_palindrome(b)
