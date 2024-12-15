import './css/Home.css';
import React, { useState, useEffect } from "react";
const packageJson = require('../../package.json');

const IP = packageJson.apiConfig.baseURL;
const fetchStats = async () => {
  const res = await fetch(`${IP}/stat`, {
      method: "get",
      headers: new Headers({
        "User-Agent": "69420",
      }),
    })
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
