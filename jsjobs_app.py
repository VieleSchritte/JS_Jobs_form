import os
import sqlite3
from flask import Flask, render_template, request
from vacancy_builder import VacancyBuilder
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from contextlib import closing



DATABASE = 'db_schema.sql'

app = Flask('js_jobs', template_folder='templates/', static_folder='static/')
app.config.from_object('js_jobs')
static_path = os.path.join('JS_Jobs', '../client/static')
app.debug = True


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('db_schema.sql') as vacancies_db:
            db.cursor().executescript(vacancies_db.read())
        db.commit()


@app.route('/', methods=['GET'])
def index():
    return render_template('welcome_form.html')


@app.route('/', methods=['POST'])
def data_processing():
    form_data = request.form
    business = request.form['business']
    v = VacancyBuilder()
    vacancy = v.build_vacancy(form_data, business)

    vacancy_name, company_name, city, salary, key_technologies, vacancy_description, contacts = v.draft_vacancy_builder(form_data, business)
    return render_template('vacancy_draft.html', vacancy_name=vacancy_name, company_name=company_name, city=city,
                           salary=salary, key_technologies=key_technologies, vacancy_description=vacancy_description,
                           contacts=contacts)


@app.route('/vacancy_draft')
def status():
    return 'Vacancy draft ready to post'


@app.route("/thank_you")
def hello():
    return "Thanks for using our service!"


if __name__ == "__main__":
    app.run()
