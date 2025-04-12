import './css/Login.css';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

function Login() {
  const navigateor = useNavigate();

  const handleLogin = async (event) => {
    event.preventDefault();
    const userData = new FormData(event.target);
    const input = Object.fromEntries(userData.entries());

    try {
      const response = await fetch('api/v1/login', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(input),
      });

      if (response.ok) {
        console.log('Logged in, check for the cookie');
        navigateor('/Articles'); // Use navigate to programmatically redirect
      } else {
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleLogin}>
        <button type="submit">Login</button>
        <input type="text" name="username" placeholder="Username" />
        <input type="text" name="email" placeholder="Email" required />
        <input type="password" name="password" placeholder="Password" required />
      </form>
    </div>
  );
}

export default Login;
