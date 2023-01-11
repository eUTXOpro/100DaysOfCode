import Functions (f1, f2, f3, f4)

main :: IO ()
main = do 
    print (f1 2 4 8)
    print (f2 2 4 8)
    print (f3 True False)
    print (f4 "ab" "a" "b")
