-- Day 5
import System.Random

randomInt :: IO Int
randomInt = do
   n <- getStdGen  -- Get the global random number generator
   return $ fst $ randomR (0, 4) n

main :: IO ()
main = do
  n <- randomInt
  if n == 1 then putStrLn "Heads" 
  else if putStrLn "Tails"

-- When installing packages, remember to add --lib (no idea why but it seems to work)