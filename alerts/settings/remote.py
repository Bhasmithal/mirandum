#  Copyright 2016 Google Inc. All Rights Reserved.
#  
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License. 

from settings.base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'alerts',
        'USER': 'alerts',
        'PASSWORD': 'password',
        'HOST': os.environ.get('POSTGRESQL_HOST', '127.0.0.1'),
        'PORT': '',
    }
}
SERVER_BASE="https://www.livestreamalerts.com/"
SECRET_KEY="Un!%}$eV&kxw=ZN!&eP@BO!=Oso0b2m-|gf/J-.3FbL/a%q2hk"
