class VacancyBuilder:
    @staticmethod
    def build_vacancy(form_data, business):
        full_vacancy = ''

        hash_tags = {
            'office': '#офис',
            'remote': '#удаленка',
            'parttime': '#парттайм',
            'project': '#проект'
        }

        areas = [
            'vacancy-name',
            'company-name',
            'city',
            'salary',
            'key-technologies',
            'vacancy-description',
            'contacts'
        ]
        for area in areas:
            switch = {
                'vacancy-name': '**' + form_data[area] + '**\n',
                'salary': '**' + form_data[area] + '**\n',
                'company-name': '__' + form_data[area] + '__\n',
                'city': '#' + form_data[area] + ' ' + hash_tags[business] + '\n'
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
