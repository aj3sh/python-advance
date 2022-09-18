import datetime

def parse_date_input(arg=None):
    '''
    arg is func (closure) if not called.
    arg is format if called.
    '''
    format='%Y-%m-%d'
    
    def _wrapper_factory(func, format):
        def _wrapper(date):
            if isinstance(date, datetime.datetime):
                date = date.date()
            if isinstance(date, str):
                date = datetime.datetime.strptime(date, format).date()
            return func(date)
        return _wrapper

    def _decorator(func):
        return _wrapper_factory(func, format=format)

    if arg == None or isinstance(arg, str):
        format = arg or format
        return _decorator
    
    return _wrapper_factory(arg, format)

@parse_date_input
def is_expired(date):
    return date < datetime.date.today()

@parse_date_input('%m/%d/%Y')
def is_valid(date):
    return date >= datetime.date.today()

if __name__ == '__main__':
    print(is_expired(datetime.datetime(2022, 12, 12)))
    print(is_expired('2013-10-21'))
    print(is_valid('03/21/2013'))