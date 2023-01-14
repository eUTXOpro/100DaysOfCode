-- Define a function that calculates the area of a circle.

areaOfCircle :: Float -> Float
areaOfCircle r = pi * r^2

-- Could also use Pi module from prelude or calculate Pi directly

main :: IO ()
main = do
    let rad = 4
    print (areaOfCircle rad)