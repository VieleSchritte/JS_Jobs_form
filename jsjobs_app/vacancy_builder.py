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

    def build_vacancy(self, form_data, business):
        full_vacancy = ''

        for area in self.areas:
            switch = {
                'vacancy-name': '**' + form_data[area] + '**\n',
                'salary': '**' + form_data[area] + '**\n',
                'company-name': '__' + form_data[area] + '__\n',
                'city': '#' + form_data[area] + ' ' + self.hash_tags[business] + '\n'
            }
            if area in switch.keys():
                full_vacancy += switch[area]
            elif area == 'key-technologies':
                string = form_data[area].strip().split()
                for skill in string:
                    full_vacancy += '#' + skill + ' '
                for i in range(2):
                    full_vacancy += '\n'
            else:
                full_vacancy += form_data[area] + '\n'

        return full_vacancy

    def get_vacancy_areas(self, form_data, business):
        areas_content = []
        for area in self.areas:
            if area == 'city':
                areas_content.append('#' + form_data[area] + ' ' + self.hash_tags[business])
            else:
                areas_content.append(form_data[area])
        return areas_content
