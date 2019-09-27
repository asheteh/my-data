# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r8sit#efghgfd+h7*q^10pw+(1rx20hnset=(d2a*ep$=sz(l@b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True 

ALLOWED_HOSTS = ['165.22.254.36','ccatcracker.in','www.ccatcracker.in']





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'ccatcracker',
        'USER': 'ccatcracker',
        'PASSWORD':'Abhi.@239',
        'HOST' : 'localhost'
    }
}

# Email Config 
EMAIL_HOST='smtp.ccatcracker.in'
EMAIL_PORT=587
EMAIL_HOST_USER='help@ccatcracker.in'
EMAIL_HOST_PASSWORD='GeTx!As7'
EMAIL_USE_TLS = True

