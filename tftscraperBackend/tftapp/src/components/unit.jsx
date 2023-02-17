import React, { Component } from "react";

class Unit extends Component {
  

  state = {
    unitName: this.props.unitName,
    items : this.props.items,
    url: 'https://rerollcdn.com/characters/Skin/8.0/Idas.png',
  };

  urlCreator(){
    let unitname = this.state.unitName.replaceAll(" ","");
    unitname = unitname.replaceAll("'","");

    unitname = unitname.charAt(0) + unitname.substring(1).toLowerCase();
    if(unitname.includes('Aurelion'))unitname = 'AurelionSol';
    if(unitname.includes('fortune'))unitname = 'MissFortune';
    if(unitname.includes('Leesin'))unitname = 'LeeSin';

    // if(unitname.includes('Nomsy'))unitname = 'Nomsy';
    // if(unitname.includes('Swain'))unitname = 'Swain';

    this.state.url=  'https://rerollcdn.com/characters/Skin/8/'+ unitname + '.png';
    // this.state.url=  'https://cdn.lolchess.gg/upload/images/champions/MissFortune_1657240754.png';
    
  }

  itemUrlCreator(){
    

    let itemName = this.state.items.replaceAll(" ","");
    itemName = itemName.replaceAll("'","");

    // itemName = itemName.charAt(0) + itemName.substring(1).toLowerCase();
    // if(itemName.includes('Aurelion'))itemName = 'AurelionSol';
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
    this.urlCreator();
    // this.itemUrlCreator();
    let tempItemsList = [];
    for (var i = 0; i < this.state.items.length; i++){
      let myItem = this.state.items[i] 
      myItem = myItem.replaceAll(" ","");
      myItem = myItem.replaceAll("'","");
      tempItemsList.push(myItem);
      
      
    }

    let itemOne;
    let itemTwo;
    let itemThree;
    if (this.state.items.length !=0){
      itemOne = <img 
        class = ""  
        src={'https://rerollcdn.com/items/'+ tempItemsList[0] + '.png'} 
        style={this.stylesImg2} alt="" 
      />;
      if (this.state.items.length !=1){
        itemTwo = <img 
          class = ""  
          src={'https://rerollcdn.com/items/'+ tempItemsList[1] + '.png'} 
          style={this.stylesImg2} alt="" 
        />;
        if (this.state.items.length !=1){
          itemThree = <img 
            class = ""  
            src={'https://rerollcdn.com/items/'+ tempItemsList[2] + '.png'} 
            style={this.stylesImg2} alt="" 
          />;
        }
      }
    }else{
      itemOne = <img/>;
    }
        


    return (
      <div style = {this.stylesDiv} class = " float-child ">
        
        <img class = ""  src={this.state.url} style={this.stylesImg} alt="" />
        
        {/* <img class = ""  src="https://rerollcdn.com/items/HandofJustice.png" style={this.stylesImg2} alt="" /> */}
        {/* <img class = ""  src={this.state.itemOneUrl} style={this.stylesImg2} alt="" /> */}
        {itemOne}
        {itemTwo}
        {itemThree}

        <p class = "text-center mb-1" style = {this.stylesWords}>{this.state.unitName}</p>


        
      </div>
    );
  }
}

export default Unit;
