#Find the Root of the Quractic Equation

A = int( input( "Enter the value of A  = " ) )
B = int( input( "Enter the value of B  = " ) )
C = int( input( "Enter the value of C  = " ) )

Root1 = ( -B + ( ( B**2 - 4 * A * C) ** 0.5 ) ) / ( 2 * A ) 

Root2 = ( -B + ( ( B**2 - 4 * A * C) ** 0.5 ) ) / ( 2 * A ) 

print ( "The Roots of the quraditic equaction = " , Root1 , " And " , Root2 )