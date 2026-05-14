import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Upload from "./components/upload"
import Chatbox from "./components/chatbox"

function App() {
  const [pdfUploaded, setpdfUploaded] = useState(false);

  return (
    
      <div className="-containeappr">
        <h1>PDF Chatbot</h1>

        <Upload setpdfUploaded={setpdfUploaded}></Upload>

        <Chatbox pdfUploaded={pdfUploaded}></Chatbox>
      </div>
   
  );
}

export default App
