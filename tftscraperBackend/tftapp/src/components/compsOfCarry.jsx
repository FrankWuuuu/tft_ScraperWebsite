import React, { Component } from "react";
import Carry from "./carry";
import Teamcomp from "./teamcomp";
import Unit from "./unit";

class Compsofcarry extends Component {
  state = {
    carry: this.props.carry,
    teamcomps: this.props.teamcomps,
  };

  style2 = {
    backgroundColor: "#31313c",
    margin: 0,
    padding: 30,
    borderRadius: "4px 0px 0px 4px",
  };
  style1 = {
    backgroundColor: "#31313c",
    margin: 0,
    padding: 30,
    borderRadius: "0px 4px 4px 0px",
  };

  styleMain = {
    margin: 10,
    padding: "0px",
    width: 900,
  };

  render() {
    return (
      // <div class = "container  my-5" >
      <div class="row" style={this.styleMain}>
        <div class="col-3  " style={this.style2}>
          <div class="position-relative start-0">
            <Unit
              unitName={this.state.carry}
              items = {"jo"}
              class=" position-absolute top-50 start-50"
            />
          </div>
        </div>

        <div class="col" style={this.style1}>
          {/* {console.log(Object.keys(this.state.teamcomps[0]["units"]))} */}
          {/* <Unit value = {Object.keys(this.state.teamcomps[0]["units"])[0]}/> */}
          {this.state.teamcomps.map((teamComp) => (
            <Teamcomp key={"h"+ this.state.carry} composition = {teamComp["units"]} />
            // <Teamcomp key={"h"+ this.state.carry} composition = {teamComp["units"]} />
            // <h1>hiojhi</h1>
          ))}
        </div>
      </div>

      // </div>
    );
  }
}

export default Compsofcarry;
