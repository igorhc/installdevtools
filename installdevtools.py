#!/usr/bin/env python3

import argparse
import subprocess

import sys
import os

def run_command(command, shell=False):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=shell)
        print(f"Comando executado com sucesso: {' '.join(command) if isinstance(command, list) else command}\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {' '.join(command) if isinstance(command, list) else command}\nErro: {e.stderr}")
        return False

def check_dependency_installed(dependency):
    """Verifica se uma dependência está instalada."""
    try:
        subprocess.run([dependency, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_dependency(dependency):
    """Instala uma dependência."""
    print(f"Instalando {dependency}...")
    return run_command(["sudo", "apt-get", "install", dependency, "-y"])


def update_system():
    print("Atualizando sistema...")
    if not run_command(["sudo", "apt-get", "update"]):
        print("Falha ao atualizar a lista de pacotes.")
        return False
    if not run_command(["sudo", "apt-get", "upgrade", "-y"]):
        print("Falha ao atualizar os pacotes.")
        return False
    return True

def purge_libreoffice():
    print("Removendo LibreOffice...")
    if not run_command(["sudo", "apt-get", "purge", "-y", "libreoffice*"]):
        print("Falha ao remover o LibreOffice. Verifique as permissões.")
        return False
    if not run_command(["sudo", "apt-get", "autoremove", "-y"]):
        print("Falha ao executar autoremove após a remoção do LibreOffice.")
        return False
    return True

def check_dependency_installed(dependency):
    """Verifica se uma dependência está instalada usando `which`."""
    try:
        result = subprocess.run(["which", dependency], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            print(f"{dependency} já está instalado.")
            return True
        else:
            print(f"{dependency} não está instalado.")
            return False
    except subprocess.CalledProcessError:
        # O comando falhou, o que significa que a dependência não foi encontrada
        print(f"{dependency} não está instalado.")
        return False

def install_dependency(dependency):
    """Instala uma dependência."""
    print(f"Instalando {dependency}...")
    return run_command(["sudo", "apt-get", "install", dependency, "-y"])

def install_tool(tool_name):
    tool_install_commands = {
        "chrome": "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb -y",
        "vscode": "wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add - && sudo add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\" && sudo apt-get update && sudo apt-get install code -y",
        "sublime3": "wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add - && echo \"deb https://download.sublimetext.com/ apt/stable/\" | sudo tee /etc/apt/sources.list.d/sublime-text.list && sudo apt-get update && sudo apt-get install sublime-text -y",
        "fnm": "curl -fsSL https://fnm.vercel.app/install | bash",
        "spotify": "curl -sS https://download.spotify.com/debian/pubkey_6224F9941A8AA6D1.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg | echo  \"deb http://repository.spotify.com stable non-free\" | sudo tee /etc/apt/sources.list.d/spotify.list && sudo apt-get update && sudo apt-get install spotify-client -y"
    }
    if tool_name in tool_install_commands:
        print(f"Instalando {tool_name}...")
        if not run_command(tool_install_commands[tool_name], shell=True):
            print(f"Falha ao instalar {tool_name}.")
            return False

        if tool_name == "fnm":
            if not detect_shell_and_configure_fnm():
                print("Falha ao configurar fnm.")
                return False

        print(f"{tool_name} instalado com sucesso.")
        return True
    else:
        print(f"Ferramenta {tool_name} desconhecida.")
        return False

def detect_shell_and_configure_fnm():
    shell = os.getenv('SHELL')
    if 'bash' in shell:
        config_file = os.path.expanduser("~/.bashrc")
    elif 'zsh' in shell:
        config_file = os.path.expanduser("~/.zshrc")
    else:
        print("Shell não suportado para configuração automática do fnm.")
        return False

    fnm_config = "\nexport PATH=\"$HOME/.fnm:$PATH\"\neval \"$(fnm env)\"\n"
    with open(config_file, "a") as file:
        file.write(fnm_config)
    print(f"Configuração do fnm adicionada ao {config_file}.")

    return True    


def check_tool_dependecy(tool):
    dependencies = {
        "chrome": "wget",
        "vscode": "wget",
        "sublime3": "wget",
        "fnm": "curl",
        "spotify": "curl",  # Adicionando `curl` como dependência para o Spotify
    }

    # Verifica e instala dependências se necessário
    if tool in dependencies:
        dependency = dependencies[tool]
        if dependency:
            dependency_installed = check_dependency_installed(dependency)
            if not dependency_installed:
                print(f"{dependency} não está instalado. Tentando instalar...")
                install_tool(tool)
                success = install_dependency(dependency)
                if not success:
                    print(f"Não foi possível instalar {dependency}. Por favor, instale manualmente e tente novamente.")
                    return False  # Retorna falso mas não sai do programa, permite que o script continue
            else:
                print(f"{dependency} já está instalado.")
                install_tool(tool)

def main():
    parser = argparse.ArgumentParser(description="Prepara o ambiente de desenvolvimento. Ferramenta para Ubuntu, testado no Ubuntu 23.10")
    parser.add_argument("-i", "--install", type=str, help="Instala as ferramentas especificadas (fnm, chrome, sublime3, vscode, spotify, all para todos). Para instalar mais de um tool separe por vírgula sem espaço.", nargs='+')
    parser.add_argument("-p", "--purge", action="store_true", help="Executa o purge_tool para LibreOffice.")
    parser.add_argument("-u", "--upgrade", action="store_true", help="Executa o update_system.")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)  # Exibe a mensagem de ajuda
        sys.exit(1)  # Sai do script com um código de erro

    if args.install:
        for tool in args.install:
            if tool == "all":
            # Especifica a ordem de instalação das ferramentas
                for tool in ["fnm", "chrome", "sublime3", "vscode", "spotify"]:
                    check_tool_dependecy(tool)
            else:
                check_tool_dependecy(tool)

    if args.purge and not purge_libreoffice():
        return

    if args.upgrade and not update_system():
        return


if __name__ == "__main__":
    main()
