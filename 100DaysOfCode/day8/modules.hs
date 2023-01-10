module Modules (hello, leapYear) where

    hello :: String
    hello = "Test"

    leapYear :: Integer -> Bool
    leapYear x = isLeap x
        where  
        isLeap x = x `mod` 4 == 0

