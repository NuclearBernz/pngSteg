import sys
import pngStegHelper
from PIL import Image

# Command Line arguments
ENCRYPT = ('-e', '-E')
DECRYPT = ('-d', '-D')
INFO = ('-i', '-I')
SIZE = ('-s', '-S')

# check for program state
check = 0

try:
	x = sys.argv[1]
	
	# Test for correct arguments,
	if x in ENCRYPT:
		try:
			y = sys.argv[3]
			check = -1	#case where given a text file argument
		except:
			check = 1	# case where not given a text file argument
	elif x in DECRYPT:
		try: 
			y = sys.argv[3]
			check = -2 # case where given image key
		except:
			check = 2 #case where not given image key
	elif x in INFO:
		check = 3
	elif x in SIZE:
		check = 4
		
	else:
		check = 0
		
except: 
	print("Error 001 - Invalid arguments given, for help use -i")

#encrypt image case
if check == 1 or check == -1:
	try:
		# get path of image to include
		y = sys.argv[2]
		#open image to be edited
		orig = Image.open(y)
		if orig.format != 'PNG':
			exit()
		print("Successful Image Load")
	except:
		print("Error 002 - Encrypt: Invalid Image Load / no image given");
		exit()
	#Minimum image size requirement
		width, height = orig.size
		if width <500:
			print('Error 002a - Encrypt: Image too small')
		elif height<500:
			print('Error 002a - Encrypt: Image too small')
	#for text file case
	if check == -1:
		try:
			myfile = open(sys.argv[3])
			text  = myfile.read()
		except:
			print("Error 003 - Encrypt: Invalid Text File Load")
	#For no text file case
	else:
		text = input('Enter text to be encrypted ==> ')
	
	#get mode
	try:
		mode = input('Enter mode, s for square and l for linear width\nNOTE: square= significantly less space, \nlinear width = much more space, but can be more visible\n ==> ')
		if mode == 's':
			pass
		elif mode == 'l':
			pass
		else:
			exit()
	except:
		print('Error 005 - Encrypt: Invalid mode given')
		exit()
	
	#get pixel Density (1 through 100, 1 being high density)
	try:
		s = 'Input density 1-100 (1 is highest density, 100 is lowest)\nNOTE: lower pixel density = less message space\n ==> '
		focus = int(input(s))
		if focus < 0: 
			exit()			
		elif focus > 101:
			exit()
	except:
		print('Error 004 - Encrypt: Invalid entry for Density')
		exit()

			
	#get destination of output
	dest = input('Enter name (or full path) of destination file (NO EXTENTION) ==> ')
	
	#call encryption function
	pngStegHelper.encryptPNG(orig, text, focus, mode, dest)
	exit();


#decrypt image case
elif check == 2 or check == -2:
	#for encrypt image
	try:
		# get path of image to decryot
		y = sys.argv[2]
		#open image to be edited
		orig = Image.open(y)
		if orig.format != 'PNG':
			exit()
		print("Successful Image Load")
	except:
		print("Error 012 - Decrypt: Invalid Image Load / no image given");
		exit()
	
	#for image key
	if check ==-2:
		try:
			# get path of image to decryot
			y = sys.argv[3]
			#open image to be edited
			orig2 = Image.open(y)
			if orig2.format != 'PNG':
				exit()
			print("Successful Image key Load")
		except:
			print("Error 013 - Decrypt: Invalid Image key Load");
			exit()	
	else:
		keyPath = input('Enter path of image key ==> ')
		try:
			orig2 = Image.open(keyPath)
			if orig2.format != 'PNG':
				exit()
			print("Successful Image key Load")
		except:
			print("Error 013a - Decrypt: Invalid Image key Load");
			exit()	
	
	
	
	#get destination of output
	dest = input('Enter name (or full path) of destination file (NO EXTENTION) ==> ')
	
	#call decryption function
	pngStegHelper.decryptPNG(orig, orig2, dest)
	exit()

elif check ==3:
# put helper info here
	print('''
	Welcome to the PNG Steganographer - BERNZ EDITION
	
		Here are the following functions (are case insensitive)
		
		-e ==> Encrypt Text into Image. Can be used in the following formats:
			-e [Base PNG path to be encrypted] [path of .txt file to encrypt into image]
			-e [Base PNG path to be encrypted]
				* In the case without a .txt file argument, text can be inputted manually
				* Will be prompted to select mode
					--> enter 's' for square distrbution mode: much more descrete and 
							visualy uniform at cost of space available 
							(suggest use of low density)
					--> enter 'l' for linear width distribution mode: less discreet and 
							uniform, but can hold exponentially more information
				* Will be prompted for density of encryption
					1 is lowest = most space for encryption
					100 is highest = least space for encryption
				* Will be asked to give a destination path/name for the encrypted PNG
					--> WARNING, DO NOT INCLUDE THE .png EXTENTION
				
							
		-d ==> Decrypt PNG Image and extract hidden text. Can be used in the following 
				formats:
			-d [Encrypted PNG path] [Base/Key PNG path]
			-d [Encrypted PNG path]
				* In the case without a base/key PNG path given, will be prompted to 
					include in order to proceed
				* Will be asked to give a destination path/name for the extracted text
					--> WARNING, DO NOT INCLUDE THE .txt EXTENTION
		
		-s ==> Utility to check in advance how many characters will fit into chosen 
					PNG at chosen density. Does not accept any additional arguments
						* Will request valid path of PNG to test
						* Will request valid Denstiy range (1-100)
				
		-i ==> Print info for this program to console.
	''')
	exit()

elif check == 4:
	try:
		# get path of image to decryot
		x = input('Path of desired PNG ==> ')
		#open image to be edited
		orig = Image.open(x)
		if orig.format != 'PNG':
			exit()
		print("Successful Image Load")
	except:
		print("Error 020 - Size: Invalid Image Load / no image given");
		exit()
	
	# get density scheme (mode)
	try:
		mode = input('Enter mode, s for square and l for linear width\nNOTE: square= significantly less space, linear width = much more space, but can be more visible\n ==> ')
		if mode == 's':
			pass
		elif mode == 'l':
			pass
		else:
			exit()
	except:
		print('Error 021 - Encrypt: Invalid mode given')
		exit()
	
	
	
	#get pixel Density (1 through 100, 1 being high density)
	try:
		s = 'Input density 1-100 (1 is highest density, 100 is lowest)\nNOTE: lower pixel density = less message space\n ==> '
		density = int(input(s))
		if density < 0: 
			exit()			
		elif density > 101:
			exit()
	except:
		print('Error 022 - Size: Invalid entry for Density')
		exit()
	
	if mode == 'l':
		width, height = orig.size
		y = ((width//density) *(height-2)) - 10
	elif mode == 's':
		width, height = orig.size
		y = ((width*(height-2))//density) -10
	
	print('This image will fit', y ,'characters at a density of', density, 'using mode --> ', mode)
	exit()
		
		
else:
	print("INVALID INPUT, for further assistance, use command argument -i")
	








