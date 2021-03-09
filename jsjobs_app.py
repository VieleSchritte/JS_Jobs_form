import os
from flask import Flask, render_template

app = Flask('js_jobs', template_folder='templates/', static_folder='static/')
static_path = os.path.join('JS_Jobs', '../client/static')
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return render_template('welcome_draft.html')


@app.route('/', methods=['POST'])
def data_processing(request):
    vacancy_name = request.POST.get('vacancy-name', 0)
    company_name = request.POST.get('company-name', 0)
    city = request.POST.get('city', 0)
    key_technologies = request.POST.get('key-technologies', 0)
    vacancy_description = request.POST.get('vacancy-description', 0)
    contacts = request.POST.get('contacts', 0)
    print('heko')
    print(vacancy_name, company_name, city, key_technologies, vacancy_description, contacts)


@app.route('/vacancy_draft')
def status():
    return 'Vacancy draft ready to post'


@app.route("/thank_you")
def hello():
    return "Thanks for using our service!"


if __name__ == "__main__":
    app.run()
