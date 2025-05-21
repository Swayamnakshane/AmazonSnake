Thanks! Here's the **updated blog post** with your **preferred Amazon Q CLI installation commands using `.deb` package** for Linux systems.

---

# 🐍 Building a Classic Snake Game with Amazon Q CLI & Pygame

## 🎮 Introduction

Remember the thrill of guiding a pixelated snake to gobble up food while avoiding collisions? Let's recreate that nostalgia by building the classic Snake game using **Amazon Q CLI** and **Pygame**.

Amazon Q CLI is an AI-powered command-line tool that assists in generating code through conversational prompts. By leveraging it alongside Pygame, we can streamline the game development process on a **Linux** environment.

---

## ⚙️ Setup: Development Environment

### 🛠 Tools Required

* **Amazon Q CLI**: AI-driven code generation tool
* **Pygame**: Library for game development in Python
* **Python 3.8+**: Programming language
* **Linux**: Ubuntu/Debian-based system recommended

### 📦 Installation Steps (Linux)

#### 1. Update and install dependencies:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
```

#### 2. Install Pygame:

```bash
pip3 install pygame
```

---

## 🧰 Installing Amazon Q CLI on Linux

You can install **Amazon Q CLI** using the official `.deb` package provided by AWS.

#### 1. Download the `.deb` installer:

```bash
wget https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb
```

#### 2. Install the package with `dpkg`:

```bash
sudo dpkg -i amazon-q.deb
```

#### 3. Fix any missing dependencies:

```bash
sudo apt-get install -f
```

#### 4. Verify the installation:

```bash
q --version
```

You should now see the installed version of Amazon Q CLI.

#### 5. Start an interactive session:

```bash
q chat
```
![Screenshot 2025-05-22 022325](https://github.com/user-attachments/assets/f460a014-e215-4e8e-b04c-c7cad93753fc)

---

## 🧠 Prompt-Driven Development: Building the Game

With Amazon Q CLI ready, we can start crafting our Snake game by providing specific prompts.

### 1. 🐍 Game Skeleton & Movement

**Prompt**:

> Create a basic Snake game using Pygame where the snake moves with arrow keys, grows when it eats food, and the game ends upon collision with walls or itself.

**Outcome**:

* Initialized game window
* Snake movement via arrow keys
* Randomly placed food
* Snake grows upon eating food
* Game ends on collision

### 2. 🖥️ Title Screen

**Prompt**:

> Add a title screen displaying "Classic Snake Game" with a start button centered on the screen.

**Outcome**:

* Title screen with game name
* Start button to begin the game

### 3. 🧮 Score Display
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot 2025-05-22 035105](https://github.com/user-attachments/assets/9c655489-4975-448a-91d5-b953de325340)


**Prompt**:

> Display the player's current score at the top-left corner of the game screen using a readable font.

**Outcome**:

* Real-time score tracking
* Score updates as the snake eats

### 4. 🎨 Game Over Screen
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot 2025-05-22 033701](https://github.com/user-attachments/assets/a79e68cb-cc17-4acb-898e-86f8c3ef52cc)

**Prompt**:

> Upon game over, display a screen showing "Game Over" and the player's final score, with an option to restart or quit.

**Outcome**:

* Game over screen with final score
* Option to restart or exit

---

## 📝 Final Features Recap

* ✅ Snake movement with arrow keys
* ✅ Randomly appearing food
* ✅ Snake grows when eating food
* ✅ Collision detection with walls and self
* ✅ Score display
* ✅ Title and game over screens

---

## 🚀 Conclusion

By using **Amazon Q CLI** and **Pygame** on a Linux system, we've efficiently built a classic Snake game with just a few smart prompts. This AI-assisted workflow boosts productivity and makes game development accessible even to beginners.

Feel free to extend the game with features like:

* Increasing speed over time
* Multiple levels or themes
* Sound effects and music
* Leaderboards with persistent scores

Happy coding! 🐍

---


https://github.com/user-attachments/assets/633ea655-ea38-449c-a0c4-793a9f76c718


