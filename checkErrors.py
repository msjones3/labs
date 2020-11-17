from validate import isEmpty, numberValid, credentialsValid


myForm = {
    'username': 'x',
    'password': 'x', 
    'number': 20, 
    'email': ''
    }

def evaluateErrors(form):
    errors = []
    for item in form:
        if isEmpty(form[item]):
            errors.append(f'{item} cannot be blank')
    if not numberValid(form['number']):
        errors.append('number must be between 1 and 10. If you would like to purchase more tickets, please ring us.')
    return(errors)

errors = evaluateErrors(myForm)
for error in errors:
    print(error)
