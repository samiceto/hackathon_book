import React from 'react';
import ChatBot from '@site/src/components/ChatBot';

// Root component wraps the entire Docusaurus app
export default function Root({ children }) {
  return (
    <>
      {children}
      <ChatBot />
    </>
  );
}
