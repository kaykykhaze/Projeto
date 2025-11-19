IFBA - INSTITUTO FEDERAL DA BAHIA - CAMPUS VALENÇA
CURSO TEC. EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS


Abner Silva de Azevedo 
Kayky Santos Góes 
Marcos Azevedo


Especificação funcional
Better Team


Valença/Ba

1. INTRODUÇÃO
1.1 Propósito
O objetivo deste documento é especificar de forma detalhada os requisitos do sistema de listas compartilhadas e gamificadas desenvolvido para equipes esportivas.
 Ele destina-se a desenvolvedores, testadores, gestores de projeto e demais stakeholders, oferecendo uma visão clara e precisa do software a ser implementado.
1.2 Escopo
O sistema permitirá a criação de equipes esportivas, listas de tarefas, acompanhamento de progresso individual e coletivo, além da aplicação de elementos de gamificação, como pontos, níveis, medalhas e rankings.
As principais funcionalidades são:
- Gerenciamento de usuários
- Criação e administração de equipes
- Listas compartilhadas de atividades
- Progresso e dashboards
- Gamificação
- Notificações
- Feed de atividade

1.3 Definições, Acrônimos e Abreviações
SRS – Software Requirements Specification
RF – Requisito Funcional
RNF – Requisito Não Funcional
API – Application Programming Interface
UI – User Interface
JWT – JSON Web Token

2. DESCRIÇÃO GERAL
2.1 Perspectiva do Produto
O sistema será uma plataforma composta por:
- Aplicação mobile-first
- Interface Web opcional
- Backend baseado em API
- Banco de dados relacional ou NoSQL
- Integrações com serviços de notificação

O produto deve permitir colaboração entre membros de equipes esportivas e incentivar engajamento via gamificação.

2.2 Funções do Produto
O sistema executará as seguintes funções principais:
- Gerenciar contas de usuários
- Gerenciar equipes esportivas
- Criar e manter listas compartilhadas e tarefas
- Registrar progresso e atividades
- Aplicar gamificação: pontos, medalhas e rankings
- Exibir dashboards individuais e coletivos
- Enviar notificações em tempo real

2.3 Características dos Usuários
Atletas: concluem tarefas e acompanham seu progresso.
Líderes/Treinadores: criam listas, atribuem tarefas e monitoram a equipe.
Gestores: visualizam dados macro e desempenho geral.

Perfil esperado:
Usuários com conhecimento básico de aplicativos móveis.
Idade variada, dependendo da modalidade esportiva.

2.4 Restrições
O sistema deve ser desenvolvido com foco mobile-first.
As senhas devem ser armazenadas com criptografia.
A aplicação deve manter disponibilidade mínima de 99%.
Deve suportar escalabilidade para times com muitos membros.
Integração obrigatória com serviços de notificação.

2.5 Suposições e Dependências
O usuário terá acesso à internet.
Os serviços externos (login, push, banco remoto) estarão disponíveis.

3. REQUISITOS ESPECÍFICOS
3.1 Requisitos Funcionais (RF)
3.1.1 Gerenciamento de Usuários
RF01 – O sistema deve permitir criação de contas via e-mail/senha ou login social.
RF02 – Deve permitir login e logout.
RF03 – Deve permitir recuperação de senha.
RF04 – Deve permitir edição de perfil.

3.1.2 Gerenciamento de Equipes
RF05 – Criar equipes com nome, imagem e descrição.
RF06 – Gerar código de convite para novos membros.
RF07 – Permitir entrada por código.
RF08 – Visualizar membros da equipe.
RF09 – Editar informações da equipe.

3.1.3 Listas e Tarefas Compartilhadas
RF10 – Criar listas de atividades.
RF11 – Adicionar tarefas à lista.
RF12 – Definir responsáveis por tarefa.
RF13 – Marcar tarefa como concluída.
RF14 – Editar ou excluir tarefas.
RF15 – Visualizar progresso individual e coletivo.

3.1.4 Gamificação
RF16 – Conceder pontos quando uma tarefa for concluída.
RF17 – Calcular níveis (level) dos usuários.
RF18 – Conceder medalhas por marco ou desempenho.
RF19 – Gerar rankings semanais e mensais.

3.1.5 Feed e Notificações
RF20 – Registrar no feed toda atividade concluída.
RF21 – Enviar notificações push ao concluir tarefas.
RF22 – Enviar notificações quando ranking atualizar.
RF23 – Permitir reações (emojis) no feed.

3.1.6 Dashboard
RF24 – Exibir gráficos de progresso individual.
RF25 – Exibir gráficos de desempenho coletivo.
RF26 – Comparar atletas da equipe.

3.2 Requisitos Não Funcionais (RNF)
3.2.1 Performance
RNF01 – Tempo máximo de resposta da API: 300ms.
RNF02 – Suporte mínimo a 500 usuários simultâneos.

3.2.2 Confiabilidade
RNF03 – Disponibilidade mínima de 99%.
RNF04 – O sistema deve se recuperar automaticamente de falhas simples.

3.2.3 Segurança
RNF05 – Criptografia de senhas via bcrypt.
RNF06 – Token JWT para autenticação.
RNF07 – Controle de acesso baseado em função (membro/líder).
RNF08 – Proteção contra ataques comuns (SQL Injection, XSS, CSRF).

3.2.4 Usabilidade
RNF09 – Interface deve seguir padrões mobile-first.
RNF10 – Navegação deve ser intuitiva e consistente.
RNF11 – Deve seguir diretrizes básicas de acessibilidade.

3.2.5 Manutenibilidade
RNF12 – Arquitetura modular (Clean Architecture).
RNF13 – Código deve possuir documentação mínima nos módulos principais.

3.2.6 Portabilidade
RNF14 – O sistema deve rodar em Android, iOS e Web.
RNF15 – Deve ser implantable via containers.

4. ANEXOS
4.1 Cartões de Tarefas (XP)
User Story 01 – Criar conta
Como usuário, desejo criar uma conta para acessar o sistema.
Critérios de aceitação: cadastro funcionando, validação de dados.

User Story 02 – Criar equipe
Como líder, desejo criar uma equipe para organizar as atividades.

User Story 03 – Criar lista
Como membro, desejo criar listas de tarefas para meu time.

User Story 04 – Concluir tarefa
Como atleta, desejo marcar tarefas realizadas.

User Story 05 – Ganhar pontos
Como atleta, desejo subir de nível e aparecer no ranking.

User Story 06 – Ver dashboard
Como usuário, desejo ver meu progresso.

User Story 07 – Receber notificações
Como usuário, desejo ser notificado das atividades da equipe.

4.2 Spikes
- Estudo de sistemas de ranking gamificado
- Estudo da arquitetura (React Native + Node, ou Flutter)
- Estudo de Push Notification
- Estudo de bibliotecas de gráficos

4.3 Mockups (Descrição)
Tela: Login
- Campo de e-mail
- Campo de senha
- Botão de “Entrar”
- Botão “Criar conta”

Tela: Dashboard
- Gráfico semanal
- Ranking (top 3)
- Resumo de tarefas concluídas

Tela: Equipe
- Foto e nome da equipe
- Lista de membros
- Botão “Criar Lista”

Tela: Lista
- Nome da lista
- Tarefas com checkbox
- Botão “Adicionar Tarefa”

Tela: Gamificação
- Nível atual
- XP acumulado
- Medalhas

4.4 Cronograma (Gantt)
Tabela
Etapa | Semana 1 | Semana 2 | Semana 3 | Semana 4
Planejamento | X |  |  | 
Spikes | X | X |  | 
Backend – Autenticação | X |  |  | 
Backend – Listas |  | X | X | 
Gamificação |  |  | X | 
Frontend – Telas principais |  | X | X | 
Dashboard |  |  | X | X
Testes |  |  |  | X
Deploy |  |  |  | X

Gantt ASCII 
Semana: 1 2 3 4
 Planejamento ██████
 Spikes ██████ ████
 Auth ██████
 Listas ██████ ███
 Gamificação ██████
 Frontend telas █████ ██████
 Dashboard ████ ███
 Testes ██████
 Deploy ███
