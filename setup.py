#!/usr/bin/env python3
"""
Setup script for AI Resume Matcher
Automated installation and configuration
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} detected")
    return True

def create_virtual_environment():
    """Create and activate virtual environment."""
    if os.path.exists('venv'):
        print("✅ Virtual environment already exists")
        return True
    
    if run_command("python -m venv venv", "Creating virtual environment"):
        print("✅ Virtual environment created")
        return True
    return False

def install_dependencies():
    """Install required packages."""
    system = platform.system()
    
    if system == "Windows":
        pip_command = "venv\\Scripts\\pip install -r requirements.txt"
    else:
        pip_command = "source venv/bin/activate && pip install -r requirements.txt"
    
    return run_command(pip_command, "Installing dependencies")

def create_directories():
    """Create necessary directories."""
    directories = ['uploads', 'demo']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created {directory} directory")
        else:
            print(f"✅ {directory} directory already exists")

def create_env_file():
    """Create .env file if it doesn't exist."""
    if not os.path.exists('.env'):
        env_content = """# AI Resume Matcher Configuration
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=change-this-secret-key-in-production
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216
"""
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Created .env file")
    else:
        print("✅ .env file already exists")

def main():
    """Main setup function."""
    print("🤖 AI Resume Matcher Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Create .env file
    create_env_file()
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate virtual environment:")
    
    system = platform.system()
    if system == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("2. Run the application:")
    print("   python main.py")
    print("3. Open http://localhost:5000 in your browser")
    print("\n📖 Read README.md for more information")

if __name__ == "__main__":
    main()