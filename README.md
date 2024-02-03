# Configurador Completo de Ambiente de Desenvolvimento para Ubuntu

Este aplicativo Python3 é a solução definitiva para configurar um ambiente de desenvolvimento robusto em sistemas Ubuntu. Projetado para simplificar e automatizar não apenas a instalação do Node.js através do fnm, mas também a configuração de ferramentas essenciais como Visual Studio Code, Sublime Text 3, Google Chrome, e até o Spotify para seus momentos de relaxamento. Com apenas um comando, este aplicativo transforma seu sistema Ubuntu em um ambiente de desenvolvimento completo e pronto para uso, otimizando seu tempo e reduzindo a margem para erros manuais.

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
./installdevtools.py
usage: installdevtools.py [-h] [-i INSTALL [INSTALL ...]] [-p] [-u]

Prepara o ambiente de desenvolvimento. Ferramenta para Ubuntu, testado no Ubuntu 23.10

options:
  -h, --help            show this help message and exit
  -i INSTALL [INSTALL ...], --install INSTALL [INSTALL ...]
                        Instala as ferramentas especificadas (fnm, chrome, sublime3, vscode, spotify, all para todos). Para instalar mais de um tool
                        separe por vírgula sem espaço.
  -p, --purge           Executa o purge_tool para LibreOffice.
  -u, --upgrade         Executa o update_system.
```

4. Siga o assistente de instalação para selecionar e instalar os componentes desejados.

## Pré-requisitos

- Ubuntu 16.04 LTS ou superior.
- Python 3.6 ou mais recente.

## Contribuições

Contribuições são bem-vindas e incentivadas. Se você tem ideias de melhorias, funcionalidades adicionais ou correções de bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT, promovendo uma ampla liberdade de uso, modificação e distribuição.
