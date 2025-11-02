#!/bin/bash

# Para qualquer servidor rodando
pkill -f sistema_academico_server 2>/dev/null

# Inicia o servidor em background
echo "🚀 Iniciando servidor em background..."
./sistema_academico_server &
SERVER_PID=$!

# Aguarda o servidor inicializar
sleep 2

# Verifica se o servidor está rodando
if ps -p $SERVER_PID > /dev/null; then
    echo "✅ Servidor rodando (PID: $SERVER_PID)"
    echo "📱 Iniciando cliente..."
    echo "================================"
    echo ""
    
    # Executa o cliente (interativo)
    ./sistema_academico_client
    
    # Quando o cliente fechar, para o servidor
    echo ""
    echo "Encerrando servidor..."
    kill $SERVER_PID 2>/dev/null
else
    echo "❌ Erro ao iniciar servidor"
fi
