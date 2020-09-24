import React, { useState } from 'react'

export default function Name() {

    const [cnt, setCnt] = React.useState([{name:"이수만", age:'60', address:'인천'}, {name:"유희열", age:'45', address:'서울'},
    {name:"방시혁", age:'43', address:'부산'}, {name:"박진영", age:'34', address:'광주'}])

    const [student, setStudent] = React.useState({name:"이수만", age:'60', address:'인천'});

    // setStudent({...student, name:'오호정', age:31})
    
    return (
               
        <>
        
        <table border='1'>
          <thead>
            <tr>
              <th>이름</th>
              <th>나이</th>
              <th>주소</th>
            </tr>
            
          </thead>
          <tbody>
                 
        
            {cnt.map((v, i) => {
                return (<tr>
                            <td>{v.name}</td>
                            <td>{v.age}</td>
                            <td>{v.address}</td>
                        </tr>)  
            })}
            {cnt.name}

          </tbody> 
        </table>
        </>


    )

}