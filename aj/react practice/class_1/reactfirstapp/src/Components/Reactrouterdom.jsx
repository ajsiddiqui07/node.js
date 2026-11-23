import React from 'react'
import { Link } from 'react-router-dom'

const Reactrouterdom = () => {
    
  return (
    <div>
      <nav className='h-10 w-221 bg-black border rounded-lg flex justify-between'>
        <div className='text-white  pl-3 pt-1  w-80'>router</div>
        <div className='text-white pr-3 pt-1 flex gap-5 mr-15'>
            
            <div><Link to='/home'>home</Link></div>
            <div><Link to='/props'>props</Link></div>
            <div><Link to='/formhandle'>formhandle</Link></div>
            <div><Link to='/lecture'>lecture</Link></div>
            <div><Link to='/useeffect'>useeffect</Link></div>
        </div>
      </nav>
    </div>
  )
}

export default Reactrouterdom
