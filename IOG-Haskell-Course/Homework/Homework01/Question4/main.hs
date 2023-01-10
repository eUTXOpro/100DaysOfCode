{- Define a function that calculates the volume of a cylinder...
by composing the previous function together with the height of the cylinder.-}

areaOfCircle :: Float -> Float
areaOfCircle r = pi * r^2

volumeOfCylinder :: Float -> Float -> Float
volumeOfCylinder r h = h * areaOfCircle r

greaterThan :: Float -> String 
greaterThan volume = if volume <= 42 then "less than or equal to 42" 
    else "greater than 42"

main :: IO ()
main = do
    let rad = 4
    let height = 4
    let area = (areaOfCircle rad)
    let volume = volumeOfCylinder rad height

    print area
    print volume

    print (greaterThan volume)