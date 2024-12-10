import './css/Home.css';
import React, { useState, useEffect } from "react";

const fetchStats = async () => {
  const res = await fetch("https://solid-waddle-6qxr79xwxr5frx79-5000.app.github.dev/api/v1/stats");
  const data = await res.json();
  return `So far, ${data.Users} are on board, with an article count` +
         ` reaching up to ${data.Articles} articles so far`;
};

function Home() {
  const [intel, setIntel] = useState("Grabing stats...");
  useEffect(() => {
    fetchStats().then((stats) => {
      setIntel(stats);
    });
  }, []);

  return (
    <div className="Home">
      <div className="account">
          <div className="signUp">
            Sign Up
          </div>
          <div className="logIn">
            Log In
          </div>
      </div>
      <p>{intel}</p>
      <footer>ACME Corp</footer>
    </div>
  );
}

export default Home;
