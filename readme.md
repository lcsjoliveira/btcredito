# Projeto CNJ Processing

Este projeto utiliza Django para criar dois endpoints que processam números CNJ (Cadastro Nacional de Justiça) e realizam integrações com um serviço externo. Para gerenciar o processamento assíncrono das requisições, utilizei **Celery** em conjunto com **Redis** como Message Broker.

## Justificativa para o uso de Celery e Redis

### Celery:
O Celery foi escolhido como solução para executar tarefas em segundo plano, possibilitando o processamento assíncrono. Isso é fundamental para:

- Evitar que a aplicação web fique bloqueada enquanto realiza chamadas a serviços externos.
- Melhorar a escalabilidade e o desempenho, especialmente em cenários com alta demanda, como o processamento de até 100 chamadas por minuto.

### Redis:
Redis foi escolhido como o Message Broker por ser rápido, eficiente e fácil de integrar com o Celery. Redis gerencia as filas de tarefas, distribuindo-as para os workers de forma escalável. Ele garante que as tarefas sejam processadas de forma eficiente e paralela, ajudando o sistema a lidar com picos de carga e evitar congestionamento.

Essa combinação de Celery e Redis torna a arquitetura do projeto robusta e escalável, pronta para processar grandes volumes de requisições sem sacrificar o desempenho.

# Endpoints:
Primeiro Endpoint (api_cnj_process/) é responsável por receber e iniciar o processamento de um número CNJ de forma assíncrona.
Segundo Endpoint (api_cnj_external-service/) faz a chamada a um serviço externo para obter mais informações sobre o CNJ e armazena esses dados no banco de dados.
Esses dois endpoints trabalham em conjunto para garantir que o processamento do CNJ e a comunicação com serviços externos sejam feitos de maneira eficiente e escalável.

# Dependências do Projeto
No arquivo requirements.txt, está listado as dependências necessárias para funcionamento do projeto.