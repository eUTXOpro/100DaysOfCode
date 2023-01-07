-- Day 5

{- CURRENT OBJECTIVE

Write a function that takes a list of integers and returns their sum. 
For example, the call sum [1, 2, 3] should return 6.

-}

-- Define the 'sumNumbers' function, which takes a list of strings (farts) and returns an IO action*
sumNumbers farts = do 
    -- Apply the lambda function (\msg -> putStrLn msg >> getLine) to each element of the 'farts' list using 'mapM'
    xs <- mapM (\msg -> putStrLn msg >> getLine) farts
    -- Parse the strings in the 'xs' list as integers
    let xyz = map read xs :: [Int]
    -- Return the sum of the integers
    return $ sum xyz

-- Define the 'main' function, which is the entry point of the program
main :: IO ()
main = do
    -- Call the 'sumNumbers' function with the list of strings ["Enter a number:", "Enter another number:", "Enter a third number:"]
    -- and bind the result to the 'result' variable
    result <- sumNumbers ["Enter a number:", "Enter another number:", "Enter a third number:", "Do it again"]
    -- Print the value of 'result'
    print result


