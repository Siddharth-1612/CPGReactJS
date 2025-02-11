import logo from './logo.svg';
import './App.css';
import Basic from './sidd/src/Greetings.js';
import Body from './sidd/src/Body.js';
function App() {
  return (
      <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Hi I am Siddharth Rao</p>
        <Basic/>
        <Body/>
        

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
