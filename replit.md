# Sistema Acadêmico PIM

## Visão Geral
Este é um sistema acadêmico desenvolvido em C com arquitetura cliente-servidor. O sistema permite o gerenciamento de alunos, professores, disciplinas, notas e frequências.

## Data da Importação
- **Data**: 01 de Novembro de 2025
- **Origem**: GitHub Import

## Arquitetura do Projeto

### Estrutura
O projeto está organizado em módulos:
- **admin/**: Funcionalidades administrativas (CRUD de usuários)
- **student/**: Funcionalidades do aluno (visualizar notas, faltas)
- **professor/**: Funcionalidades do professor (lançar notas, gerenciar turmas)
- **server_logic/**: Lógica de negócios do servidor
- **storage/**: Persistência de dados em arquivos
- **common_utils/**: Funções utilitárias compartilhadas

### Componentes
- **Servidor**: `sistema_academico_server` - Porta 8080
- **Cliente**: `sistema_academico_client` - Conecta ao servidor

## Configuração do Ambiente Replit

### Compilação
O projeto usa Make para compilação:
```bash
make clean   # Limpa builds antigos
make         # Compila servidor e cliente
```

### Execução
O servidor é executado automaticamente através do workflow configurado:
- **Workflow**: `servidor`
- **Porta**: 8080
- **Comando**: `./sistema_academico_server`

Para executar o cliente manualmente:
```bash
./sistema_academico_client
```

### Persistência de Dados
Os dados são armazenados em:
- `system_data.dat` - Dados binários do sistema
- `alunos.json`, `disciplinas.json`, `notas.json` - Arquivos JSON auxiliares

## Modificações para Replit

### Alterações Realizadas
1. **Makefile atualizado**: Removido flag `-lws2_32` (específico do Windows) para compatibilidade com Linux
2. **Workflow configurado**: Servidor executa automaticamente na porta 8080
3. **Gitignore criado**: Ignora executáveis, arquivos objeto e DLLs
4. **Configuração de Rede**: Adicionado arquivo `config.ini` para configurar IP do servidor
5. **Validação de Segurança**: Cliente valida IP e porta antes de conectar

### Compatibilidade
O código fonte mantém compatibilidade multiplataforma:
- Linux: Usa sockets POSIX padrão
- Windows: Usa Winsock2 (com preprocessador `#ifdef _WIN32`)

### Configuração de Rede Local
O sistema pode funcionar em rede! Consulte `MANUAL_REDE.md` para instruções completas.

**Configuração Rápida:**
1. Edite o arquivo `config.ini` e defina o IP do servidor:
   ```ini
   SERVER_IP=192.168.10.173
   SERVER_PORT=8080
   ```
2. Execute o servidor na máquina principal
3. Copie o cliente + config.ini para outras máquinas
4. Execute o cliente - ele conectará automaticamente ao servidor!

## Estado Atual
- ✅ Projeto compilado com sucesso
- ✅ Servidor rodando na porta 8080
- ✅ Bug de notas corrigido (01/11/2025)
- ✅ Sistema interativo funcionando

## Como Usar o Sistema

O sistema já está rodando! Basta clicar no **Console** do Replit para interagir.

### Credenciais Padrão
**Administrador:**
- Email: `admin@admin.com`
- Senha: `admin123`

### Funcionalidades
1. **Admin**: Criar/gerenciar alunos, professores, disciplinas e turmas
2. **Professor**: Lançar notas e registrar faltas dos alunos
3. **Aluno**: Visualizar suas notas e faltas

## Correções Realizadas

### Bug de Notas Corrigidas (01/11/2025)
- **Problema**: Notas apareciam com valores gigantes ou negativos
- **Causa**: Campo duplicado `score` na estrutura `Grade` não era inicializado
- **Solução**: Removido campo duplicado, sistema agora usa apenas `grade_value`
- **Arquivos alterados**: `src/models.h`, `src/student/student.c`

## Tecnologias
- **Linguagem**: C (C11)
- **Compilador**: GCC
- **Sistema de Build**: Make
- **Rede**: Sockets TCP/IP
- **Persistência**: Arquivos binários e JSON
