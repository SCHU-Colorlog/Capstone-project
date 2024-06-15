import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import UserPage from "./pages/userPage.jsx";
import Main from "./pages/main.jsx";

import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/user/:userId" element={<UserPage />} />
        <Route path="/" element={<Main />} />
      </Routes>
    </Router>
  );
}

export default App;
