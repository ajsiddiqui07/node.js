import React from 'react'

const Props = (props) => {
    console.log(props);
    
  return (
    <div>
      <h2 className='m-5' >hello i am arbaz  your age is {props.age}</h2>
    </div>
  )
}

export default Props
