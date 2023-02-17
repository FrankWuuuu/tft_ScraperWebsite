import React, { Component } from "react";
import Unit from "./unit";

class Teamcomp extends Component {
  state = {
    units: this.props.composition
  };

  teamCompStyle ={
    display: 'flex',
    

  }

  addUnitsToState() {
    for (let i = 0; i < this.props.composition.length; i++ ){
      var unitDic = {};
      unitDic['id'] = i;
      unitDic['champName'] = this.props.composition[i];
      this.state.units.push(unitDic);
    }

    
  }

  render() {
    return (
      <div>
        {/* {this.addUnitsToState()} */}
        
        {/* {console.log(Object.keys(this.state.units))} */}
        {/* {console.log(this.state.units)} */}
        {/* {this.state.units.map((unit) => (<Unit key={"header"+ unit}  value = {unit} />))} */}
        {/* {Object.entries(this.state.units).map((unit, items) => ( */}
        {Object.keys(this.state.units).map((unit) => (
          // <h1>{this.state.units[unit]}</h1>
          <Unit key={"header"+ unit} unitName = {unit} items = {this.state.units[unit]}/>
        ))}

        <div class = "clearfix"></div>

      </div>
    );
  }
}

export default Teamcomp;
