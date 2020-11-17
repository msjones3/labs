# validate inputs
Validating inputs is important to help users fix their mistakes, ensure the data we enter into the database is of high quality and consistency, and to prevent malicious attacks (e.g. SQL injection)

{% next %}

Let's assume we need to collect the following data:
- username
- password
- number
- email

{% next %}
# write isEmpty() function
Let's assume that the user is going to input their username.  
We need to first make sure they haven't left this form blank.  
You must write the code for the function isEmpty().  
This function should take in a paramaeter called 'input' and will return True if the input is blank, and False if the input isn't blank. 

### requirements
- returns True if blank
- will work on both strings and numbers

### example usage
- isEmpty('myusername') evaluates to False
- isEmpty('') evaluates to True
- isEmpty(3) evaluates to False
- isEmpty('     ') evaluates to True

Make sure to test all possible inputs, e.g.
- print(isEmpty('myusername'))

{% next %}

Validate the number so that it must be between 1 and 10. 

# Check to see if number is valid
Write a function called numberValid(input) that takes in a number and returns true if the number is an integer between 1 and 10. 
### requirements
- input must be an integer
- input must be an integer between 1 and 10 

## example usage
- numberValid(20) returns False
- numberValid('a') returns False
- numberValid(10) returns True
- numberValid(0) returns False
- numberValid(-3) returns False

{% spoiler "Hint" %} To check to see if the number is an integer, consider using a 'try' {% endspoiler %}

{% next %}
# Check to see if the username and password are correct
Write a function called credentialsValid() to check to see if a username and password are correct  
Let's assume that the correct username is 'admin' and the correct password is 'secret'
### requirements
- takes in 2 parameters: username and password
- returns True if the username is 'admin' and the password is 'secret
### example usage
- credentialsValid('wrong', 'secret') returns False
- credentialsValid('admin', 'secret') returns True
- credentialsValid(3, 4) returns False
- credentialsValid('admin', 'wrong') returns False

{% next %}

# Show Error Messages
The second file in your file manager is one called checkErrors.py  
This will run all the tests you wrote previously on your form data and provide useful feedback to the user on how they can improve their code.  
We don't have a form at the moment. However, we will simulate a form by creating a dictionary to store our data. Look in the file for the dictionary.   
## how to access values from a dictionary
run the following print statement to see how we can access values from the dictionary:  
`print(form['username'])`  
We can also use this dictionary value as an input in a function.  
For example, let's run our isEmpty() function on the form data:  
`print(isEmpty(form['username'])`


{% next %}
# Check entire form for errors
Look closely at the function called evaluateErrors()  
This will provide some feedback to the user.  
Run the code as is:  
`print(evaluateErrors(myForm))`  
then try changing the values of the form to see how the output changes. 
{% next %}

# print each error on one line
Instead of printing an ugly list, loop through the errors and print individually.  

{% spoiler "Hint" %}
The errors are saved in a variable called 'errors'  
Loop through the errors list by using a for loop  
`for error in errors:`  
`   print(error)`  
{% endspoiler %}  
{% next %}

# Add the code to check credentials
Update the evaluateErrors() code so that it checks to see if the credentials are valid.  
If they are, print 'login successful' and if they are not, add the error 'credentials invalid' to the error messages displayed


{% spoiler "Solution" %} Just kidding - I'm not giving you the solution. BUT... here's a cool video!
{% video https://www.youtube.com/watch?v=oHg5SJYRHA0 %}
{% endspoiler %}


