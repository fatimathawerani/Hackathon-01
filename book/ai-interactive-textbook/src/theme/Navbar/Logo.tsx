// src/theme/Navbar/Logo.tsx
import React from 'react';
import { SiProbot } from 'react-icons/si';
import Link from '@docusaurus/Link';

export default function Logo() {
  return (
    <Link to="/" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <SiProbot style={{ fontSize: '2.5rem', color: '#01287eff' }} />
    </Link>
  );
}
