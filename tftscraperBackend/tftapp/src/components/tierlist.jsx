import React, { Component } from 'react';
import axios from 'axios'
import Compsofcarry from './compsOfCarry';
import Unit from './unit.jsx';

const api = axios.create({
    baseURL: 'http://localhost:8000/'

})

class Tierlist extends Component {

    state = {  
        carryComps: [],
        hi : { 'a': 1, 'b': 2, 'c': 3 }
    } 


    componentDidMount() {
  
      let data ;

      axios.get('http://localhost:8000/carryAndComps/')
      .then(res => {
          data = res.data;
          // console.log(data[1]["name"])
          this.state.carryComps = data;
          this.setState({
            carryComps : data    
          });
      })
      .catch(err => {})
    }
    
  

  style69 = {
    backgroundColor : "#31313c",
    margin :0,
    padding: 30,
  }

  styleMain = {
    margins : "10px",
    width: 9000
  }
 



  render() { 
    console.log()
    return (
      
      <div class = "container my-5" >

        <style>{'body { background-color: #1c1c1f; }'}</style>
        <style>{'body { background-color: #ffffff; }'}</style>


        {this.state.carryComps.map((carryComp, id) =>  (

            
            <div key={id}>
            <div >
                  <div >
                        {/* {this.state.carryComp["body"].map((carryComps2) => (<Compsofcarry key={"header"+ carryComps2.carry} carry = {carryComps2.carry} teamcomps2 = {carryComps2.teamcomps} />))} */}
                        
                        {Object.entries(carryComp["body"]).map(([carryName,theTeamcomps]) => (
                          <div>
                            {/* <Unit key = {"h"+ carryName} value = {carryName} class=  " position-absolute top-50 start-50"/> */}
                            <Compsofcarry key = {"h "+ carryName} carry = {carryName} teamcomps = {theTeamcomps}/>
                          </div>
                        ))}
                        


                        <Unit unitName = {Object.keys( carryComp["body"]["Vayne"][0]["units"])[0]}
                         items= {carryComp["body"]["Vayne"][0]["units"]["Kai'Sa"]}/>
                        
                        {/* <h1>{carryComp["body"]["Vayne"][0]["units"]["Kai'Sa"][0]} </h1> */}
                        
                        {/* <h1>{carryComp["name"]} </h1>
                        <footer >--- by
                        <cite title="Source Title">
                        {carryComp.name}</cite>
                        </footer> */}


                  </div>
            </div>
            </div>
            )
        )}
        



      
      
      
      
      </div>



    );
  }
}
 
export default Tierlist;  