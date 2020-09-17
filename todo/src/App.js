import React from 'react';
import 'App.css';
import 'antd/dist/antd.css'



// 컴포넌트 클래스, 함수형
function Count() {
  const [cnt, setCnt] = React.useState(0)   // useState 후기, setCnt는 cnt값 변화를 주는 함수

  const click = () => {
    setCnt(cnt + 1)
  }

  return (
    <div>
    합계숫자는? <span>{cnt}</span>
    <div onClick={click}>클릭</div>

    </div>
    
     
  )
}


function App() {
  return (
    <div>
      <Count/>
    </div>
  );
}

export default App;
