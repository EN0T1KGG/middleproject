#инациализация файлов 
# редактирование файла с определением окружения для разработки продакшена и тестировки 
# cat > src/config/settings/__init__.py << "EOF"

import os 
# определяем окружение 
enviroment = os.environ.get('DJANGO_ENV',"development")
if enviroment == "production":
    from .production import * 
elif enviroment == "testing":
    from .testing import *
else:
    from .development import *
    