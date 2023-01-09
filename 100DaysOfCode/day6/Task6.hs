-- 6. Write a function that takes a list of strings and returns the length
--    of the longest string in the list.
import Data.List


getStrings :: [String] -> IO [String]
getStrings userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return xs

longestStringLength :: [String] -> Int
longestStringLength list = maximum $ map length list


main :: IO ()
main = do
  
  list1 <- getStrings ["Enter a number:", "Enter another number:", "Enter a third number:", "Do it again"]
  putStrLn "List1:"
  print list1
  let longestLength = longestStringLength list1
  putStrLn $ "The length of the longest string is: " ++ show longestLength