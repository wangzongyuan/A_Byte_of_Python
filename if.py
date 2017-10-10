# --coding:utf8--

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
	# 新塊從這邊開始
	print ('Congratulations, you guessed it.')
	print ('(but you do not win any prizes!)')
	# 新塊在這裡結束
elif guess < number:
	# 另一代碼塊
	print ('No, it is a little higher than that')
	# 你可以在此做任何你希望在該代碼塊內進行的事情
else:
	print ('No, it is a little lower than that')
	# 你必須通過猜測一個大於設置數的數字來到達這裡。

print ('Done')
# 這是最後一句語句將在
# if 語句執行完畢後執行
