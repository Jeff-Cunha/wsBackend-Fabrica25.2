# wsBackend-Fabrica25.2
Seja bem-vindo ao Master's Receitas, um projeto Django completo, para que você possa ter seu próprio livro de receitas on-line.

# Funcionalidades
- **CRUD** completo, que permite adicionar novas receitas com nome, tempo, instruções e ingredientes.
- **Ingredientes** são salvos no banco de dados
- **Importar** permite a importação de receitas já prontas, para que você possa apenas aproveitar, buscando o prato por nome na **API** TheMealDB.

# Tecnologias Usadas
-**Backend:**
  -Python 3.12.4
  -Django 5.2.6
-**Frontend:**
  -HTML
  -CSS
  -Bootstrap 5
-**Banco de Dados:**
  -SQLite 3

**Passos:**

1.  **Clone o repositório:**
    git clone https://github.com/Jeff-Cunha/wsBackend-Fabrica25.2.git
    cd masters-receita  
2.  **Crie e ative um ambiente virtual:**
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
3.  **Instale as dependências do projeto:**
    pip install -r requirements.txt
4.  **Crie e Aplique as migrações do banco de dados:**
5.  python manage.py makemigrations
    python manage.py migrate
6.  **Execute o servidor de desenvolvimento:**
    python manage.py runserver
7.  **Acesse a aplicação:**
    * Abra seu navegador e acesse o site: `http://127.0.0.1:8000/`
