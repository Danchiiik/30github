import React from "react";
import "./../styles/Home.css";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

function Home() {
    return (
        <section className="home">
            <Navbar />
        <div>
            <h1>ChooseMe</h1>
            <h2>hello</h2>
            <h3>bye</h3>
        </div>
            <Footer />

        </section>
    );
}

export default Home;


