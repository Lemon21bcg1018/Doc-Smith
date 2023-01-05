from flask import Blueprint, render_template,request,redirect,session,url_for

sec= Blueprint("second",__name__, static_folder="static",template_folder="templates")


@sec.route('/')

@sec.route("/s_name", methods=['GET', 'POST'])
def s_name():
    if request.method == "POST":
        s_name = request.form["s_name"]
        session["s_name"] = s_name
        return redirect("/sec/r_name")
    else:
        return render_template('senders_name.html')

@sec.route("/r_name", methods=['GET', 'POST'])
def r_name():
    if request.method == "POST":
        r_name = request.form["r_name"]
        session["r_name"] = r_name
        return redirect("/sec/r_add")
    else:
        return render_template('recivers_name.html')

@sec.route("/r_add", methods=['GET', 'POST'])
def r_add():
    if request.method == "POST":
        r_add = request.form["r_address"]
        session["r_add"] = r_add
        return redirect(("/sec/date"))
    else:
        return render_template('recivers_address.html')


@sec.route("/date", methods=['GET', 'POST'])
def date():
    if request.method == "POST":
        date = request.form["date"]
        session["date"] = date
        return redirect("/sec/pf")
    else:
        return render_template('date.html')

@sec.route("/pf", methods=['GET', 'POST'])
def pf():
    if request.method == "POST":
        p_f = request.form["p_f"]
        session["p_f"] = p_f
        return redirect("/sec/pm")
    else:
        return render_template('paragraph_f.html')

@sec.route("/pm", methods=['GET', 'POST'])
def pm():
    if request.method == "POST":
        p_m = request.form["p_m"]
        session["p_m"] = p_m
        return redirect("/sec/pl")
    else:
        return render_template('paragraph_m.html')


@sec.route("/pl", methods=['GET', 'POST'])
def pl():
    if request.method == "POST":
        p_l = request.form["p_l"]
        session["p_l"] = p_l
        return redirect("/sec/res")
    else:
        return render_template('paragraph_l.html')

@sec.route("/res", methods=['GET', 'POST'])
def result():
    
    s_name = ((session["s_name"]).capitalize())
    date = ((session["date"]).capitalize())
    r_name = ((session["r_name"]).capitalize())
    r_add = ((session["r_add"]).capitalize())
    p_f = session["p_f"]
    p_m = session["p_m"]
    p_l = session["p_l"]
    result = f"""
{r_add}

{date}

Dear {r_name},

{p_f}
{p_m}
{p_l}

Take Care,

With Love,

{s_name}
"""

    return render_template('result.html', result=result)