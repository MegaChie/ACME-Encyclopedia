import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from './components/Signup';
import Login from './components/Login';
import Homepage from './components/Homepage';
import PrivateRoute from "./components/PrivateRoute";
import {AuthProvider} from "./components/AuthContext";



import logo from './logo.svg';
import './App.css';



function App() {
    return (
  <AuthProvider>
  <Router>
    <Routes>
        <Route path="/" element={<Signup />} />  {/* Standard routee */}
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<PrivateRoute><Homepage /> </PrivateRoute>} />

    </Routes>
  </Router>
  </AuthProvider>
    );

}

export default App;
