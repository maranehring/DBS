main =
 do 
  putStrLn ("Wie heissen Sie?") --Print "Wie heissen Sie?"
  k <- getLine --Nimm die Eingabe k als String auf
  putStrLn("Hallo " ++ k ++ "!") --Print "Hallo k!"
