# 🖱️ Mouse Mover — Anti-Idle Simulator

A lightweight Python script that simulates user activity on Windows to prevent the system from going idle or triggering screen lock/sleep. It does this by periodically pressing the Windows Start key and moving the mouse in a defined pattern.

---

## ✨ Features

- **Randomized intervals** — waits between 100 and 200 seconds between activity bursts to avoid predictable patterns
- **Windows key simulation** — presses the Start button a random number of times (5–15) to register keyboard input
- **Mouse movement pattern** — moves the cursor in a square path (right → down → left → up) to simulate presence
- **Zero configuration** — runs out of the box with a single command
- **Continuous loop** — keeps running until manually stopped with `Ctrl+C`

---

## 📋 Requirements

- Python 3.7+
- [pyautogui](https://pyautogui.readthedocs.io/)

Install dependencies:

```bash
pip install pyautogui
```

---

## 🚀 Usage

```bash
python mouse_mover.py
```

To stop the script, press `Ctrl+C` in the terminal.

---

## ⚙️ How It Works

1. Presses the Windows Start key a random number of times (5–15), with a 1-second pause between each press
2. Waits a random interval between **100 and 200 seconds**
3. Repeats indefinitely

> **Note:** The `move_mouse()` function is defined but not called in the main loop. You can enable it by adding `move_mouse()` inside `main()` if you also want mouse movement in addition to key presses.

---

## ⚠️ Disclaimer

This tool is intended for personal use only (e.g., keeping a workstation active during long downloads or automated tasks). Use responsibly and in compliance with your organization's IT policies.

---

## 📄 License

MIT
