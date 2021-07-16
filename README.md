# Problema
Um grupo de médicos criou uma empresa para atender, em conjunto, um grupo de postos de
trabalho. Anteriormente, cada um deles atendia individualmente os seus próprios postos de
trabalho, mas tinham dificuldades de tirar dias de folga pois sempre precisavam procurar
alguém para cobrir o dia de ausência.
A formação do grupo permitiu que eles definissem uma escala de atendimento e cada um deles pode, agora, folgar um dia da semana.

Todo o problema e descrição do trabalho está no arquivo DesafioDjango.pdf

## Tecnologias
* Python 3.9.6
    Linguagem de programação utiliza
* Django 3.2.5
    Framework para desenvolvimento web
* Coverage 5.5
    Biblioteca para auxiliar na criação nos testes automatizado.
* flake8 3.9.2
    Biblioteca para auxiliar na adequação ao pep8.
* isort 5.9.2
    Biblioteca para automaticamento organizar os imports segundo o pep8.
* sqlite3
    Banco de dados relacinal leve e de facíl utilização.
# Criação do ambiente de desenvolvimento
* python3.9 -m venv venv .
## Ativando o ambiente de desenvolvimento
* source venv/bin/activate para linux
## Instalação do dos requerimentos
* Vá para raiz do projeto
* pip install -r requirements.txt
# Criando os modelos 
* python manage.py makemigrations
* python manage.py migrate
# Criando super user
* python manage.py createsuperuser
# Execução
* python manage.py runserver
# Estrutura do Projeto
* http://127.0.0.1:8000/ fica a escala dos médicos
* http://127.0.0.1:8000/admin/ fica administração da aplicação
* essas urls são válidas no localhost
