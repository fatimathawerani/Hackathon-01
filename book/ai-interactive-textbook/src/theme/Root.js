import React from 'react';
import ChatWidget from '../components/ChatWidget/chatbot';
import ChapterActions from '../components/ChapterActions';

export default function Root({ children }) {
  return (
    <>
      {children}
      <ChapterActions />
      <ChatWidget />
    </>
  );
}
