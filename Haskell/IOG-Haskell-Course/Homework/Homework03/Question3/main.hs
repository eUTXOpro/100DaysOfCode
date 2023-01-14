
main :: IO ()
main = do
    let xs = [1,2,3,4,5]
    print (calculateSum xs)

calculateSum :: [Int] -> Int
calculateSum xs = 
    let 
        squared = map (^2) xs
        cubed = map (^3) xs
        sumSquared = sum squared
        sumCubed = sum cubed
    in sumSquared + sumCubed
