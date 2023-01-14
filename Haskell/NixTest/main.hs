import System.Random 

randomInt :: IO Int
randomInt = do
   n <- getStdGen  -- Get the global random number generator
   return $ fst $ randomR (0, 4) n

main :: IO ()
main = do
  n <- randomInt
  if n == 1 then putStrLn "Heads" 
  else putStrLn "Tails"