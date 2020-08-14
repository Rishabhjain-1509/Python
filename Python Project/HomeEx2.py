#Swapping of Two number

def Swap( A , B ):
	Temp = A
	A = B
	B = Temp
	print( "The value of First number after swap = ", A )
	print( "The value of Second number after swap = ", B )
	
	A = A + B
	B = A - B
	A = A - B 
	
	print( "The value of First number after swap = ", A )
	print( "The value of Second number after swap = ", B )
	
A = int( input( "Enter the  first number = " ) )
B = int( input( "Enter the  Second number = " ) )

Swap( A , B)
