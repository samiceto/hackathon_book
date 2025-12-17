import React, { useState, useEffect, useRef } from 'react';
import './chatbot.css';

export default function ChatBot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: 'Hello! I can answer questions about the Physical AI & Humanoid Robotics book. Ask me anything!',
    },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');
  const messagesEndRef = useRef(null);

  // API URL based on environment
  const API_URL = typeof window !== 'undefined' && window.location.hostname === 'localhost'
    ? 'http://localhost:8000/api/chat'
    : 'https://hackathon-book-kr56.onrender.com/api/chat';

  // Auto-scroll to bottom when new messages arrive
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Handle text selection from the page
  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      const text = selection?.toString().trim();

      if (text && text.length > 0) {
        setSelectedText(text);
        console.log('Text selected:', text.substring(0, 100));
      }
    };

    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('keyup', handleSelection);

    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('keyup', handleSelection);
    };
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!inputValue.trim()) return;

    const userMessage = inputValue.trim();
    setInputValue('');

    // Add user message to chat
    setMessages((prev) => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);

    try {
      // Call backend API with selected text if available
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: userMessage,
          selection_text: selectedText || null,
        }),
      });

      if (!response.ok) {
        if (response.status === 429) {
          throw new Error('Rate limit exceeded. Please wait a moment and try again.');
        }
        throw new Error(`API error: ${response.status}`);
      }

      const data = await response.json();

      // Add assistant response to chat
      setMessages((prev) => [...prev, { role: 'assistant', content: data.answer }]);

      // Clear selected text after using it
      setSelectedText('');
    } catch (err) {
      console.error('Chat error:', err);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: `⚠️ Error: ${err.message}`,
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      {/* Floating chat button */}
      <button
        className="chatbot-toggle-button"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle chat"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12 2C6.48 2 2 6.48 2 12C2 13.54 2.38 14.99 3.06 16.27L2 22L7.73 20.94C9.01 21.62 10.46 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM12 20C10.74 20 9.55 19.72 8.5 19.22L3.5 20.5L4.78 15.5C4.28 14.45 4 13.26 4 12C4 7.59 7.59 4 12 4C16.41 4 20 7.59 20 12C20 16.41 16.41 20 12 20Z"
            fill="currentColor"
          />
        </svg>
      </button>

      {/* Chat window */}
      {isOpen && (
        <div className="chatbot-container">
          <div className="chatbot-header">
            <div>
              <span>AI Assistant</span>
              {selectedText && (
                <div style={{ fontSize: '0.75rem', opacity: 0.8, marginTop: '2px' }}>
                  📌 Text selected: "{selectedText.substring(0, 30)}{selectedText.length > 30 ? '...' : ''}"
                </div>
              )}
            </div>
            <button
              className="chatbot-close-button"
              onClick={() => setIsOpen(false)}
              aria-label="Close chat"
            >
              ×
            </button>
          </div>

          <div className="chatbot-content">
            <div className="chatbot-messages">
              {messages.map((message, index) => (
                <div
                  key={index}
                  className={`chatbot-message chatbot-message-${message.role}`}
                >
                  <div className="chatbot-message-content">
                    {message.content}
                  </div>
                </div>
              ))}
              {isLoading && (
                <div className="chatbot-message chatbot-message-assistant">
                  <div className="chatbot-message-content">
                    <div className="chatbot-loading">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>

            <form className="chatbot-input-form" onSubmit={handleSubmit}>
              <input
                type="text"
                className="chatbot-input"
                placeholder="Ask about the book..."
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                disabled={isLoading}
              />
              <button
                type="submit"
                className="chatbot-send-button"
                disabled={isLoading || !inputValue.trim()}
                aria-label="Send message"
              >
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 20 20"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M2 10L18 2L10 18L8 11L2 10Z"
                    fill="currentColor"
                  />
                </svg>
              </button>
            </form>
          </div>
        </div>
      )}
    </>
  );
}
