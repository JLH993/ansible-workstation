# MacOS

1. Install pip:
   ```
   sudo easy_install pip
   ```
2. Install ansible:
   ```
   sudo pip install ansible
   ```
3. Run the playbook.
   ```
   ansible-playbook playbooks/workstation.yml --ask-become-pass
   ```

# Windows

## WSL Setup

1. Configure the Linux subsytem for windows:
   ```
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart
   ```
2. Restart Computer
   ```
   Restart-Computer
   ```
3. Install a distro of your choice:
   https://docs.microsoft.com/en-us/windows/wsl/install-win10#install-your-linux-distribution-of-choice

## Ansible Setup

1. Install ansible via pip:
   ```
   pip install ansible
   ```

# Linux

1. Install ansible via pip:
   ```
   pip install ansible
   ```

2. Run the playbook.
   ```
   ansible-playbook playbooks/workstation.yml --ask-become-pass
   ```
