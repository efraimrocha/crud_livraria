# Livraria - Projeto Django

Este é um projeto básico desenvolvido com o framework Django chamado "Livraria". O sistema permite listar os livros cadastrados, adicionar, editar e deletar informações sobre livros. Para uma estilização básica, utilizamos o Bootstrap 5. Este projeto foi desenvolvido para Efraim como parte de um exercício prático de desenvolvimento de sistemas web com o Django.


![Captura de tela de 2023-11-02 07-09-09](https://github.com/efraimrocha/crud_livraria/assets/67542881/a25c6c7a-f743-466e-be73-a89e61819d70)


## Funcionalidades

O sistema Livraria oferece as seguintes funcionalidades:

- Listagem de todos os livros cadastrados.
- Adição de novos livros.
- Edição das informações de livros existentes.
- Remoção de livros do sistema.

## Instruções para Executar o Projeto

Para executar este projeto em seu ambiente local, siga as instruções abaixo:

1. Clone o repositório do projeto:
   ```
   git clone https://github.com/seurepositorio/livraria.git
   ```

2. Crie e ative um ambiente virtual (virtual environment):
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências do projeto a partir do arquivo `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados para criar as tabelas necessárias:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento do Django:
   ```
   python manage.py runserver
   ```

6. Acesse a aplicação em seu navegador web, normalmente disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Agora você pode explorar a aplicação Livraria, listar livros, adicionar novos livros, editá-los e remover livros conforme necessário.

Lembre-se de que este é um projeto básico destinado a fins educacionais. Você pode personalizá-lo e expandi-lo de acordo com suas necessidades e requisitos específicos.
