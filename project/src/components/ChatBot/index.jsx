import React, { useState, useEffect, useRef } from 'react';
import { ChatKit, useChatKit } from '@openai/chatkit-react';
import './chatbot.css';

export default function ChatBot() {
  const [isOpen, setIsOpen] = useState(false);
  const [error, setError] = useState(null);
  const [selectedText, setSelectedText] = useState('');
  const chatkitRef = useRef(null);

  const { control } = useChatKit({
    api: {
      // Demo configuration - replace with your actual backend URL in docusaurus.config.js customFields
      url: 'http://localhost:8000/chatkit',
      domainKey: 'local-dev',
    },
    onError: (err) => {
      console.error('ChatKit error:', err);
      setError(err.message);
    },
  });

  useEffect(() => {
    console.log('ChatBot component mounted');
    console.log('Control:', control);

    // Store control reference for sending actions
    if (control) {
      chatkitRef.current = control;
    }
  }, [control]);

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

    // Listen for selection changes on the document
    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('keyup', handleSelection);

    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('keyup', handleSelection);
    };
  }, []);

  // Send selected text when chat opens (if there's a selection)
  useEffect(() => {
    const sendSelectionToBackend = async () => {
      if (isOpen && selectedText && chatkitRef.current) {
        try {
          console.log('Sending selected text to backend:', selectedText.substring(0, 100));

          // Send custom action with selected text
          await chatkitRef.current.sendCustomAction({
            type: 'text_selection',
            payload: { text: selectedText },
          });

          console.log('Selected text sent successfully');
        } catch (err) {
          console.error('Error sending selected text:', err);
        }
      }
    };

    sendSelectionToBackend();
  }, [isOpen, selectedText]);

  if (error) {
    console.log('ChatKit error detected:', error);
  }

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
            {error ? (
              <div className="chatbot-error">
                <p>⚠️ Unable to connect to chat service</p>
                <p className="error-details">{error}</p>
              </div>
            ) : (
              <ChatKit
                control={control}
                className="chatbot-widget"
              />
            )}
          </div>
        </div>
      )}
    </>
  );
}
