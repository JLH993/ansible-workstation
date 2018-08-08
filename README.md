# MacOS

1. Install pip:
   ```
   sudo easy_install pip
   ```
2. Install ansible:
   ```
   sudo pip install ansible
   ```
3. Modify /etc/sudoers to allow unrestricted sudo access to your user.
   ```
   sudo visudo
   ```
4. Run the playbook.
   ```
   ansible-playbook Playbooks/workstation.yml
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
