import React, {useState, useEffect} from 'react';
import axios from 'axios';
import './Login.css'
import {useNavigate} from "react-router-dom";
import { useAuth } from "./AuthContext";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';


const Login = () => {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();
    const { login } = useAuth();

    const handleLogin = async e => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/v1/login', {
                username,
                email,
                password,
            }, {
                withCredentials: true
            });

            if (response.status === 201 || response.status === 200)
            {
                console.log('User logged in', response.data);
               // const sessionCookie = response.data.cookie;
                //console.log('Session cookie', sessionCookie);

                login();
                navigate('/home');



            } else
            {
                setErrorMessage('Login failed. Please Check your Credentials');
            }




        } catch (e) {
            console.error('Error logging in:', e);
        }



    };

   const handleGithubLogin = async () => {

    try {
        // Check if the user is already authenticated

        const response = await axios.get('/api/v1/auth/github/callback', { withCredentials: true });

        if (response.status === 200) {
            console.log('User logged in', response.data);
            login();
            navigate('/home');
        } else {
            console.log('User not logged in', response.data);
            window.location.href = '/api/v1/login/github';
        }
    } catch (e) {
        // If there's an error (e.g., not authenticated), start the GitHub login flow
        console.error('Error during GitHub login:', e);

    }
};
    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Login</button>

                {/* Wrapping the GitHub button in a div */}
                <div className="github-login-container">
                    <button type="button" className="github-login-button" onClick={handleGithubLogin}>
                        <FontAwesomeIcon icon={faGithub}/> Login with GitHub
                    </button>
                </div>
            </form>
            {errorMessage && <p className="error-message">{errorMessage}</p>}
        </div>
    )


}

export default Login;