from flask import Flask, render_template, request, redirect, flash, send_file
from config.lbvserver import nitro_vserver
from config.lbvserver_binding import nitro_vserver_binding
from config.file import save_to_file


app = Flask("SLBInfo")

db = []      

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lbvserver")
def lbvserver():
    l4_name = request.args.get("name")
    l4_ip = request.args.get("ip")
    if l4_name == None:
        return redirect("/")
    elif l4_ip == None:
        return redirect("/")
    for i in db:
        if i['name'] == l4_name or i['ip'] == l4_ip:
            l4_info = i
            lbvservers = nitro_vserver(l4_info)
            return render_template("lbvserver.html", lbvservers=lbvservers, l4_name=l4_name, l4_ip=l4_ip)
    return redirect("/")
        
    

@app.route("/lbvserver_binding")
def lbvserver_binding():
    l4_name = request.args.get("name")
    l4_ip = request.args.get("ip")
    l4_vserver = request.args.get("vserver")
    for i in db:
        if i['name'] == l4_name or i['ip'] == l4_ip:
            l4_info = i
            lbvserver_binding = nitro_vserver_binding(l4_info, l4_vserver)
            print(lbvserver_binding)
            return render_template("lbvserver_binding.html", lbvserver_binding=lbvserver_binding, l4_name=l4_name, l4_ip=l4_ip) 
    if l4_name == None:
        return redirect("/")
    elif l4_ip == None:
        return redirect("/")
    elif l4_vserver == None:
        return redirect("/")

@app.route("/export")
def export():
    l4_name = request.args.get("name")
    l4_ip = request.args.get("ip")
    if l4_name == None:
        return redirect("/")
    elif l4_ip == None:
        return redirect("/")
    for i in db:
        if i['name'] == l4_name or i['ip'] == l4_ip:
            l4_info = i
            lbvserver = nitro_vserver(l4_info)
            save_to_file(l4_info, lbvserver)
    return send_file(f"{l4_name}.csv", as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), {"Refresh": "2; url=/"}

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), {"Refresh": "2; url=/"}
      

app.run("0.0.0.0")
