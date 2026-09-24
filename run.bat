@echo off
echo ========================================================
echo Verificando dependencias do sistema...
echo ========================================================

:: 1. Verifica se o comando 'docker' existe (se esta instalado)
where docker >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] O Docker nao foi encontrado nesta maquina!
    echo Para rodar a API de Pedidos, voce precisa do Docker Desktop instalado.
    echo.
    echo Pressione qualquer tecla para abrir a pagina de download do Docker...
    pause >nul
    start https://www.docker.com/products/docker-desktop/
    exit /b
)

:: 2. Verifica se o Docker Engine esta rodando
docker info >nul 2>&1
if %ERRORLEVEL% EQU 0 goto DOCKER_RUNNING

echo O Docker esta instalado, mas nao esta rodando.
echo Iniciando o Docker Desktop automaticamente...
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
echo Aguardando o motor do Docker iniciar (isso pode levar alguns instantes)...

:WAIT_DOCKER
timeout /t 5 /nobreak >nul
docker info >nul 2>&1
if %ERRORLEVEL% NEQ 0 goto WAIT_DOCKER

echo Docker iniciado com sucesso!

:DOCKER_RUNNING
echo.
echo Preparando o ambiente...
echo [1/3] Parando e removendo containers antigos...
docker compose down

echo [2/3] Reconstruindo a imagem sem cache para aplicar alteracoes...
docker compose build --no-cache

echo [3/3] Iniciando o ambiente em segundo plano...
docker compose up -d

echo ========================================================
echo Ambiente pronto! Acesse a documentacao em:
echo http://localhost:8000/docs
echo ========================================================
pause