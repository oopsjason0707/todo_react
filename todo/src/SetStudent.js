import React, { useState } from 'react';

export default function SetStudent() {
    const [stu, setStudent] = React.useState({name: "아이언맨", math: "95", science: "100", english: "88" })

    const click = () => {
        setStudent({
            ...stu,
            math:0,
            science:0,
            english:0
        })
    }


    return (

        <>
        <span>{stu.name} {stu.math} {stu.science} {stu.english}</span>
        <div onClick={click}>클릭</div>

        </>
    )
}

