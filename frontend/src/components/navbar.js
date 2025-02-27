import { Link } from "react-router-dom";
// import "./Navbar.css";  // Add styles if needed

function Navbar() {
    return (
        <nav>
            <ul>
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/signup">Sign up</Link></li>
            </ul>
        </nav>
        
    );
}

export default Navbar;
