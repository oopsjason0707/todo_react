import React from 'react';
import  { BrowserRouter, Route, NavLink, Link, Switch } from 'react-router-dom'
import queryString from 'query-string';

export default function RouterTest2() {

    const active = {
       color: "blue" 
    }

    return (

        <BrowserRouter>
        <div id="menu">

            <NavLink exact to="/" activeStyle={active}>Home</NavLink>
            <NavLink to="/students" activeStyle={active}>Students</NavLink>
            <NavLink to="/scores" activeStyle={active}>Scores</NavLink>
            

        </div>
        <div id="content">

            <Switch>
                <Route exact path="/" component={Home}/>
                <Route path="/students" component={Students}/>
                <Route path="/scores" component={Scores}/>
                <Route component={NoPage}/>
            </Switch>

        </div>
        
        
        </BrowserRouter>



    )
}

function Home(history, location, match){

    console.dir(location)
    console.dir(match)
    
    return(
        <div>
            Home
        </div>
    )
}


function Students(history, location, match){

    console.dir(location)
    console.dir(match)

    const click = () => {
        history.push('/')
    }

    return (
        <div>
            Student
            {/* <button onClick={click}>go home</button> */}
            {/* <a><Link to="/">Go Home</Link></a> */}
        </div>
    )
}


function Scores(history, location, match){

    console.dir(location)
    console.dir(match)

    const click = () => {
        history.push('/')
    }
    
    return (
        <div>
            Scores
            {/* <button onClick={click}>go home</button>
            <a><Link to="/">Go Home</Link></a> */}
        </div>
    )
}

function NoPage(history, location, match){

    console.dir(location)
    console.dir(match)
    
    return (
        <div>
            NO PAGE
        </div>
    )
}