import React, { useState } from 'react';

const ChapterActions = () => {
  const [isTranslated, setIsTranslated] = useState(false);
  const [content, setContent] = useState("This is the original content.");
  const [isPersonalized, setIsPersonalized] = useState(false);

  // TODO: Check if the user is authenticated
  const isAuthenticated = true;

  const handleTranslate = async () => {
    const response = await fetch('api/translate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content: "This is the original content." }),
    });
    const data = await response.json();
    setContent(data.translated_content);
    setIsTranslated(true);
  };

  const handleShowOriginal = () => {
    setContent("This is the original content.");
    setIsTranslated(false);
    setIsPersonalized(false);
  };

  const handlePersonalize = async () => {
    // TODO: Get user profile
    const userProfile = {
      software_experience: 'Advanced',
      hardware_access: 'GPU',
      learning_depth: 'Practical',
    };
    const response = await fetch('https://backend-hackathon-01.vercel.app/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        question: "This is the original content.",
        user_profile: userProfile,
      }),
    });
    const data = await response.json();
    setContent(data.answer);
    setIsPersonalized(true);
  };

  return (
    <div>
      {isTranslated || isPersonalized ? (
        <button onClick={handleShowOriginal}>Show Original</button>
      ) : (
        <>
          <button onClick={handleTranslate}>Translate to Urdu</button>
          {isAuthenticated && (
            <button onClick={handlePersonalize}>Personalize</button>
          )}
        </>
      )}
      <p>{content}</p>
    </div>
  );
};

export default ChapterActions;
