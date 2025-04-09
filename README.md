📦 Chef Virtual
Um projeto simples e divertido que usa IA (Gemini) para gerar receitas com base nos ingredientes que o usuário tem em casa. Ideal para quem quer aprender a cozinhar ou está sem ideias!

🚀 Funcionalidades
🧠 Geração de receitas usando a API do Gemini (Google AI)

🌐 Interface web com Flask

🔐 Uso de variáveis de ambiente com python-dotenv

📋 Planejamento de integração com banco de dados ou Google Sheets

📱 Preparado para virar um app futuramente!

🛠️ Como rodar o projeto localmente
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/chef-virtual.git
cd chef-virtual
Crie e ative o ambiente virtual:

bash
Copiar código
python -m venv venv
venv\Scripts\activate  # no Windows
source venv/bin/activate  # no Linux/Mac
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Crie um arquivo .env com sua chave da API Gemini:

ini
Copiar código
GEMINI_API_KEY=sua_chave_aqui
Rode a aplicação:

bash
Copiar código
python app.py
💡 Exemplo de uso
Digite os ingredientes no campo do formulário, como por exemplo:

Copiar código
tomate, arroz, frango
E o Chef Virtual vai te surpreender com uma receita exclusiva! 👨‍🍳✨

🔮 Próximos passos
Conectar com Google Sheets ou banco de dados

Armazenar receitas geradas

Criar login de usuários

Transformar em aplicativo mobile

🧑‍💻 Desenvolvido por
Raquel 💙
Estudante de Engenharia da Computação, apaixonada por tecnologia, IA e comida boa!

