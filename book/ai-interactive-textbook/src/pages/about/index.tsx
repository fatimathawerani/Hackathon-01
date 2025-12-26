// src/pages/about.tsx
import React from 'react';
import Layout from '@theme/Layout';

export default function About() {
  return (
    <Layout title="About Physical AI" description="Learn about our Physical AI & Humanoid Robotics project">
      <main style={{ maxWidth: '800px', margin: '2rem auto', padding: '0 1rem', lineHeight: '1.8' }}>
        <h1 style={{ color: '#9cb4e9ff' }}>About Physical AI & Humanoid Robotics</h1>
        <p>
          Welcome to <strong>Physical AI & Humanoid Robotics</strong> – where cutting-edge robotics meets human-inspired intelligence. 
          Our mission is to explore the intersection of artificial intelligence, humanoid robotics, and plug-and-play robotic systems 
          for research, aeducation, and hands-on innovation.
        </p>
        <p>
          From intelligent humanoid robots capable of mimicking human movements to AI-driven systems inspired by neural networks, 
          we aim to create interactive and engaging experiences for enthusiasts, students, and professionals alike.
        </p>
        <p>
          Dive into our chapters, explore our AI-powered modules, and get inspired by the future of robotics today.
        </p>
      </main>
    </Layout>
  );
}
