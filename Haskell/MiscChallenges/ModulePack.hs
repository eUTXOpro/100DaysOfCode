-- import Data.List 
{-
import Data.List

    import
     This keywork is used to include a specific module into the program.
     import can be used to third party moudles or modules you have created in your code

    Data. List
     This is a Haskell module that

    -}




module ModulePack (getNumbers, getStrings) where

getNumbers :: [String] -> IO [Int]
getNumbers userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return (map read xs :: [Int])

getStrings :: [String] -> IO [String]
getStrings userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return xs
