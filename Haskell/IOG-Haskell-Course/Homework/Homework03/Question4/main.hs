-- Question 4
-- Write a function that takes in two numbers and returns their quotient such that it is not greater than 1.
-- Return the number as a string, and in case the divisor is 0, return a message why the division is not
-- possible. To implement this function using both guards and if-then-else statements.  

divide :: Double -> Double -> String
divide x y
    | y == 0 = "Error: division by zero is not possible"
    | quotient > 1 = "Quotient is not greater than 1: " ++ show (quotient)
    | otherwise = "Quotient is: " ++ show (quotient)
    where
        quotient = x / y

divide' :: Double -> Double -> String
divide' x y = 
    if y == 0 
        then "Error: division by zero is not possible"
    else if quotient > 1 
        then "Quotient is not greater than 1: " ++ show (quotient)
    else 
        "Quotient is: " ++ show (quotient)
    where 
        quotient = x/y

-- makes sense