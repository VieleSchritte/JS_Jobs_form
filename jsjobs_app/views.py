import os
from flask import render_template, request
from jsjobs_app.vacancy_builder import VacancyBuilder
from jsjobs_app import app


static_path = os.path.join('JS_Jobs', '../client/static')


@app.route('/', methods=['GET'])
def index():
    return render_template('welcome_form.html', title='JS_Jobs')


@app.route('/', methods=['POST'])
def data_processing():
    form_data = request.form
    business = request.form['business']
    v = VacancyBuilder()
    # vacancy = v.build_vacancy(form_data, business)

    vacancy_name, company_name, city, salary, key_technologies, vacancy_description, contacts = v.get_vacancy_areas(form_data, business)
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
