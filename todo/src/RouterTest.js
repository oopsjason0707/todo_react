import React from 'react';
import  { BrowserRouter, Route, NavLink, Link, Switch } from 'react-router-dom'
import queryString from 'query-string';

export default function RouterTest() {

    const active = {
        color:"red"
    }
    return (
        <BrowserRouter>
        <div id="menu"> 
            <NavLink exact to="/" activeStyle={active}>Home</NavLink>  {/* 위에 active에서 지정한 색을 밑에와서 이렇게 지정해줌 */}
            <NavLink to="/students" activeStyle={active}>Students</NavLink>


        </div>
        <div id="content">
            <Switch>
                <Route exact path="/" component={Home}/>
                <Route path="/students/:id" component={Detail}/>
                <Route path="/students" component={Students}/>
                <Route component={NoPage}/>
            </Switch>


        </div>
        
        </BrowserRouter>
    )
}

function Layout({children}) {
    return(
        <>  
        <div>Design</div>
        {children}

        </>
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
    
    return(
        <div>
            STUDENT
            <button onClick={click}>go home</button>
            <a><Link to="/">Go Home</Link></a>
        </div>
    )
}


function NoPage(history, location, match){

    console.dir(location)
    console.dir(match)
    
    return(
        <div>
            NO PAGE
        </div>
    )
}


function Detail(history, location, match){

    console.dir(match)
    console.log(location.search)
    console.log(match.param)

    const qs = queryString.parse(location.search);
    console.dir(qs)
    
    return(
        <div>
            {match}
            Detail
        </div>
    )
}