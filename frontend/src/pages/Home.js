import React from "react";
import "./../styles/Home.css";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

function Home() {
    return (
        <section className="home">
        <div>
            <Navbar />
            <h1>Welcome to Home Page</h1>
        </div>
            <Footer />

        </section>
    );
}

export default Home;


