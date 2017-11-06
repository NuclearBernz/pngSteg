README - PNGSteg by Jesse Bernz

NOTE - Must have package Pillow 3.0 or higher in order to run this program.`
NOTE - This program runs in Python3
NOTE - This program is designed to work with .PNG pictures and .txt files only. Using other file types may produce undesired results.

This Program is designed to hide text or .txt files inside an image using visual pixel distortion. Why this method may be visible to the human eye, current steganography detection techniques have a much harder time detecting it. Currently, this program uses the base image as a comparison or “key” to retrieve the hidden text. By comparing the encrypted image with the base image, this program can retrieve the text that was stored and outputs it to a .txt file. 

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
