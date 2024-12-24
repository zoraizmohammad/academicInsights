import { initializeApp } from "https://www.gstatic.com/firebasejs/9.16.0/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/9.16.0/firebase-auth.js";
import { firebaseConfig } from "./firebase-config.js";

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

document.getElementById("google-signin-button").addEventListener("click", () => {
  const provider = new GoogleAuthProvider();
  signInWithPopup(auth, provider)
    .then((result) => {
      const user = result.user;
      document.getElementById("signin-status").innerHTML = `Signed in as: ${user.email}`;
      document.getElementById("analyze-history-button").disabled = false;
    })
    .catch((error) => console.error("Sign-in error:", error.message));
});

document.getElementById("analyze-history-button").addEventListener("click", () => {
  chrome.history.search({ text: "", maxResults: 10 }, (data) => {
    const userId = auth.currentUser.uid;
    const historyData = data.map((item) => ({ url: item.url, title: item.title }));

    // Send history data to backend
    fetch("http://localhost:5000/analyze-website", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, history: historyData }),
    })
      .then((response) => response.json())
      .then((result) => {
        // Display analysis results
        const analysisDiv = document.getElementById("analysis-results");
        analysisDiv.innerHTML = `
          <h2>Analysis Results</h2>
          <p>Learning Style: ${result.learning_style}</p>
          <p>Topic: ${result.topic} (Relevance: ${result.relevance_score})</p>
        `;
      })
      .catch((error) => console.error("Error:", error));
  });
});
