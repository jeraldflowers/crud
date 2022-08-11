PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input('Cual es la contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta.')

    return wrapper


@password_required
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


@upper
def say_may_name(name):
    return 'Hola, {}'.format(name)


if __name__=='__main__':
    print(say_may_name('David'))