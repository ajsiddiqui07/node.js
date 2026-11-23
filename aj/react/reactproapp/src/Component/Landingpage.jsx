import React, { useEffect, useState } from 'react'

function Landingpage() {

    const [count,setCount] = useState(0)

    useEffect(()=>{
        console.log("hello")
        
        
    },[count])

    const [name,setname] = useState('atul')

    useEffect(()=>{
        
        
        
    },[count])

    const countapp = ()=>{
        setCount(count+1)
    }
  return (
    <div>
        <p>{count}</p>
        <h1 className='w-full h-10 bg-emerald-500 border rounded-lg '>hello</h1>
        <button onClick={countapp} className='border bg-indigo-400 rounded h-10 w-20 m-10'>counting</button>
        <h2>{count>5 && name}</h2>
    </div>
  )
}

export default Landingpage
