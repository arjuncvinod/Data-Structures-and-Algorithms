import sys 
import math 



# define a function egyptianFraction 
# which receive parameter nr as 
# numerator and dr as denominator 
def egyptianFraction(nr, dr): 

	print("\nThe Egyptian Fraction " +
		"Representation of {0}/{1} is". 
				format(nr, dr), end=" ") 

	# empty list ef to store 
	# denominator 
	ef = [] 

	# while loop runs until 
	# fraction becomes 0 i.e, 
	# numerator becomes 0 
	while nr != 0: 

		# taking ceiling 
		x = math.ceil(dr / nr) 

		# storing value in ef list 
		ef.append(x) 

		# updating new nr and dr 
		nr = x * nr - dr 
		dr = dr * x 

	# printing the values 
	for i in range(len(ef)): 
		if i != len(ef) - 1: 
			print(" 1/{0} +" . 
					format(ef[i]), end = " ") 
		else: 
			print(" 1/{0}" . 
					format(ef[i]), end = " ") 

if __name__ == '__main__':
	print('enter the fraction you want to find egyptian fraction of')

	nr,dr=input().split('/') #enter the number in fraction form and then take the numerator and denominator part
	nr,dr=int(nr),int(dr)

	egyptianFraction(nr,dr)


