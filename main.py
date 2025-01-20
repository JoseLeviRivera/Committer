import argparse
import os
import subprocess
import sys
from InquirerPy import inquirer


def print_banner():
    """Prints an ASCII banner and a brief description of the tool."""
    banner = r"""
   ______                                     _    _                       __          ______                                 _  _    
 .' ___  |                                   / |_ (_)                     [  |       .' ___  |                               (_)/ |_  
/ .'   \_| .--.  _ .--. _   __ .---.  _ .--.`| |-'__   .--.  _ .--.  ,--.  | |______/ .'   \_| .--.  _ .--..--.  _ .--..--.  __`| |-' 
| |      / .'`\ [ `.-. [ \ [  ] /__\\[ `.-. || | [  |/ .'`\ [ `.-. |`'_\ : | |______| |      / .'`\ [ `.-. .-. |[ `.-. .-. |[  || |   
\ `.___.'\ \__. || | | |\ \/ /| \__., | | | || |, | || \__. || | | |// | |,| |      \ `.___.'\ \__. || | | | | | | | | | | | | || |,  
 `.____ .''.__.'[___||__]\__/  '.__.'[___||__]__/[___]'.__.'[___||__]'-;__[___]      `.____ .''.__.'[___||__||__|___||__||__|___]__/  
"""
    description = "Welcome to Conventional Commit: A CLI tool for generating Conventional Commits with emojis.\n"
    print(banner)
    print(description)

def execute_git_commit(commit_message):
    """Executes the git add and git commit commands with the provided message."""
    try:
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("✅ Commit successfully created.")
    except subprocess.CalledProcessError:
        print("❌ Error executing the commit. Make sure there are staged changes.")
        sys.exit(1)

def create_commit_message(commit_type, emoji, description, body=None, footer=None):
    """Creates the commit message following Conventional Commits."""
    message = f"{emoji} {commit_type}: {description}"
    if body:
        message += f"\n\n{body}"
    if footer:
        message += f"\n\n{footer}"
    return message

def prompt_user_for_commit():
    """Interacts with the user to collect commit data."""
    print("\n=== Conventional Commit Generator ===")

    # Menu for commit type selection
    commit_types = {
        "feat": "✨ feat: A new feature",
        "fix": "🐛 fix: Bug fix",
        "docs": "📝 docs: Documentation changes",
        "style": "🎨 style: Code style changes (non-functional)",
        "refactor": "♻️ refactor: Code refactoring",
        "test": "✅ test: Adding or updating tests",
        "chore": "🔧 chore: Maintenance tasks",
    }

    commit_type = inquirer.select(
        message="Select the type of commit:",
        choices=[f"{emoji}" for emoji in commit_types.values()],
    ).execute()

    # Extract the actual type and emoji
    commit_type_key = commit_type.split(" ")[1][:-1]  # Removes colon from type
    emoji = commit_type.split(" ")[0]

    # Ask for the description
    description = input("Brief description of the change: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input("Brief description of the change: ").strip()

    # Ask for the commit body (optional)
    body = input("Do you want to add a body to the commit? (Press Enter to skip): ").strip()

    # Ask for the footer (optional)
    footer = input("Do you want to add a footer to the commit? (Press Enter to skip): ").strip()

    return commit_type_key, emoji, description, body, footer

def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Conventional-Commit: A CLI tool for generating Conventional Commits with emojis."
    )
    parser.add_argument(
        "path",
        help="Path to the directory where the commit will be made. Use '.' for the current directory."
    )

    args = parser.parse_args()

    # Change to the specified directory if not current
    if args.path != ".":
        try:
            os.chdir(args.path)
        except FileNotFoundError:
            print(f"❌ The directory '{args.path}' does not exist.")
            sys.exit(1)
        except PermissionError:
            print(f"❌ You don't have permission to access the directory '{args.path}'.")
            sys.exit(1)

    # Verify it's a Git repository
    if not os.path.exists(".git"):
        print("❌ The specified directory is not a Git repository.")
        sys.exit(1)

    # Gather commit data from the user
    commit_type, emoji, description, body, footer = prompt_user_for_commit()

    # Create the commit message
    commit_message = create_commit_message(commit_type, emoji, description, body, footer)

    print("\n📋 Generated commit message:")
    print(commit_message)

    # Confirm and make the commit
    confirm = input("\nDo you want to proceed with this commit? (y/n): ").lower()
    if confirm == "y":
        execute_git_commit(commit_message)
    else:
        print("❌ Commit canceled.")

# Install pyinstaller
# pip install pyinstaller 
# pyinstaller --onefile --name gcz main.py
if __name__ == "__main__":
    main()
