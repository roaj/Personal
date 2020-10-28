#!/bin/bash

# Add .hidden to Home.
cp ./.hidden ~

# Remember git credentials
git config --global credential.helper store

# Write Gnome Settings
dconf load / < saved_settings.dconf

# Hide Mounted Drives in Dock.
gsettings set org.gnome.shell.extensions.dash-to-dock show-mounts false

# Hide Recent from Nautilus Sidebar.
gsettings set org.gnome.desktop.privacy remember-recent-files false

# Pin Favorites in Dock
gsettings set org.gnome.shell favorite-apps "['chromium-browser.desktop', 'org.gnome.Nautilus.desktop', 'org.gnome.Terminal.desktop']"

# Add Git Settings
git config --global user.email "daniyal.s.ansari+github@gmail.com"
git config --global user.name "Daniyal Ansari"

# Install oh-my-zsh
#sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

# Add .zshrc to Home.
#cp ./.zshrc ~


# Install Metasploit

cd /tmp
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod +x msfinstall
sudo ./msfinstall

# Install SET

cd /tmp
git clone https://github.com/trustedsec/social-engineer-toolkit/ set/
cd set
sudo pip3 install -r requirements.txt
sudo python3 setup.py install
