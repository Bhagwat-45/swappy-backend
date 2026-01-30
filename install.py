import os
import subprocess
import sys


def run_command(command: str) -> None:
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as error:
        print(f"Command failed: {error}")
        sys.exit(1)


def main() -> None:
    print("Starting backend setup...")


    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        run_command(f"{sys.executable} -m venv venv")
    else:
        print("Virtual environment already exists.")

    
    if os.name == "nt":  
        venv_python = os.path.join("venv", "Scripts", "python.exe")
        activate_cmd = ".\\venv\\Scripts\\activate"
    else:  
        venv_python = os.path.join("venv", "bin", "python")
        activate_cmd = "source venv/bin/activate"

    print("Upgrading pip...")
    run_command(f"{venv_python} -m pip install --upgrade pip")

    if os.path.exists("requirements.txt"):
        print("Installing dependencies from requirements.txt...")
        run_command(f"{venv_python} -m pip install -r requirements.txt")
    else:
        print("requirements.txt not found.")
        sys.exit(1)

    print("\n" + "=" * 40)
    print("Setup completed successfully.")
    print("=" * 40)
    print("Activate the virtual environment:")
    print(f"  {activate_cmd}")
    print("Run the application:")
    print("  uvicorn app.main:app --reload")
    print("=" * 40)


if __name__ == "__main__":
    main()
