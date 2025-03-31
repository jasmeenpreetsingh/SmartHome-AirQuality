# Add to INSTALLED_APPS
INSTALLED_APPS = [
    ...,
    'airquality'
]

# Configure database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'airquality.db',
    }
}

# Add MQTT config (bottom of file)
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883