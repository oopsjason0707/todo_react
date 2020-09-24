import React from 'react';

function Parents()
{
    const [num, setNum] = React.useState(0)
    return (
        <>
        {num}
        <child num={num}
            color="red"
            number={10}
            student={{name: 'Batman', age:35, address:'NewYork'}}/>
        </>
    )
}


function Child(prop)
{
    console.log(prop.num)
    console.log(prop.number)
    console.log(prop.student)
    console.log(prop.color)
    
    return(
        <>
    <div>{prop.num}</div>
    <div>{prop.number}</div>
    <div>{prop.student.name}</div>
    <div>{prop.color}</div>
    </>

    )
}


export default Parents;