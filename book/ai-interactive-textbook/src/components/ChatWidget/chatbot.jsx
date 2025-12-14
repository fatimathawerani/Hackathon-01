import React, { useState, useEffect, useRef } from 'react';
import styles from './chatbot.module.css';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const handleSendMessage = async () => {
  if (!inputMessage.trim()) return;

  const userMessage = inputMessage;

  // Show user message immediately
  setMessages(prev => [...prev, { text: userMessage, sender: 'user' }]);
  setInputMessage('');
  setIsTyping(true);

  try {
    const response = await fetch(
      'https://backend-hackathon-01.vercel.app/ask',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          messages: [
            {
              role: 'user',
              text: userMessage,
            },
          ],
        }),
      }
    );

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`);
    }

    const data = await response.json();

    // ✅ Backend returns { role: "bot", text: "..." }
    setMessages(prev => [
      ...prev,
      { text: data.text, sender: 'bot' },
    ]);
  } catch (error) {
    console.error('Chatbot error:', error);
    setMessages(prev => [
      ...prev,
      { text: 'Could not connect to chatbot.', sender: 'bot' },
    ]);
  } finally {
    setIsTyping(false);
  }
};


  const handleClearChat = () => {
    setMessages([]);
  };

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  return (
    <div className={styles.chatContainer}>
      <button className={styles.chatButton} onClick={toggleChat}>
        {isOpen ? 'X' : '💬'}
      </button>

      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <h3>AI Chatbot</h3>
            <button onClick={toggleChat}>X</button>
          </div>
          <div className={styles.messageList}>
            {messages.map((msg, index) => (
              <div key={index} className={`${styles.message} ${styles[msg.sender]}`}>
                {msg.text}
              </div>
            ))}
            {isTyping && (
              <div className={`${styles.message} ${styles.bot}`}>
                <em>Bot is typing...</em>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
          <div className={styles.chatInputContainer}>
            <input
              type="text"
              className={styles.chatInput}
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
              placeholder="Type your message..."
            />
            <button className={styles.sendButton} onClick={handleSendMessage}>
              Send
            </button>
          </div>
          <button className={styles.clearChatButton} onClick={handleClearChat}>
            Clear Chat
          </button>
        </div>
      )}
    </div>
  );
};

export default ChatWidget;