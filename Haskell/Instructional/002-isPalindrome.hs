import Data.List

flipString :: String -> String
flipString s = reverse s

main :: IO ()
main = do
    putStrLn "Enter a word, this program will check it it is a palindrome!"
    s <- getLine
    let checked = flipString s
    if s == checked then putStrLn "It's a palindrome!"
    else putStrLn "Yeah, it's not a palindrome"