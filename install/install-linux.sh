#!/bin/bash

# Define download URL and install path
DOWNLOAD_URL="https://github.com/JoseLeviRivera/Committer/releases/latest/download/gcz-linux"
INSTALL_PATH="/usr/local/bin/gcz"

# Download the file
echo "📥 Downloading gcz..."
curl -L $DOWNLOAD_URL -o $INSTALL_PATH

# Make it executable
chmod +x $INSTALL_PATH

# Verify installation
if command -v gcz &> /dev/null
then
    echo "gcz installed successfully! You can now use 'gcz' from any terminal."
else
    echo "Installation failed. Try running with sudo."
fi
