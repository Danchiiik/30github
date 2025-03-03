import React from "react";

import '../styles/Signup.css';

function Signup () {
    return (
        <section class="register-section">
        <div class="container">
            <div class="register-form" v-if="!IsRegistered">
                <div class="preview-text">
                    <h1 class="register-header">Sign up</h1>
                </div>
        
                <form class="main-form">
                    <div class="form">
                        <ul class="register-fields">
                            {/* <!-- <span>Электронная почта</span> -->
                            <li class="li-button"><input type="text" v-model="email" placeholder="Email"></li>
                            <!-- <span>Пароль</span> -->
                            <li class="li-button"><input type="password" v-model="password" placeholder="Password"></li>
                            <!-- <span>Подтвердите пароль</span> -->
                            <li class="li-button"><input type="password" v-model="password2" placeholder="Confirm password"></li > */}
                        </ul>
                        <div class="register-buttons">
                            <button type="submit" class="signup-button">Sign up</button>
                        </div>
                        
                        <div class="access-quickly">
                            <span>ACCESS QUICKLY</span>
                        </div>
                        
                        <div class="google-div">
                            <router-link to="/google">
                                <button class="google-button">Google</button>
                            </router-link>
                        </div>

                    </div>    
                    
                    <div class="logining-div">
                        <span class="logining-text">Уже регистрировались?</span>
                        <router-link to="/login">
                            <button class="logining-button">Login</button>
                        </router-link>
                    </div>
                </form>     
            </div>


            <div class="register-form" v-else>
                <div class="registered-text-div">
                    <p class="registered-text">
                        Вы успешно зарегестрировались! Пожалуйста проверьте свою почту для дальнейших действий
                    </p> 
                </div>
            </div>
        </div>
        </section>
);

}


export default Signup;