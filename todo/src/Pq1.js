import React from 'react';


function Pq1() {

    const [state, setState] = React.useState({name:'Wayne', math: 80, science: 30, english: 60});

    const resetForm = () => {
        setState({
            ...state,
            math: 0,
            science: 0,
            english: 0

        })
    }
   
    
    
    
  
    return (
    <div>
        {JSON.stringify(state)}
        <button onClick={resetForm}>Click!</button>
    </div>
    )
}
export default Pq1;