# Levantamento de Requisitos – Projeto Baronet

## 1. Introdução

### 1.1. Objetivo do Documento
Este documento tem como objetivo registrar os requisitos do projeto **Baronet**, um jogo digital desenvolvido por estudantes do Ensino Médio da escola Orígenes Lessa – Turma 2B. O projeto é voltado para o aprendizado multidisciplinar, desenvolvimento de competências e práticas de trabalho em equipe, tendo como produto final um jogo funcional a ser apresentado até a segunda sexta-feira de outubro.

### 1.2. Escopo do Sistema
O Baronet será um jogo desenvolvido em **Python puro**, voltado à plataforma **PC (desktop)**. O projeto não tem fins comerciais nem usuários finais definidos, sendo direcionado à avaliação interna e possível continuidade em anos seguintes.

---

## 2. Descrição Geral

### 2.1. Contexto e Motivação
O projeto foi idealizado como ferramenta pedagógica para integrar diferentes disciplinas e fomentar o comprometimento dos alunos com um trabalho prático de médio prazo.

### 2.2. Stakeholders
- Estudantes desenvolvedores (2 programadores principais)
- Professores e orientadores
- Demais alunos da turma 2B
- Coordenação escolar (avaliação e apresentação final)

---

## 3. Requisitos de Negócio

### 3.1. Objetivos de Negócio
- Desenvolver competências técnicas e interpessoais nos alunos
- Entregar um produto jogável, funcional e coeso até o prazo estipulado
- Usar o projeto como ferramenta interdisciplinar

### 3.2. Regras de Negócio
- O jogo deve funcionar em qualquer PC (baixa exigência de hardware)
- Os dados do jogador (saves) não podem ser perdidos entre sessões
- O progresso do jogador deve ser salvo de forma automática ou manual com consistência

---

## 4. Requisitos de Usuário

### 4.1. Perfis de Usuário
- **Jogador local**: membro da própria equipe ou colegas testando o projeto
- **Apresentadores**: estudantes que irão conduzir a exibição final do jogo
- **Professores**: avaliadores da execução e apresentação

### 4.2. Jornada do Usuário
1. Abrir o jogo  
2. Iniciar ou continuar uma partida  
3. Jogar com progressão básica (ex: combate)  
4. Salvar e carregar progresso  
5. Encerrar sessão  

---

## 5. Requisitos Funcionais

| Código | Requisito             | Descrição                                                                 |
|--------|------------------------|---------------------------------------------------------------------------|
| RF‑01  | Tela de Início         | Permitir iniciar nova partida ou carregar uma existente                  |
| RF‑02  | Sistema de Combate     | Implementar combate funcional com feedback visual                        |
| RF‑03  | Sistema de Salvamento  | Permitir salvar e carregar progresso do jogador                          |
| RF‑04  | Tela de Jogo           | Exibir HUD com informações relevantes (vida, itens etc.)                 |
| RF‑05  | Progresso de Fase      | Incluir ao menos uma fase jogável com objetivo visual claro              |

---

## 6. Requisitos Não Funcionais

| Código | Requisito      | Descrição                                                                 |
|--------|----------------|---------------------------------------------------------------------------|
| RNF‑01 | Acessibilidade | O jogo deve rodar em qualquer PC sem exigir instalação externa complexa   |
| RNF‑02 | Persistência   | Os dados devem ser armazenados localmente com segurança e integridade     |
| RNF‑03 | Baixo Consumo  | O desempenho deve ser aceitável em máquinas com recursos limitados        |
| RNF‑04 | Robustez       | O sistema não deve travar ou corromper saves em caso de falhas            |

---

## 7. Interfaces e Integrações

- **Sem integrações externas planejadas**
- Sistema de arquivos local para manipulação de saves (`.json`, `.txt`, ou `.pickle`)

---

## 8. Restrições e Premissas

- Desenvolvimento apenas em Python, sem uso de engines externas (ex: Unity, Godot)
- Sem orçamento para licenças ou recursos pagos
- Prazo final: **segunda sexta-feira de outubro**
- Equipe de desenvolvimento limitada a **2 programadores**
- Recursos visuais e sonoros limitados à produção própria ou fontes gratuitas

---

## 9. Riscos e Mitigações

| Risco         | Descrição                                 | Mitigação                                                  |
|---------------|-------------------------------------------|------------------------------------------------------------|
| Atrasos       | Poucos programadores e muito escopo       | Reduzir funcionalidades não essenciais, focar em um MVP    |
| Perda de dados| Saves corrompidos ou não persistidos      | Implementar backup automático ou duplo sistema de save     |
| Bugs críticos | Falhas em combate ou tela de jogo         | Testes semanais e versão mínima funcional até setembro     |
