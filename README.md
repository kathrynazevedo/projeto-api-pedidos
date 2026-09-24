## 👥 Integrantes do Grupo

1. **Nome Completo:** Kauê Vitor Pereira Santos
   - **RA:** N083BC4
   - **Turma:** CC8Q13

2. **Nome Completo:** Kathryn Azevedo do Sacramento
   - **RA:** F3560F5
   - **Turma:** CC7P13

3. **Nome Completo:** Renan Albuquerque Nunes
   - **RA:** G8046A4
   - **Turma:** CC8P13

4. **Nome Completo:** Patrick Albuquerque Nunes
   - **RA:** G804759
   - **Turma:** CC8P13

---

## 🚀 Como executar a aplicação

Precisará do **Docker** e do **Docker Compose** (ou Docker Desktop) instalados na sua máquina.

### Método 1: Padrão (Recomendado para a Avaliação)
Conforme especificado nas instruções do trabalho, pode iniciar toda a solução sem procedimentos manuais adicionais utilizando o terminal na pasta raiz do repositório:

```bash
docker compose up -d --build
Método 2: Script Automatizado (Apenas Windows)
Se estiver no Windows, pode também simplesmente dar um duplo clique no ficheiro run.bat. Ele verificará automaticamente se o Docker está a correr e executará os comandos de build e inicialização dos containers de forma segura.

🌐 Acesso à API
Após subir os containers, a API estará disponível na porta 8000.
Pode interagir com ela através da documentação interativa (Swagger UI/Scalar):

👉 Documentação interativa: http://localhost:8000/docs

Endpoints Principais
POST /pedidos: Cria um novo pedido (status inicial: CRIADO).

GET /pedidos/{id}: Consulta um pedido específico pelo seu ID.

GET /pedidos: Lista todos os pedidos existentes.

PATCH /pedidos/{id}/status: Altera o status de um pedido.

GET /health: Verifica a saúde da aplicação.