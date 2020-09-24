import React, { useState } from 'react';

import { button } from 'antd';


function BloodType() {



    const [state, setState] = useState('Please Select Your Type')



    const click = (e) => {
        // console.dir(e.target);
        // console.log(e.target.innerHTML);
        console.log(e.target.getAttribute("data"));
        console.log(e.target)
        setState(e.target.getAttribute('name'));
    

        

        // console.dir(e.target.getAttribute());


    }



    return(
        
        <>
        <div>{state}</div>
        <div>
            <button data="A Type" name='A Type' onClick={click}>A Type</button>
            <button data="B Type" name='B Type' onClick={click}>B Type</button>
            <button data="O Type" name='O Type' onClick={click}>O Type</button>
            <button data="AB Type" name='AB Type' onClick={click}>AB Type</button>
        </div>







        </>

    )

}






















export default BloodType;