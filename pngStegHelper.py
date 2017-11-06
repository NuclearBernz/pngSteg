import random

#encryption function
def encryptPNG(image, text, density, mode, destpath):
	
	print("Starting Encryption (May take more time based on size of text and image)")
	#Check that file/text will fit
	width, height = image.size
	loop = True
	area = (width-32) * height
	if area-(width-32) < (len(text)*density)-10:
		print('Error 100 - encryptPNG: Maximum Text size exceeded for this image')
		exit()
	
	# load image
	im = image.load()
	x,y = 0,0
	
	#encrypt text into image
	for c in list(text):
		ascii = ord(c) - 9
		#split into three equal (or near equal) parts
		n = ascii//3
		r_sub, g_sub, b_sub = n, n, ascii - (2*n)
		
		#determine what color scheme
		try:
			r,g,b = im[x,y]
		except:
			try:
				r,g,b,a = im[x,y]
			except:
				pass
		
		#calculate new pixel color to hide data
		if r+r_sub < 256:
			r=r+r_sub
		else:
			r=r-r_sub
		
		if g+g_sub < 256:
			g=g+g_sub
		else:
			g=g-g_sub
			
		if b+b_sub < 256:
			b=b+b_sub
		else:
			b=b-b_sub
		
		color = (r, g, b)
		im[x,y] = color
		
		#increment location
		if mode=='s':
			# increment location square
			if x+density<width:
				x=x+density
			elif(y+density) < height:
				x=0+(ascii%(random.randint(1, 6))) #offset per row
				y=y+density
			else:
				if y+density > height-1 and y!=height-1:
					y=height-1
				else:
					print("Error 101a - encryptPNG: Cannot fit at this density")
					exit();
		elif mode=='l':
			#increment location linear (width only)
			if x+density<width:
				x=x+density
			else:
				if y < height:
					x=0+(ascii%(random.randint(1, 6))) #offset per row
					y=y+1
				else:
					print("Error 101b - encryptPNG: Cannot fit at this density / bounds error")
					exit();
	
				
	outFile = destpath + '.png'
	try:
		image.save(outFile)
		print('Encryption Success')
	except:
		print('Error 102 - encryptPNG: Bad Destination')
		exit()

#decryption function
def decryptPNG(image, imageKey, destpath):

	print("Starting Decryption (May take more time based on size of text and image)")
	
	#load images
	im = image.load()
	key = imageKey.load()
	
	#check for valid image pair
	if image.size != imageKey.size:
		print("Error 110 - decryptPNG: image and image key are of different sizes")
		exit()
	
	width, height = image.size
	flag = False
	output = ""
	
	for y in range(height):
		if flag == True:
			break;
		
		for x in range(width):
			
			#determine what color scheme for image
			try:
				r,g,b = im[x,y]
			except:
				try:
					r,g,b,a = im[x,y]
				except:
					pass
	
			#determine what color scheme for imageKey
			try:
				r1,g1,b1 = key[x,y]
			except:
				try:
					r1,g1,b1,a1 = key[x,y]
				except:
					pass
			var = abs(r-r1) + abs(g-g1) + abs(b-b1)
			#check for variations
			if var >0:
				ascii = var + 9
				char = chr(ascii)
				output+=char
	
	#send output to destination file
	try:
		dest = destpath + '.txt'
		outfile = open(dest, 'w')
		outfile.write(output)
		outfile.close()
		print("Decryption Success")
	except:
		print('Error 111: Bad Destination / cannot write out to file specified')
		
