import React from "react";
import "./../styles/home.css";

import Navbar from "../components/navbar";
import Footer from "../components/footer";

function Home() {
    return (
        <div className="home">
            <Navbar />
            <h1>Welcome to Home Page</h1>
            <Footer />
        </div>
    );
}

export default Home;


