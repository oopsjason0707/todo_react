import React from 'react';

function Toggle() {

    const [state, setState] = React.useState(true);
    // const state = true;} 와 비슷

    

    const click_1 = function(e) {
        if (state == true) {
            setState(false);
        }else {
            setState(true);
        }
        
    }

    const click = (e) => {
        if (state == true) {
            setState(false);
        }else {
            setState(true);
        }
        
    }

    return (
        <>

            {state ? <div>True 입니다.</div>: <div>False 입니다.</div>}
            <button onClick={click}>버튼</button>

        </>
    
    )
    }



    export default Toggle;