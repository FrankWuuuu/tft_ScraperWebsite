import React, { Component } from 'react';
import axios from 'axios'
import Compsofcarry from './compsOfCarry';

const api = axios.create({
    baseURL: 'http://localhost:8000/'

})

class Tierlist extends Component {

    state = {  
        carryComps: [],
        hi : "eragf"
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
 

  start(){
    // for (let i = 0; i < this.lolchess.length; i++) {
    //   this.lolchess[i].carry
    // }
    // this.state.carryComps = this.lolchess;
    // console.log (this.state.carryComps);
    
    let i = 0;
    for (const [key, value] of Object.entries(this.lolchess)) {
      // console.log(key, value);
      let carryDict = {};
      carryDict['carry'] = key;
      carryDict['id'] = i;
      i++;
      let unitArrArr = [];
      let j = 0;
      for (const unitArr of value){
        let compDict = {};
        compDict["teamCompName"] = unitArr['units'];
        compDict["id"] = j;
        j++;
        unitArrArr.push(compDict);
      }
      carryDict['teamcomps']= unitArrArr;
      this.state.carryComps.push(carryDict);
      

    }
  }


  render() { 
    // this.start ()
    console.log()
    return (
      
      <div class = "container my-5" >

        <style>{'body { background-color: #1c1c1f; }'}</style>
        <style>{'body { background-color: #ffffff; }'}</style>


        {this.state.carryComps.map((carryComp, id) =>  (

            
            <div key={id}>
            <div >
                  <div >
                        {this.state.carryComp["body"].map((carryComps2) => (<Compsofcarry key={"header"+ carryComps2.carry} carry = {carryComps2.carry} teamcomps2 = {carryComps2.teamcomps} />))}
{/*                         
                        <h1>{carryComp["body"]["Fiddlesticks"][0]["carry"][1]} </h1>
                        <h1>{carryComp["name"]} </h1>
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