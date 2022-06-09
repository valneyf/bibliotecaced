# Biblioteca CED

> Projeto feito utilizando as seguintes tecnologias:
>
> ***Python 3.8 + Django 4.0:*** Backend
>
> ***PostgreSQL 13:*** Banco de dados Relacional
>
> ***Bootstrap4 + Lib Crispy-Forms:*** Criação de Interface e Formulários

## Para executar o projeto
 - Para ambiente Linux, no terminal utilizar os seguintes comandos

 > Construção das imagens e arquitetura de comunicação
 ```sh
 docker-compose up --build
 ```

> Execução do docker-compose como daemon(serviço em segundo plano)
 ```sh
 docker-compose up -d
 ```
 
> Execução das migrations
 ```sh
 docker-compose exec web python manage.py migrate
 ```

> Criação de superusuário para a área admin
 ```sh
 docker-compose exec web python manage.py createsuperuser
 ```

> Para acessar o site
 ```url
 http://localhost:8000/
 ```
> Para acessar o site a parte administrativa
 ```url
 http://localhost:8000/admin/
 ```

 - A parte administrativa ficará em uso até posterior refatoração do código de botão Editar e Remover da interface de detalhes do livro para o cliente

 - Será implementada a tradução completa da interface

 - Será implementado também a autenticação de usuário, para cadastrar somente quem estiver em sessão no site.

### Referências
 - https://github.com/fabioruicci/tutorial-e-commerce-django/tree/parte-1/setup-e-catalogo
 - https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
 - https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/
 - https://www.geeksforgeeks.org/django-forms/
 - https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
 - https://stackoverflow.com/questions/tagged/django+django-views