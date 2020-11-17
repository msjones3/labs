from validate import isEmpty, numberValid, credentialsValid


myForm = {
    'username': 'x',
    'password': 'x', 
    'number': 20, 
    'email': ''
    }

def evaluateErrors(form):
    # takes in a dictionary
    # return a list of errors on running the tests in validate.py on given form values
    errors = []
    for item in form:
        if isEmpty(form[item]):
            errors.append(f'{item} cannot be blank')
    if not numberValid(form['number']):
        errors.append('number must be between 1 and 10. If you would like to purchase more tickets, please ring us.')
    # to do: add the credentialsValid check here!
    return(errors)

errors = evaluateErrors(myForm)

