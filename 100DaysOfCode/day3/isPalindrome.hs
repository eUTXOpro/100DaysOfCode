-- Day 3

{- CURRENT OBJECTIVE
Write a program that checks to see if a string is a Palindrome' -}

import Data.List

-- Can't figure out how to import package using ChatGPT yet.
-- Problem with package manager??? Data.List.Split not recongized
-- Made the executive decicion to use a different module (Data.List)

flipString :: String -> String
flipString s = reverse s
main :: IO ()
main = do
    putStrLn "Enter a word, this program will check it it is a palindrome!"
    s <- getLine
    let checked = flipString s
    if s == checked then putStrLn "It's a palindrome!"
    else putStrLn "Yeah, it's not a palindrome"