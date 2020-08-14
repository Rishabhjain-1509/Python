# Area of the triangle 

Side1 = int( input( "Enter the First side of the triangle = " ) )
Side2 = int( input( "Enter the Second side of the triangle = " ) )
Side3 = int( input( "Enter the Third side of the triangle = " ) )

SSum = ( Side1 + Side2 + Side3 ) / 2

Area  = (SSum * ( SSum - Side1 ) * ( SSum - Side2 ) * ( SSum - Side3 ) ) ** 0.5

print( "The area of the triangle = " , Area )