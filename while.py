# --coding:utf8--

number = 23
running = True

while running:
	guess = int(input('Enter an integer'))

	if guess == number:
		print ('Congratulations, you guessed it.')
		# 這將導致 while 循環中止
		running = False
	elif guess < number:
		print ('No, it is a litter higher than that.')
	else:
		print('No, it is a litter lower than that.')
else:
	print('The while loop is over.')
	# 在這裡你可以做你想做的任何事
print('Done')
