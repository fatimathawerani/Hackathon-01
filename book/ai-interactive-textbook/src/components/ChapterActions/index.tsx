import React, { useState } from "react";

type Props = {
  originalContent: string;
};

const ChapterActions: React.FC<Props> = ({ originalContent }) => {
  const [content, setContent] = useState(originalContent);
  const [mode, setMode] = useState<"original" | "translated" | "personalized">(
    "original"
  );
  const [loading, setLoading] = useState(false);

  // TODO: Replace with real auth check later
  const isAuthenticated = true;

  // 🔹 TRANSLATE TO URDU
  const handleTranslate = async () => {
    setLoading(true);

    const response = await fetch(
      "https://backend-hackathon-01.vercel.app/translate",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: originalContent,
          target_language: "Urdu",
        }),
      }
    );

    const data = await response.json();
    setContent(data.translated_text);
    setMode("translated");
    setLoading(false);
  };

  // 🔹 PERSONALIZE CONTENT
  const handlePersonalize = async () => {
    setLoading(true);

    const userProfile = {
      software_experience: "Advanced",
      hardware_access: "GPU",
      learning_depth: "Practical",
    };

    const response = await fetch(
      "https://backend-hackathon-01.vercel.app/ask",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          messages: [
            {
              role: "user",
              text: `
Personalize the following chapter content for this user profile.

USER PROFILE:
${JSON.stringify(userProfile, null, 2)}

CHAPTER CONTENT:
${originalContent}
`,
            },
          ],
        }),
      }
    );

    const data = await response.json();
    setContent(data.text);
    setMode("personalized");
    setLoading(false);
  };

  // 🔹 RESET
  const handleShowOriginal = () => {
    setContent(originalContent);
    setMode("original");
  };

  return (
    <div style={{ marginBottom: "24px" }}>
      {mode !== "original" ? (
        <button onClick={handleShowOriginal}>↩ Show Original</button>
      ) : (
        <>
          <button onClick={handleTranslate}>Translate to Urdu</button>
          {isAuthenticated && (
            <button onClick={handlePersonalize} style={{ marginLeft: "10px" }}>
              Personalize
            </button>
          )}
        </>
      )}

      {loading && <p> Processing...</p>}

      <div
        style={{
          marginTop: "20px",
          direction: mode === "translated" ? "rtl" : "ltr",
        }}
      >
        <p>{content}</p>
      </div>
    </div>
  );
};

export default ChapterActions;
