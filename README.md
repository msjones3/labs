# validate inputs
Validating inputs is important to help users fix their mistakes, ensure the data we enter into the database is of high quality and consistency, and to prevent malicious attacks (e.g. SQL injection)

{% next %}

We have created a form that is going to return the following fields:
- username
- password
- number
- email

Let's start the validation by making sure every form has been filled out. 

{% next %}

# Check to see if fields are empty
Write a function called isEmpty(input), which takes a parameter called 'input'.
It should return True if the field is blank and will return False if the field has been filled out. 

## example usage
username = ''
password = 'mypassword'
email = '     '

- isempty(username) evaluates to True
- isempty(password) evaluates to False
- isempty(email) evaluates to True

Make sure to test all possible inputs

{% next %}

Validate the number so that it must be between 1 and 10. 

# Check to see if number invalid
Write a function called numberValid(input) that takes in a number and returns true if the number is an integer between 1 and 10. 

## example usage
- numberValid(20) returns False
- numberValid('a') returns False
- numberValid(10) returns True
- numberValid(0) returns False
- numberValid(-3) returns False

{% spoiler "Hint" %} To check to see if the number is an integer, consider using a 'try' {% endspoiler %}
# Run all Tests and show error messages
Write a function called checkErrors(form) that will take in a dictionary  

{% spoiler "Solution" %} Just kidding - I'm not giving you the solution. BUT... you've been Rick Rolled
{% video https://www.youtube.com/watch?v=oHg5SJYRHA0 %}
{% endspoiler %}


