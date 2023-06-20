# --------------------------- import statements ----------------
from flask import Flask,flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from programs import count,stress_module,split
from werkzeug.utils import secure_filename


#--------------------- app initialisation -----------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)


# -------------------- MODELS ------------------------------
class Vocabulary(db.Model):
    _tablename_ = "vocabulary"
    v_id = db.Column(db.Integer, primary_key = True, unique=True)
    word = db.Column(db.String,unique=True)
    phonetics = db.Column(db.String)
    syllables = db.Column(db.String)
   

    def __repr__(self) -> str:
        return f" {self.v_id}-{self.word}-{self.phonetics}-{self.syllables}"






class Doubt(db.Model):
    _tablename_ = "doubt"
    D_no = db.Column(db.Integer, primary_key=True,unique = True)
    word = db.Column(db.String,unique=True)
    status = db.Column(db.String)

    def __repr__(self) -> str:
        return f" {self.D_no}-{self.word}-{self.status}"
#--------------------- CONTROLLERS --------------------

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/input")
def input():
    return render_template('info.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('abt.html')

@app.route('/team', methods=['GET','POST'])
def team():
    return render_template('team.html')

@app.route('/phon', methods=['GET','POST'])
def phon():
    return render_template('phon.html')

@app.route('/linguists', methods=['GET','POST'])
def linguists():
    return render_template('linguists.html')

@app.route('/queries', methods=['GET','POST'])
def queries():
    return render_template('queries.html')


@app.route('/phonetic/<fname>', methods=['GET','POST'])
def phone(fname):
    ph = count.phone(fname)
    return render_template('displayph.html',text=fname, ph=ph)


@app.route('/work/<fname>', methods=['GET','POST'])
def syllable(fname):
    c = count.count_syl(fname)
    syl=split.splits(fname)
    return render_template('display.html',count=c, text=fname, syl=syl)
    
@app.route('/uploader', methods = ['POST'])
def upload_file():
    audio = request.files['audio_file']
    with open('audio.wav','wb') as f:
        f.write(audio.read())
    return render_template('stress.html')

@app.route('/play', methods=['GET','POST'])
def play():
    stress_module.stress_detect()
    return render_template("stress.html")


      

#-----------------final app run ----------------------

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)    
