import React from 'react';
import ChatWidget from '../components/ChatWidget/chatbot';

export default function Root({ children }) {
  return (
    <>
      {children}
      <ChatWidget />
    </>
  );
}
