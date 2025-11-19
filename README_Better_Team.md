# 📘 Especificação Funcional — **Better Team**

Instituto Federal da Bahia — **Campus Valença**  
Curso Técnico em **Análise e Desenvolvimento de Sistemas**

---

## 👤 Autores
- **Abner Silva de Azevedo**  
- **Kayky Santos Góes**  
- **Marcos Azevedo**

---

## 📄 Documento: *Especificação Funcional — Better Team*  
Local: Valença/BA  

---

# 1. Introdução

## 1.1 Propósito  
Este documento descreve de maneira detalhada os requisitos funcionais e não funcionais do sistema **Better Team**, voltado para gerenciamento de equipes esportivas por meio de listas compartilhadas e gamificação.  
O material destina-se a desenvolvedores, analistas, gestores e demais stakeholders envolvidos no projeto.

## 1.2 Escopo  
O sistema permitirá:  
- Criação de equipes esportivas  
- Listas compartilhadas de atividades  
- Acompanhamento de progresso  
- Gamificação (pontos, níveis, medalhas, ranking)  
- Notificações  
- Dashboards  
- Feed de atividades  

## 1.3 Glossário  
| Sigla | Definição |
|-------|-----------|
| **SRS** | Software Requirements Specification |
| **RF** | Requisito Funcional |
| **RNF** | Requisito Não Funcional |
| **API** | Application Programming Interface |
| **UI** | User Interface |
| **JWT** | JSON Web Token |

---

# 2. Descrição Geral

## 2.1 Perspectiva do Produto  
O sistema será composto por:  
- Aplicativo *mobile-first*  
- Web App opcional  
- Backend em API  
- Banco relacional ou NoSQL  
- Integração com notificações push  

## 2.2 Funções Principais  
- Gerenciar usuários  
- Gerenciar equipes  
- Criar e acompanhar listas de tarefas  
- Gamificação  
- Dashboards  
- Notificações  

## 2.3 Perfil dos Usuários  
- **Atletas**: execução de tarefas  
- **Líderes/Treinadores**: gerenciamento  
- **Gestores**: supervisão macro  

## 2.4 Restrições  
- Foco *mobile-first*  
- Criptografia de senhas  
- Disponibilidade mínima de 99%  
- Escalabilidade  
- Notificações obrigatórias  

## 2.5 Suposições  
- Usuários terão acesso à internet  
- Serviços externos estarão operacionais  

---

# 3. Requisitos Específicos

## 3.1 Requisitos Funcionais (RF)

### 3.1.1 Usuários  
- **RF01** Criar contas (e-mail/senha ou social login)  
- **RF02** Login/logout  
- **RF03** Recuperação de senha  
- **RF04** Edição de perfil  

### 3.1.2 Equipes  
- **RF05** Criar equipes  
- **RF06** Código de convite  
- **RF07** Entrada via código  
- **RF08** Visualizar membros  
- **RF09** Editar equipe  

### 3.1.3 Listas  
- **RF10** Criar listas  
- **RF11** Adicionar tarefas  
- **RF12** Atribuir responsáveis  
- **RF13** Concluir tarefas  
- **RF14** Editar/excluir  
- **RF15** Visualizar progresso  

### 3.1.4 Gamificação  
- **RF16** Pontuação  
- **RF17** Níveis  
- **RF18** Medalhas  
- **RF19** Rankings  

### 3.1.5 Feed & Notificações  
- **RF20** Registro de atividades  
- **RF21** Notificações push  
- **RF22** Atualização de ranking  
- **RF23** Reações (emojis)  

### 3.1.6 Dashboard  
- **RF24** Gráficos individuais  
- **RF25** Gráficos coletivos  
- **RF26** Comparações entre atletas  

---

## 3.2 Requisitos Não Funcionais (RNF)

### Performance  
- **RNF01** API ≤ 300ms  
- **RNF02** 500 usuários simultâneos  

### Confiabilidade  
- **RNF03** Disponibilidade 99%  
- **RNF04** Recuperação automática  

### Segurança  
- **RNF05** Hash de senhas (bcrypt)  
- **RNF06** JWT  
- **RNF07** Controle de acesso por função  
- **RNF08** Proteção contra ataques comuns  

### Usabilidade  
- **RNF09** Mobile-first  
- **RNF10** Navegação intuitiva  
- **RNF11** Acessibilidade básica  

### Manutenibilidade  
- **RNF12** Arquitetura modular  
- **RNF13** Documentação mínima  

### Portabilidade  
- **RNF14** Suporte Android, iOS e Web  
- **RNF15** Deploy via containers  

---

# 4. Anexos

## 4.1 Cartões de Tarefa (XP)  
- **US01** Criar conta  
- **US02** Criar equipe  
- **US03** Criar lista  
- **US04** Concluir tarefa  
- **US05** Ganhar pontos  
- **US06** Visualizar dashboard  
- **US07** Receber notificações  

---

## 4.2 Spikes  
- Ranking gamificado  
- Arquitetura (RN + Node ou Flutter)  
- Notificações push  
- Bibliotecas de gráficos  

---

## 4.3 Mockups (Descrição)  
- Login  
- Dashboard  
- Equipe  
- Lista  
- Gamificação  

---

## 4.4 Cronograma (Gantt)  
```
Semana:       1   2   3   4
Planejamento ██████
Spikes       ██████ ████
Auth         ██████
Listas       ██████ ███
Gamificação            ██████
Frontend         █████ ██████
Dashboard               ████ ███
Testes                        ██████
Deploy                        ███
```

---



