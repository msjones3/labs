from validate import isEmpty, numberValid, credentialsValid


myForm = {
    'username': 'x',
    'password': 'x', 
    'number': 3, 
    'email': 'x'
    }

def evaluateErrors(form):
    errors = []
    for item in form:
        if isEmpty(form[item]):
            errors.append(f'{item} cannot be blank')
    if not numberValid(form['number']):
        errors.append('number must be between 1 and 10. If you would like to purchase more tickets, please ring us.')
    if not credentialsValid(form['username'], form['password']):
        errors.append('credentials invalid')
    if len(errors) < 1:
        errors.append('login successful')
    return(errors)

errors = evaluateErrors(myForm)
for error in errors:
    print(error)
