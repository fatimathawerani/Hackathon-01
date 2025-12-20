import React from 'react';
import ChatWidget from '../components/ChatWidget/chatbot';
import ChapterActions from '../components/Translation/ChapterTranslator';

export default function Root({ children }) {
  return (
    <>
      {children}
      <ChapterActions />
      <ChatWidget />
      
    </>
  );
}
