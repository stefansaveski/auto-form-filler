# auto-form-filler

A simple Python/Selenium bot that automatically fills and submits a two-page Google Form in Macedonian, including demographic info and 40 scaled questions with random answers and generated Macedonian-style emails.

## 🔧 Requirements

- Python 3.7+
- Selenium (`pip install selenium`)
- ChromeDriver (in your PATH)

## 🚀 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/auto-form-filler-mk.git
   cd auto-form-filler-mk
   ```
2. Install dependencies:
   ```bash
   pip install selenium
   ```
3. Download ChromeDriver matching your Chrome version and ensure it's on your PATH.

## ⚙️ Configuration

- Edit `main.py`, setting the `FORM_URL` and desired number of submissions (`N`).
- Adjust gender, age selectors, and question logic as needed.

## ▶️ Usage

Run the script:
```bash
python main.py
```

Each run fills the form with randomized Macedonian names, emails, and answers.

## 📄 License

MIT © Stefan Saveski

