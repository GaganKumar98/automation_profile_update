
# 🔄 Naukri Resume Auto Updater using Selenium

This Python script automatically logs into your Naukri.com account and updates your **Resume Headline** and optionally uploads your **resume PDF**. Keeping your Naukri profile active improves visibility to recruiters.

---

## 📦 Requirements

- Python 3.x
- Google Chrome Browser
- ChromeDriver (must match your Chrome version)
- Python package: `selenium`

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Script

```bash
git clone https://github.com/your-username/naukri-profile-updater.git
cd naukri-profile-updater
```

### 2. Install Required Python Package

```bash
pip install selenium
```

### 3. Download ChromeDriver

- Visit [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
- Download the version matching your Chrome browser
- Extract the `.exe` and note its path

### 4. Update Your Script

Open the Python script and update the following variables:

```python
EMAIL = "your-naukri-email@example.com"
PASSWORD = "your-password"
NEW_SUMMARY = "This is my updated summary for today."
RESUME_PATH = r"C:\Path\To\Your\Resume.pdf"
CHROME_DRIVER_PATH = "C:/Path/To/chromedriver.exe"
```

---

## ▶️ How to Use

Simply run the script:

```bash
python naukri_updater.py
```

### What it does:

1. Opens [Naukri.com](https://www.naukri.com)
2. Logs in with your credentials
3. Goes to your profile
4. Updates the Resume Headline section
5. (Optional) Uploads a new resume
6. Saves and exits

---

## 🧠 Tips

- Do not share your credentials in public repositories
- Use a `.env` file or encrypted secrets for sensitive info (if needed)
- Avoid overusing the automation to prevent account restrictions

---

## 🛡️ Disclaimer

This tool is for **educational and personal use only**. Automated scripts may violate the terms of service of Naukri.com. Use responsibly.

---

## 🧑‍💻 Author

**Gagan Kumar**  
Email: gagan25398@gmail.com  
GitHub: [@your-username](https://github.com/your-username)
