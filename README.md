# 🤖 Lathasri AI Portfolio Assistant

An intelligent, interactive chatbot that showcases Lathasri Ravirala's professional portfolio through conversational AI. Built with Flask, powered by Meta's Llama 3.3 70B model via OpenRouter API, featuring a stunning glassmorphic UI with animated elements.

## 🌟 Live Demo

**[Try it now!](https://chat-lq7m.onrender.com/)**

## ✨ Features

- **🧠 AI-Powered Conversations**: Utilizes Meta Llama 3.3 70B for intelligent, context-aware responses
- **💬 Session Memory**: Maintains conversation history for natural, flowing interactions
- **🎨 Modern Glassmorphic UI**: Beautiful gradient backgrounds with blur effects and smooth animations
- **📱 Fully Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **⚡ Quick Actions**: Pre-defined questions for instant information access
- **🔄 Real-time Updates**: Live typing indicators and smooth message animations
- **🎯 Portfolio Focus**: Specialized knowledge about skills, projects, experience, and contact information

## 🛠️ Tech Stack

### Backend
- **Flask 3.0.0** - Python web framework
- **OpenRouter API** - AI model access via Meta Llama 3.3 70B
- **Session Management** - Server-side conversation history
- **Gunicorn** - Production WSGI server

### Frontend
- **HTML5 & CSS3** - Modern semantic markup and styling
- **Vanilla JavaScript** - No dependencies, pure JS for interactions
- **Google Fonts** - Poppins & Playfair Display typography
- **CSS Animations** - Smooth transitions and particle effects

### Design Features
- Animated gradient background
- Floating particle effects
- Glassmorphism (frosted glass) design
- Responsive grid layout
- Custom scrollbars
- Loading states and transitions

## 📋 Prerequisites

- Python 3.8 or higher
- OpenRouter API key ([Get one here](https://openrouter.ai/))
- pip (Python package manager)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd portfolio-chatbot
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
SECRET_KEY=your_secret_key_for_sessions
```

### 5. Run the Application

```bash
# Development mode
python app.py

# Production mode with Gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```

Visit `http://localhost:5000` in your browser.

## 📁 Project Structure

```
portfolio-chatbot/
│
├── app.py                      # Flask application & API routes
├── portfolio_data.py           # Portfolio information & system prompt
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in repo)
├── .gitignore                 # Git ignore rules
│
├── static/
│   ├── css/
│   │   └── style.css          # Glassmorphic UI styles
│   └── js/
│       └── script.js          # Frontend interaction logic
│
└── templates/
    └── index.html             # Main chatbot interface
```

## 🎨 Customization

### Update Portfolio Information

Edit `portfolio_data.py` to customize:

```python
PORTFOLIO_DATA = {
    "name": "Your Name",
    "role": "Your Role",
    "skills": {...},
    "experience": [...],
    "projects": [...],
    # ... more fields
}
```

### Modify AI Behavior

Adjust the `SYSTEM_PROMPT` in `portfolio_data.py` to change how the AI responds.

### Customize Appearance

Edit `static/css/style.css` to modify:
- Color schemes and gradients
- Animation speeds
- Layout and spacing
- Responsive breakpoints

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chatbot interface |
| `/api/chat` | POST | Send message, get AI response |
| `/api/clear` | POST | Clear conversation history |
| `/api/portfolio` | GET | Get portfolio data JSON |
| `/health` | GET | Health check for deployment |

### Example API Usage

```javascript
// Send a message
fetch('/api/chat', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({message: 'What are your skills?'})
})
```

## 🌐 Deployment

### Deploy to Render

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Set environment variables in Render dashboard
4. Deploy with these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### Deploy to Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create new app
heroku create your-app-name

# Set environment variables
heroku config:set OPENROUTER_API_KEY=your_key
heroku config:set SECRET_KEY=your_secret

# Deploy
git push heroku main
```

## 🔒 Security Notes

- Never commit `.env` file to version control
- Use strong secret keys for production
- Keep API keys secure and rotate them regularly
- Enable HTTPS in production deployments
- Consider rate limiting for API endpoints

## 🐛 Troubleshooting

### Common Issues

**API Timeout Errors**
```python
# Increase timeout in app.py
response = requests.post(..., timeout=60)
```

**Session Not Persisting**
```python
# Ensure secret key is set
app.secret_key = os.environ.get('SECRET_KEY')
session.modified = True
```

**Styling Not Loading**
- Clear browser cache
- Check Flask static file paths
- Verify CSS file location

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Lathasri Ravirala**
- Email: lathasriravirala2003@gmail.com
- LinkedIn: [lathasri-ravirala](https://www.linkedin.com/in/lathasri-ravirala-06b606309)

## 🙏 Acknowledgments

- Meta AI for Llama 3.3 70B model
- OpenRouter for API access
- Flask community for excellent documentation
- Design inspiration from modern glassmorphism trends

## 📞 Support

For questions or issues:
1. Check existing documentation
2. Open an issue on GitHub
3. Contact via email or LinkedIn

---

**Built with ❤️ and AI** | Powered by Meta Llama 3.3 70B 🚀
