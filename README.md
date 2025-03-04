# CRUD com Django

Este repositório contém um sistema CRUD (Create, Read, Update, Delete) desenvolvido em Django, um framework web baseado em Python. O projeto tem como objetivo demonstrar a implementação das operações básicas de um banco de dados utilizando Django.

## Tecnologias Utilizadas

- Python 3.12.6
- Django
- SQLite3
- Bootstrap

## Funcionalidades

- Criar registros
- Ler registros
- Atualizar registros
- Deletar registros

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/DRBenedetti/CRUD-Django.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd CRUD-Django
   ```

3. Crie um ambiente virtual e ative-o (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:8000/
   ```

## Estrutura do Projeto

```
├── manage.py        # Arquivo de gerenciamento do Django
├── crud_app/        # Aplicação principal do CRUD
│   ├── models.py    # Definição dos modelos do banco de dados
│   ├── views.py     # Lógica das views
│   ├── urls.py      # Rotas da aplicação
│   ├── templates/   # Arquivos HTML para renderização
├── db.sqlite3       # Banco de dados SQLite
├── requirements.txt # Lista de dependências do projeto
└── README.md        # Documentação do projeto
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias e novas funcionalidades. Para isso:

1. Faça um fork do repositório
2. Crie uma branch com sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das suas alterações:
   ```bash
   git commit -m "Adicionando nova funcionalidade"
   ```
4. Faça o push para a sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.


 
