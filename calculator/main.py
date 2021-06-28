from flask import Flask, request, abort
import calc_functions as calc_functions


def read_number(number_id):
    number = input("Please enter a number {}:  ".format(number_id))

    return int(number)

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the app"

@app.route('/add/<int:number1>/<int:number2>')
def perform_add(number1, number2):
    number3 = calc_functions.add(number1, number2)
    return str(number3)

# using query string
# URL: 127.0.0.1:5000/add?num1=1&num2=2
@app.route('/add')
def perform_add_query():
    number1 = request.args.get('num1', type=int, default=0) #Say you want the request to be an Intergar and if user doesn't provide into it will use the default
    number2 = int(request.args.get('num2'))

    if number1 is None or number2 is None:#if the user passes a str instead of int it will display the error stated below
        abort(400)
    number3 = calc_functions.add(number1,number2)
    return str(number3)




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0') # allows it recieve all teh connections on the same container
    #number1 = read_number(1)
    #number2 = read_number(2)

#    result = calc_functions.add(number1, number2)
#    print(result)
