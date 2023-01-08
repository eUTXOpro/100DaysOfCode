-- Day 5
import System.Random

randomInt :: IO Int
randomInt = do 
   n <- getStdGen  -- Get the global random number generator
   return $ fst $ randomR (0, 1) n

main :: IO ()
main = do
  n <- randomInt
  -- Heads = Kali
  -- Tails = Parrot
  if n == 1 then putStrLn "Heads" else putStrLn "Tails"