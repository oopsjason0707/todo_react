import React from 'react';


function Fruits() {
    const [cnt1, setCnt1] = React.useState(0)   // useState 후기, setCnt는 cnt값 변화를 주는 함수
    const [cnt2, setCnt2] = React.useState(0) 
    const [cnt3, setCnt3] = React.useState(0) 
  
    const click1 = () => {
      setCnt1(cnt1 + 1)
    }

    const click2 = () => {
        setCnt2(cnt2 + 1)
      }

      const click3 = () => {
        setCnt3(cnt3 + 1)
      }



    
    
    return (

      
    <div>
        Your Favorite!? <span>MapleStory{cnt1}</span> <span>Clash of Clans{cnt2}</span> <span>CounterStrike{cnt3}</span>
        <div onClick={click1}>MapleStory</div> <div onClick={click2}>Clash of Clans</div> <div onClick={click3}>CounterStrike</div>
    </div>

    
  
    
      
       
    )
  }





  
  export default Fruits;