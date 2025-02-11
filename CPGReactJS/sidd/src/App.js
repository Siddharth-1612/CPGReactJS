import logo from './logo.svg';
import React from 'react';
import './App.css';
import Header from './Header.js';
import Body from './Body.js';
import Footer from './Footer.js';
import InterestCalculator from './calculator.js';
import FetchUser from './fetcher.js';
function App() {
  return (
      <div>
        <Header/>
        <Body/>
        <InterestCalculator/>
        <Footer/>
        <FetchUser/>
    </div>
  );
}

export default App;
