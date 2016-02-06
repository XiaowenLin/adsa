from flask import Flask
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
name = None
form = NameForm()
if form.validate_on_submit():
name = form.name.data
form.name.data = ''
return render_template('index.html', form=form, name=name)

@app.route('/')
def hello_world():
    return 'Hello World from nginx!'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
