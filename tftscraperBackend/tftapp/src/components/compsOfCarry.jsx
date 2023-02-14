import React, { Component } from 'react';
import Carry from './carry';
import Teamcomp from './teamcomp';
import Unit from './unit';

class Compsofcarry extends Component {
  state = {  
    carry: this.props.carry,
    teamcomps: this.props.teamcomps2 

  } 



  style69 = {
    backgroundColor : "#31313c",
    margin : 0,
    padding: 30,
    borderRadius: "4px 0px 0px 4px",
  }
  style692 = {
    backgroundColor : "#31313c",
    margin : 0,
    padding: 30,
    borderRadius: "0px 4px 4px 0px",
  }

  styleMain = {
    margin : 10,
    padding: '0px',
    width: 900
  }
 
  

  render() { 
    return (
      // <div class = "container  my-5" >
        <div class = "row" style = {this.styleMain}>
          <div class = "col-3  " style = {this.style69} >

            <div class = "position-relative start-0" > 
              <Unit value = {this.state.carry} class=  " position-absolute top-50 start-50"/>
            </div>

          </div>



          <div class = "col" style = {this.style692}>
            {this.state.teamcomps.map((teamComp) => (<Teamcomp key={teamComp.id} value2 = {teamComp.teamCompName} />))}

            
          </div>


        </div>
        
      
        
        


        
      // </div>


    );
  }
}
 
export default Compsofcarry
;  