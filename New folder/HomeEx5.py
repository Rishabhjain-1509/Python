# Using od the bitewise operators 

A =  int( input( " Enter the number = " ) )
B =  int( input( " Enter the number = " ) )
C =  int( input( " Enter the number = " ) )
D =  int( input( " Enter the number = " ) )


if A > B and A > C :
	
	print( "The value of A is Greater" )
	
	if  D > A or D > B :
		
		print( "The value of D is Greater" )
		
		A = ~A
		
		print( A )

G = bin( B ^ C)
print(G)