-- Thanks ChatGPT! (and the_lazer_aio)
main :: IO ()
main = do
  let a = "test"
  let b = "hannah"    

  if a == b then
    putStrLn "It's a palindrome!"
  else
    putStrLn "Not a palindrome"