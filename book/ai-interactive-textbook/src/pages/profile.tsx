import React from 'react';
import UserProfileForm from '../components/UserProfileForm';
import Layout from '@theme/Layout';

const ProfilePage = () => {
  return (
    <Layout>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh' }}>
        <UserProfileForm />
      </div>
    </Layout>
  );
};

export default ProfilePage;
