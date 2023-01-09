--Write a function that takes two lists of integers and returns a new list with the elements of the first list followed by the elements of the second list.
   --Example: concatLists [1, 2, 3] [4, 5, 6] should return [1, 2, 3, 4, 5, 6].


getNumbers :: [String] -> IO [Int]
getNumbers userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return (map read xs :: [Int]) --map read is converting the input into integers

main :: IO ()
main = do
    list1 <- getNumbers ["Enter a number:", "Enter another number:", "Enter a third number:", "Do it again"]
    putStrLn "List1:"
    print list1
    
    list2 <- getNumbers ["Enter a number:", "Enter another number:", "Enter a third number:", "Do it again"]
    putStrLn "List2:"
    print list2

    print (list1 ++ list2)
    