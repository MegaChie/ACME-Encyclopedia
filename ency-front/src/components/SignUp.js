import './css/SignUp.css';
import React, { useState } from "react";

function Signup() {
  const [popupMessage, setPopupMessage] = useState("");
  const [popupClass, setPopupClass] = useState(""); // To determine the styling of the popup

  const handleSignup = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
      const response = await fetch("api/v1/add_users", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        setPopupMessage("Signup successful!");
        setPopupClass("success");
      } else {
        const errorData = await response.json();
        setPopupMessage(`Signup failed: ${errorData.error}`);
        setPopupClass("error");
      }
    } catch (error) {
      setPopupMessage(`Signup failed: ${error.message}`);
      setPopupClass("error");
    }

    setTimeout(() => {
      setPopupMessage("");
      setPopupClass("");
    }, 4000); // Hides the popup after 4 seconds
  };

  return (
    <div>
      <form onSubmit={handleSignup}>
        <input type="text" name="username" placeholder="Username" />
        <input type="email" name="email" placeholder="Email" required />
        <input type="password" name="password" placeholder="Password" required />
        <button type="submit">Sign Up</button>
      </form>

      {popupMessage && (
        <div className={`popup ${popupClass}`}>{popupMessage}</div>
      )}
    </div>
  );
}

export default Signup;
