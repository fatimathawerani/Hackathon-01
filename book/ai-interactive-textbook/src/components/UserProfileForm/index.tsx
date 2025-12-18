import React, { useState } from 'react';

const UserProfileForm = () => {
  const [softwareExperience, setSoftwareExperience] = useState('');
  const [hardwareAccess, setHardwareAccess] = useState('');
  const [learningDepth, setLearningDepth] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Save the user profile using Better Auth's mechanisms
    console.log({
      softwareExperience,
      hardwareAccess,
      learningDepth,
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Complete Your Profile</h2>
      <label>
        Software Experience:
        <select value={softwareExperience} onChange={(e) => setSoftwareExperience(e.target.value)}>
          <option value="">Select...</option>
          <option value="Beginner">Beginner</option>
          <option value="Intermediate">Intermediate</option>
          <option value="Advanced">Advanced</option>
        </select>
      </label>
      <br />
      <label>
        Hardware Access:
        <select value={hardwareAccess} onChange={(e) => setHardwareAccess(e.target.value)}>
          <option value="">Select...</option>
          <option value="Laptop">Laptop</option>
          <option value="GPU">GPU</option>
          <option value="Robotics kit">Robotics kit</option>
        </select>
      </label>
      <br />
      <label>
        Preferred Learning Depth:
        <select value={learningDepth} onChange={(e) => setLearningDepth(e.target.value)}>
          <option value="">Select...</option>
          <option value="Conceptual">Conceptual</option>
          <option value="Practical">Practical</option>
          <option value="Research">Research</option>
        </select>
      </label>
      <br />
      <button type="submit">Save Profile</button>
    </form>
  );
};

export default UserProfileForm;
