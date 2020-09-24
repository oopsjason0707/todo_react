import React, { useState } from 'react'

function ClickCount() {
    
    const [cnt, setCnt] = React.useState(0)

    const click = () => {
        setCnt(cnt + 1) 
    }


    return (
               
        <>
        Total clicks<span>{cnt}</span>
        <div onClick={click}>Click</div>
        </>
    )

}
export default ClickCount;