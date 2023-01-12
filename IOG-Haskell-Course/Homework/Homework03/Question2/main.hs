

main :: IO ()
main = do
    let w = 5000
    let hours = 3
    let kWh = hours * w
    let mUse = kWh * 30
    let maxWHrsPerMonth = 420000
    
    print mUse
    print maxWHrsPerMonth 
    putStrLn (calcAndPrint mUse maxWHrsPerMonth)

calcAndPrint :: Int -> Int -> String 
calcAndPrint mUse maxWHrsPerMonth = 
    let remainingPower = (mUse - maxWHrsPerMonth) in 
    if remainingPower > 0 
        then "Your monthly consumption is bigger than the maximum allowed by " ++ show remainingPower  ++ " units"
    else if remainingPower == 0 
        then "Your monthly consumption is equal to the maximum allowed."
    else 
        "Your monthly consumption is smaller than the maximum allowed by " ++ show remainingPower  ++ " units"