-- Day 5

import System.Random

-- Define the 'randomInt' function, which returns an IO action that generates a random integer between 0 and 1 (inclusive)
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