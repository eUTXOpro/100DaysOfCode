import ModulePack

main :: IO ()
main = do

    initialList <- getNumbers ["Enter a number:", "Enter another number:", "Enter a third number:", "Do it again"]
    putStrLn "Initial List:"