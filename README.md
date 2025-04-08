# Penguin Revival - Wand

Place these assets inside `legacy-media/` and `vanilla-media/` folders to run the project:

🔗 **[Download WAND media files from MediaFire](https://www.mediafire.com/folder/zdvtl4a3olran/wand-files)**

Penguin Revival - Wand makes it easy to configure Dash, Houdini, and a media server using Docker & Docker Compose.

> **Note**  
> This also works on Windows using WSL.

---

## 🔧 Installation Script

**Step 1 – Run the install script:**

```bash
bash <(curl -s https://raw.githubusercontent.com/solero/wand/master/install.sh)
```

**Step 2 – Answer the following prompts:**

- Database password (Leave blank for a random password)
- Hostname (example: `clubpenguin.com`) (Leave blank for localhost)
- External IP Address (Leave blank for localhost)

**Step 3 – Run and enjoy:**

```bash
cd wand && sudo docker-compose up
```

---

## ⚙️ Manual Setup

> **Important**  
> Not recommended for beginners. Use the install script if you're unsure.

### Step 1 – Choose your Linux Distribution

<details>
  <summary>Debian / Ubuntu</summary>

```bash
sudo apt update
sudo apt install git curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
</details>

<details>
  <summary>Fedora / RHEL</summary>

```bash
sudo dnf update
sudo dnf install git curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
</details>

<details>
  <summary>Arch-based distros</summary>

```bash
sudo pacman -Syu
sudo pacman -S docker docker-compose git curl
systemctl start docker.service
systemctl enable docker.service
```
</details>

---

### Step 2 – Clone the repository & submodules

```bash
git clone --recurse-submodules https://github.com/solero/wand
cd wand
```

### Step 3 – Edit configuration (optional for local setup)

```bash
nano .env
```

### Step 4 – Start the services

```bash
sudo docker-compose up
```

---

## ✅ You're done!

Make sure you have the media files in place (`legacy-media/` and `vanilla-media/`) before starting.
