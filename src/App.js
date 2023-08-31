import logo from './logo.svg';
import './App.css';
import Amplify, { API } from 'aws-amplify'
import React, { useEffect, useState } from 'react'
import { Route, Routes, useNavigate } from 'react-router-dom';

import Home from './pages/home';
import Results from './pages/results';

const myAPI = "apia8164923";
const path = '/locations'; 


//By default we are taken to the "/" path so we load function Home

//  API Gateway: https://4hij28qp0f.execute-api.us-west-1.amazonaws.com/dev

function App() {  
    return (
      <div className='App'>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </div>
    )
}



//stores current state of values 
  // const [inputs, setInputs] = useState({});
  // const navigate = useNavigate();

  // //when traveling to input textbox is changed then I map it to values 
  // //I think this is mapping to something called values ( c++ ex: values[name] = value )
  // const handleChange = (event) => {

  //   const name = event.target.name;
  //   const value = event.target.value;
  //   setInputs(values => ({...values, [name]: value})) 
  // }

  // const handleSubmit = (event) => {

  //   //assuming that inputs is not empty 
  //   event.preventDefault();

  //   console.log("Checking: " + inputs.toTravel);    
  //   console.log(inputs);
  // }

  // return (
    
  //   <form onSubmit={handleSubmit}>
  //     <label>Traveling to? :</label>

  //       <input
  //         type="text"
  //         name="toTravel"
  //         value={inputs.toTravel || ""}
  //         onChange={handleChange} 
  //       />


  //     <label>Coming from? :</label>

  //       <input
  //         type="text"
  //         name="fromTravel"
  //         value={inputs.fromTravel || ""}
  //         onChange={handleChange}
  //      />

  //     <input type="submit" value='Check' />
  //   </form>
    
  // )


//const App = () => {

  // const [input, setInput] = useState("")
  // const [locations, setLocations] = useState([])

  // //Function to fetch from our backend and update customers array
  // function getLocation(e) {
  //   let locationId = e.input
  //   API.get(myAPI, path + "/" + locationId)
  //      .then(response => {
  //        console.log(response)
  //        let newLocation = [...locations]
  //        newLocation.push(response)
  //        setLocations(newLocation)

  //      })
  //      .catch(error => {
  //        console.log(error)
  //      })
  // }

  // return (
    
  //   <div className="App">
  //     <h1>Super Simple React App</h1>
  //     <div>
  //         <input placeholder="location id" type="text" value={input} onChange={(e) => setInput(e.target.value)}/>      
  //     </div>
  //     <br/>
  //     <button onClick={() => getLocation({input})}>Get Location From Backend</button>

  //     <h2 style={{visibility: locations.length > 0 ? 'visible' : 'hidden' }}>Response</h2>
  //     {
  //      locations.map((thisLocation, index) => {
  //        return (
  //       <div key={thisLocation.locationId}>
  //         <span><b>LocationId:</b> {thisLocation.locationId} - <b>LocationName</b>: {thisLocation.locationName}</span>
  //       </div>)
  //      })
  //     }
  //   </div>
  // )
//}

export default App;
