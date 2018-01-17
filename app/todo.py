from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'todo key'
bootstrap = Bootstrap(app)
tasks = []


class AddForm(FlaskForm):
    task1 = StringField("please input new task", validators=[DataRequired()])
    add_submit = SubmitField('Add')


class CompleteForm(FlaskForm):
    task2 = StringField("please input complete task", validators=[DataRequired()])
    complete_submit = SubmitField('Complete')


class RestartForm(FlaskForm):
    task3 = StringField("please input restart task", validators=[DataRequired()])
    restart_submit = SubmitField('Restart')


@app.route('/', methods=['GET', "POST"])
def index():
    add_form = AddForm()
    complete_form = CompleteForm()
    restart_form = RestartForm()
    if add_form.add_submit.data and add_form.validate_on_submit():
        task = {'task': add_form.task1.data, 'status': 'Waiting'}
        tasks.append(task)
        add_form.task1.data = ''
        return render_template('index.html', tasks=tasks, add_form=add_form,
                               complete_form=complete_form,
                               restart_form=restart_form)
    if complete_form.complete_submit.data and complete_form.validate_on_submit():
        for k, i in enumerate(tasks):
            if i['task'] == complete_form.task2.data:
                tasks[k]['status'] = 'Complete'
        complete_form.task2.data = ''
        return render_template('index.html', tasks=tasks, add_form=add_form,
                               complete_form=complete_form,
                               restart_form=restart_form)
    if restart_form.restart_submit and restart_form.validate_on_submit():
        for k, i in enumerate(tasks):
            if i['task'] == restart_form.task3.data:
                tasks[k]['status'] = 'Waiting'
        restart_form.task3.data = ''
        return render_template('index.html', tasks=tasks, add_form=add_form,
                               complete_form=complete_form,
                               restart_form=restart_form)
    else:
        return render_template('index.html', tasks=tasks, add_form=add_form,
                               complete_form=complete_form,
                               restart_form=restart_form)


@app.route('/<name>/')
def index1(name):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
