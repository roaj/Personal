#!/bin/bash

# Promt for root password
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

# Check for internet connection.
printf "\nChecking for internet connection.\n"
wget -q --spider http://google.com
if [ $? -eq 0 ]; then
    echo -e "\n\e[1m\e[32mConnected.\e[0m\n"
else
    echo -e "\n\e[1m\e[31mERROR: No Internet Connection!\e[0m"
    exit
fi

apt update >/dev/null 2>&1
apt upgrade -y >/dev/null 2>&1
apt dist-upgrade -y >/dev/null 2>&1
apt --fix-broken install -y >/dev/null 2>&1
apt autoremove -y >/dev/null 2>&1

echo -e "\nAdding APT Repositories.\n"

apt_repositories=$(cat ./packages/apt_repositories.txt | tr "\n" " ")
IFS=' ' read -r -a apt_repositories <<< "$apt_repositories"
arr_len=${#apt_repositories[@]}
for (( i=1; i<${arr_len}+1; i++ ));
do
    echo -n "APT:[$i/${#apt_repositories[@]}] Adding ${apt_repositories[$i-1]} repository."
    log=$(add-apt-repository -y ppa:"${apt_repositories[$i-1]}" >/dev/null 2>&1)
    if [ $? != 0 ]; then
        echo $log
    fi
    echo -e "\r\e[1m\e[32mAPT:[$i/${#apt_repositories[@]}] Added ${apt_repositories[$i-1]} repository. ✓\e[0m"
done

echo -e "\nInstalling APT Packages.\n"

apt_packages=$(cat ./packages/apt_packages.txt | tr "\n" " ")
IFS=' ' read -r -a apt_packages <<< "$apt_packages"
arr_len=${#apt_packages[@]}
for (( i=1; i<${arr_len}+1; i++ ));
do
    echo -n "APT:[$i/${#apt_packages[@]}] Installing ${apt_packages[$i-1]}."
    log=$(apt install -qq -y "${apt_packages[$i-1]}" >/dev/null 2>&1)
    if [ $? != 0 ]; then
        echo $log
    fi
    echo -e "\r\e[1m\e[32mAPT:[$i/${#apt_packages[@]}] Installed ${apt_packages[$i-1]}. ✓\e[0m"
done

echo -e "\nInstalling Snap Packages.\n"

# Damn you snap packages.
snap_packages=$(cat ./packages/snap_packages.txt | tr "\n" " ")
IFS=' ' read -r -a snap_packages <<< "$snap_packages"
arr_len=${#snap_packages[@]}
for (( i=1; i<${arr_len}+1; i++ ));
do
    echo -n "Snap:[$i/${#snap_packages[@]}] Installing ${snap_packages[$i-1]}."
    log=$(snap install --classic "${snap_packages[$i-1]}" >/dev/null 2>&1)
    if [ $? != 0 ]; then
        echo $log
    fi
    echo -e "\r\e[1m\e[32mSnap:[$i/${#snap_packages[@]}] Installed ${snap_packages[$i-1]}. ✓\e[0m"
done

# I definitely don't need pip2 anymore 
# pip2_packages=$(cat ./packages/pip2_packages.txt | tr "\n" " ")
# IFS=' ' read -r -a pip2_packages <<< "$pip2_packages"

# for package in "${pip2_packages[@]}"
# do
#     pip2 install "$package"
# done

echo -e "\nInstalling Pip3 Packages.\n"

pip3_packages=$(cat ./packages/pip3_packages.txt | tr "\n" " ")
IFS=' ' read -r -a pip3_packages <<< "$pip3_packages"
arr_len=${#pip3_packages[@]}
for (( i=1; i<${arr_len}+1; i++ ));
do
    echo -n "Snap:[$i/${#pip3_packages[@]}] Installing ${pip3_packages[$i-1]}."
    log=$(pip3 install "${pip3_packages[$i-1]}" >/dev/null 2>&1)
    if [ $? != 0 ]; then
        echo $log
    fi
    echo -e "\r\e[1m\e[32mSnap:[$i/${#pip3_packages[@]}] Installed ${pip3_packages[$i-1]}. ✓\e[0m"
done

# Sorry Atom. VS Code is better.
# atom_packages=$(cat ./packages/atom_packages.txt | tr "\n" " ")
# IFS=' ' read -r -a atom_packages <<< "$atom_packages"

# for package in "${atom_packages[@]}"
# do
#     apm install "$package"
# done

apt update >/dev/null 2>&1
apt upgrade -y >/dev/null 2>&1
apt dist-upgrade -y >/dev/null 2>&1
apt --fix-broken install -y >/dev/null 2>&1
apt autoremove -y >/dev/null 2>&1
apt autoclean -y >/dev/null 2>&1

# final_file=./final.sh
# if test -f "$final_file"; then
#     bash ./final.sh
# fi

