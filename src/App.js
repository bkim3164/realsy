import './App.css';
import logo from './realsy_logo.png'

function App() {
  return (
    <div className="App">
      <img id="logo" src={logo} alt="Realsy logo"></img>
      <header> Welcome to Realsy!</header>
      <div className="firstpage-bottom-container">
        <div className="firstpage-button"></div>
        <div className="firstpage-bottom-text"> Get Started </div>
      </div>
    </div>
  );
}

export default App;
