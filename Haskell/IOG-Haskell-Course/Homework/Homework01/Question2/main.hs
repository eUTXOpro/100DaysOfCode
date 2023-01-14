-- Define a function that takes a value and multiplies it by 3.

question2Function :: Integer -> Integer
question2Function x = multi x
    where  
    multi x = (x * 3)

main :: IO ()
main = do
    let x = 1
    print (question2Function x)