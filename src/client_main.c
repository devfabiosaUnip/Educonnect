#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "client.h"

#ifdef _WIN32
#include <windows.h> // Necessário para SetConsoleOutputCP
#endif

#define DEFAULT_SERVER_IP "192.168.10.173"
#define DEFAULT_SERVER_PORT 8080
#define CONFIG_FILE "config.ini"

// Função para ler configuração do arquivo config.ini
void read_config(char* server_ip, int* server_port) {
    FILE* config = fopen(CONFIG_FILE, "r");
    
    // Valores padrão
    strncpy(server_ip, DEFAULT_SERVER_IP, 49);
    server_ip[49] = '\0';
    *server_port = DEFAULT_SERVER_PORT;
    
    if (config == NULL) {
        printf("⚠️  Arquivo config.ini não encontrado. Usando configuração padrão.\n");
        printf("   Servidor: %s:%d\n\n", server_ip, *server_port);
        return;
    }
    
    char line[256];
    int line_number = 0;
    
    while (fgets(line, sizeof(line), config)) {
        line_number++;
        
        // Ignora comentários e linhas vazias
        if (line[0] == '#' || line[0] == '\n' || line[0] == '\r') {
            continue;
        }
        
        // Remove espaços e quebras de linha
        line[strcspn(line, "\r\n")] = 0;
        
        // Procura por SERVER_IP
        if (strncmp(line, "SERVER_IP=", 10) == 0) {
            char* ip_value = line + 10;
            size_t ip_len = strlen(ip_value);
            
            // Valida tamanho do IP (máximo 49 caracteres)
            if (ip_len == 0) {
                printf("⚠️  Aviso: SERVER_IP vazio na linha %d. Usando padrão.\n", line_number);
            } else if (ip_len >= 50) {
                printf("⚠️  Aviso: SERVER_IP muito longo na linha %d (max 49 chars). Usando padrão.\n", line_number);
            } else {
                strncpy(server_ip, ip_value, 49);
                server_ip[49] = '\0';
            }
        }
        // Procura por SERVER_PORT
        else if (strncmp(line, "SERVER_PORT=", 12) == 0) {
            int port = atoi(line + 12);
            
            // Valida range da porta (1-65535)
            if (port < 1 || port > 65535) {
                printf("⚠️  Aviso: SERVER_PORT inválida na linha %d (%d). Deve estar entre 1-65535. Usando padrão.\n", 
                       line_number, port);
            } else {
                *server_port = port;
            }
        }
    }
    
    fclose(config);
    printf("✅ Configuração carregada de %s\n", CONFIG_FILE);
    printf("   Servidor: %s:%d\n\n", server_ip, *server_port);
}

int main() {
#ifdef _WIN32
    // Configura a página de código do console para UTF-8 no Windows
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
#endif
    
    char server_ip[50];
    int server_port;
    
    printf("Iniciando o cliente de sistema acadêmico...\n");
    
    // Lê configuração
    read_config(server_ip, &server_port);
    
    // Inicia cliente
    start_client(server_ip, server_port);
    return 0;
}
