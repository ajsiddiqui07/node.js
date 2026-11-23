import axios from 'axios'
import React, { useState } from 'react'

const Fatchdatainserver = () => {
    const [data,setdata] = useState([])
    const getdata = async ()=>{
        const response = await axios.get('https://picsum.photos/v2/list')
        setdata(response.data)
        console.log(data);
        
        
    }
  return (
    <div className='p-10 pl-20'>
      <button onClick={getdata} className='bg-gray-500 h-15 w-30 text-xl border-2 border-black rounded active:scale-97 text-green-500'> get data</button>
        <div>
            {data.map((d)=>{
                return <div className='border bg-white h-59 w-70 rounded mt-2'>
                    <h2 className='pt-1 inline'>id {d.id}</h2><br />
                    <h3 className='inline'>Author {d.author}</h3><br />
                    <img className='border rounded-lg h-32 w-32 object-cover ' src={d.download_url} alt="" />
                    </div>
            })}
        </div>
    </div>
  )
}

export default Fatchdatainserver
