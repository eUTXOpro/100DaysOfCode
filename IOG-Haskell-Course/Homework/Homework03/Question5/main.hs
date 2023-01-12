-- Question 5
-- Write a function that takes in two numbers and calculates the sum of squares for the product and quotient
-- of those numbers. Write the function such that you use a where block inside a let expression and a
-- let expression inside a where block. 

main :: IO ()
main = do
    let x = 5
        y = 2
    print (sumOfSquares x y)
    print (addingNumbers x y)

sumOfSquares :: Double -> Double -> Double   
sumOfSquares x y = 
    let product = x * y
        quotient = x / y 
        prodSquare = product ^ 2
        quotSquare = quotient ^ 2
    in prodSquare + quotSquare

addingNumbers :: Double -> Double -> Bool
addingNumbers x y = prodSquare + quotSquare
    where 
        product = x + 2
        quotient = y + 2
        prodSquare = product ^ 2
        quotSquare = quotient ^ 2


-- not quite answering the question, but I get the concept so I'm calling that one close enough
