-- Question 1
-- Add the type signatures for the functions below and then remove the comments and try to compile.

module Functions (f1, f2) where

f1 :: Double -> Double -> Double -> Double
f1 x y z = x ** (y/z)

f2 :: Double -> Double -> Double -> Double
f2 x y z = sqrt (x/y - z)

-- f3 x y = [x == True] ++ [y]

-- f4 x y z = x == (y ++ z)