from jsjobs_app.models import Company


class VacancyBuilder:
    def __init__(self):
        self.hash_tags = {
            'office': '#офис',
            'remote': '#удаленка',
            'parttime': '#парттайм',
            'project': '#проект'
        }
        self.areas = [
            'vacancy-name',
            'company-name',
            'city',
            'salary',
            'key-technologies',
            'vacancy-description',
            'contacts'
        ]

    @staticmethod
    def key_techs_hashtags(key_techs):
        key_techs = key_techs.strip().split()
        string_to_add = ''
        for tech in key_techs:
            string_to_add += '#' + tech + ' '
        for i in range(2):
            string_to_add += '\n'
        return string_to_add

    def city_business_proc(self, city, business):
        business = self.hash_tags[business]
        return '#' + city + ' ' + business + '\n'

    def build_vacancy(self, form_data, business):
        full_vacancy = ''

        for area in self.areas:
            switch = {
                'vacancy-name': '**' + form_data[area] + '**\n',
                'salary': '**' + form_data[area] + '**\n',
                'company-name': '__' + form_data[area] + '__\n',
                'city': self.city_business_proc(form_data[area], business),
                'key-technologies': self.key_techs_hashtags(form_data[area])
            }
            if area in switch.keys():
                full_vacancy += switch[area]
            else:
                full_vacancy += form_data[area] + '\n'
        self.add_vacancy_to_db(form_data, business)
        return full_vacancy

    def get_vacancy_areas(self, form_data, business):
        print('=======vacancy builder')
        areas_content = []
        for area in self.areas:
            if area == 'city':
                areas_content.append(self.city_business_proc(form_data[area], business))
            elif area == 'key-technologies':
                areas_content.append(self.key_techs_hashtags(form_data[area]))
            else:
                areas_content.append(form_data[area])
        return areas_content

    def add_vacancy_to_db(self, form_data, business):
        from jsjobs_app import db
        new_company = Company(
            dev=form_data['vacancy-name'],
            city_business=self.city_business_proc(form_data['city'], business),
            salary=form_data['salary'],
            hashtags=form_data[self.key_techs_hashtags(form_data['key-technologies'])],
            description=form_data['vacancy-description'],
            contacts=form_data['contacts']
        )

        db.session.add(new_company)
        db.session.commit()
