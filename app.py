from flask import Flask, render_template, Response, g, current_app as app, make_response

app = Flask(__name__)

import os
import os.path
import requests
import time
import csv
data = {'Band': 'x', 'Name': 'xxx', 'Location': 'xxx', 'In_Time': "1", 'Out_Time': "2", 'Date': "15"}
ifttt_key = "iYiYhj3KyPFEwyVRuJzEb"


app = Flask(__name__)

dome1 = []
dome2 = []
dome3 = []
dome4 = []
area = []

@app.route('/')
def page():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')



@app.route('/live')
def status():
    area.append(os.environ.get("beacon1"))
    area.append(os.environ.get("beacon2"))
    area.append(os.environ.get("beacon3"))
    area.append(os.environ.get("beacon4"))
    return render_template('responsive.html', dome1=dome1, dome2=dome2, dome3=dome3, dome4=dome4, area=area)


       
@app.route("/download")
def download():
    return render_template('download.html')

@app.route("/getPlotCSV")
def getPlotCSV():
    csv = 'foo,bar,baz\nhai,bai,crai\n'
    response = make_response(csv)
    cd = 'attachment; filename=flask-demooutput.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype='text/csv'

    return response
   
def email_alert(key, band_id, person_name, location):
    report = {}
    report["value1"] = band_id
    report["value2"] = person_name
    report["value3"] = location
  
    requests.post("https://maker.ifttt.com/trigger/update_sheet/with/key/" + str(key), data=report)    

@app.route('/<device_id>/<person_id>')
def trackPerson(device_id, person_id):
    g.device_id = device_id
    g.person_id = person_id
    person_name = os.environ.get(g.person_id)
    location = os.environ.get(g.device_id)
    if person_name != data['Name'] or location != data['Location']:
       data['Location'] = location
       data['Name'] = person_name
       data['Band'] = g.person_id
       if g.device_id == "beacon1":
          if person_name not in dome1:  
             email_alert(ifttt_key, data['Band'],data['Name'],data['Location'])
       if g.device_id == "beacon2":
          if person_name not in dome2:  
             email_alert(ifttt_key, data['Band'],data['Name'],data['Location'])
       if g.device_id == "beacon3":
          if person_name not in dome3:  
             email_alert(ifttt_key, data['Band'],data['Name'],data['Location'])
       if g.device_id == "beacon4":
          if person_name not in dome4:  
             email_alert(ifttt_key, data['Band'],data['Name'],data['Location'])         
    data['Location'] = location
    data['Name'] = person_name
    data['Band'] = g.person_id
    if g.device_id == "beacon1":
       if person_name not in  dome1:
          dome1.append(person_name)
       if person_name in dome2:
          dome2.remove(person_name)
       if person_name in dome3:
          dome3.remove(person_name)
       if person_name in dome4:
          dome4.remove(person_name)

    if g.device_id == "beacon2":
       if person_name not in  dome2:
          dome2.append(person_name)
       if person_name in dome3:
          dome3.remove(person_name)
       if person_name in dome4:
          dome4.remove(person_name)
       if person_name in dome1:
          dome1.remove(person_name)

    if g.device_id == "beacon3":
       if person_name not in  dome3:
          dome3.append(person_name)
       if person_name in dome2:
          dome2.remove(person_name)
       if person_name in dome1:
          dome1.remove(person_name)
       if person_name in dome4:
          dome4.remove(person_name)
    if g.device_id == "beacon4":
       if person_name not in  dome4:
          dome4.append(person_name)
       if person_name in dome2:
          dome2.remove(person_name)
       if person_name in dome3:
          dome3.remove(person_name)
       if person_name in dome1:
          dome1.remove(person_name)
    

         
    return "<h3> OK </h3>" 
    '''
    file_basename = 'output.csv'
    server_path = os.path.dirname(os.path.abspath(__file__))
    file_exists = os.path.isfile(server_path+file_basename)
    w_file = open(server_path+file_basename, 'a')

    if not file_exists:
        w_file.write('Band,Name,Location,In-Time,Out_Time,Date \n')
        w_file.write('%s,%s,%s,%s,%s,%s \n' %(data['Band'],data['Name'],data['Location'],data['In_Time'],data['Out_Time'],data['Date']))

    #for row, x in data.items():
     #   x_as_string = str(x)
      #  w_file.write(x_as_string+ '\n')
    else:
        w_file.write('%s,%s,%s,%s,%s,%s \n' %(data['Band'],data['Name'],data['Location'],data['In_Time'],data['Out_Time'],data['Date']))
    w_file.close()
'''
       



if __name__ == '__main__':
    app.run(debug=True)



