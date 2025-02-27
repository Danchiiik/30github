import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import "../src/styles/reset.css";

// import About from "./pages/About";
// import Profile from "./pages/Profile";
// import Login from "./pages/Login";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;
