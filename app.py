from flask import Flask, render_template, Response, g, current_app as app

app = Flask(__name__)

import os



app = Flask(__name__)

dome1 = []
dome2 = []
dome3 = []
dome4 = []


@app.route('/')
def page():
   return render_template('index.html')

@app.route('/live')
def status():
    return render_template('responsive.html', dome1=dome1, dome2=dome2, dome3=dome3, dome4=dome4)


@app.route('/<device_id>/<person_id>')
def trackPerson(device_id, person_id):
    g.device_id = device_id
    g.person_id = person_id
    #person_name = os.environ.get(g.person_id)
    if g.device_id == "beacon1":
        dome1.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)

    if g.device_id == "beacon2":
        dome2.append(g.person_id)
        if g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
    if g.device_id == "beacon3":
        dome3.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)
    if g.device_id == "beacon4":
        dome4.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
    return "<h3> OK </h3>"

if __name__ == '__main__':
    app.run(debug=True)


