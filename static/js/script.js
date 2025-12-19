// ==================== DOM ELEMENTS ====================
const chatMessages = document.getElementById('chatMessages');
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');
const typingIndicator = document.getElementById('typingIndicator');

// ==================== UTILITY FUNCTIONS ====================

/**
 * Get current time in 12-hour format
 */
function getCurrentTime() {
    const now = new Date();
    let hours = now.getHours();
    const minutes = now.getMinutes();
    const ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12;
    const minutesStr = minutes < 10 ? '0' + minutes : minutes;
    return `${hours}:${minutesStr} ${ampm}`;
}

/**
 * Scroll to the bottom of chat messages
 */
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Show typing indicator
 */
function showTypingIndicator() {
    typingIndicator.style.display = 'flex';
    scrollToBottom();
}

/**
 * Hide typing indicator
 */
function hideTypingIndicator() {
    typingIndicator.style.display = 'none';
}

/**
 * Disable/Enable input
 */
function setInputState(disabled) {
    userInput.disabled = disabled;
    sendBtn.disabled = disabled;
    
    if (!disabled) {
        userInput.focus();
    }
}

// ==================== MESSAGE RENDERING ====================

/**
 * Create and append a message to the chat
 */
function appendMessage(text, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    
    const avatarDiv = document.createElement('div');
    avatarDiv.className = 'message-avatar';
    avatarDiv.innerHTML = `<span>${isUser ? 'U' : 'LR'}</span>`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    const bubbleDiv = document.createElement('div');
    bubbleDiv.className = 'message-bubble';
    
    // Convert line breaks to HTML and preserve formatting
    const formattedText = text.replace(/\n/g, '<br>');
    bubbleDiv.innerHTML = formattedText;
    
    const timeSpan = document.createElement('span');
    timeSpan.className = 'message-time';
    timeSpan.textContent = getCurrentTime();
    
    contentDiv.appendChild(bubbleDiv);
    contentDiv.appendChild(timeSpan);
    
    messageDiv.appendChild(avatarDiv);
    messageDiv.appendChild(contentDiv);
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

/**
 * Remove quick questions after first user message
 */
function removeQuickQuestions() {
    const quickQuestions = document.querySelector('.quick-questions');
    if (quickQuestions) {
        quickQuestions.style.transition = 'opacity 0.3s ease';
        quickQuestions.style.opacity = '0';
        setTimeout(() => {
            quickQuestions.remove();
        }, 300);
    }
}

// ==================== API COMMUNICATION ====================

/**
 * Send message to backend API
 */
async function sendMessage(message) {
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        if (response.ok && data.status === 'success') {
            return { success: true, message: data.response };
        } else {
            return { 
                success: false, 
                message: data.error || 'Sorry, I encountered an error. Please try again.' 
            };
        }
    } catch (error) {
        console.error('Error:', error);
        return { 
            success: false, 
            message: 'Network error. Please check your connection and try again.' 
        };
    }
}

/**
 * Clear chat history
 */
async function clearChat() {
    try {
        const response = await fetch('/api/clear', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        if (response.ok) {
            // Clear all messages except welcome message
            const messages = chatMessages.querySelectorAll('.message');
            messages.forEach((msg, index) => {
                if (index > 0) { // Keep first message (welcome)
                    msg.remove();
                }
            });
            
            // Re-add quick questions if they were removed
            if (!document.querySelector('.quick-questions')) {
                location.reload(); // Simple reload to restore initial state
            }
            
            return true;
        }
        return false;
    } catch (error) {
        console.error('Error clearing chat:', error);
        return false;
    }
}

// ==================== EVENT HANDLERS ====================

/**
 * Handle form submission
 */
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const message = userInput.value.trim();
    
    if (!message) return;
    
    // Remove quick questions after first message
    removeQuickQuestions();
    
    // Display user message
    appendMessage(message, true);
    
    // Clear input
    userInput.value = '';
    
    // Disable input while processing
    setInputState(true);
    
    // Show typing indicator
    showTypingIndicator();
    
    // Send message to API
    const response = await sendMessage(message);
    
    // Hide typing indicator
    hideTypingIndicator();
    
    // Display bot response
    appendMessage(response.message, false);
    
    // Re-enable input
    setInputState(false);
});

/**
 * Handle quick question buttons
 */
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('quick-btn')) {
        const question = e.target.getAttribute('data-question');
        userInput.value = question;
        chatForm.dispatchEvent(new Event('submit'));
    }
});

/**
 * Handle clear chat button
 */
clearBtn.addEventListener('click', async () => {
    if (confirm('Are you sure you want to clear the chat history?')) {
        const success = await clearChat();
        if (!success) {
            alert('Failed to clear chat. Please try again.');
        }
    }
});

/**
 * Auto-focus input on load
 */
window.addEventListener('load', () => {
    userInput.focus();
});

/**
 * Handle Enter key (submit) and Shift+Enter (new line)
 */
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event('submit'));
    }
});

// ==================== INITIALIZATION ====================
console.log('Portfolio Chatbot initialized ✓');
console.log('Ready to answer questions about Lathasri Ravirala');
