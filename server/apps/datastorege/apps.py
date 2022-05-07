from django.apps import AppConfig

# ------------------------------------------------------------------------------------------------
# base  django congif class for config datastorege application :
class DatastoregeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.datastorege'
