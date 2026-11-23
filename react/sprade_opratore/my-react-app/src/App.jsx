import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import Sprade_opratoreuse from './components/Sprade_opratoreuse'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Sprade_opratoreuse/>
    </>
  )
}

export default App
