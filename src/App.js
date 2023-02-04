import './App.css';
import logo from './realsy_logo.png'

function App() {
  return (
    <div className="App">
      <img id="logo" src={logo} alt="Realsy logo"></img>
      <header> Welco
      <div className="firstpage-bottom-container">
        <div className="firstpage-bottom-text"> Get Started </div>
        <button className="firstpage-bottom-button">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z" />
          </svg>
        </button>
      </div>
    </div>
  );
}

export default App;
