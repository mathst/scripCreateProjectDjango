import os
import subprocess

def create_django_project_in_core(project_name):
    # Criar o projeto Django na raiz
    print("Criando projeto Django na raiz...")
    subprocess.run(f"django-admin startproject {project_name}", shell=True)
    
    # Entrar no diretório 'projeto'
    proj_dir = os.path.join(project_name)
    os.chdir(proj_dir)
    
    # Criar o aplicativo 'core' dentro da pasta do projeto
    print("Criando aplicativo 'core' dentro do diretório 'core'...")
    core_dir = os.path.join(proj_dir, 'core')
    os.makedirs(core_dir, exist_ok=True)
    
    subprocess.run(f"django-admin startapp core {core_dir}", shell=True)

    # Criar diretórios para arquivos estáticos
    static_dir = os.path.join(core_dir, 'static')
    os.makedirs(os.path.join(static_dir, 'css'), exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'js'), exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'img'), exist_ok=True)

    # Atualizar as configurações para arquivos estáticos
    settings_file = os.path.join(f"{project_name}/settings.py")
    with open(settings_file, "r") as f:
        lines = f.readlines()

    # Encontrar a linha que contém 'STATIC_URL'
    for i, line in enumerate(lines):
        if "STATIC_URL" in line:
            lines.insert(i + 1, f"STATICFILES_DIRS = [\n")
            lines.insert(i + 2, f"    os.path.join(BASE_DIR, 'static'),\n")
            lines.insert(i + 3, f"    os.path.join(BASE_DIR, 'core/static'),\n")
            lines.insert(i + 4, f"]\n")
            break

    # Escrever as alterações de volta ao arquivo settings.py
    with open(settings_file, "w") as f:
        f.writelines(lines)

    print("Aplicativo 'core' criado dentro do diretório 'core'.")

def create_django_project_in_root(project_name):
    # Criar o projeto Django na raiz
    print("Criando projeto Django na raiz...")
    subprocess.run(f"django-admin startproject {project_name}", shell=True)

    # Entrar no diretório do projeto
    os.chdir(project_name)
    
    # Criar o aplicativo 'core' dentro do diretório 'core'
    print("Criando aplicativo 'core' dentro do diretório 'core'...")
    core_dir = os.path.join(project_name, 'core')
    os.makedirs(core_dir, exist_ok=True)
    
    subprocess.run(f"django-admin startapp core {core_dir}", shell=True)
    
    # Criar diretórios para arquivos estáticos
    static_dir = os.path.join(project_name, 'static')
    os.makedirs(os.path.join(static_dir, 'css'), exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'js'), exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'img'), exist_ok=True)

    # Atualizar as configurações para arquivos estáticos
    settings_file = os.path.join(project_name, f"{project_name}/settings.py")
    with open(settings_file, "r") as f:
        lines = f.readlines()

    # Encontrar a linha que contém 'STATIC_URL'
    for i, line in enumerate(lines):
        if "STATIC_URL" in line:
            lines.insert(i + 1, f"STATICFILES_DIRS = [\n")
            lines.insert(i + 2, f"    os.path.join(BASE_DIR, 'static'),\n")
            lines.insert(i + 3, f"]\n")
            break

    # Escrever as alterações de volta ao arquivo settings.py
    with open(settings_file, "w") as f:
        f.writelines(lines)

    print("Projeto Django criado na raiz.")

if __name__ == "__main__":
    project_name = input("Digite o nome do projeto Django: ")
    level = input("Digite o nível de diretório para criar o projeto (1.raiz/2.core): ")

    # Verificar se o nível é válido
    if level.lower() not in ["1", "2"]:
        print("Opção inválida. Escolha '1.raiz' ou '2.core'.")
    else:
        if level.lower() == "2":
            create_django_project_in_core(project_name)
        else:
            create_django_project_in_root(project_name)
