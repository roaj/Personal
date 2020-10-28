#!/bin/bash

# Save .hidden.
cp ~/.hidden .

# Save .zshrc.
cp ~/.zshrc .

# Save Gnome Tweaks Settings
dconf dump / > saved_settings.dconf

