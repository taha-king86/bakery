# 🥖 Smart Bakery Queue System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-green.svg)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey)]()

> An intelligent queue management system for bakeries using **Face Recognition** and **QR Code** technology.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
  - [Linux (Arch)](#linux-arch)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
  - [Windows](#windows)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🧠 Overview

**Smart Bakery Queue System** is a desktop application designed to automate and streamline the customer queuing process in bakeries. It eliminates confusion, reduces waiting time, and provides a seamless experience for both customers and bakers.

The system uses **QR codes** for order identification and **facial recognition** to verify customers when they arrive to collect their bread.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📱 **QR Code Generation** | Each customer receives a unique QR code containing their order details |
| 👤 **Face Recognition** | Customers verify their identity by scanning their face at the pickup station |
| 📋 **Real-Time Queue Display** | Baker sees sorted queue on a monitor with customer names and bread counts |
| 🗄️ **Local Database** | All orders and customer data stored securely using SQLite |
| 🖥️ **User-Friendly GUI** | Built with Tkinter for simplicity and ease of use |
| 📊 **Order Tracking** | Track order status: pending → verified → completed |

---

## 🔄 How It Works

1. **Customer places an order** → System registers the order with bread count
2. **QR code is generated** → Customer receives a unique QR code
3. **Customer arrives at pickup** → Scans QR code at the device
4. **Face is captured** → System takes a photo and verifies identity
5. **Baker's monitor updates** → Queue is sorted by turn number with customer names and bread counts

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core programming language |
| **OpenCV** | Camera handling and image processing |
| **face_recognition** | Face detection and verification |
| **dlib** | Face recognition backend |
| **pyzbar** | QR code scanning |
| **Pillow** | Image processing and manipulation |
| **SQLite3** | Local database management |
| **Tkinter / ttk** | Graphical user interface |
| **python-dotenv** | Environment variable management |

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Git
- CMake (for dlib compilation)
- Webcam (for face capture)

---

### 🐧 Linux (Arch)

```bash
# 1. Install system dependencies
sudo pacman -S --needed \
    python \
    python-pip \
    cmake \
    base-devel \
    opencv \
    tcl \
    tk \
    sqlite \
    boost \
    eigen

# 2. Install dlib from Arch repositories (RECOMMENDED)
sudo pacman -S python-dlib

# If python-dlib is not available, install from AUR:
yay -S python-dlib

# 3. Clone the repository
git clone https://github.com/yourusername/bakery-queue-system.git
cd bakery-queue-system

# 4. Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# 5. Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 6. Set up environment variables
cp .env.example .env

# 7. Run the application
python src/main.py
