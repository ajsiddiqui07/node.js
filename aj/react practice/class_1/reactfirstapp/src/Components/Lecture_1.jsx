import React, { useState } from 'react'

function Lecture_1() {
 const [num, setnum] = useState(0)

  const add = ()=>{
   setnum(num+1)
    
  }

  // how to use state hook
  const [users, setusers] = useState("atul")
  const HowToUseHook = ()=>{
    setusers("arbaz")
  }

  return <div>
        <h1 className='bg-red-400'>helo {num}</h1>
        <h2> hello {users}</h2>
        <button onClick={add}>increment</button>
        <button onClick={()=>{
          setnum(num-1)
        }}>dicrement</button>
        <button onClick={HowToUseHook}>change user</button>
        </div>
  
}

export default Lecture_1
