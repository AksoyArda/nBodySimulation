# 🌌 N-Body Simulation on Raspberry Pi Pico

This project is a **real-time N-body simulation** running on the **Raspberry Pi Pico**, programmed in **MicroPython**. By default, it simulates **3 celestial bodies**, but thanks to its **object-oriented design (OOP)**, it can easily handle more bodies.

## 📽️ Demo
Run `main.py` on your Raspberry Pi Pico to see the simulation in action on an **SSD1306 OLED display**.

## 📦 Features
- Simulates the gravitational interaction between multiple bodies
- Supports more than 3 bodies through **OOP** extensibility
- Displays the simulation on an **SSD1306 OLED screen**

## 🛠️ Setup & Wiring

### 🧰 Requirements
- **Raspberry Pi Pico** (running **MicroPython**)  
- **SSD1306 OLED Display** (I2C interface)  
- Power source (preferably NOT a low-draw power bank—see the [Important Note](#important-note))

### 🔌 Wiring Instructions

| **SSD1306 Pin** | **Raspberry Pi Pico Pin**        |
|-----------------|---------------------------------|
| **VCC**         | **5V** (Power)                   |
| **GND**         | **GND** (Ground)                 |
| **SCL**         | **GPIO17** (Physical Pin 22)     |
| **SDA**         | **GPIO16** (Physical Pin 21)     |

### 📋 Installation
1. Ensure your Raspberry Pi Pico is flashed with **MicroPython**. You can follow the [official MicroPython guide](https://micropython.org/download/rp2-pico/).

2. Clone this repository or download the `main.py` file:

```bash
# Clone the repository
git clone https://github.com/yourusername/n-body-simulation.git
cd n-body-simulation
```

3. Upload the code to your Pico using a tool like `rshell`, `Thonny`, or `ampy`:

```bash
# Using rshell to upload the code
rshell -p /dev/ttyUSB0
cp main.py /pyboard/
```

4. Reset the Pico or run the code:

```python
import main
```

## 🚀 Running the Simulation
Once uploaded, the simulation will start automatically, displaying the motion of **3 gravitational bodies** on the SSD1306 display.

- Modify the number of bodies by editing the `bodies` list in `main.py`.
- Adjust physical parameters (e.g., mass, position, velocity) to explore different system dynamics.

## ⚠️ Important Note
You may experience issues running this project on certain **power banks**. The **Raspberry Pi Pico** draws **low current**, causing some power banks to enter **standby mode** and shut down. For best results, use a **USB power adapter** or a reliable **battery pack** designed for low-power devices.

## 📚 Customization
1. **Add More Bodies**: Extend the `Body` class and update the `bodies` list.
2. **Adjust Physics**: Tweak gravitational constants, initial velocities, and positions.

## 📄 License
This project is open-source and available under the **MIT License**.

---

Happy coding and exploring the universe! 🌠
