import "../styles/footer.css";

function Footer() {
    return (
        <footer class="footer">
          <div class="container">
            <div class="footer-content">
              <div class="footer-section">
              <h3>About Us</h3>
              <p><b><i>ChooseMe</i></b><br/> it is a platform for students to seek opportunities to study abroad</p>
            </div>
            <div class="footer-section">
              <h3>Quick Links</h3>
              <ul>
                <li><router-link to="/">Home</router-link></li>
                <li><router-link to="/about">About</router-link></li>
              </ul>
            </div>
            <div class="footer-section">
              <h3>Contact Us</h3>
              <p class="contact">Email: dcabatar@gmail.com</p> 
              <p class="contact">Phone: +996 995 75 07 07</p>
              {/* <a href="https://www.instagram.com/danc_iiik/" class="media" target="_blank"><img src="../static_files/free-icon-social-12940260.png" alt="" class="logo-contact"></a>
              <a href=" https://t.me/danchiiiiik/" class="media" target="_blank"><img src="../static_files/free-icon-telegram-logo-87413.png" alt="" class="logo-contact"></a> */}
            </div>
          </div>
          <div class="footer-bottom">
            <p>&copy; 2024 Events.kg | All Rights Reserved</p>
          </div>
        </div>
        </footer>
    );
}

export default Footer;
