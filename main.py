from flask import Flask , render_template , request , session , redirect
from flask_sqlalchemy import SQLAlchemy
import json
import os
import math
from datetime import datetime
from flask_mail import Mail
from werkzeug import secure_filename

local_server = True
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = 'kuldeep-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_username'],
    MAIL_PASSWORD = params['gmail_password'],
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(120), unique=False, nullable=False)
    created = db.Column(db.String(120))

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=True)
    tagname = db.Column(db.String(80), unique=True, nullable=True)
    slug = db.Column(db.String(120), unique=True, nullable=True)
    content = db.Column(db.String(120), unique=False, nullable=True)
    image = db.Column(db.String(120), unique=False, nullable=True)
    created = db.Column(db.String(120))    

@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    #[0:params['no_of_posts']]
    page = request.args.get('page')
    if(not unicode(page).isnumeric()):
        page = 1
    page = int(page)    
    posts = posts[(page-1)*int(params['no_of_posts']) : (page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]    
    # pagination logic
    #first
    if (page == 1):
        prev = "#"
        next = "/?page="+ str(page+1)
    elif (page == last):
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)    
        next = "/?page="+ str(page+1)
    return  render_template('index.html' , params = params , posts = posts , prev = prev , next = next)

@app.route('/about')
def about():
    return  render_template('about.html' , params = params)

@app.route('/contact' , methods = ['GET' , 'POST'])
def contact():
    if(request.method == 'POST'):
      name = request.form.get('name')
      email = request.form.get('email')
      phone = request.form.get('phone')
      message = request.form.get('message')

      entry = Contacts(name = name , phone = phone , message = message , email = email , created = datetime.utcnow())
      db.session.add(entry)
      db.session.commit()
      mail.send_message('New Message from ' + name, 
        sender = email , 
        recipients = [params['gmail_username']],
        body = message + "/n" + phone
      )
    return  render_template('contact.html' , params = params)

@app.route('/post/<string:post_slug>',methods = ['GET'])
def post(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first() 
    return  render_template('post.html' , params = params , post = post)   

@app.route('/dashboard' , methods = ['GET' , 'POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return  render_template('dashboard.html' , params = params , posts = posts)    
    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if(username == params['admin_user'] and userpass == params['admin_pass']):
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return  render_template('dashboard.html' , params = params , posts = posts)    
     
    return  render_template('login.html' , params = params)  





@app.route('/edit/<string:id>' , methods = ['GET' , 'POST'])
def edit(id):
    # print(id)

    if ('user' in session and session['user'] == params['admin_user']):
        # print("loggedin")
        if(request.method == 'POST'):
            # print("post mentod")
            title = request.form.get('title')
            tagname = request.form.get('tagname')
            slug = request.form.get('slug')
            content = request.form.get('content')
            image = request.form.get('image')
            if id == '0':
                post = Posts(title = title , tagname = tagname , slug = slug ,content = content ,image = image , created = datetime.utcnow())
                db.session.add(post)
                db.session.commit()
            else:
                post =  Posts.query.filter_by(id=id).first()
                post.title = title
                post.tagname = tagname
                post.slug = slug
                post.content = content
                post.image = image
                post.created = datetime.utcnow()
                db.session.commit()
                return redirect('/edit/'+id) 

        post = Posts.query.filter_by(id=id).first()
        print(post)
        return render_template('edit.html' , params = params ,post = post , id =id)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/delete/<string:id>' , methods = ['GET' , 'POST'] )
def delete(id):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(id = id).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')    


       
@app.route('/uploader' , methods = ['GET' , 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if(request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return "Uploaded Sucessfully"

#app.run( host = 0.0.0.0 , port = 5000 ,  debug = True)
app.run(debug = True)
