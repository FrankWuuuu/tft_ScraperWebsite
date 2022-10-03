import React, { Component } from "react";

class Carry extends Component {
  

  state = {
    unitName: this.props.value,
    url: 'https://rerollcdn.com/characters/Skin/7.5/Idas.png'
  };

  urlCreator(){
    this.state.url=  'https://rerollcdn.com/characters/Skin/7.5/'+ this.state.unitName + '.png';
    
  }

  stylesImg = {
    width: 60,
    height: "auto",
  };

  stylesDiv = {
    width: 60,
    height: "auto",
    float: "left"
  };

  render() {
    this.urlCreator()
    return (
      <div style = {this.stylesDiv} class = "bg-warning float-child">
        <img class = ""  src={this.state.url} style={this.stylesImg} alt="" />
        <p class = "text-center">{this.state.unitName}</p>
      </div>
    );
  }
}

export default Carry;
