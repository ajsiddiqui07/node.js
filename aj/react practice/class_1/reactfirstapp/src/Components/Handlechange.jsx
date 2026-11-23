import React, { useState } from 'react'

function Handlechange() {
    const [username,setname] = useState()
    const handlesubmit = (e)=>{
        
        console.log(username);
        setname('')
        e.preventDefault()
        
    }

    
  return (
    <div>
      <form onSubmit={(e)=>{
        handlesubmit(e)
      }}>
      <input type="text" onChange={(e)=>{setname(e.target.value);
      }} value={username} className='bg-gray-300 border rounded px-5 py-3 ml-30 mt-10' placeholder='Enter Your name'  /><br />

      <button className='bg-red-600 p-3 ml-10 ml-30 mt-2 border rounded'>Submit</button>
      
      </form>
    </div>
  )
}

export default Handlechange
