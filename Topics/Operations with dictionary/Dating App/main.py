def select_dates(potential_dates):
    names = []
    age_limit = 30
    for date in potential_dates:
        if date['age'] > age_limit and 'art' in date['hobbies'] and date['city'] == 'Berlin':
            names.append(date['name'])
    return ', '.join(names)