Sistema de Cadastro de Pessoas (Curso em Vídeo - Python 3 Mundo 3 - Exercício 115)
Visão Geral do Projeto
Este projeto é uma aplicação desenvolvida em Python como parte do curso Python 3 Mundo 3 do Curso em Vídeo (Exercícios 115a, 115b e 115c). O sistema é um Sistema de Cadastro de Pessoas que permite gerenciar uma lista de pessoas, com seus nomes e idades, armazenada de forma persistente em um arquivo de texto. O sistema conta com uma interface de menu amigável, tratamento robusto de erros e manipulação de arquivos para garantir a persistência de dados entre execuções do programa.
O projeto está dividido em três partes principais, conforme os módulos do curso:

Exercício 115a: Criação de um sistema modularizado com uma interface de menu e validação básica de entradas.
Exercício 115b: Implementação de manipulação de arquivos para leitura e escrita dos dados de cadastro em um arquivo de texto.
Exercício 115c: Finalização do projeto, integrando todos os componentes e adicionando tratamento de erros para operações de arquivo e entradas do usuário.

Funcionalidades

Menu Interativo: Permite ao usuário escolher entre:
Visualizar todas as pessoas cadastradas.
Cadastrar uma nova pessoa (nome e idade).
Sair do sistema.


Manipulação de Arquivos: Armazena os dados de cadastro em um arquivo de texto (cadastro.txt) para persistência.
Tratamento de Erros: Valida entradas do usuário (por exemplo, garantindo que a idade seja um número inteiro válido) e gerencia erros relacionados a arquivos (como arquivo não encontrado).
Estrutura Modular: O código é organizado em módulos separados para melhor manutenibilidade:
interface.py: Gerencia a interface do usuário, como exibição do menu e formatação de saídas.
arquivo.py: Contém funções para leitura e escrita no arquivo de texto.
sistema.py: Integra os módulos e contém a lógica principal do programa.



Tecnologias Utilizadas

Python 3: Linguagem de programação usada para desenvolver o sistema.
Módulos Python:
time: Para pausas na interface, melhorando a experiência do usuário.
Não são utilizados módulos externos, apenas a biblioteca padrão do Python.


Arquivo de Texto: Armazenamento simples dos dados em formato .txt.

Estrutura do Projeto
sistema_cadastro/
│
├── lib/
│   ├── interface.py    # Funções para a interface do usuário (menu, cabeçalhos, etc.)
│   └── arquivo.py      # Funções para manipulação de arquivos (leitura e escrita)
│
├── sistema.py          # Arquivo principal que integra os módulos e executa o sistema
├── cadastro.txt        # Arquivo de texto para armazenar os dados de cadastro
└── README.md           # Este arquivo

Como Executar

Certifique-se de ter o Python 3 instalado em seu sistema.
Clone este repositório:git clone https://github.com/fabioliveira-dev/Sistema_de_Cadastro_de_Pessoas


Navegue até o diretório do projeto:cd sistema_cadastro


Execute o arquivo principal:python sistema.py


Siga as instruções do menu interativo para cadastrar pessoas, visualizar cadastros ou sair.

Exemplo de Uso
Ao executar o programa, o usuário verá um menu como este:
----------------------------------------
          SISTEMA DE CADASTRO
----------------------------------------
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
----------------------------------------
Digite sua opção: 


Escolhendo 1, o sistema exibe a lista de pessoas cadastradas no arquivo cadastro.txt.
Escolhendo 2, o usuário pode inserir o nome e a idade de uma nova pessoa, que será salva no arquivo.
Escolhendo 3, o programa encerra com uma mensagem de despedida.

Aprendizados
Este projeto foi desenvolvido para praticar os seguintes conceitos de Python:

Modularização de código.
Manipulação de arquivos (leitura e escrita).
Tratamento de erros com try-except.
Criação de interfaces de usuário simples e funcionais.
Boas práticas de organização de código.

Contribuições
Este é um projeto educacional, mas sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
Créditos
Desenvolvido como parte do curso Python 3 Mundo 3 do Curso em Vídeo, ministrado por Gustavo Guanabara.
