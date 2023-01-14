{- day 6
Write a function that takes a list of integers and returns a new list with all even numbers doubled.
   Example: doubleEvens [1, 2, 3, 4] should return [2, 4, 6, 8]. -}

getNumbers :: [String] -> IO [Int]
getNumbers userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return (map read xs :: [Int])

doubleEvens :: [Int] -> [Int]
doubleEvens xs = map doubleIfEven xs

doubleIfEven :: Int -> Int
doubleIfEven x = if x `mod` 2 == 0 then 2 * x else x

main :: IO ()
main = do

    initialList <- getNumbers ["Enter a number:", "Enter another number:", "Enter a third number:", "Do it again"]
    putStrLn "Initial List:"
    print initialList
    putStrLn "Modified List:"
