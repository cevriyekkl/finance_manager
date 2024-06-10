from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Login failed. Please try again.', 'danger')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

    