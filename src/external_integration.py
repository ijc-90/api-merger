default = {'deductible': 1000, 'stop_loss': 14000, 'oop_max': 5000}


def call_external_api(api, member_id):
    #mockup calls
    if api == 'https://api1.com':
        if member_id == 1:
            return {'deductible': 1190, 'stop_loss': 11020, 'oop_max': 5103}
        if member_id == 2:
            return {'deductible': 1120, 'stop_loss': 12300, 'oop_max': 5250}
        if member_id == 3:
            return {'deductible': 3100, 'stop_loss': 100, 'oop_max': 310}
    if api == 'https://api2.com':
        if member_id == 1:
            return {'deductible': 1101, 'stop_loss': 11010, 'oop_max': 5102}
        if member_id == 2:
            return {'deductible': 1121, 'stop_loss': 12300, 'oop_max': 5220}
        if member_id == 3:
            return {'deductible': 3100, 'stop_loss': 100, 'oop_max': 302}
    if api == 'https://api3.com':
        if member_id == 1:
            return {'deductible': 1110, 'stop_loss': 11090, 'oop_max': 5101}
        if member_id == 2:
            return {'deductible': 1126, 'stop_loss': 12300, 'oop_max': 5210}
        if member_id == 3:
            return {'deductible': 3100, 'stop_loss': 100, 'oop_max': 304}
    return default