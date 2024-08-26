import React, { createContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    const savedAuthState = localStorage.getItem('isAuthenticated') === 'true';
    const expirationTime = localStorage.getItem('authExpiration');
    const hasExpired = expirationTime && new Date().getTime() > expirationTime;

    if (hasExpired) {
      localStorage.removeItem('isAuthenticated');
      localStorage.removeItem('authExpiration');
      return false;
    }

    return savedAuthState;
  });

  const login = () => {
    const expirationTime = new Date().getTime() + 8 * 60 * 60 * 1000; // 8 hours from now
    setIsAuthenticated(true);
    localStorage.setItem('isAuthenticated', 'true');
    localStorage.setItem('authExpiration', expirationTime);
  };

  const logout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('isAuthenticated');
    localStorage.removeItem('authExpiration');
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return React.useContext(AuthContext);
};