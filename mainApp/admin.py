from django.contrib import admin

import Spotify
# Register your models here.
from .models import *

admin.site.register([Qoshiq, Qoshiqchi, Albom])