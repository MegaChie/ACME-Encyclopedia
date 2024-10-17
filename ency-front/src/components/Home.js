import './Home.css'

const stats = async () => {
  fetch('http://localhost:5000/api/v1/stats').then((res) => {
    return res.json();
  }).then((data) => {
    console.log(`So far, {data.users} are on board, with an article count`+
                `reaching up to {data.articles} articles so far`);
  });
};

function Home() {
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
      <p>{stats}</p>
      <footer>ACME Corp</footer>
    </div>
  );
}

export default Home;
