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

# to do
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

# to do
Write a function called numberInvalid(input) that takes in a number and returns true if the number is not between 1 and 10. 

{% spoiler "Hint" %} You're really not going to like it. {% endspoiler %}

{% spoiler "Solution" %} Forty-two. {% endspoiler %}

{% video https://www.youtube.com/watch?v=oHg5SJYRHA0 %}
