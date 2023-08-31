import React, {createContext, useEffect, useState} from 'react';
import { useNavigate } from 'react-router-dom';

function Home(){

    const [inputs, setInputs] = useState({});
    const navigate = useNavigate();

    // -     
    function handleChange(event){

        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
    }

    // - 
    function handleSubmit(event){

        event.preventDefault();
        //routing to path '/results' then passing state with {key: value}         
        navigate('/results', {state : {toCountry: inputs.toTravel, fromCountry: inputs.fromTravel}});
    }

    return (
     
        <div name="submitForm">
            <h1> Home </h1>
            <form onSubmit={handleSubmit}>
                <label> Traveling to? :  </label>
                <input type="text" name="toTravel" value={inputs.toTravel || ""} 
                    onChange={handleChange}/>
                <label> Coming from? :  </label>
                <input type='text' name="fromTravel" value={inputs.fromTravel || ""}
                    onChange={handleChange} />       
                <button type="submit">Submit</button>
            </form>
        </div>
       
    )
}

export default Home;