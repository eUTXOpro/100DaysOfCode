
--Write a function that takes a list of integers and returns the largest number in the list
-- Example: maxNumber [1, 2, 3, 4] should return 4.

import Data.List (maximum)

getNumbers :: [String] -> IO [Int]
getNumbers userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return (map read xs :: [Int])




main :: IO ()
main = do

    putStrLn "Largest Number"
    let max = maximum initialList
    print max
