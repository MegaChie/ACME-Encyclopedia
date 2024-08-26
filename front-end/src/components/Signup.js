import React, { useState } from "react";
import axios from "axios";
import './Signup.css';
import {Link, useNavigate} from "react-router-dom";
import { useAuth } from "./AuthContext";

const Signup = () =>
{
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const { login } = useAuth();

    const handleSignup = async (e) =>
    {
        e.preventDefault();
        try
        {
            const response = await axios.post('/api/v1/add_users',{
                email,
                username,
                password,
            },{withCredentials: true});
            console.log('User signed up', response.data);
            login();
            navigate('/home');

        }catch (e) {
            e.error('Error signing up', e);
        }

    };
    return (
        <div className="signup-container">
            <h2>Sign Up</h2>
            <form onSubmit={handleSignup}>
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
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
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
                <button type="submit">Sign Up</button>
            </form>
            <div className="login-redirect">
            <p>Already have an account? <Link to="/login" className="login-link"> Log in</Link> </p>
            </div>
        </div>


    );
};

export default Signup;