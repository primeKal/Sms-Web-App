# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request, flash, redirect
import sender as send
import sqlconnector as sql
from random import randint
import json
import SMPPApi.smpp_server_managers as smpps
from threading import Thread

def sendinit(uname, pwd, num, mes, type2):
    re = send.send_same_message_to_many(uname, pwd, mes, num)
    nu = num[0] + "," + num[1] + "," + num[2]
    res = re.json()
    mid = res['data']['batchId']
    print(res)
    print(type(res))
    print(nu)
    print(type(nu))
    sql.save_data(randint(1, 10000000), "1111", nu, mes, mid, type2)


def sendsing(uname, pwd, num, message, type):
    res = send.sendSingle(uname, pwd, num, message)

    res = res[7:]
    sql.save_data(randint(1, 1000000), "1111", num, message, res, type)


headings = ("No", "Sender", "Destination", "Message", "Mid", "Api")


def fetch_datas():
    data = sql.fetch_all_list()
    data = tuple(data)
    print(data)
    return data


def fetch_data(no):
    re = sql.fetcha_data(no=no)
    return re


def create_app():

    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/send", methods=["POST"])
    def send():
        print("send selected")
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        sms = request.form["sms"]
        number = request.form["number"]
        type = request.form['options']
        print(sms + " :: " + number)
        sendsing(uname, pwd, number, sms, type)
        flash("sms sent and saved")
        return render_template("sendasms.html")

    @app.route("/multi", methods=["POST"])
    def send_multi():
        print("sending many")
        uname = request.form["uname2"]
        pwd = request.form["pwd2"]
        sms = request.form["message"]
        num1 = request.form["number1"]
        num2 = request.form["number2"]
        num3 = request.form["number3"]
        type2 = request.form['options2']
        print(sms + ":::" + num1 + "," + num2 + "," + num3)
        numbers = [num1, num2, num3]
        sendinit(uname, pwd, numbers, sms, type2)
        flash("sms sent and saved")
        return render_template("tomany.html")

    @app.route("/ad_send", methods=["POST"])
    def send_adv():
        print("starting advanced send")
        uname = request.form["uname2"]
        pwd = request.form["pwd2"]
        sms = request.form["message"]
        type2 = request.form['options2']
        #numbers = request.form.getlist("numbers")
        numbers= request.args.get("numbers")
        print(numbers)
        #print(numbers)
        # sendinit(uname, pwd, numbers, sms, type2)
        # flash("sms sent and saved")
        return render_template("advansced.html")

    @app.route("/messages")
    def to_messages():
        return render_template("messages.html", headings=headings, data=fetch_datas())

    @app.route("/message/<no>")
    def to_message(no):
        print(no)
        return render_template("message.html", data=fetch_data(no))
    @app.route("/single")
    def to_single():
        return render_template("sendasms.html")

    @app.route("/many")
    def to_many():
        return render_template("tomany.html")

    @app.route("/advanced")
    def to_advanced():
        return render_template("advanced.html", headings=sql.fetch_sener(), data=sql.fetch_destinations())

    @app.route("/rcv")
    def to_rcv():
        smpps.bind_client()
        return render_template("mo.html", headings=sql.fetch_mo())

    @app.route("/rcvrs")
    def to_rcvrs():
        return render_template("mo.html", headings=sql.fetch_mo())

    app.static_folder = 'static'

    return app


app = create_app()
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.run(threaded=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
