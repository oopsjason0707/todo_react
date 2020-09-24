import React, {useState} from 'react';

export default function TestReducer2() {

    const [name, setName] = React.useState('홍길동')   //이름 하고 나이 상태값을 만듬
    const [age, setAge] = Reset.useState(35)

    const [student, setStudent] = React.useState({
        "name": "홍길동",
        "age": 35
    })

    const change = () => {
        
    }

    return (

        <>

        <div>{name} {age}</div>
        <input name="name" onChange={(e)=>setName(e.target.value)} type="text" value={name}/>
        <input age="age" onChange={(e)=>setAge(e.target.value)}type="text" value={age} />
        </>
    )
}