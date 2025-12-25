import React from "react";
import Layout from "@theme-original/Layout";
import ChatWidget from "@site/src/components/ChatWidget/chatbot";
import { ChatProvider } from "@site/src/context/ChatContext";

export default function LayoutWrapper(props) {
  return (
    <>
      <ChatProvider>
        <Layout {...props} />
        <ChatWidget />
      </ChatProvider>
    </>
  );
}