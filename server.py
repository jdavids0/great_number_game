from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'Rand0m$!'

@app.route ('/')
def index():
        if "comp_num" not in session:
            session['comp_num'] = random.randint(1,100)
            session['message'] = "Take a shot!"
            session['count'] = 0
        return render_template ('index.html', message = session['message'], count = session['count'])

@app.route ('/guess', methods=['POST'])
def guess():
    print(request.form['guess_num'])

    session['count'] += 1

    if len(request.form['guess_num']) < 1:
        print("Guess!")
        session['message'] = "Take a Shot!"
        return redirect('/')
    guess_num = int(request.form['guess_num'])
    comp_num = session['comp_num']

    if guess_num < comp_num:
        print ("Too low! Take another shot!")
        session['message'] = "Too low! Take another shot!"
    elif guess_num > comp_num:
        print("Too high! Take another shot!")
        session['message'] = "Too high! Take another shot!"
    else:
        print("Nailed it!")
        session['message'] = "Nailed it!"

    # session ['guess_num'] = int(request.form['guess-num'])
    return redirect ('/')

@app.route ('/clear')
def clear_session():
    session.clear()
    return redirect ('/')

if __name__=="__main__":
    app.run(debug=True, port=5001) 