import React, { useState } from 'react';
import 'App.css';
import 'antd/dist/antd.css'
import Count from 'Count';
import { Button } from 'antd';
import Welcome from 'Welcome';
import Summary from 'Summary';
import Fruits from 'Fruits';
import Frut from 'Frut';
import Pq1 from 'Pq1';
import Parents from 'Parents';
import Gugudan from 'Gugudan';
import Greeting from 'Greeting';
import Message from 'Message';
import BloodType from 'BloodType';
import ClickCount from 'ClickCount';
import Name from 'Name';
import TestReducer from 'TestReducer';
import SetStudent from 'SetStudent';
import RouterTest from 'RouterTest';
import RouterTest2 from 'RouterTest2';
import Language from 'Language';









/* function StateTest() {

  const [x1, setX1] = useState(10)
  const [x2, setX2] = useState("안녕하세요")
  const [x3, setX3] = useState(name:"홍길돌", age:35)
  const [x4, setX4] = useState([1, 2, 3, 4, 5, 6])

return (


  <>
    <div>{x1}</div>
    <div>{x2}</div>
    <div>{setX3.name} {setX3.age}</div>



  </>





)


} */


function Persona() {

  const namesList = [{'name':'이수만', 'age': 60, 'address': '인천'}, 
                    {'name': '유희열', 'age': 45, 'address': '서울'}, 
                    {'name': '방시혁', 'age': 43, "address": '부산'}, 
                    {'name': '박진영', 'age': 34, 'address': '광주'}]
  
  //v['name']
  //v.name
                    
  // ['name':'이수만', 'age': 60]

  return (
    <>

        <table border='1'>
          <thead>
            <tr>
              <th>name</th>
              <th>age</th>
              <th>address</th>
            </tr>
          </thead>
          <tbody>

            
          </tbody>
        </table>
      {

        
        
        namesList.map((v, i) => {
          return <div>{v.name} {v.age} {v.address} {i}</div>



        })
      }
      
    
    
    
    </>

  )
}
function JsxTest() {

  const datas = [1, 2, 3, 4, 5,  6, 7]

  for (let i =0; i < 10; i++){
    datas.push(i)
  }

  const c = [
    <div>호정</div>,
    <div>홍길동</div>
  ]

  return (
    <>
      {
        datas.map((v, i) => {
          return <div>{v} {i}</div>

        })
      }
      </>
  )
}

  function JsxTest2() {

  const [a, setA] = React.useState(true);

  const user = 1;

  return (
    <div>
      {false && <div>참일경우만 나오는</div>}
      {a ? <div>참일경우</div> : <div>거짓일경우</div>}
      {
        (
          () => {
            //함수s
            if (user==1){
              return <div>User가 1</div>
            }
            else if (user==2){
              return <div>User가 2</div>
            }
          }
        )()  
      }
       {/* </> 이렇게만 해도 됨 */}
    </div>    
  );

}

function App() {
  return (
    <div>
      {/* <Count/>
      <Summary/>
      <Frut/>
      <JsxTest/>
      <JsxTest2/> }
      <Persona/> 
      <Toggle/> 
      <StateTest/>}
      <Pq1/> 
      <Parents/> 
      <Gugudan x={2} 
      <Welcome/> 
      <Greeting/>
      <Message/> 
      <Frut/> 
      <BloodType/> 
      <ClickCount/>
      <Name/> 
      <RouterTest/> 
      <RouterTest2/> */}
      <Language/>
      
    </div>
  );
}

export default App;