import logo from './logo.svg';
import React from "react";
function Header() {
  return (
    <header style={styles.header}>
      <marquee>
        <h1> Welcome to my website</h1>
      </marquee>
      <div style={styles.conn}>
        
      <img src={logo} alt="Logo" style={styles.logo} /> 

      </div>
      <nav>
        <ul style={styles.navList}>
          <li><a href="#" style={styles.navLink}>Home</a></li>
          <li><a href="#" style={styles.navLink}>About</a></li>
          <li><a href="#" style={styles.navLink}>Contact</a></li>
        </ul>
      </nav>
    </header>
  );
}

const styles = {
  header: {
    backgroundColor: "#333",
    color: "white",
    padding: "10px",
    display: "flex",
    justifyContent: "space-between", 
    alignItems: "center", 
  },
  siteTitle: {
    margin: 0, 
  },
  logo: {
    width: "50px",  
    height: "50px",
    marginLeft: "90px", 
    textAlign:"center",
  },
  navList: {
    listStyleType: "none",
    padding: 0,
    display: "flex",
    gap: "15px", 
  },
  navLink: {
    color: "white",
    textDecoration: "none",
    fontSize: "18px",
  },
  conn:{
    textAlign:"center",
  }
};

export default Header;
