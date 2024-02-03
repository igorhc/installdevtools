# Configurador de Ambiente de Desenvolvimento para Ubuntu

Transforme sua máquina Ubuntu em uma poderosa estação de trabalho de desenvolvimento com apenas alguns comandos. Nosso configurador foi meticulosamente testado e aprimorado para a versão 23.10 do Ubuntu, garantindo uma instalação sem problemas das ferramentas mais essenciais para desenvolvedores modernos. Seja para programação, design, ou qualquer outra necessidade de desenvolvimento, nossa ferramenta proporciona uma instalação rápida e eficiente de softwares indispensáveis, como Visual Studio Code, Google Chrome, e muito mais. Simplifique a configuração do seu ambiente de desenvolvimento e maximize sua produtividade com nossa solução tudo-em-um.

## Recursos Principais

- **Instalação Automatizada do Node.js:** Aproveite a facilidade de instalar o Node.js com o fnm, escolhendo a versão que melhor se adapta aos seus projetos.
- **Editores de Código de Ponta:** Tenha acesso imediato aos editores de código líderes de mercado, Visual Studio Code e Sublime Text 3, instalados automaticamente para maximizar sua produtividade.
- **Navegação e Testes com Chrome:** O Google Chrome é instalado para assegurar que você tenha as melhores ferramentas para testar e depurar suas aplicações web.
- **Música com Spotify:** Para aqueles momentos em que você precisa relaxar ou se concentrar, o Spotify é instalado como parte do seu ambiente de desenvolvimento.

## Como Utilizar

1. Clone este repositório para sua máquina Ubuntu com:

```sh
git clone https://github.com/igorhc/installdevtools
cd installdevtools
cd installdevtools
chmod +755 installdevtools.py
```

2. Entre no diretório do aplicativo e inicie a configuração com:

```sh
python3 installdevtools.py
usage: installdevtools.py [-h] [-i INSTALL [INSTALL ...]] [-p] [-u]

Configurador de Ambiente de Desenvolvimento para Ubuntu - Otimizado para Ubuntu 23.10

Opções Disponíveis:

-h, --help
Mostra esta mensagem de ajuda e sai.

-i --install [vscode,fnm,sublime3,chrome,spotify,all]
    Instala ferramentas específicas. Utilize -i seguido de uma ou mais ferramentas, separadas por vírgulas sem espaços. Exemplo: -i vscode,fnm para instalar o Visual Studio Code e o Fast Node Manager.

    Ferramentas disponíveis:
        vscode: Instala o Visual Studio Code, um editor de código fonte com suporte extensivo para desenvolvimento.
        fnm: Instala o Fast Node Manager, um gerenciador de versões Node.js.
        sublime3: Instala o Sublime Text 3, um editor de texto leve e poderoso.
        chrome: Instala o Google Chrome, um navegador web rápido e seguro.
        spotify: Instala o Spotify, um serviço de streaming de música.
        all: Instala todas as ferramentas acima.

-p, --purge
Executa a remoção completa do LibreOffice, liberando espaço no sistema.

-u, --upgrade
Atualiza o sistema e suas aplicações para as últimas versões disponíveis.

Exemplo de Uso:

Para instalar o Visual Studio Code e o Fast Node Manager, o comando seria:
python3 installdevtools.py -i vscode,fnm

Para atualizar o sistema, você utilizaria:
python3 installdevtools.py -u
```

##Descrição Detalhada das Opções de Instalação:

-i vscode - Instala o Visual Studio Code, um editor de código fonte desenvolvido pela Microsoft. Ele é amplamente reconhecido pela sua performance e suporte a uma vasta gama de linguagens de programação, além de possuir uma extensa biblioteca de extensões que ampliam suas funcionalidades.

-i fnm - Instala o Fast Node Manager (fnm), um gerenciador de versões para Node.js extremamente rápido e eficiente. Facilita a gestão de múltiplas versões do Node.js em uma única máquina, permitindo a fácil troca entre elas conforme necessário.

-i sublime3 - Realiza a instalação do Sublime Text 3, uma versão avançada deste popular editor de texto leve, mas poderoso. Conhecido por sua velocidade e interface de usuário minimalista, o Sublime Text oferece suporte a muitas linguagens de programação e ferramentas de marcação, com uma ampla variedade de plugins disponíveis.

-i chrome - Instala a versão mais recente do Google Chrome, um navegador web de alta velocidade, seguro e de uso gratuito, desenvolvido pelo Google. O Chrome é conhecido por sua interface de usuário simples, desempenho robusto e suporte extensivo a padrões web modernos.

-i spotify - Instala o Spotify, um serviço de streaming de música que oferece acesso a milhões de músicas, podcasts e vídeos de artistas de todo o mundo. O Spotify é uma ferramenta essencial para amantes da música, permitindo descobrir, ouvir e organizar suas músicas favoritas com facilidade.

-i all - Instala todas as ferramentas acima mencionadas, proporcionando um ambiente de desenvolvimento abrangente e atualizado, além de acesso a entretenimento de qualidade através do Spotify. Ideal para usuários que desejam configurar rapidamente um novo dispositivo com todas as suas ferramentas favoritas.

Algumas destas ferramentas requerem o uso do curl ou do wget para serem instaladas. Durante o processo de instalação, é verificado se o curl ou o wget já estão presentes no sistema. Caso não estejam, o instalador procederá com a instalação desses componentes.

## Pré-requisitos

- Ubuntu 22.04 LTS ou superior.
- Python 3.x.

## Contribuições

Contribuições são bem-vindas e incentivadas. Se você tem ideias de melhorias, funcionalidades adicionais ou correções de bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT, promovendo uma ampla liberdade de uso, modificação e distribuição.
````
