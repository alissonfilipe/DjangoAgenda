# projeto agenda

- django-admin é a mesma coisa que o python manage.py

# app contact

    <h2>TEMPLATES</h2>

# o que precisamos
- venv
- django
- pip install faker -> script para geração de dados aleatórios(cuidado ao usar)

# informações importantes
- `local_settings.py` não vai para o github
- e você vai precisar criar ele manualmente

SECRET_KEY = 'CHANGE-ME'
DEBUG = True
ALLOWED_HOSTS: list[str] = []

- importante não esquecer de quando adicionar uma view na pasta views
você deve colocar o import dela no arquivo `__init__.py`

# o que foi feito

- deletado as views para a criação de um pacote