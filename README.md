# 🚀 LabSpace - Jogo de Nave em Python

![Banner do Jogo](https://prnt.sc/83olBgY-EEtX)  
*Um jogo de nave espacial desenvolvido com Pygame para a disciplina de Orientação a Objetos*

## 📌 Índice
- [🎮 Sobre o Jogo](#-sobre-o-jogo)
- [✨ Funcionalidades](#-funcionalidades)
- [🛠 Tecnologias](#-tecnologias)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [🚀 Como Executar](#-como-executar)
- [🎛 Controles](#-controles)
- [🧠 Conceitos de OO](#-conceitos-de-oo)
- [📊 Critérios Atendidos](#-critérios-atendidos)
- [📅 Informações Acadêmicas](#-informações-acadêmicas)

## 🎮 Sobre o Jogo
LabSpace é um jogo 2D onde o jogador controla uma nave espacial que deve:
- Destruir naves inimigas
- Sobreviver o máximo de tempo possível
- Atingir altas pontuações
- Competir pelo top 10 do ranking

## ✨ Funcionalidades
| Feature | Descrição |
|---------|-----------|
| 🎛 Menu Interativo | Telas de Jogar, Ranking e Sair |
| 📈 Sistema de Pontos | Pontuação com bônus por nível |
| 🏆 Ranking | Top 10 jogadores persistido em JSON |
| � Níveis Progressivos | Dificuldade aumenta a cada fase |
| ❤️ Sistema de Vida | Barra de vida e dano por colisão |

## 🛠 Tecnologias
- ![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
- ![Pygame](https://img.shields.io/badge/Pygame-2.0+-green?logo=pygame)
- ![JSON](https://img.shields.io/badge/JSON-Data%20Persistence-yellow)

## 📂 Estrutura do Projeto

```bash
LabSpace/
├── main.py                 # Ponto de entrada
├── package/
│   ├── classes/            # Classes do sistema
│   │   ├── button.py       # Botões UI
│   │   ├── controlador.py  # Lógica principal
│   │   ├── inimigos.py     # Inimigos
│   │   └── ...             # Demais classes
│   └── assets/             # Recursos visuais
├── ranking.json            # Dados do ranking
└── README.md               # Documentação
```

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/LabSpace.git
cd LabSpace
```
2. Instale as dependências:
```bash
pip install pygame
```
4. Execute o jogo:
```bash
python main.py
```

## 🎮 Controles
Tecla	Ação
↑ ↓ ← → Para a Movimentação da nave
Espaço	Disparar lasers
Enter	Confirmar nome no ranking


## 🧠 Conceitos de OO
Conceito	Implementação	Arquivo
Herança	Jogador e Inimigo herdam de Nave	nave.py
Polimorfismo	move_lasers() com comportamentos diferentes	jogador.py/inimigos.py
Composição	Nave contém Laser	nave.py
Encapsulamento	Atributos privados com métodos públicos	Todas classes

## 📊 Critérios Atendidos
✔️ Programa funcional sem bugs

✔️ Modelagem OO completa (4+ relacionamentos)

✔️ Serialização (JSON para ranking)

✔️ Interface gráfica elegante

✔️ Documentação completa

## 📅 Informações Acadêmicas
Item	Detalhe
🏫 Instituição	UnB Gama
📚 Disciplina	Orientação a Objetos
👨‍🏫 Professor	Henrique Moura
📆 Data de Entrega	23/05/2025

👨‍💻 Desenvolvido por: Pablo Antonio
🔗 GitHub: github.com/pablosousaa
