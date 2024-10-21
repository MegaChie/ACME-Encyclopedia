import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import NotFound from './components/NotFound'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/home" element={<Home />}></Route>
        <Route path="/404" element={<NotFound />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
