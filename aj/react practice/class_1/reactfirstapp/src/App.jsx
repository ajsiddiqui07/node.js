import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Lecture_1 from './Components/Lecture_1'
import Formhandling from './Components/Formhandling'
import Handlechange from './Components/Handlechange'
import Props2 from './Components/Props2'
import Fatchdatainserver from './Components/Fatchdatainserver'
import UseEffect from './Components/UseEffect'
import Reactrouterdom from './Components/Reactrouterdom'
import { Route, Routes } from 'react-router-dom'

function App() {

  return <div>
    <Reactrouterdom />
    <Routes>
      
      <Route path='/lecture' element={ <Lecture_1/>}/>
      <Route path='/formhandle' element={ <Formhandling/>}/>
      <Route path='/handlechange' element={ <Handlechange/>}/>
      <Route path='/props' element={ <Props2/>}/>
      <Route path='/fatchdata' element={ <Fatchdatainserver/>}/>
      <Route path='/useeffect' element={ <UseEffect/>}/>

      
      
      
      
      
      
     
    </Routes>

  </div>

}

export default App
