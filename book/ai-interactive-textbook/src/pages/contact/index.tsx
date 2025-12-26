// src/pages/contact.tsx
import React, { useState } from 'react';
import Layout from '@theme/Layout';


export default function Contact() {
  const [formData, setFormData] = useState({ name: '', email: '', message: '' });
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <Layout title="Contact Us" description="Get in touch with Physical AI & Humanoid Robotics">
      <main style={{ maxWidth: '600px', margin: '2rem auto', padding: '0 1rem', lineHeight: '1.8' }}>
        <h1 style={{ color: '#9cb4e9ff' }}>Contact Us</h1>
        <p>
          Have questions, suggestions, or want to collaborate? We'd love to hear from you!
          Please fill out the form below, and we’ll get back to you as soon as possible.
        </p>

        {submitted ? (
          <div style={{ marginTop: '2rem', padding: '1rem', backgroundColor: '#1f2937', color: 'white', borderRadius: '8px' }}>
            <h2>Thank you!</h2>
            <p>Your message has been received. We'll get back to you shortly.</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginTop: '1rem' }}>
            <input
              type="text"
              name="name"
              placeholder="Your Name"
              value={formData.name}
              onChange={handleChange}
              required
              style={{ padding: '0.5rem', borderRadius: '6px', border: '1px solid #9cb4e9ff' }}
            />
            <input
              type="email"
              name="email"
              placeholder="Your Email"
              value={formData.email}
              onChange={handleChange}
              required
              style={{ padding: '0.5rem', borderRadius: '6px', border: '1px solid #9cb4e9ff' }}
            />
            <textarea
              name="message"
              placeholder="Your Message"
              value={formData.message}
              onChange={handleChange}
              required
              rows={5}
              style={{ padding: '0.5rem', borderRadius: '6px', border: '1px solid #9cb4e9ff' }}
            />
            <button
              type="submit"
              style={{
                padding: '0.75rem',
                borderRadius: '6px',
                backgroundColor: '#4d6992ff',
                color: 'white',
                fontWeight: 'bold',
                cursor: 'pointer',
                border: 'none',
              }}
            >
              Send Message
            </button>
          </form>
        )}
      </main>
    </Layout>
  );
}
