# 🎭 Arabic Poetry Generator

A Streamlit web application that generates beautiful Arabic poetry using AI.

## Features

- 🎨 Generate Arabic poetry on any topic
- 📜 Multiple classical Arabic meters (البحور)
- 🎯 Classical and modern poetry styles
- 📱 Responsive design for mobile and desktop
- 📥 Download generated poems

## Setup

### 1. Local Development

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create `.streamlit/secrets.toml` and add your Anthropic API key:
   ```toml
   ANTHROPIC_API_KEY = "your-actual-api-key-here"
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

### 2. Deploy on Streamlit Cloud

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Create new app from your GitHub repository
4. In app settings → Secrets, add:
   ```toml
   ANTHROPIC_API_KEY = "your-actual-api-key-here"
   ```
5. Deploy!

## Get API Key

1. Go to [Anthropic Console](https://console.anthropic.com)
2. Create an account or sign in
3. Generate an API key
4. Add credits to your account

## Usage

1. Enter a poetry topic (e.g., love, nature, homeland)
2. Choose poetic meter and style
3. Set number of verses
4. Click "Generate Poem"
5. Download or share your poem!

## Arabic Meters Supported

- البسيط (Al-Basit)
- الطويل (Al-Tawil)
- الوافر (Al-Wafir)
- الكامل (Al-Kamil)
- الهزج (Al-Hazaj)
- الرجز (Ar-Rajaz)
- المتقارب (Al-Mutaqarib)
- الرمل (Ar-Ramal)

## License

MIT License