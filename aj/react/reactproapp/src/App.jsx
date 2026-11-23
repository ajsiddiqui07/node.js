import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import Landingpage from './Component/Landingpage'
import { Route, Routes } from 'react-router-dom'
import Productlist from './Component/Productlist'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Productlist/>
      <Routes>
        <Route path='/home' elemente={<Landingpage/>}/>
      </Routes>
      
    </>
  )
}

export default App
