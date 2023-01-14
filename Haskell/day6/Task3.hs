-- Write a function that takes a list of integers and returns a new list with only the odd numbers.
-- Example: filterOdds [1, 2, 3, 4] should return [1, 3]

getNumbers :: [String] -> IO [Int]
getNumbers userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return (map read xs :: [Int])

removeOdds :: [Int] -> [Int]
removeOdds xs = filter isEven xs
    where  
    isEven x = x `mod` 2 == 0


main :: IO ()
main = do
    initialList <- getNumbers ["Enter a number:", "Enter another number:", "Enter a third number:", "Do it again"]
    putStrLn "Initial List:"
    print initialList

    putStrLn "Modified List:"
    let modifiedList = removeOdds initialList 
    print modifiedList
