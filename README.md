# 👨‍🍳 Chef Virtual

Um projeto simples e divertido que usa **IA (Gemini)** para gerar receitas com base nos ingredientes que o usuário tem em casa. Ideal para quem quer aprender a cozinhar ou está sem ideias!

🌐 Acesse aqui: [https://chef-virtual-qzkk.onrender.com/](https://chef-virtual-qzkk.onrender.com/)

---

## 🚀 Funcionalidades

- 🧠 Geração de receitas usando a API do Gemini (Google AI)
- 🌐 Interface web com Flask + Bootstrap
- 🔐 Uso seguro de variáveis de ambiente com `python-dotenv`
- 💬 Limite de chamadas à API por sessão
- ☁️ Deploy automático com Render

---

## 🛠️ Como rodar localmente

```bash
git clone https://github.com/seu-usuario/chef-virtual.git
cd chef-virtual
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/Mac
pip install -r requirements.txt
