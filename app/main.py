import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.api import pedidos

# Cria as tabelas no banco de dados se não existirem
Base.metadata.create_all(bind=engine)

# Inicializa o app FastAPI
app = FastAPI(title="API de Pedidos", docs_url=None, redoc_url=None)

# Descobre o diretório atual onde main.py está (pasta app)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho da pasta static que agora está dentro de app
STATIC_DIR = os.path.join(CURRENT_DIR, "static")

# Monta a pasta estática com o novo caminho
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Inclui as rotas de pedidos
app.include_router(pedidos.router)

@app.get("/health", tags=["Sistema"])
def health_check():
    return {"status": "ok"}

@app.get("/docs", include_in_schema=False)
def custom_docs():
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>API de Pedidos</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="/static/styles.css?v=3" />
      </head>
      <body>
        
        <!-- Botão flutuante para reabrir o menu quando ele estiver escondido -->
        <button id="show-sidebar-btn" onclick="toggleSidebar()">
            ☰ Mostrar Menu
        </button>

        <script 
            id="api-reference" 
            data-url="/openapi.json"
            data-configuration='{
                "hideSearch": true,
                "hideDownloadButton": true
            }'
        ></script>
        <script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>

        <script>
            // Função para alternar o estado do menu
            function toggleSidebar() {
                document.body.classList.toggle('hide-sidebar');
            }

            // Injeta o botão de fechar dentro do menu lateral assim que a página carregar
            window.addEventListener('DOMContentLoaded', () => {
                const checkSidebar = setInterval(() => {
                    const sidebar = document.querySelector('.sidebar');
                    if (sidebar && !document.getElementById('toggle-sidebar-btn')) {
                        clearInterval(checkSidebar);
                        
                        const closeBtn = document.createElement('button');
                        closeBtn.id = 'toggle-sidebar-btn';
                        closeBtn.innerHTML = '✕ Fechar Menu';
                        closeBtn.onclick = toggleSidebar;
                        
                        // Insere o botão no topo da barra lateral
                        sidebar.prepend(closeBtn);
                    }
                }, 100);
            });
        </script>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)