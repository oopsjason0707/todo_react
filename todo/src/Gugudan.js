import React, { useState } from 'react';

function Gugudan({x}) {
    
    // 여기서부터 계속 실행이 됨
    const num = []

    for(let i=0; i<10; i++) {
        num.push(i)   
    }
    
    return(

        <div>
            {
                num.map((v, i)=>{
                    return <div>{x} * {v}={ x * v }</div>
                }
                
                
                )
            }


        </div>


    )

}

export default Gugudan;






// 클릭 기능 만들때

// const click = () => {
//     setTodoList([..todoList,text])
// }


// <button onClick={click}>추가</button>