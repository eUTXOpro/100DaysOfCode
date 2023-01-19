flipString :: String -> String              {- flipString :: String -> String   
    flipstring
     This is a function that is defined prior to the "main" function.
     It can be called in the "main" function as "flipString"
     Functions must start with a lower-case character. 
     It is good practice to use camelCase when naming a function.
    ::
     This is used to specify the type or value of a function. 
     It can be read as "has the type of"
     When you define a function, you must define its type.
     Gemerally functions must return a value however there are some exceptions.
    String -> String
     This is the type setting of the function.
     Haskell is a statically-typed language and must know the type of a value at compile time.
     This function takes a String and produces a String. -}
flipString s = reverse s                    {- flipString s = reverse s

    flipString s =
     This defines the -}


main :: IO ()
main = do
    putStrLn "Enter a word, this program will check it it is a palindrome!"
    s <- getLine
    let checked = flipString s
    if s == checked then putStrLn "It's a palindrome!"
    else putStrLn "Yeah, it's not a palindrome"