from flask import Flask, render_template, request, redirect, flash, send_file
from config.lbvserver import nitro_vserver
from config.lbvserver_binding import nitro_vserver_binding
from config.file import save_to_file


app = Flask("SLBInfo")

db = [{"name" : "BJENL401", "ip" : "203.240.73.252" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJENL402", "ip" : "203.240.74.252" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJENL403", "ip" : "172.16.72.125" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJENL404", "ip" : "172.16.72.252" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJENL405", "ip" : "172.16.80.125" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJENL406", "ip" : "172.16.80.252" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJENL407", "ip" : "172.16.68.220" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJENL408", "ip" : "172.16.68.221" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJVNL401", "ip" : "172.30.1.252" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJVNL402", "ip" : "172.30.1.253" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJVNL403", "ip" : "172.30.4.252" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJVNL404", "ip" : "172.30.5.252" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJVNL405", "ip" : "172.30.8.252" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJVNL406", "ip" : "172.30.9.252" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJVNL411", "ip" : "172.29.96.250" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJVNL412", "ip" : "172.29.96.252" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJINL401", "ip" : "172.16.18.12" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJINL402", "ip" : "172.16.18.13" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJINL409", "ip" : "172.16.13.12" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJINL410", "ip" : "172.16.13.13" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJINL403", "ip" : "172.16.16.12" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJINL404", "ip" : "172.16.16.13" , "id" : "nsroot" , "password" : "wkdb1100"},  
{"name" : "BJINL411", "ip" : "172.20.138.252" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJINL412", "ip" : "172.20.138.253" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJINGD01", "ip" : "172.16.25.12" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJINL407", "ip" : "172.16.4.8" , "id" : "nsroot" , "password" : "wkdb1100"},   
{"name" : "BJINL408", "ip" : "172.16.4.9" , "id" : "nsroot" , "password" : "wkdb1100"},   
{"name" : "BJHNL401", "ip" : "172.16.51.12" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJXNL401", "ip" : "172.20.201.12" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJXNL402", "ip" : "172.20.201.13" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJRNL401", "ip" : "172.16.65.16" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJRNL402", "ip" : "172.16.65.18" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJONLB01", "ip" : "172.20.244.45" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BRONLB01", "ip" : "172.20.244.77" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJINL401", "ip" : "172.16.150.12" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJINL402", "ip" : "172.16.150.13" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJINL403", "ip" : "172.16.155.12" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJINL404", "ip" : "172.16.155.13" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJINL405", "ip" : "172.16.151.12" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJINL406", "ip" : "172.16.151.13" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJINGD01", "ip" : "172.16.159.12" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "DJVNL407", "ip" : "172.29.27.12" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "DJVNL408", "ip" : "172.29.27.13" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "DJHNL401", "ip" : "172.21.12.12" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "DJHNL402", "ip" : "172.21.12.13" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJDNL401", "ip" : "172.20.2.8" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJDNL403", "ip" : "172.20.12.8" ,"id" : "ophnsjh0" , "password" : "fnxmfnxm123"},
{"name" : "BJDNL402", "ip" : "172.20.11.8" , "id" : "nsroot" , "password" : "wkdb1100"},
{"name" : "BJDNL404", "ip" : "172.20.15.8" , "id" : "nsroot" , "password" : "wkdb1100"}, 
{"name" : "BJDNL405", "ip" : "172.20.20.8" , "id" : "nsroot" , "password" : "wkdb1100"},     
{"name" : "brenl401", "ip" : "192.168.56.252" , "id" : "nsroot" , "password" : "~2Iros!rp"}, 
{"name" : "brenl402", "ip" : "192.168.58.252" , "id" : "nsroot" , "password" : "~2Iros!rp"}, 
{"name" : "brenl403", "ip" : "192.168.46.252" , "id" : "nsroot" , "password" : "~2Iros!rp"}, 
{"name" : "brenl404", "ip" : "192.168.48.252" , "id" : "nsroot" , "password" : "~2Iros!rp"}, 
{"name" : "brenl405", "ip" : "192.168.52.252" , "id" : "nsroot" , "password" : "~2Iros!rp"}, 
{"name" : "brenl406", "ip" : "192.168.54.252" , "id" : "nsroot" , "password" : "~2Iros!rp"}, 
{"name" : "BRMNL401", "ip" : "211.61.13.210" , "id" : "nsroot" , "password" : "~2imc!rp"},  
{"name" : "brenl407", "ip" : "172.20.245.252" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "brenl408", "ip" : "172.20.245.253" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "BRENGD01", "ip" : "211.61.13.184" , "id" : "nsroot" , "password" : "~2imc!rp"}, 
{"name" : "brinl401", "ip" : "140.1.1.7" , "id" : "nsroot" , "password" : "~2imc!rp"},     
{"name" : "brinl402", "ip" : "140.1.1.8" , "id" : "nsroot" , "password" : "~2imc!rp"},     
{"name" : "BRINL405", "ip" : "140.1.1.13" , "id" : "nsroot" , "password" : "~2imc!rp"},    
{"name" : "BRINL406", "ip" : "140.1.1.14" , "id" : "nsroot" , "password" : "~2imc!rp"},    
{"name" : "brrnl405", "ip" : "192.168.12.9" , "id" : "nsroot" , "password" : "~2imc!rp"},  
{"name" : "brrnl406", "ip" : "192.168.12.10" , "id" : "nsroot" , "password" : "~2imc!rp"}, 
{"name" : "brrnl401", "ip" : "192.168.34.5" , "id" : "nsroot" , "password" : "~2imc!rp"},  
{"name" : "brrnl402", "ip" : "192.168.34.6" , "id" : "nsroot" , "password" : "~2imc!rp"},  
{"name" : "brunl401", "ip" : "140.2.250.86" , "id" : "nsroot" , "password" : "~2imc!rp"},  
{"name" : "brunl402", "ip" : "140.2.250.88" , "id" : "nsroot" , "password" : "~2imc!rp"},  
{"name" : "dcdj0el401", "ip" : "172.31.7.129" , "id" : "nsroot" , "password" : "nsroot"}, 
{"name" : "dronl401", "ip" : "172.20.65.12" , "id" : "nsroot" , "password" : "nsroot"},  
{"name" : "dronl402", "ip" : "172.20.65.13" , "id" : "nsroot" , "password" : "nsroot"},  
{"name" : "drenl401", "ip" : "192.168.77.2" , "id" : "nsroot" , "password" : "~2Iros!rp"},  
{"name" : "drenl402", "ip" : "192.168.76.2" , "id" : "nsroot" , "password" : "~2Iros!rp"}, 
{"name" : "drenl403", "ip" : "192.168.82.252" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "drenl404", "ip" : "192.168.84.252" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "drenl405", "ip" : "192.168.52.252" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "drenl406", "ip" : "192.168.54.252" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "drenl407", "ip" : "172.20.245.252" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "drenl408", "ip" : "172.20.245.253" , "id" : "nsroot" , "password" : "~2Iros!rp"},
{"name" : "DRENGD01", "ip" : "211.61.13.84" , "id" : "nsroot" , "password" : "~2tj!rp"},  
{"name" : "DRINL401", "ip" : "140.2.1.7" , "id" : "nsroot" , "password" : "~2tj!rp"},   
{"name" : "DRINL402", "ip" : "140.2.1.8" , "id" : "nsroot" , "password" : "~2tj!rp"},     
{"name" : "DRINL405", "ip" : "140.2.1.13" , "id" : "nsroot" , "password" : "~2tj!rp"},    
{"name" : "DRINL406", "ip" : "140.2.1.14" , "id" : "nsroot" , "password" : "~2tj!rp"},    
{"name" : "DRINL403", "ip" : "140.2.2.12" , "id" : "nsroot" , "password" : "~2tj!rp"},    
{"name" : "DRINL404", "ip" : "140.2.2.13" , "id" : "nsroot" , "password" : "~2tj!rp"},   
{"name" : "BRDNL401", "ip" : "172.20.31.12" , "id" : "ophnsjh0" , "password" : "fnxmfnxm123"},    
{"name" : "brdnl402", "ip" : "172.20.34.8" , "id" : "ophnsjh0" , "password" : "fnxmfnxm123"}]      

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
      

app.run("172.20.129.103")