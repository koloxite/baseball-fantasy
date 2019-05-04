import configparser
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
import mysql.connector

# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')

# Set up application server.
app = Flask(__name__)
app.secret_key = "super secret key"
# Create a function for fetching data from the database.
def sql_query(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def sql_execute(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

# For this example you can select a handler function by
# uncommenting one of the @app.route decorators.

#@app.route('/')
def Login():
    return render_template('FantasyPickerLogin.html')

@app.route('/FantasyPickerLogin.html')
def Login_Link():
    return render_template('FantasyPickerLogin.html')

@app.route('/', methods=['GET', 'POST'])
def Main_Menu():
    if request.method == 'POST':
        if(request.form['flag']=='add'):
            x=0
        else:
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            HR = request.form['HR']
            if HR == "": HR = "0"
            BA = request.form['BA']
            if BA == "": BA = "0"
            ERA = request.form['ERA']
            if ERA == "": ERA = "10000"
            SLG = request.form['SLG']
            if SLG == "": SLG = "0"
            OBP = request.form['OBP']
            if OBP == "": OBP = "0"
            Wins = request.form['wins']
            if Wins == "": Wins = "0"
            Losses = request.form['losses']
            if Losses == "": Losses = "10000"
            SO = request.form['SO']
            if SO == "": SO = "0"
            WHIP = request.form['WHIP']
            if WHIP == "": WHIP = "0"
            POS = request.form['POS']
            if POS == "All": POS = ""
            #print(HR)
            sql = "SELECT * FROM player WHERE first_name LIKE '" + firstName + "%' AND last_name LIKE '" + lastName + "%' AND (HR >= " + HR + " OR HR IS NULL)" + \
            " AND (BA >= " + BA + " OR BA IS NULL)" + \
            " AND (ERA <=" + ERA + " OR ERA IS NULL)" +\
            " AND (SLG >= " + SLG + " OR SLG IS NULL)" +\
            " AND (OBP >= " + OBP + " OR OBP IS NULL)" + \
            " AND (W >= " + Wins + " OR W IS NULL)" + \
            " AND (L <= " + Losses + " OR L IS NULL)" + \
            " AND (SO >= " + SO + " OR SO IS NULL)" + \
            " AND (WHIP >= " + WHIP + " OR WHIP IS NULL)" + \
            " AND pos LIKE '" + POS + "%';"
            #rs = sql_query(sql)

            p=[]
            b=[]
            rs=[(1,"Chrisopher","Davis","BAL","2B",470,40,79,16,49,2,0.168,.243,.539,.296,"","",""),(2,"jacop","degron","NYM","P","","","","","","","","","","",10,9,1.7,32,32,0,217,269,.91),(2,"Chrisopher","Davis","BAL","2B",470,40,79,16,49,2,0.168,.243,.539,.296,"","",""),(2,"jacop","degron","NYM","P","","","","","","","","","","",10,9,1.7,32,32,0,217,269,.91)]
            for row in rs:
                if row[4]=="P":
                    p.append(row)
                else:
                    b.append(row)
                session.clear()
                session['p']=p
                session['b']=b



        return redirect(url_for('Main_Menu'))
    return render_template('FantasyPicker.html')

@app.route('/FantasyPickerMyTeam.html')
def My_Team():
	return render_template('FantasyPickerMyTeam.html')

#@app.route('/', methods=['GET', 'POST'])
def template_response_with_data():
	sql = "select * from player where first_name like 'first_name+%' and last_name like 'last_name+%'"
	players = sql_query(sql)
	print(players)
	return render_template('FantasyPickerLogin.html')

if __name__ == '__main__':
    app.run(**config['app'])
