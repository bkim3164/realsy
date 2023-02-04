import './App.css';
import Home from './pages/Home.js'
import SearchPage from './pages/SearchPage.js'
import { BrowserRouter, Routes, Route, Outlet, Link } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<SearchPage />} />

          {/* Using path="*"" means "match anything", so this route
                  acts like a catch-all for URLs that we don't have explicit
                  routes for. */}
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
