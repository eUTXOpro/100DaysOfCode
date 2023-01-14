
module ModulePack (getNumbers, getStrings) where

getNumbers :: [String] -> IO [Int]
getNumbers userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return (map read xs :: [Int])

getStrings :: [String] -> IO [String]
getStrings userInput = do
  xs <- mapM (\msg -> putStrLn msg >> getLine) userInput
  return xs
