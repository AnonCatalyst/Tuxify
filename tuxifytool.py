import os
import subprocess
import sys

# Colors
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
CYAN = '\033[0;36m'
MAGENTA = '\033[0;35m'
BLUE = '\033[0;34m'
WHITE = '\033[1;37m'
ORANGE = '\033[0;33m'
PURPLE = '\033[0;35m'
GRAY = '\033[0;37m'
NC = '\033[0m'  # No Color

TOOL_NAME = "TuxifyTool"

def execute_command(command, message_color):
    print(f'{message_color}{command}{NC}')
    subprocess.run(command, shell=True)

def update_upgrade():
    execute_command('pkg update -y && pkg upgrade -y', YELLOW)

def install_packages():
    execute_command('pkg install -y python python-dev clang git wget curl vim nano', BLUE)

def install_pip():
    execute_command('curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm get-pip.py', CYAN)

def install_python_packages():
    execute_command('pip install setuptools', MAGENTA)

def install_termux_api():
    execute_command('pkg install -y termux-api', WHITE)

def install_oh_my_zsh():
    execute_command('pkg install -y zsh && sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"', BLUE)

def install_additional_tools():
    execute_command('pkg install -y nmap hydra openssh && pip install requests', MAGENTA)

def install_proot():
    execute_command('pkg install -y proot', GREEN)

def set_up_proot_alias():
    with open(os.path.expanduser('~/.zshrc'), 'a') as zshrc_file:
        zshrc_file.write('alias pr="proot -0 -w $PWD -r $PREFIX"\n')
    print(f'{WHITE}Setting up proot alias...{NC}')

def additional_cleanup():
    execute_command('pkg autoclean && pkg clean', GREEN)

def main():
    try:
        # Update and upgrade packages
        update_upgrade()

        # Install essential packages
        install_packages()

        # Install pip
        install_pip()

        # Install necessary Python packages
        install_python_packages()

        # Install termux-api
        install_termux_api()

        # Install oh-my-zsh
        install_oh_my_zsh()

        # Install additional tools
        install_additional_tools()

        # Install proot for fake root environment
        install_proot()

        # Set up proot alias for convenience
        set_up_proot_alias()

        # Additional cleanup
        additional_cleanup()

        print(f'{ORANGE}{TOOL_NAME} setup completed.{NC} You may need to restart Termux for changes to take effect.')

    except Exception as e:
        print(f'{RED}Error: {e}{NC}')
        sys.exit(1)

if __name__ == '__main__':
    main()
