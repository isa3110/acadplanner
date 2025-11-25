# Informações relevantes sobre o repositório

## Como navegar pelo repositório
* No diretório `/src` está contido todos os códigos da aplicação. 
    * `/src/config` -> Configuração do banco de dados.
    * `/src/controllers` -> Blueprints da aplicação.
        * `auth` -> Blueprint com rotas de login, registro e logout.
        * `error` -> Blueprint com rotas de error handlers (404, etc). 
        * `main` -> Blueprint com a rota home da aplicação.
> [!IMPORTANT]
> Se precisar mudar alguma coisa referente a porta do banco de dados, user, host e senha, é no arquivo `/src/config/__init__.py` que você deve fazer a alteração. 

* O banco de dados está contido no diretório `/model`
* O diretório `/static` possui subdiretórios referentes ao estilo (`style`) e imagens.
* O diretório `/templates` é onde está localizado os arquivos HTML da aplicação.
* O arquivo `app.py` é o aplicativo onde todos os Blueprints são registrados e assim, a aplicação é executada.