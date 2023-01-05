-- Day 3

{- CURRENT OBJECTIVE
Write a function 'isPalindrome' that takes a list of elements
and returns 'true' if the list is a palindrome' -}

import Data.List.Split

-- Can't figure out how to import package using ChatGPT yet.

main :: IO ()
main = do

putStrLn "Enter a word, this program will check it it is a palindrome!"
checkMe <- getLine
let checkMeAsList = tolist checkMe

putStrLn ("output = " ++ checkMe)

--This still doesn't work, but that's because there's nothing of value here yet