main :: IO () {-
main :: IO ()    
   
    main
     This is the function that is executed when the program runs. 
     It is considered a special function as it is the entry point for the program.
     It is also the only function that can be invoked by the operating system.
     It is where the last statement will be execututed before the program ends.    
    
    ::
     This is used to specify the type or value of a function. 
     It can be read as "has the type of"
     When you define a function, you must define its type.
     Gemerally functions must return a value however there are some exceptions.
    
    IO ()
     This stands for "input/output". 
     This type allows the program to interact with the outside world.
     The "main" function must have the type signature "IO ()" -}

main = putStrLn "Hello, World!" {-
main = putStrLn "Hello, World"

Here we define the properties of the main function.
Everything following the "=" will become a property of "main"

putStrLn
    This is a function.
    It is part of the standard libarary of Haskell functions.
    Here is a breakdown of how this function works: 

        putStrLn :: String -> IO ()


-}