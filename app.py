from flask import Flask, render_template, request, url_for, redirect, session
from second import sec
# def returnapp():
app = Flask(__name__)

app.secret_key = "218632"

app.register_blueprint(sec, url_prefix="/sec")


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/s_name", methods=['GET', 'POST'])
def s_name():
    if request.method == "POST":
        s_name = request.form["s_name"]
        session["s_name"] = s_name
        return redirect(url_for("s_add"))
    else:
        return render_template('senders_name.html')


@app.route("/s_add", methods=['GET', 'POST'])
def s_add():
    if request.method == "POST":
        s_add = request.form["s_add"]
        session["s_add"] = s_add
        return redirect(url_for("date"))
    else:
        return render_template('senders_address.html')


@app.route("/date", methods=['GET', 'POST'])
def date():
    if request.method == "POST":
        date = request.form["date"]
        session["date"] = date
        return redirect(url_for("r_name"))
    else:
        return render_template('date.html')


@app.route("/r_name", methods=['GET', 'POST'])
def r_name():
    if request.method == "POST":
        r_name = request.form["r_name"]
        session["r_name"] = r_name
        return redirect(url_for("r_add"))
    else:
        return render_template('recivers_name.html')


@app.route("/r_add", methods=['GET', 'POST'])
def r_add():
    if request.method == "POST":
        r_add = request.form["r_address"]
        session["r_add"] = r_add
        return redirect(url_for("r_des"))
    else:
        return render_template('recivers_address.html')


@app.route("/r_des", methods=['GET', 'POST'])
def r_des():
    if request.method == "POST":
        r_des = request.form["r_designation"]
        session["r_des"] = r_des
        return redirect(url_for("company_name"))
    else:
        return render_template('recivers_designation.html')


@app.route("/company_name", methods=['GET', 'POST'])
def company_name():
    if request.method == "POST":
        c_name = request.form["c_name"]
        session["c_name"] = c_name
        return redirect(url_for("subject"))
    else:
        return render_template('company_name.html')


@app.route("/subject", methods=['GET', 'POST'])
def subject():
    if request.method == "POST":
        subject = request.form["subject"]
        session["subject"] = subject
        return redirect(url_for("gender"))
    else:
        return render_template('subject.html')


@app.route("/gender", methods=['GET', 'POST'])
def gender():
    if request.method == "POST":
        gender = request.form["gender"]
        session["gender"] = gender
        return redirect(url_for("pf"))
    else:
        return render_template('gender.html')


@app.route("/pf", methods=['GET', 'POST'])
def pf():
    if request.method == "POST":
        p_f = request.form["p_f"]
        session["p_f"] = p_f
        return redirect(url_for("pm"))
    else:
        return render_template('paragraph_f.html')


@app.route("/pm", methods=['GET', 'POST'])
def pm():
    if request.method == "POST":
        p_m = request.form["p_m"]
        session["p_m"] = p_m
        return redirect(url_for("pl"))
    else:
        return render_template('paragraph_m.html')


@app.route("/pl", methods=['GET', 'POST'])
def pl():
    if request.method == "POST":
        p_l = request.form["p_l"]
        session["p_l"] = p_l
        return redirect(url_for("result"))
    else:
        return render_template('paragraph_l.html')


@app.route("/res", methods=['GET', 'POST'])
def result():
    
    s_name = ((session["s_name"]).capitalize())
    s_add = ((session["s_add"]).capitalize())
    date = ((session["date"]).capitalize())
    r_name = ((session["r_name"]).capitalize())
    r_add = ((session["r_add"]).capitalize())
    r_des = ((session["r_des"]).capitalize())
    c_name = ((session["c_name"]).capitalize())
    subject = ((session["subject"]).capitalize())
    gender = session["gender"]
    p_f = session["p_f"]
    p_m = session["p_m"]
    p_l = session["p_l"]

    result = f"""
{s_name}
{s_add}
{date}
{r_name}
{r_add}
{r_des}
{c_name}
{subject}
{gender}
    {p_f}   
    {p_m}   
    {p_l}
sincerly,
{s_name}
    """

    return render_template('result.html', result=result)


app.run(debug=False)
