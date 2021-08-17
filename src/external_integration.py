default = {'deductible': 1000, 'stop_loss': 14000, 'oop_max': 5000}


def call_external_api(api, member_id):
    #mockup calls
    if api == 'https://api1.com':
        if member_id == 1:
            return {'deductible': 1100, 'stop_loss': 11000, 'oop_max': 5100}
        if member_id == 2:
            return {'deductible': 1120, 'stop_loss': 12000, 'oop_max': 5220}
        if member_id == 3:
            return {'deductible': 3100, 'stop_loss': 100, 'oop_max': 30}
    if api == 'https://api2.com':
        if member_id == 1:
            return {'deductible': 1100, 'stop_loss': 11000, 'oop_max': 5100}
        if member_id == 2:
            return {'deductible': 1120, 'stop_loss': 12000, 'oop_max': 5220}
        if member_id == 3:
            return {'deductible': 3100, 'stop_loss': 100, 'oop_max': 30}
    if api == 'https://api3.com':
        if member_id == 1:
            return {'deductible': 1100, 'stop_loss': 11000, 'oop_max': 5100}
        if member_id == 2:
            return {'deductible': 1120, 'stop_loss': 12000, 'oop_max': 5220}
        if member_id == 3:
            return {'deductible': 3100, 'stop_loss': 100, 'oop_max': 30}
    return default