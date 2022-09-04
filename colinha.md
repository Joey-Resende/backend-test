# Passo a Passo para criar um projeto Django

## Criar pasta inicial do projeto
1: Diretorio que vai guardar todo nossos arquivos

## Criar o ambiente virtual (pyenv, poetry)
1: Instalando com o pyenv a versao do python que iremos usar local na pasta do projeto
2: pyenv local <@.@.@>          #sem as <> coloca a versao que sera instalada (pyenv install <@.@.@> instalada global)
3: poetry init -n               #Cria o ambiente e configura na mao pelo arquivo pyproject.toml
4: poetry add django            #se for no caso um site em django
5: poetry shell                 #Inicia o ambiente
6: deactivate                   #Desativa o ambiente virtual (poetry)

## Criar iniciar o git    

1: git init                    #So e feito uma vez
2: git add .
3: git commit -m ""
4: git branch -M "main"        #So e feito uma vez
5: git remote add origin "link do repositorio"  (sem as aspas, So faz uma vez) #linka o diretorio local com o remoto
6: git push origin main
7: git pull origin master

## Criando o .gitignore com o https://www.toptal.com/developers/gitignore
1: escolhendo as coisas que queremos ignorar nos commits


## Instalando o blue (para organizar o codigo pela pep8)
1: poetry add --dev blue        #instala o blue
2: blue .                       #faz a verificacao

## Instalando o isort (para organizar os imports)
1: poetry add --dev isort       #instala o isort
2: isort .                      #faz o isort ordenar em todos os arquivos

## Instalando o mkdocs (para criar as documentacoes do projeto)
1: poetry add --dev mkdocs      #instala o mkdocs
2: mkdocs new .                 #cria os arquivos de documentacao    

## Instalando o prospector (para checagem geral)
1: poetry add --dev prospector  #instala o prospector
2: prospector                   #Faz uma checagem geral

## Instalando o pip-audit (para verificar vulnerabilidades)
1: poetry add --dev pip-audit   #instala o pip-audit
2: pip-audit                    #Checa as vulnerabilidades

## Criar arquivo make (makefile) para automatizar todas as ferramentas
1: makefile (coloca dentro desse arquivo os comandos que pretendemos usar)
2: make (roda todos os comando do arquivo)

## Criar o projeto
1: django-admin startproject <nomedoprojeto>
2: python3 manage.py startapp <nomedoapp> (na pasta onde fica o arquivo manage.py)
3: registrar a app criada no settings.py (sessao INSTALED APPS), tambem pode mudar o fuso horario e o idioma
4: adicione no arquivo urls.py as urls do projeto #no app que foi criado
5: python3 manage.py makemigrations #Criar as migracoes de banco
6: python3 manage.py migrate          #Aplicar as migracoes de banco
7: criar os modelos no aquivo models.py
8: no arquivo settings.py na parte da constante TEMPLATES adicionar 'DIRS': [os.path.join(BASE_DIR, 'templates')], #verificar se tem o os importado (import os)
9: criar a pasta templates no diretorio do nosso app
10: criar um arquivo html dentro de templates para fazer a primeira pagina
11: criar um class view no arquivo views.py
12: criar no urls.py do app uma url para a view que acabamos de criar
13: no urls.py do projeto adicionar o include aos imports e adicionar mais uma linha de path # path('core/', include('core.urls')),
14: Criar o diretorio static dentro do diretorio principal do projeto e dentro dele diretorios para os css, js, e imagem que vamos adicionar ao projeto
15: adicionar a constante STATIC_URL = 'static/' e STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] no settings.py
16: adiconar o bootstrap, font awesome e popper, coloquei tudo por cdn
00: python3 manage.py createsuperuser    #criar um superusuario para o admin
00: Intalar o braces para o controle de acesso por grupos #pip install django-braces
