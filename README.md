# validate inputs
Validating inputs is important to help users fix their mistakes, ensure the data we enter into the database is of high quality and consistency, and to prevent malicious attacks (e.g. SQL injection)

{% next %}

Let's assume we need to collect the following data:
- username
- password
- number
- email

{% next %}

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
Write a function called credentialsValid() to check to see if a username and password are correct \n
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

# Run all Tests and show error messages
We don't have a form at the moment. However, we will simulate a form by creating a dictionary to store our data. Place the following dictionary in the code:  
`form = {'username': '', 'password':'wrong', 'number: 20, 'email':''}`
{% next %}
## check the form to see if any values are blank
Let's use the code we wrote called isEmpty().\n
- Call the function with the value of the key 'username' as the input.
- if the result is False, print('username cannot be blank')
{% spoiler "hint" %}
This is how you call the function:  
`isEmpty(form['username'])`
{% endspoiler %}

{% next %}
# Check entire form for errors
Copy this code. 
  
`def evaluateErrors(form):`
  `errors = []`
  `for item in form:`
    `if isEmpty(form[item]):`
      `errors.append(f'{item} cannot be blank')`
  `if not numberValid(form['number']):`
    `errors.append('number must be between 1 and 10. If you would like to purchase more tickets, please ring us.')`
  `return errors`
  
{% next %}
Study the code you just entered for understanding.  
run the code as is `print(evaluateErrors(form))`, then try changing the values of the form to see how the output changes. 
{% next %}

# Add the code to check credentials
Update the evaluateErrors() code so that it checks to see if the credentials are valid.  
If they are, print 'login successful' and if they are not, add the error 'credentials invalid' to the error messages displayed


{% spoiler "Solution" %} Just kidding - I'm not giving you the solution. BUT... here's a cool video!
{% video https://www.youtube.com/watch?v=oHg5SJYRHA0 %}
{% endspoiler %}


