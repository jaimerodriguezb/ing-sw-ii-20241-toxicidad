import logo from './logo.svg';
import './App.css';
import { useEffect } from "react";
import Form from "./Form";

function App() {
  useEffect(() => {
    if (document) {
      const stylesheet = document.createElement("link");
      stylesheet.rel = "stylesheet";
      stylesheet.href = "https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css";

      document.head.appendChild(stylesheet);
    }
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-tiny-logo" alt="logo" width={'600px'}/>
        <div className="py-6">
          <Form />
        </div>
      </header>
    </div>
  );
}

export default App;