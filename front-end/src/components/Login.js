import React, {useState, useEffect} from 'react';
import axios from 'axios';
import './Login.css'
import {useNavigate} from "react-router-dom";
import { useAuth } from "./AuthContext";


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
            </form>
            {errorMessage && <p className="erro-message">{errorMessage}</p>}
        </div>
    )


}

export default Login;