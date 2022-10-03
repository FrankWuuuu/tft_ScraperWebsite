import React, { Component } from "react";
import Unit from "./unit";

class Teamcomp extends Component {
  state = {
    units: [
      // { id: 1 , champName : 'Wukong' },
  
  
    ],
  };

  teamCompStyle ={
    display: 'flex',
    

  }

  addUnitsToState() {
    for (let i = 0; i < this.props.value2.length; i++ ){
      var unitDic = {};
      unitDic['id'] = i;
      unitDic['champName'] = this.props.value2[i];
      this.state.units.push(unitDic);
    }

    
  }

  render() {
    return (
      <div>
        {this.addUnitsToState()}
        
        {this.state.units.map((unit) => (<Unit key={unit.id} value = {unit.champName} />))}

        <div class = "clearfix"></div>

      </div>
    );
  }
}

export default Teamcomp;
