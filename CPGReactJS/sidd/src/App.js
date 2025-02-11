import logo from './logo.svg';
import React from 'react';
import './App.css';
import Header from './Header.js';
import Body from './Body.js';
import Footer from './Footer.js';
import Greeting from './func_comp.js';
function App() {
  return (
      <div>
        <Header/>
        <Body/>
        <Greeting name="John"/>
        <Footer/>
    </div>
  );
}

export default App;
