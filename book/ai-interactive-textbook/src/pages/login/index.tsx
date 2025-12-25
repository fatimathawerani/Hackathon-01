import React, { useState } from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link'; // Better for internal linking
import { useHistory } from '@docusaurus/router';
import { useAuth } from '../../context/AuthContext';
import styles from './styles.module.css'; // Import the CSS

export default function Login() {
  const { login, user } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await login(email, password);
      history.push('/docs/chapter-1-physical-ai');
    } catch (err) {
      setError('Invalid email or password. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  if (user) {
    history.push('/docs/chapter-1-physical-ai');
    return null;
  }

  return (
    <Layout title="Login">
      <div className={styles.authWrapper}>
        <div className={styles.authCard}>
          <h1 className={styles.authTitle}>Welcome Back</h1>
          
          <form onSubmit={handleSubmit}>
            <div className={styles.formGroup}>
              <label className={styles.label}>Email Address</label>
              <input 
                type="email" 
                required
                placeholder="name@example.com"
                className={styles.input}
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
              />
            </div>
            
            <div className={styles.formGroup}>
              <label className={styles.label}>Password</label>
              <input 
                type="password" 
                required
                placeholder="••••••••"
                className={styles.input}
                value={password} 
                onChange={(e) => setPassword(e.target.value)} 
              />
            </div>

            {error && <div className={styles.errorMessage}>{error}</div>}

            <button 
              type="submit" 
              disabled={loading}
              className={`button button--primary button--block ${styles.submitButton}`}
            >
              {loading ? 'Logging in...' : 'Login'}
            </button>
          </form>

          <div className={styles.linkText}>
            Don't have an account? <Link to="/register">Create one here</Link>
          </div>
        </div>
      </div>
    </Layout>
  );
}