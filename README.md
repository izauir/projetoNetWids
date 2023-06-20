# Net Wids
![Image 1](imgReadme/logoNetwids.png)

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/devsuperior/sds1-wmazoni/blob/master/LICENSE) 

# Sobre o projeto

Este trabalho visa apresentar a prototipação de um software de agenda infantil através de
cronograma de tarefas e suas recompensas. A plataforma oferece opções de criação de
tarefas e gerenciamento das mesmas e leitura.

## Layout mobile
![Image 2](imgReadme/01.png) ![Image 3](imgReadme/02.png)

![Image 4](imgReadme/03.png) ![Image 5](imgReadme/04.png)

## Modelo conceitual
![Modelo Conceitual](imgReadme/05.png)

# Tecnologias utilizadas

## Linguagem
- Python
## Ferramentas
- Figma (construção do layout)

# Como funciona o sistema:

+ **Cadastro:** Ao clicar em cadastro será direcionado a um formulário no final da 
página, e ao submete-lo o envio, será realizada a conferencia dos dados e 
apresentação dos termos de uso.
+ **Login:** Ao clicar será redirecionado a página de login do sistema em uma outra 
aba (Se estiver o fazendo pela primeira vez o sistema cria automaticamente um 
usuário e senha “admin”,” admin” respectivamente). Os campos para 
preenchimento são intuitivos e descritos.
+ **Dentro do sistema:** As funções de cada menu serão descritas abaixo.

## Tarefas
1) **Criação Tarefa:** O responsável pode fazê-lo ao selecionar a 
opção “Tarefas” na página de menu e em seguida o símbolo “+”.
Será direcionado a página de criação dos cartões de tarefa, onde 
se estabelece a tarefa, uma capa, descrição, quantidade de 
troféus, prazo e recompensa.

2)  **Seleção Tarefa:** Página direcionada a visualização dos cartões 
de tarefas disponíveis de acordo com a criação do responsável, 
para que sejam escolhidas e selecionadas. O acesso é através 
da seleção da opção “Tarefas” na página de menu

3) **Status Tarefa:** Existem campos a serem preenchidos (seleção 
do ícone de status), após completa-los será gerada realizada a 
contagem de troféus comparada a expectativa. O acesso é 
através da seleção do cartão de determinada tarefa, é possível 
checar a situação da tarefa, seu prazo e quantidade de troféus.

5) create file .env (can copy from .env.example)
6) configure your database variables in .env
7) run shell: php artisan migrate
8) run shell: php artisan serve


+ sequency num
+ dificult category
+ i know
+ user_id
+ image

# Autores

*FELIPE RAFAEL - 059402* <br>
*GABRIEL MICHELAN - 059009* <br>
*IZAUIR GUILHERME - 175353* <br>
*JOYCE BARROS - 059339*
