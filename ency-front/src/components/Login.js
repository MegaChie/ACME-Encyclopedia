import './css/Login.css';

const handelLogin = async (event) => {
  event.preventDefault();
  const userData = new FormData(event.target);
  const input = Object.fromEntries(userData.entries());

  try {
    const response = await fetch('api/v1/login',
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(input)
      });
      if (response.ok) {
        console.log(`Logged in, check for the cookie`);
      }
  } catch (error) {
    console.error(error);
  }
}

function Login() {
  return(
    <div>
      <form onSubmit={handelLogin}>
        <button type="submit">Login</button>
        <input type="text" name="username" placeholder="Username" />
        <input type="text" name="email" placeholder="Email" required />
        <input type="password" name="password" placeholder="Password" required />
      </form>
    </div>
  );
}

export default Login;
