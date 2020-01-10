The goal of this lab is to explore the infinite monkey theorem using python functions. The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. The following python code runs this experiment by generating random letters from the alphabet and comparing it to our target sentence. The target sentence is: “methinks it is like a weasel”.

The program will then compare the random letters to our target sentence and will score each try. If the score is not 100% it will try again, constantly updating the best score and letters every 100 tries. As expected, this can take a very long time to finally complete depending on the target string but in the end it was able to prove the thereom.

Overall the python function was able to find a perfect match eventually but it took a very large amount of iterations to do so and thus a very long time.


monkeyTypist()
String   Score  Try
leapiextfwsuxsrdknokxgcpjdgs    10.714286 0
methinks it isolike a weasel    96.428571 100
methinks it is like a weasel    100.000000 145
