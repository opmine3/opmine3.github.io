# flask_ngrok_example.py
#author: Thbop
#date completed: 8/20/2021
#feel free to use any of this code for your own projects.


from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

#file func
def addtofile(i, a):
    with open(str(i), 'a') as f:
        f.write(str(a))

def savefile(i, a):
    with open(str(i), 'w') as f:
        f.write(str(a))

def openfile(i):
    fileread = open(str(i), 'r')
    fileread = fileread.read()
    return fileread

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

#pages
@app.route('/')
def index():
    return render_template('apply.html')

#processes application
@app.route('/form', methods=["POST"])
def form():
    ign = request.form.get("ign")
    dis = request.form.get("dis")
    why = request.form.get("why")
    rank = request.form.get("rank")
    Help = request.form.get("help")
    xp = request.form.get("xp")

    #compiles data into a file, later to be displayed
    data = '\n\nIGN: '+ign+'\nDiscord: '+dis+'\nWhy does '+ign+' want to be staff: '+why+'\n'+ign+' wants the rank of '+rank+'\n'+ign+' can help by: '+Help+'\n'+ign+' has experience with: '+xp
    addtofile('data.txt', data)
    return render_template('form.html')

    #staff login page
@app.route('/staffstuff')
def pc():
    return render_template('pc.html')

    #views all data
@app.route('/view', methods=["POST"])
def view():
    password = request.form.get("password")
    #this is where the password would go, but I didn't want to put the actual password in there for security reasons.
    if password == 'yourstaffpassword':
        text = openfile('data.txt')
    #if the password was wrong
    else:
        text = 'Whoops, something went wrong!'
    
    return render_template('view.html', text=text)

if __name__ == '__main__':
    app.run()

