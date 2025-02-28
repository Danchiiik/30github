import { Link } from "react-router-dom";
import "../styles/Navbar.css";  // Add styles if needed

function Navbar() {
    return (
        <nav> 
            <div className="navbar_main_div">                
                <div className="logo_div">
                    <p className="logo_text">ChooseMe</p>
                </div>
                <div className="signup_login">
                    <span className="signup"><Link to="/signup">Sign Up</Link></span>
                    <span className="login"><Link to="/login">Login</Link></span>
                </div>
            </div>
        </nav>
        
    );
}

export default Navbar;
