import { initializeApp } from "https://www.gstatic.com/firebasejs/9.16.0/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/9.16.0/firebase-auth.js";
import { firebaseConfig } from "./firebase-config.js";

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Google Sign-In
document.getElementById("google-signin-button").addEventListener("click", () => {
  const provider = new GoogleAuthProvider();
  signInWithPopup(auth, provider)
    .then((result) => {
      const user = result.user;
      document.getElementById("signin-status").innerHTML = `Signed in as: ${user.email}`;
      loadWebHistory();
    })
    .catch((error) => {
      console.error("Sign-in error:", error.message);
    });
});

// Load Web History
function loadWebHistory() {
  chrome.history.search({ text: "", maxResults: 10 }, (data) => {
    const historyList = document.getElementById("history-list");
    historyList.innerHTML = "";
    data.forEach((item) => {
      const listItem = document.createElement("li");
      listItem.textContent = `${item.title} - ${item.url}`;
      historyList.appendChild(listItem);
    });
  });
}
