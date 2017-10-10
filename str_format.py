# --coding:utf8--

# 這是<A Byte of Python> 的練習
age = 20 
name = 'Swaroop'

print ('{0} was {1} years old when he wrote thos book'.format (name, age))
print ('Why is {0} playing with that python?'.format(name))

print ('Done')

print (name + 'is' +str(age) + 'years old')

print ('Done2')

age = 20
name = 'swaroop'

print ('{} was {} years old when he wrote this book'.format(name, age))
print ('Why is {} playing with that python'.format(name))

print ('Done3')

# 對於浮點數 '0.333' 保留小數點(.)後三位
print ('{0:.3f}'.format(1.0/3))
# 使用下滑線填充文本，並保持文字處於中間位置
# 使用(^)定義 '___hello___'字符串長度為11
print ('{0:_^11}'.format('hello'))  
print ('{name} wrote {book}'.format(name = 'swaroop', book = 'A Byte of python'))
print ('Done4')

# 下面是解釋透過end 指定其應以空白結尾

print ('a',end=' ')
print ('b',end=' ')
print ('c',end=' ')
print ('Done5')
# 以上出現錯誤，需查資料

# 下面夠過\了解轉義序列
 
print ('This is the first line\nThis is the second line.')
print (r"Newline are indicated by \n")
