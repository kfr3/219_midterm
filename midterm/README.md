This README file will have an explanation for my code and link to my demo video.

I used the Command design patterns by utilizing Commands for the calculator functions, like add, subtract, multiply, and divide. By using commands, I only had to write the function for the calculator operations once, and then just references the commands where I needed them in my project. That way, the code was more organized and I could reference the code for each operation function in one place. 
I used logging in my code in place of print statements so it is less cluttered, and I am able track each command that is used in the application in the logging folder.
I used environment variables in this program (app __init__ ) so I didn't have to hardcode the configuration, and have the ability to change it later on. 
I used the EAFP principle by using try and except blocks in the function class commands so that if there was an error, the program would be able to handle it. I used the LBYL principle in a similar way by preparing try and except blocks for the function classes in case the user inputted something incorrectly, like not inputting a number or trying to divide by zero. I also used this in the clear function for the csv file by having an if statement. 


Link to youtube demo video: https://youtu.be/eeLFkNFx1I8