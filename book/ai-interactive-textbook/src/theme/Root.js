import React from 'react';
// Ensure this path matches exactly where your AuthContext file is
import { AuthProvider } from '@site/src/context/AuthContext'; 

export default function Root({children}) {
  return (
    <AuthProvider>
      {children}
    </AuthProvider>
  );
}
