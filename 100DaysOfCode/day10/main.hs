--Given two strings ransomNote and magazine,
-- return true if ransomNote can be constructed 
-- by using the letters from magazine and false otherwise.
-- each letter can only be used once

--sortChar :: [Char] -> [Char]
--sortChar x = sort x

-- isPossible :: [Char] -> [Char] -> Bool
import Data.List

canConstruct :: [Char] -> [Char] -> [Char]
canConstruct z y = filter (`elem` z) y

main :: IO ()
main = do
    let ransomNote = "vv"
    let magazine = "This is a very long string with lots of letters in it"
    let magRemainder = canConstruct ransomNote magazine

    isPossible :: [Char] -> [Char] -> Bool
    isPossible magRemainder ransomNote
    
    if (sort magRemainder) == (sort ransomNote) then
        putStrLn "true"
    else if (lenght magRemainder) < (length ransomNote) then
        putStrLn "impossible"
     else 
        putStrLn "false"