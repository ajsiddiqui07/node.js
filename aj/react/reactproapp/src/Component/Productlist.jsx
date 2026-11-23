import axios from 'axios'
import React, { useEffect, useState } from 'react'

const Productlist =  () => {

    const [pname,setpname] = useState([])
    const getdata = async ()=>{
        const response = await axios('https://fakestoreapi.com/products')
        setpname(response.data)
        console.log(response.data);
        
        
    }
    useEffect(()=>{

         getdata()
    },[])
   
    
  return (
    <div className=''>
      {pname.map((d)=>{
        return <div className='border bg-blue-300 rounded-2xl h-180 w-50 mt-20'>{d.id}
        <h2> title = {d.title}</h2>
        <h2> price = {d.price}</h2>
        <h2> category = {d.category}</h2>
        <h2> discription = {d.description}</h2>
        <img src={d.image} alt="" />
        </div>
      })}
    </div>
  )
}

export default Productlist
