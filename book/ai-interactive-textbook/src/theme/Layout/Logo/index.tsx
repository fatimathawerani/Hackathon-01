import React, { JSX } from 'react';
import type { Props } from '@theme/Logo';
import { SiProbot } from 'react-icons/si';
import Link from '@docusaurus/Link';

export default function CustomLogo(props: Props): JSX.Element {
  return (
    <Link
      {...props}
      to="/"
      style={{ display: 'flex', alignItems: 'center', gap: '8px' }}
    >
      <SiProbot style={{ fontSize: '2rem', color: 'white' }} />
      <span style={{ fontWeight: 700, fontSize: '1.2rem', color: 'white' }}>
        Physical AI
      </span>
    </Link>
  );
}
