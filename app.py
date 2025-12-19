from flask import Flask, render_template, request, jsonify, session
import requests
import json
import os
from datetime import timedelta
from portfolio_data import PORTFOLIO_DATA, SYSTEM_PROMPT

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# OpenRouter API Configuration
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', 'your-api-key-here')
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3.3-70b-instruct:free"

@app.route('/')
def index():
    """Render the main chatbot interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests with session-based conversation memory"""
    try:
        user_message = request.json.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Initialize or retrieve conversation history from session
        if 'conversation_history' not in session:
            session['conversation_history'] = []
        
        # Add user message to history
        session['conversation_history'].append({
            'role': 'user',
            'content': user_message
        })
        
        # Keep only last 5 messages (10 total including responses)
        if len(session['conversation_history']) > 10:
            session['conversation_history'] = session['conversation_history'][-10:]
        
        # Prepare messages for API call
        messages = [
            {'role': 'system', 'content': SYSTEM_PROMPT}
        ] + session['conversation_history']
        
        # Call OpenRouter API
        response = requests.post(
            url=OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://portfolio-chatbot.com",
                "X-Title": "Lathasri Portfolio Chatbot",
            },
            data=json.dumps({
                "model": MODEL,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 500
            }),
            timeout=30
        )
        
        if response.status_code == 200:
            api_response = response.json()
            bot_message = api_response['choices'][0]['message']['content']
            
            # Add bot response to history
            session['conversation_history'].append({
                'role': 'assistant',
                'content': bot_message
            })
            
            session.modified = True
            
            return jsonify({
                'response': bot_message,
                'status': 'success'
            })
        else:
            return jsonify({
                'error': f'API Error: {response.status_code}',
                'status': 'error'
            }), 500
            
    except requests.exceptions.Timeout:
        return jsonify({
            'error': 'Request timeout. Please try again.',
            'status': 'error'
        }), 504
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/clear', methods=['POST'])
def clear_chat():
    """Clear conversation history"""
    session.pop('conversation_history', None)
    return jsonify({'status': 'success', 'message': 'Chat cleared'})

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    """Return portfolio data for frontend display"""
    return jsonify(PORTFOLIO_DATA)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment"""
    return jsonify({'status': 'healthy', 'service': 'Portfolio Chatbot API'})

if __name__ == '__main__':
    # For development
    app.run(debug=True, host='0.0.0.0', port=5000)
