# 📡 Manual de Configuração de Rede - Sistema Acadêmico

## 🎯 Visão Geral

Este manual explica como configurar o Sistema Acadêmico para funcionar em rede, com o **servidor rodando em uma máquina** e **clientes conectando de outras máquinas**.

---

## 🖥️ Configuração do Servidor

### Passo 1: Descobrir o IP da máquina servidor

**No Windows:**
```cmd
ipconfig
```
Procure por "IPv4 Address" na interface de rede ativa (ex: `192.168.10.173`)

**No Linux/Mac:**
```bash
ip addr show
# ou
ifconfig
```
Procure pelo endereço IP da interface ativa (ex: `192.168.10.173`)

### Passo 2: Executar o Servidor

Na máquina que será o servidor, execute:

**Windows:**
```cmd
sistema_academico_server.exe
```

**Linux:**
```bash
./sistema_academico_server
```

Você verá:
```
Iniciando o servidor de sistema acadêmico...
Servidor escutando na porta 8080...
```

✅ **O servidor está pronto e aguardando conexões!**

### Passo 3: Configurar Firewall (Importante!)

O firewall precisa permitir conexões na **porta 8080**.

**Windows Firewall:**
1. Abra "Windows Defender Firewall com Segurança Avançada"
2. Clique em "Regras de Entrada" → "Nova Regra"
3. Tipo: "Porta" → Próximo
4. Protocolo: TCP, Porta específica: `8080` → Próximo
5. Ação: "Permitir a conexão" → Próximo
6. Perfil: Marque todos → Próximo
7. Nome: "Sistema Acadêmico - Porta 8080" → Concluir

**Linux (UFW):**
```bash
sudo ufw allow 8080/tcp
sudo ufw reload
```

**Linux (iptables):**
```bash
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
sudo iptables-save
```

---

## 💻 Configuração dos Clientes

### Método 1: Usando arquivo config.ini (Recomendado)

**Passo 1:** Na pasta onde está o executável do cliente, crie/edite o arquivo `config.ini`:

```ini
# Configuração do Sistema Acadêmico
SERVER_IP=192.168.10.173
SERVER_PORT=8080
```

**Passo 2:** Copie o arquivo `config.ini` junto com o executável do cliente para cada máquina cliente.

**Passo 3:** Execute o cliente:

**Windows:**
```cmd
sistema_academico_client.exe
```

**Linux:**
```bash
./sistema_academico_client
```

O cliente lerá automaticamente o IP do arquivo `config.ini` e conectará ao servidor!

---

## 🔧 Como Alterar o IP do Servidor

### Opção 1: Editar config.ini (Mais Fácil)

1. Abra o arquivo `config.ini` com qualquer editor de texto
2. Altere a linha `SERVER_IP=` para o novo IP:
   ```ini
   SERVER_IP=192.168.15.100
   ```
3. Salve o arquivo
4. Execute o cliente novamente

### Opção 2: Recompilar o cliente com novo IP padrão

Se você quiser que o IP fique embutido no executável:

1. Abra o arquivo `src/client_main.c`
2. Encontre a linha:
   ```c
   #define DEFAULT_SERVER_IP "192.168.10.173"
   ```
3. Altere para o novo IP:
   ```c
   #define DEFAULT_SERVER_IP "192.168.15.100"
   ```
4. Recompile:
   ```bash
   make clean
   make
   ```

---

## 📋 Cenários de Uso Comuns

### Cenário 1: Servidor e Cliente na mesma máquina (Desenvolvimento)

**config.ini:**
```ini
SERVER_IP=127.0.0.1
SERVER_PORT=8080
```

### Cenário 2: Servidor em outra máquina na rede local (Produção)

**config.ini:**
```ini
SERVER_IP=192.168.10.173
SERVER_PORT=8080
```

### Cenário 3: Servidor em rede diferente (VPN/Internet)

**config.ini:**
```ini
SERVER_IP=200.150.100.50
SERVER_PORT=8080
```

---

## 🧪 Testando a Conexão

### Teste 1: Ping

Antes de executar o cliente, teste se a máquina cliente consegue "enxergar" o servidor:

```bash
ping 192.168.10.173
```

Se receber respostas, a rede está OK!

### Teste 2: Telnet (Teste de Porta)

**Windows:**
```cmd
telnet 192.168.10.173 8080
```

**Linux:**
```bash
telnet 192.168.10.173 8080
# ou
nc -zv 192.168.10.173 8080
```

Se conectar, a porta está aberta e o servidor está rodando!

---

## ❌ Resolução de Problemas

### Erro: "Não foi possível conectar ao servidor"

**Causas possíveis:**

1. **Servidor não está rodando**
   - Solução: Inicie o servidor na máquina servidor

2. **IP incorreto no config.ini**
   - Solução: Verifique o IP correto com `ipconfig` ou `ip addr`

3. **Firewall bloqueando**
   - Solução: Configure o firewall conforme instruções acima

4. **Máquinas em redes diferentes**
   - Solução: Certifique-se que ambas estão na mesma rede local ou configure roteamento

5. **Porta 8080 já em uso**
   - Solução: Feche outros programas usando a porta 8080
   - Para verificar: `netstat -ano | findstr 8080` (Windows) ou `netstat -tlnp | grep 8080` (Linux)

### Erro: "Conexão recusada"

- **Causa**: Firewall ou servidor não iniciado
- **Solução**: Verifique se o servidor está rodando e configure o firewall

### Cliente conecta mas não recebe resposta

- **Causa**: Versões incompatíveis de servidor/cliente
- **Solução**: Use a mesma versão compilada em ambas as máquinas

---

## 📦 Distribuição para Outras Máquinas

### O que copiar para as máquinas clientes:

**Windows:**
```
📁 Pasta_Cliente/
  ├── sistema_academico_client.exe
  └── config.ini
```

**Linux:**
```
📁 Pasta_Cliente/
  ├── sistema_academico_client
  └── config.ini
```

**Apenas isso!** O cliente não precisa de mais nada.

---

## 🔐 Segurança

⚠️ **Importante:**
- Este sistema foi projetado para uso em **rede local confiável**
- Não exponha a porta 8080 diretamente para a Internet
- Use VPN se precisar acessar de redes externas
- Os dados são enviados sem criptografia (rede local apenas)

---

## 💡 Dicas

1. **Anote o IP do servidor**: Cole um papel físico na máquina com o IP para facilitar
2. **IP Fixo**: Configure IP fixo no servidor para não mudar toda hora
3. **Teste primeiro na mesma máquina**: Use `127.0.0.1` antes de testar em rede
4. **Backup dos dados**: Faça backup do arquivo `system_data.dat` regularmente

---

## 📞 Configurações de Exemplo

### Escola com 1 Servidor e 3 Computadores Cliente

**Servidor (Secretaria - IP: 192.168.1.100):**
```bash
./sistema_academico_server
```

**Cliente 1 (Coordenação - config.ini):**
```ini
SERVER_IP=192.168.1.100
SERVER_PORT=8080
```

**Cliente 2 (Sala dos Professores - config.ini):**
```ini
SERVER_IP=192.168.1.100
SERVER_PORT=8080
```

**Cliente 3 (Biblioteca - config.ini):**
```ini
SERVER_IP=192.168.1.100
SERVER_PORT=8080
```

Todos se conectam ao mesmo servidor e compartilham os mesmos dados! 🎉

---

## ✅ Checklist de Configuração

- [ ] Descobri o IP da máquina servidor
- [ ] Servidor está rodando
- [ ] Firewall configurado para permitir porta 8080
- [ ] Arquivo `config.ini` criado com o IP correto
- [ ] Cliente e `config.ini` copiados para máquinas clientes
- [ ] Testei a conexão com ping
- [ ] Cliente conectou com sucesso

---

**Última atualização:** 01/11/2025
