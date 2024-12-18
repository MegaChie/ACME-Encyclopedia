import './css/Home.css';
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
// const packageJson = require('../../package.json');

// const IP = packageJson.apiConfig.baseURL;
const fetchStats = async () => {
  const res = await fetch("api/v1/stats")
  const data = await res.json();
  return `So far, ${data.Users} person are on board, with an article count` +
         ` reaching up to ${data.Articles} articles`;
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
            <Link to={"/Signup"}>
              Sign Up
            </Link>
          </div>
          <div className="logIn">
            Log In
          </div>
      </div>
      <div className='stats'>
        <p>{intel}</p>
      </div>
      
      <footer>ACME Corp</footer>
    </div>
  );
}

export default Home;
