{- Write a function that checks if the monthly consumption of an electrical device is bigger,
equal, or smaller than the maximum allowed and returns a message accordingly. 
The function has to take the hourly consumption of an electrical device, 
the hours of daily use, and the maximum monthly consumption allowed.
    (Monthly usage = consumption (kW) * hours of daily use (h) * 30 days).-}

--import Mod1

main :: IO ()
main = do
    let w = 5000
    let hours = 3
    let kWh = hours * w
    let mUse = kWh * 30
    let maxWHrsPerMonth = 4200000

    if mUse > maxWHrsPerMonth then putStrLn "Your monthly consumption is bigger than the maximum allowed."
    else if mUse == maxWHrsPerMonth then putStrLn "Your monthly consumption is equal to the maximum allowed."
    else putStrLn "Your monthly consumption is smaller than the maximum allowed."