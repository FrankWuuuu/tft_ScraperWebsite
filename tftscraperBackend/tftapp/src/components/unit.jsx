import React, { Component } from "react";

class Unit extends Component {
  

  state = {
    unitName: this.props.value,
    url: 'https://rerollcdn.com/characters/Skin/7.5/Idas.png'
  };

  urlCreator(){
    let unitname = this.state.unitName.replaceAll(" ","");
    unitname = unitname.replaceAll("'","");
    if(unitname.includes('Nomsy'))unitname = 'Nomsy';
    if(unitname.includes('Swain'))unitname = 'Swain';

    this.state.url=  'https://rerollcdn.com/characters/Skin/7.5/'+ unitname + '.png';
    // this.state.url=  'https://cdn.lolchess.gg/upload/images/champions/MissFortune_1657240754.png';
    
  }

  stylesImg = {
    width: 60,
    height: "auto",
  };

  stylesImg2 = {
    width: 20,
    height: "auto",
  };


  stylesDiv = {
    width: 60,
    height: "auto",
    float: "left",
    margin : 3,
    padding: 0,
  };


  stylesWords = {
    color : "#BC8DA0",
    fontSize : "13px"
    // fontFamily: "Times New Roman"
  };

  

  render() {
    this.urlCreator()
    return (
      <div style = {this.stylesDiv} class = " float-child ">
        
        <img class = ""  src={this.state.url} style={this.stylesImg} alt="" />
        
        <img class = ""  src="https://rerollcdn.com/items/HandofJustice.png" style={this.stylesImg2} alt="" />
        <img class = ""  src="https://rerollcdn.com/items/HandofJustice.png" style={this.stylesImg2} alt="" />
        <img class = ""  src="https://rerollcdn.com/items/HandofJustice.png" style={this.stylesImg2} alt="" />  

        <p class = "text-center mb-1" style = {this.stylesWords}>{this.state.unitName}</p>


        
      </div>
    );
  }
}

export default Unit;
