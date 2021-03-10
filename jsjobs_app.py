import os
from flask import Flask, render_template, request
from vacancy_builder import VacancyBuilder

app = Flask('js_jobs', template_folder='templates/', static_folder='static/')
static_path = os.path.join('JS_Jobs', '../client/static')
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return render_template('welcome_draft.html')


@app.route('/', methods=['POST'])
def data_processing():
    form_data = request.form
    business = request.form['business']
    v = VacancyBuilder()
    vacancy = v.build_vacancy(form_data, business)
    return vacancy


@app.route('/vacancy_draft')
def status():
    return 'Vacancy draft ready to post'


@app.route("/thank_you")
def hello():
    return "Thanks for using our service!"


if __name__ == "__main__":
    app.run()
