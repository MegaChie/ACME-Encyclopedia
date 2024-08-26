import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

const PrivateRoute = ({ children }) =>
{
    const { isAuthenticated } = useAuth();
    const navigate = useNavigate();


React.useEffect( () =>
{
    if (!isAuthenticated)
    {
        navigate('/login');
    }
} , [isAuthenticated, navigate]);

    return isAuthenticated ? children : null;
};

export default PrivateRoute;