import React from 'react';
import  { BrowserRouter, Route, NavLink, Link, Switch } from 'react-router-dom'
import queryString from 'query-string';

export default function Languages() {

    const active = {
        color: "lightblue"
    } 

    return (

        <BrowserRouter>
        <div id="menu">
            <NavLink exact to="/" activeStyle={active}>Home</NavLink>
            <NavLink to="/language" activeStyle={active}>Language</NavLink>
            <NavLink to="/groupl" activeStyle={active}>GroupL</NavLink>
            <NavLink to="/languagef" activeStyle={active}>LanguageF</NavLink>
            <NavLink to="/languagefg" activeStyle={active}>LanguageFG</NavLink>
            

        </div>

        <div id="content">

            <Switch>
                <Route exact path="/" component={Home}/>
                <Route exact path="/language" component={Language}/>
                <Route path="/groupl" component={GroupL}/>
                <Route path="/languagef" component={LanguageF}/>
                <Route path="/languagefg" component={LanguageFG}/>
                <Route path="/nopage" component={NoPage}/>
                
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

function Language(history, location, match){

    console.dir(location)
    console.dir(match)
    
    return(
        <div>
            Language
        </div>
    )
}


function GroupL(history, location, match){

    console.dir(location)
    console.dir(match)

    const click = () => {
        history.push('/')
    }

    return (
        <div>
            GroupLanguage
            {/* <button onClick={click}>go home</button> */}
            {/* <a><Link to="/">Go Home</Link></a> */}
        </div>
    )
}


function LanguageF(history, location, match){

    console.dir(location)
    console.dir(match)

    const click = () => {
        history.push('/')
    }
    
    return (
        <div>
            Favorites
            {/* <button onClick={click}>go home</button>
            <a><Link to="/">Go Home</Link></a> */}
        </div>
    )
}

function LanguageFG(history, location, match){

    console.dir(location)
    console.dir(match)
    
    return (
        <div>
            FavoriteGroup
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