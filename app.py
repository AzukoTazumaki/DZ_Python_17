from flask import Flask, render_template, request, redirect
from werkzeug.exceptions import BadRequest
from exercises import Exercises

app = Flask(__name__)
ex = Exercises()


@app.route('/')
def home_page():
    return render_template('main/main_page.html')


@app.route('/ex_1', methods=['POST', 'GET'])
def ex_1():
    if request.method == 'GET':
        return render_template('ex_1/ex_1.html')
    return render_template('ex_1/ex_1.html',
                           ex_1_result=ex.ex_1(request.form['numbers_list']))


@app.route('/ex_2', methods=['POST', 'GET'])
def ex_2():
    if request.method == 'GET':
        return render_template('ex_2/ex_2_form.html')
    else:
        ex_2_dict = {
            'estimates': request.form['estimates'],
            'number_of_estimate': request.form['number_of_estimate'],
            'new_estimate': request.form['new_estimate'],
            'sort': request.form['options']
        }
        return render_template('ex_2/ex_2_answer.html',
                               ex_2_result=ex.ex_2(ex_2_dict))


@app.route('/ex_3', methods=['POST', 'GET'])
def ex_3():
    if request.method == 'GET':
        return render_template('ex_3/ex_3.html')
    return render_template('ex_3/ex_3.html',
                           ex_3_result=ex.ex_3(request.form['length_of_list']))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return render_template('errors/bad_request.html'), 400


if __name__ == '__main__':
    app.run(debug=True)
