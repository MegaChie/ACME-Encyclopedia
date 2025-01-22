import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import NotFound from './components/NotFound';
import SignUpLayout from './components/SignUp';
import Login from './components/Login';
import Articles from './components/Articles';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/home" element={<Home />}></Route>
        <Route path="*" element={<NotFound />}></Route>
        <Route path="/Signup" element={<SignUpLayout />}></Route>
        <Route path='/Login' element={<Login />}></Route>
        <Route path='/Articles' element={<Articles />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
