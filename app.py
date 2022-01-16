from flask import Flask, render_template, redirect, request, url_for, session

from rasch import Reshenie

app = Flask(__name__)
app.secret_key = 'helloooo'


@app.route('/', methods=['GET', 'POST'])
def main():
    session['data'] = []
    ctr = 0
    if request.method == 'POST':
        for i in range(1, 12):
            try:
                session['data'].append(float(request.form.get('f' + str(i - 1))))
            except ValueError:
                ctr += 1
                continue
        if ctr <= 7:
            return redirect(url_for('rasch'))
    return render_template('main.html')


@app.route('/rasch')
def rasch():
    session['a'] = Reshenie(session['data'])
    session['a'] = session['a'].get_pogr()
    return render_template('reshen.html', data=session['a'][1], data_p=session['a'][2], poln=session['a'][0],
                           vilit=session['a'][3], vilit_z=session['a'][4], vilit_sr=session['a'][5],
                           vilit_sko=session['a'][6], sr=session['a'][7], sko=session['a'][8], sr_sko=session['a'][9],
                           ochen_pogr=session['a'][10], pribor=session['a'][11])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
