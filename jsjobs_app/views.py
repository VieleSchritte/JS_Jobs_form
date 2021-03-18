import os
from flask import render_template, request, redirect, url_for
from jsjobs_app.vacancy_builder import VacancyBuilder
from jsjobs_app import app


static_path = os.path.join('JS_Jobs', '../client/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('welcome_form.html', title='JS_Jobs')
    if request.method == 'POST':
        form_data = request.form
        business = request.form['business']
        return redirect(url_for('vacancy_draft', form_data=form_data, business=business))


@app.route('/vacancy_draft/<form_data>/<business>')
def vacancy_draft(form_data, business):
    v = VacancyBuilder()
    vacancy_name, company_name, city, salary, key_technologies, vacancy_description, contacts = v.get_vacancy_areas(form_data, business)
    return render_template(
        'vacancy_draft.html',
        vacancy_name=vacancy_name,
        company_name=company_name,
        city=city,
        salary=salary,
        key_technologies=key_technologies,
        vacancy_description=vacancy_description,
        contacts=contacts
    )


@app.route("/thank_you", )
def hello():
    return "Thanks for using our service!"


if __name__ == "__main__":
    app.run()
